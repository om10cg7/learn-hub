#!/usr/bin/env python3
"""
learn-hub 静的サイト自動ビルドスクリプト (Python 標準ライブラリのみ使用)。
各カテゴリの notes/*.md と assets/* を読み込み、dist/ 以下に
ルート index.html、各カテゴリ index.html、各ノート HTML ページを生成する。
"""

import html
import json
import re
import shutil
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
DIST = ROOT / "dist"

CATEGORIES = [
    {
        "dir": "ui",
        "title": "UI/UX",
        "lead": "UI/UX デザイン＆トレンド用語 ビジュアル大図鑑と学習ノート。",
    },
    {
        "dir": "ai-skills",
        "title": "AIのスキル・道具",
        "lead": "Claude スキルや AI ツール・リポジトリ集の要約一覧とノート。",
    },
    {
        "dir": "threads-prompt",
        "title": "生成プロンプト",
        "lead": "Threads・Instagram で配布された生成プロンプトのノート集（コピーボタン付き）。",
    },
    {
        "dir": "ai-picture",
        "title": "写真の技法",
        "lead": "写真の撮り方・編集・ライティング技法のノート集。",
    },
    {
        "dir": "etc",
        "title": "etc",
        "lead": "上記4カテゴリに当てはまらない投稿の要約集。",
    },
]

COMMON_CSS = """
  :root { --bg:#f7f7f5; --card:#fff; --text:#222; --muted:#555; --border:#e3e3de; --accent:#0b5cad; }
  * { box-sizing: border-box; }
  body { font-family: -apple-system, BlinkMacSystemFont, "Hiragino Sans", "Noto Sans JP", sans-serif; margin: 0; background: var(--bg); color: var(--text); line-height: 1.65; }
  .wrap { max-width: 1120px; margin: 0 auto; padding: 28px 18px 64px; }
  a.back { font-size: 14px; color: var(--muted); text-decoration: none; display: inline-block; margin-bottom: 12px; }
  a.back:hover { text-decoration: underline; }
  h1 { font-size: 24px; margin: 0 0 8px; }
  p.lead { color: var(--muted); margin: 0 0 20px; font-size: 14px; }
  .search { margin: 0 0 20px; }
  .search input { width: 100%; padding: 10px 14px; font-size: 15px; border: 1px solid #ccc; border-radius: 8px; background: #fff; }
  .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 16px; }
  .card { background: var(--card); border: 1px solid var(--border); border-radius: 12px; overflow: hidden; display: flex; flex-direction: column; }
  .card img { width: 100%; height: 200px; object-fit: cover; display: block; background: #e5e5e0; }
  .thumb { height: 200px; overflow: hidden; background: #e5e5e0; }
  .thumb iframe { width: 100%; height: 480px; border: 0; margin-top: -52px; background: #fff; }
  .noimg { height: 140px; display: flex; align-items: center; justify-content: center; background: #ecece7; color: #888; font-size: 13px; }
  .body { padding: 14px 16px 16px; display: flex; flex-direction: column; gap: 6px; flex: 1; }
  .meta { font-size: 12px; color: #777; }
  .badge { display: inline-block; background: #eef2ff; color: #3730a3; border-radius: 999px; padding: 1px 8px; font-size: 11px; margin-left: 4px; }
  .card h2 { font-size: 16px; margin: 0; line-height: 1.4; }
  .card p.summary { font-size: 13.5px; color: #444; margin: 0; flex: 1; }
  .links { display: flex; flex-wrap: wrap; gap: 10px; align-items: center; margin-top: 8px; font-size: 13px; }
  .links a { color: var(--accent); text-decoration: none; font-weight: 600; }
  .links a:hover { text-decoration: underline; }
  .copy-btn { background: var(--accent); color: #fff; border: 0; border-radius: 6px; padding: 5px 10px; font-size: 12px; cursor: pointer; font-weight: 600; }
  .copy-btn.done { background: #2e7d32; }
"""


def parse_frontmatter(text: str) -> tuple[dict[str, Any], str]:
    if not text.startswith("---"):
        return {}, text
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)$", text, flags=re.DOTALL)
    if not m:
        return {}, text
    meta: dict[str, Any] = {}
    for line in m.group(1).splitlines():
        if ":" not in line:
            continue
        k, v = line.split(":", 1)
        k = k.strip()
        v = v.strip().strip('"').strip("'")
        if v.startswith("[") and v.endswith("]"):
            meta[k] = [x.strip().strip('"').strip("'") for x in v[1:-1].split(",") if x.strip()]
        else:
            meta[k] = v
    return meta, m.group(2)


def extract_note_info(cat: str, md_path: Path) -> dict[str, Any]:
    raw = md_path.read_text(encoding="utf-8", errors="replace")
    fm, body = parse_frontmatter(raw)
    stem = md_path.stem

    # Title
    title = fm.get("title", "")
    if not title:
        m = re.search(r"^#\s+(.+)$", body, flags=re.MULTILINE)
        title = m.group(1).strip() if m else stem

    # Date
    date = fm.get("date", "")
    if not date:
        m = re.search(r"^-\s*(?:日付|登録日)[:：]\s*(\d{4}-\d{2}-\d{2})", body, flags=re.MULTILINE)
        if m:
            date = m.group(1)
        else:
            m2 = re.match(r"^(\d{4}-\d{2}-\d{2})-", stem)
            date = m2.group(1) if m2 else ""

    # Author
    author = fm.get("author", "")
    if not author:
        m = re.search(r"^-\s*(?:作者|投稿者)[:：]\s*(.+)$", body, flags=re.MULTILINE)
        if m:
            author = m.group(1).strip()

    # Subcategory / Tag
    subcat = fm.get("subcategory", "")
    if not subcat:
        m = re.search(r"^-\s*カテゴリ[:：]\s*(.+)$", body, flags=re.MULTILINE)
        if m:
            subcat = m.group(1).strip()

    # Source URL
    url = fm.get("url", "")
    if not url:
        m = re.search(r"(https?://[^\s\)\>（」]+)", body)
        if m:
            url = m.group(1).rstrip(".,;:")

    # Summary: extract from ## 要約 or first body paragraph after metadata list
    summary = fm.get("summary", "")
    if not summary:
        sec_m = re.search(r"^##\s+要約\s*\n+(.*?)(?=\n##|\Z)", body, flags=re.MULTILINE | re.DOTALL)
        chunk = sec_m.group(1) if sec_m else body
        lines = []
        for ln in chunk.splitlines():
            s = ln.strip()
            if not s or s.startswith("#") or s.startswith("|") or s.startswith("```"):
                if lines:
                    break
                continue
            if re.match(r"^-\s*(?:日付|登録日|作者|投稿者|カテゴリ|元ネタ|出典|投稿)[:：]", s):
                continue
            s = re.sub(r"^[-*]\s+", "", s)
            s = re.sub(r"\[([^\]]+)\]\([^\)]+\)", r"\1", s)
            lines.append(s)
            if sum(len(x) for x in lines) > 160:
                break
        summary = " ".join(lines)
    if len(summary) > 180:
        summary = summary[:177] + "..."

    # Prompts (code blocks under ## プロンプト)
    prompts: list[str] = []
    pm = re.search(r"^##\s+プロンプト[^\n]*\n(.*?)(?=\n##\s+|\Z)", body, flags=re.MULTILINE | re.DOTALL)
    if pm:
        prompts = [p.strip() for p in re.findall(r"```(?:\w+)?\n(.*?)```", pm.group(1), flags=re.DOTALL) if p.strip()]

    # Thumbnail asset
    assets_dir = ROOT / cat / "assets"
    images: list[str] = []
    if fm.get("thumb"):
        images.append(fm["thumb"])
    elif assets_dir.exists():
        first = assets_dir / f"{stem}.webp"
        if first.exists():
            images.append(f"assets/{stem}.webp")
        for extra in sorted(assets_dir.glob(f"{stem}-*.webp")):
            images.append(f"assets/{extra.name}")

    return {
        "stem": stem,
        "title": title,
        "date": date,
        "author": author,
        "subcat": subcat,
        "url": url,
        "summary": summary,
        "prompts": prompts,
        "images": images,
        "body": body,
        "raw": raw,
    }


def inline_md(text: str) -> str:
    esc = html.escape(text)
    esc = re.sub(r"`([^`]+)`", r"<code>\1</code>", esc)
    esc = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", esc)
    esc = re.sub(
        r"\[([^\]]+)\]\((https?://[^\)]+)\)",
        r'<a href="\2" target="_blank" rel="noopener">\1</a>',
        esc,
    )
    esc = re.sub(
        r'(?<![">])(https?://[^\s<]+)',
        r'<a href="\1" target="_blank" rel="noopener">\1</a>',
        esc,
    )
    return esc


def md_to_html(md_text: str) -> str:
    lines = md_text.splitlines()
    out: list[str] = []
    i = 0
    in_ul = False
    in_ol = False

    def close_lists() -> None:
        nonlocal in_ul, in_ol
        if in_ul:
            out.append("</ul>")
            in_ul = False
        if in_ol:
            out.append("</ol>")
            in_ol = False

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # Code block
        if stripped.startswith("```"):
            close_lists()
            code_lines = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith("```"):
                code_lines.append(lines[i])
                i += 1
            code_str = html.escape("\n".join(code_lines))
            out.append(
                '<div class="code-wrap">'
                '<button class="copy-code" onclick="copyCode(this)">📋 コピー</button>'
                f"<pre><code>{code_str}</code></pre></div>"
            )
            i += 1
            continue

        # Table
        if stripped.startswith("|") and i + 1 < len(lines) and re.match(r"^\|[\s\-:|]+\|$", lines[i + 1].strip()):
            close_lists()
            headers = [c.strip() for c in stripped.strip("|").split("|")]
            out.append('<div class="table-wrap"><table><thead><tr>' + "".join(f"<th>{inline_md(h)}</th>" for h in headers) + "</tr></thead><tbody>")
            i += 2
            while i < len(lines) and lines[i].strip().startswith("|"):
                cols = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                out.append("<tr>" + "".join(f"<td>{inline_md(c)}</td>" for c in cols) + "</tr>")
                i += 1
            out.append("</tbody></table></div>")
            continue

        # Headings
        hm = re.match(r"^(#{1,4})\s+(.+)$", stripped)
        if hm:
            close_lists()
            lvl = len(hm.group(1))
            out.append(f"<h{lvl}>{inline_md(hm.group(2))}</h{lvl}>")
            i += 1
            continue

        # Unordered list
        um = re.match(r"^[-*]\s+(.+)$", stripped)
        if um:
            if in_ol:
                out.append("</ol>")
                in_ol = False
            if not in_ul:
                out.append("<ul>")
                in_ul = True
            out.append(f"<li>{inline_md(um.group(1))}</li>")
            i += 1
            continue

        # Ordered list
        om = re.match(r"^\d+\.\s+(.+)$", stripped)
        if om:
            if in_ul:
                out.append("</ul>")
                in_ul = False
            if not in_ol:
                out.append("<ol>")
                in_ol = True
            out.append(f"<li>{inline_md(om.group(1))}</li>")
            i += 1
            continue

        if not stripped:
            close_lists()
            i += 1
            continue

        close_lists()
        out.append(f"<p>{inline_md(stripped)}</p>")
        i += 1

    close_lists()
    return "\n".join(out)


def render_note_page(cat: dict[str, str], note: dict[str, Any]) -> str:
    cat_dir = cat["dir"]
    body_html = md_to_html(note["body"])
    imgs_html = ""
    if note["images"]:
        imgs_html = '<div class="note-imgs">' + "".join(
            f'<img src="../{html.escape(src)}" alt="{html.escape(note["title"])}" loading="lazy">'
            for src in note["images"]
        ) + "</div>"
    src_link = (
        f'<a class="src-btn" href="{html.escape(note["url"])}" target="_blank" rel="noopener">元ネタを開く ↗</a>'
        if note["url"]
        else ""
    )
    return f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{html.escape(note["title"])} | {html.escape(cat["title"])}</title>
<style>
  body {{ font-family: -apple-system, BlinkMacSystemFont, "Hiragino Sans", "Noto Sans JP", sans-serif; margin: 0; background: #f7f7f5; color: #222; line-height: 1.75; }}
  .wrap {{ max-width: 820px; margin: 0 auto; padding: 28px 18px 64px; }}
  .topbar {{ display: flex; justify-content: space-between; align-items: center; gap: 12px; flex-wrap: wrap; margin-bottom: 18px; }}
  a.back {{ font-size: 14px; color: #555; text-decoration: none; }}
  a.back:hover {{ text-decoration: underline; }}
  a.src-btn {{ font-size: 13px; background: #0b5cad; color: #fff; padding: 6px 12px; border-radius: 6px; text-decoration: none; font-weight: 600; }}
  article {{ background: #fff; border: 1px solid #e3e3de; border-radius: 12px; padding: 24px 26px; }}
  h1 {{ font-size: 22px; margin: 0 0 14px; line-height: 1.4; }}
  h2 {{ font-size: 17px; margin: 22px 0 8px; border-bottom: 1px solid #eee; padding-bottom: 4px; }}
  h3 {{ font-size: 15px; margin: 16px 0 6px; }}
  ul, ol {{ padding-left: 22px; }}
  li {{ margin: 4px 0; }}
  code {{ background: #f1f1ec; padding: 2px 5px; border-radius: 4px; font-size: 0.9em; }}
  .code-wrap {{ position: relative; margin: 12px 0; }}
  .copy-code {{ position: absolute; top: 8px; right: 8px; background: #0b5cad; color: #fff; border: 0; border-radius: 5px; padding: 4px 9px; font-size: 12px; cursor: pointer; }}
  pre {{ background: #1e293b; color: #f8fafc; padding: 14px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5; }}
  pre code {{ background: none; padding: 0; color: inherit; }}
  .table-wrap {{ overflow-x: auto; margin: 12px 0; }}
  table {{ width: 100%; border-collapse: collapse; font-size: 13.5px; }}
  th, td {{ border: 1px solid #ddd; padding: 8px 10px; text-align: left; }}
  th {{ background: #f3f3ee; }}
  .note-imgs {{ display: flex; flex-wrap: wrap; gap: 10px; margin: 14px 0; }}
  .note-imgs img {{ max-width: 100%; max-height: 420px; border-radius: 8px; border: 1px solid #e3e3de; }}
</style>
</head>
<body>
<div class="wrap">
  <div class="topbar">
    <a class="back" href="../index.html">← {html.escape(cat["title"])} 一覧へ</a>
    {src_link}
  </div>
  <article>
    {imgs_html}
    {body_html}
  </article>
</div>
<script>
function copyCode(btn) {{
  const text = btn.nextElementSibling.innerText;
  navigator.clipboard.writeText(text).then(() => {{
    btn.textContent = '✓ コピー済み';
    setTimeout(() => btn.textContent = '📋 コピー', 1800);
  }});
}}
</script>
</body>
</html>"""


def render_card(note: dict[str, Any]) -> str:
    # Thumbnail
    if note["images"]:
        media_html = f'<img src="{html.escape(note["images"][0])}" alt="{html.escape(note["title"])}" loading="lazy">'
    else:
        ig_m = re.search(r"https://www\.instagram\.com/(p|reel)/([A-Za-z0-9_-]+)", note["url"])
        if ig_m:
            embed = f"https://www.instagram.com/{ig_m.group(1)}/{ig_m.group(2)}/embed"
            media_html = f'<div class="thumb"><iframe src="{embed}" loading="lazy" scrolling="no" title="{html.escape(note["title"])}"></iframe></div>'
        else:
            media_html = '<div class="noimg">画像なし</div>'

    meta_parts = []
    if note["date"]:
        meta_parts.append(note["date"])
    if note["author"]:
        meta_parts.append(html.escape(note["author"]))
    meta_str = " ・ ".join(meta_parts)
    if note["subcat"]:
        meta_str += f' <span class="badge">{html.escape(note["subcat"])}</span>'

    prompt_btns = ""
    for idx, p in enumerate(note["prompts"], start=1):
        label = "📋 プロンプトをコピー" if len(note["prompts"]) == 1 else f"📋 プロンプト{idx}"
        prompt_btns += f'<button class="copy-btn" data-prompt="{html.escape(p)}" onclick="copyPromptText(this)">{label}</button>'

    src_link = (
        f'<a href="{html.escape(note["url"])}" target="_blank" rel="noopener">元ネタ</a>'
        if note["url"]
        else ""
    )
    search_blob = html.escape(f'{note["title"]} {note["author"]} {note["subcat"]} {note["summary"]}'.lower())

    return f"""<article class="card" data-text="{search_blob}">
  {media_html}
  <div class="body">
    <div class="meta">{meta_str}</div>
    <h2>{html.escape(note["title"])}</h2>
    <p class="summary">{html.escape(note["summary"])}</p>
    <div class="links">
      {src_link}
      <a href="notes/{html.escape(note["stem"])}.html">ノートを開く</a>
      {prompt_btns}
    </div>
  </div>
</article>"""


def build_standard_category(cat: dict[str, str], notes: list[dict[str, Any]]) -> None:
    cat_dir = cat["dir"]
    cards_html = "\n".join(render_card(n) for n in notes)
    page = f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{html.escape(cat["title"])} | 学習ノート集</title>
<style>{COMMON_CSS}</style>
</head>
<body>
<div class="wrap">
  <a class="back" href="../index.html">← 学習ノート集トップへ</a>
  <h1>{html.escape(cat["title"])}（全{len(notes)}件）</h1>
  <p class="lead">{html.escape(cat["lead"])}</p>
  <div class="search"><input id="q" type="search" placeholder="キーワード検索（タイトル・作者・内容）"></div>
  <main class="grid" id="grid">
    {cards_html}
  </main>
</div>
<script>
const q = document.getElementById('q');
const cards = document.querySelectorAll('#grid .card');
q.addEventListener('input', () => {{
  const v = q.value.trim().toLowerCase();
  cards.forEach(c => {{
    c.style.display = (!v || (c.dataset.text || '').includes(v)) ? 'flex' : 'none';
  }});
}});
function copyPromptText(btn) {{
  navigator.clipboard.writeText(btn.dataset.prompt).then(() => {{
    const orig = btn.textContent;
    btn.textContent = '✓ コピー済み';
    btn.classList.add('done');
    setTimeout(() => {{ btn.textContent = orig; btn.classList.remove('done'); }}, 1800);
  }});
}}
</script>
</body>
</html>"""
    (DIST / cat_dir / "index.html").write_text(page, encoding="utf-8")


def build_ui_category(cat: dict[str, str], notes: list[dict[str, Any]]) -> int:
    zukan_css = (ROOT / "ui" / "encyclopedia.css").read_text(encoding="utf-8")
    frag = (ROOT / "ui" / "encyclopedia.fragment.html").read_text(encoding="utf-8")
    # Point note links inside encyclopedia to generated .html files
    frag = re.sub(r'href="notes/([^"]+)\.md"', r'href="notes/\1.html"', frag)
    zukan_count = len(re.findall(r'class="term-card"', frag))

    cards_html = "\n".join(render_card(n) for n in notes)
    page = f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>UI/UX ビジュアル大図鑑（全{zukan_count}種）＆ 学習ノート（全{len(notes)}件）</title>
<style>
{zukan_css}
  .view-switch {{ display: flex; gap: 10px; margin: 14px 0 8px; flex-wrap: wrap; }}
  .view-btn {{ background: var(--surface); color: var(--text); border: 1px solid var(--border); padding: 8px 16px; border-radius: 10px; font-weight: 700; cursor: pointer; font-size: 0.9rem; }}
  .view-btn.active {{ background: var(--accent); color: #0f172a; border-color: var(--accent); }}
  .notes-panel {{ display: none; max-width: 1100px; margin: 0 auto; padding: 12px 16px 48px; }}
  .notes-panel.active {{ display: block; }}
  .notes-grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 16px; margin-top: 14px; }}
  .notes-grid .card {{ background: var(--surface); border: 1px solid var(--border); border-radius: 14px; overflow: hidden; display: flex; flex-direction: column; }}
  .notes-grid .card img {{ width: 100%; height: 190px; object-fit: cover; }}
  .notes-grid .thumb {{ height: 190px; overflow: hidden; }}
  .notes-grid .thumb iframe {{ width: 100%; height: 480px; border: 0; margin-top: -52px; }}
  .notes-grid .noimg {{ height: 120px; display: flex; align-items: center; justify-content: center; background: #090d16; color: var(--text-muted); font-size: 13px; }}
  .notes-grid .body {{ padding: 14px 16px; display: flex; flex-direction: column; gap: 6px; flex: 1; }}
  .notes-grid .meta {{ font-size: 12px; color: var(--text-muted); }}
  .notes-grid h2 {{ font-size: 16px; margin: 0; color: var(--text); }}
  .notes-grid p.summary {{ font-size: 13.5px; color: var(--text-muted); margin: 0; flex: 1; }}
  .notes-grid .links {{ display: flex; gap: 12px; margin-top: 8px; font-size: 13px; }}
  .notes-grid .links a {{ color: var(--accent); text-decoration: none; font-weight: 600; }}
  .notes-grid .badge {{ background: rgba(56,189,248,0.15); color: var(--accent); padding: 1px 8px; border-radius: 999px; font-size: 11px; }}
</style>
</head>
<body>
<header>
  <a href="../index.html" style="color:var(--text-muted);font-size:13px;text-decoration:none;display:inline-block;margin-bottom:8px;">← 学習ノート集トップへ</a>
  <h1>UI/UX デザイン＆トレンド用語 ビジュアル大図鑑</h1>
  <div class="subtitle">図鑑カード（全{zukan_count}種）と UI/UX 学習ノート（全{len(notes)}件）</div>
  <div class="view-switch">
    <button class="view-btn active" onclick="switchView('zukan', this)">📖 用語ビジュアル図鑑（{zukan_count}種）</button>
    <button class="view-btn" onclick="switchView('notes', this)">📝 学習ノート一覧（{len(notes)}件）</button>
  </div>
  <div id="zukanControls" class="controls">
    <div class="tabs">
      <button class="tab-btn active" data-cat="all">すべて</button>
      <button class="tab-btn apple-tab" data-cat="apple-related">🍎 Apple関連</button>
      <button class="tab-btn" data-cat="layout">レイアウト</button>
      <button class="tab-btn" data-cat="visual">ビジュアル・質感</button>
      <button class="tab-btn" data-cat="motion">モーション</button>
      <button class="tab-btn" data-cat="component">UI部品</button>
    </div>
    <input type="search" id="searchInput" class="search-input" placeholder="図鑑用語・英語名・プロンプトで検索...">
  </div>
</header>

<div id="zukanPanel">
  {frag}
</div>

<section id="notesPanel" class="notes-panel">
  <input type="search" id="notesSearch" class="search-input" placeholder="学習ノート（{len(notes)}件）を検索...">
  <div class="notes-grid" id="notesGrid">
    {cards_html}
  </div>
</section>

<script>
function switchView(mode, btn) {{
  document.querySelectorAll('.view-btn').forEach(b => b.classList.remove('active'));
  btn.classList.add('active');
  const isZukan = mode === 'zukan';
  document.getElementById('zukanPanel').style.display = isZukan ? 'block' : 'none';
  document.getElementById('zukanControls').style.display = isZukan ? 'flex' : 'none';
  document.getElementById('notesPanel').classList.toggle('active', !isZukan);
}}
const ns = document.getElementById('notesSearch');
const nCards = document.querySelectorAll('#notesGrid .card');
ns.addEventListener('input', () => {{
  const v = ns.value.trim().toLowerCase();
  nCards.forEach(c => {{
    c.style.display = (!v || (c.dataset.text || '').includes(v)) ? 'flex' : 'none';
  }});
}});
</script>
</body>
</html>"""
    (DIST / "ui" / "index.html").write_text(page, encoding="utf-8")
    return zukan_count


def build_root_index(stats: list[dict[str, Any]]) -> None:
    cards_html = ""
    for s in stats:
        count_txt = f'図鑑 {s["zukan"]}種 ＋ ノート {s["count"]}件' if s.get("zukan") else f'全 {s["count"]} 件'
        cards_html += f"""    <a class="card" href="{s["dir"]}/index.html">
      <h2>{html.escape(s["title"])} <span class="cnt">{count_txt}</span></h2>
      <p>{html.escape(s["lead"])}</p>
    </a>\n"""

    zip_card = ""
    if (ROOT / "lesson-match-claude-handoff-kit.zip").exists():
        zip_card = """    <a class="card" href="lesson-match-claude-handoff-kit.zip" download>
      <h2>Lesson Match 引き継ぎキット</h2>
      <p>Claude への引き継ぎ用ファイル一式（zip）のダウンロード。</p>
    </a>\n"""

    total = sum(s["count"] for s in stats)
    root_html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>学習ノート集（全{total}件）</title>
<style>
  body {{ font-family: -apple-system, BlinkMacSystemFont, "Hiragino Sans", "Noto Sans JP", sans-serif; margin: 0; background: #f7f7f5; color: #222; }}
  .wrap {{ max-width: 1100px; margin: 0 auto; padding: 40px 20px 64px; }}
  h1 {{ font-size: 28px; margin: 0 0 8px; }}
  p.lead {{ color: #555; margin: 0 0 32px; }}
  .grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 16px; }}
  a.card {{ display: block; background: #fff; border: 1px solid #e3e3de; border-radius: 12px; padding: 20px; text-decoration: none; color: inherit; transition: border-color .15s; }}
  a.card:hover {{ border-color: #0b5cad; }}
  a.card h2 {{ font-size: 18px; margin: 0 0 8px; display: flex; justify-content: space-between; align-items: baseline; gap: 8px; }}
  .cnt {{ font-size: 12px; background: #eef2ff; color: #3730a3; padding: 2px 8px; border-radius: 999px; font-weight: 600; }}
  a.card p {{ font-size: 14px; color: #555; margin: 0; line-height: 1.6; }}
</style>
</head>
<body>
<div class="wrap">
  <h1>学習ノート集（全{total}件）</h1>
  <p class="lead">SNS投稿から仕分けて蓄積した学習ノートの置き場です。GitHub Actions により自動で最新化されます。</p>
  <div class="grid">
{cards_html}{zip_card}  </div>
</div>
</body>
</html>"""
    (DIST / "index.html").write_text(root_html, encoding="utf-8")


def main() -> None:
    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir(parents=True)

    # Copy root static files if present
    zip_file = ROOT / "lesson-match-claude-handoff-kit.zip"
    if zip_file.exists():
        shutil.copy2(zip_file, DIST / zip_file.name)

    stats: list[dict[str, Any]] = []
    for cat in CATEGORIES:
        cdir = cat["dir"]
        out_cat = DIST / cdir
        (out_cat / "notes").mkdir(parents=True, exist_ok=True)

        # Copy assets
        assets_src = ROOT / cdir / "assets"
        if assets_src.exists():
            shutil.copytree(assets_src, out_cat / "assets")

        # Parse notes (newest first by date/filename)
        md_files = sorted((ROOT / cdir / "notes").glob("*.md"), reverse=True)
        notes = [extract_note_info(cdir, p) for p in md_files]

        # Write individual note HTML pages
        for n in notes:
            (out_cat / "notes" / f'{n["stem"]}.html').write_text(
                render_note_page(cat, n), encoding="utf-8"
            )

        if cdir == "ui":
            zukan_cnt = build_ui_category(cat, notes)
            stats.append({**cat, "count": len(notes), "zukan": zukan_cnt})
        else:
            build_standard_category(cat, notes)
            stats.append({**cat, "count": len(notes)})

        print(f"[BUILD] {cdir}: {len(notes)} notes")

    build_root_index(stats)
    print(f"[DONE] Site built in {DIST}")


if __name__ == "__main__":
    main()
