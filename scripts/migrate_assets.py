#!/usr/bin/env python3
"""
既存の index.html に埋め込まれている Base64 画像を抽出し、
WebP に軽量化して各カテゴリの assets/ へ保存するワンタイム移行スクリプト。
ui/index.html からは図鑑のスタイルとカード群もフラグメントとして切り出す。
"""

import base64
import io
import os
import re
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
MAX_WIDTH = 800
WEBP_QUALITY = 80


def save_webp(b64_data: str, out_path: Path) -> int:
    raw = base64.b64decode(b64_data)
    img = Image.open(io.BytesIO(raw))
    if img.mode in ("RGBA", "P"):
        img = img.convert("RGB")
    if img.width > MAX_WIDTH:
        ratio = MAX_WIDTH / img.width
        img = img.resize((MAX_WIDTH, int(img.height * ratio)), Image.Resampling.LANCZOS)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    img.save(out_path, "WEBP", quality=WEBP_QUALITY, method=6)
    return out_path.stat().st_size


def migrate_card_category(cat: str, card_tag_pattern: str) -> None:
    index_path = ROOT / cat / "index.html"
    if not index_path.exists():
        print(f"[SKIP] {index_path} not found")
        return
    html = index_path.read_text(encoding="utf-8")
    cards = re.findall(card_tag_pattern, html, flags=re.DOTALL)
    total_saved = 0
    total_orig = 0
    count = 0

    for card in cards:
        note_m = re.search(r'href="notes/([^"]+)\.md"', card)
        if not note_m:
            continue
        stem = note_m.group(1)
        b64_list = re.findall(r'data:image/[a-zA-Z0-9+]+;base64,([A-Za-z0-9+/=\s]+)', card)
        for idx, b64 in enumerate(b64_list, start=1):
            b64_clean = re.sub(r"\s+", "", b64)
            total_orig += len(b64_clean) * 3 // 4
            suffix = "" if idx == 1 else f"-{idx}"
            out_path = ROOT / cat / "assets" / f"{stem}{suffix}.webp"
            total_saved += save_webp(b64_clean, out_path)
            count += 1

    print(
        f"[{cat}] extracted {count} images: "
        f"{total_orig/1024/1024:.2f} MB -> {total_saved/1024/1024:.2f} MB WebP"
    )


def migrate_ui_encyclopedia() -> None:
    index_path = ROOT / "ui" / "index.html"
    html = index_path.read_text(encoding="utf-8")

    # Extract <style>...</style>
    style_m = re.search(r"<style>(.*?)</style>", html, flags=re.DOTALL)
    if style_m:
        (ROOT / "ui" / "encyclopedia.css").write_text(
            style_m.group(1).strip() + "\n", encoding="utf-8"
        )

    # Extract <main ...>...</main>
    main_m = re.search(r'(<main[^>]*>.*?</main>)', html, flags=re.DOTALL)
    if not main_m:
        raise RuntimeError("Could not find <main> in ui/index.html")
    main_html = main_m.group(1)

    # Extract filter/copy script from ui/index.html
    script_m = re.search(r"(<div id=\"copyToast\">.*?<script>.*?</script>)", html, flags=re.DOTALL)
    extra_html = script_m.group(1) if script_m else ""

    counter = 0
    total_orig = 0
    total_saved = 0

    def repl(match: re.Match) -> str:
        nonlocal counter, total_orig, total_saved
        counter += 1
        b64_clean = re.sub(r"\s+", "", match.group(1))
        total_orig += len(b64_clean) * 3 // 4
        fname = f"zukan-{counter:03d}.webp"
        out_path = ROOT / "ui" / "assets" / fname
        total_saved += save_webp(b64_clean, out_path)
        return f"assets/{fname}"

    new_main = re.sub(
        r'data:image/[a-zA-Z0-9+]+;base64,([A-Za-z0-9+/=\s]+)', repl, main_html
    )

    fragment = new_main + "\n" + extra_html
    (ROOT / "ui" / "encyclopedia.fragment.html").write_text(fragment, encoding="utf-8")

    print(
        f"[ui encyclopedia] extracted {counter} images: "
        f"{total_orig/1024/1024:.2f} MB -> {total_saved/1024/1024:.2f} MB WebP"
    )


if __name__ == "__main__":
    migrate_card_category("ai-picture", r"<article\b.*?</article>")
    migrate_card_category("etc", r"<article\b.*?</article>")
    migrate_card_category("threads-prompt", r"<section\b.*?</section>")
    migrate_ui_encyclopedia()
