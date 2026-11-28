#!/usr/bin/env python3
"""
learn-hub 重複チェックスクリプト。
使い方:
  python scripts/check_duplicate.py <URLまたはキーワード> [キーワード2 ...]
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def normalize_url(url: str) -> str:
    u = re.sub(r"\?.*$", "", url.strip()).rstrip("/")
    u = u.replace("https://twitter.com/", "https://x.com/")
    u = u.replace("http://", "https://")
    return u


def extract_post_id(url: str) -> str:
    for pat in [
        r"instagram\.com/(?:p|reel|tv)/([A-Za-z0-9_-]+)",
        r"threads\.(?:net|com)/@[^/]+/post/([A-Za-z0-9_-]+)",
        r"(?:x|twitter)\.com/[^/]+/status/(\d+)",
        r"(?:youtube\.com/watch\?v=|youtube\.com/shorts/|youtu\.be/)([A-Za-z0-9_-]+)",
    ]:
        m = re.search(pat, url)
        if m:
            return m.group(1)
    return ""


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python scripts/check_duplicate.py <url_or_keyword> [...]")
        sys.exit(1)

    queries = sys.argv[1:]
    url_queries = [normalize_url(q) for q in queries if q.startswith("http")]
    id_queries = [pid for q in queries if q.startswith("http") and (pid := extract_post_id(q))]
    kw_queries = [q.lower() for q in queries if not q.startswith("http")]

    exact_hits = []
    kw_hits = []

    for p in sorted(ROOT.glob("*/notes/*.md")):
        txt = p.read_text(encoding="utf-8", errors="replace")
        txt_lower = txt.lower()
        title = txt.splitlines()[0].lstrip("# ").strip() if txt.splitlines() else p.stem
        rel = str(p.relative_to(ROOT)).replace("\\", "/")

        # Check URL / Post ID match
        matched_url = False
        for uq in url_queries:
            if uq in txt:
                exact_hits.append((rel, title, f"URL一致: {uq}"))
                matched_url = True
                break
        if not matched_url:
            for pid in id_queries:
                if pid in txt or pid in p.stem:
                    exact_hits.append((rel, title, f"PostID一致: {pid}"))
                    matched_url = True
                    break

        if not matched_url and kw_queries:
            if all(k in txt_lower or k in rel.lower() for k in kw_queries):
                kw_hits.append((rel, title))

    if exact_hits:
        print(f"=== 重複候補（URL / PostID 一致: {len(exact_hits)}件）===")
        for rel, title, reason in exact_hits:
            print(f"- {rel} | {title} ({reason})")
    if kw_hits:
        print(f"=== キーワード一致（{len(kw_hits)}件）===")
        for rel, title in kw_hits[:20]:
            print(f"- {rel} | {title}")
    if not exact_hits and not kw_hits:
        print("一致する既存ノートはありません（新規作成OK）。")


if __name__ == "__main__":
    main()
