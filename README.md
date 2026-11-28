# learn-hub

Instagram / Threads / X / YouTube の投稿から仕分け・要約した学習ノート集です。
公開ページ: https://om10cg7.github.io/learn-hub/

## フォルダ構成

| フォルダ | 内容 |
|---|---|
| `ui/` | UI/UX デザイン・モーション・ビジュアル大図鑑＆学習ノート |
| `ai-skills/` | AI スキル・ツール・MCP・リポジトリ集 |
| `threads-prompt/` | 画像・動画生成プロンプト集 |
| `ai-picture/` | 写真の撮影・編集・ライティング技法 |
| `etc/` | 上記に分類されない投稿の要約 |
| `scripts/` | サイト自動ビルド (`build_site.py`)・重複チェック (`check_duplicate.py`) |
| `_queue.md` | X 取得保留・ユーザー判断待ちキュー |

※ `lesson-match-claude-handoff-kit.zip` は引き継ぎ用アーカイブとしてルートに保持しています。

## 自動ビルド・公開の仕組み

- `.github/workflows/deploy.yml` により、`main` ブランチへ push すると GitHub Actions が自動で `python scripts/build_site.py` を実行し、全カテゴリの `index.html` および各ノートの HTML ページを生成して GitHub Pages へデプロイします。
- 各カテゴリ直下の `index.html` はリポジトリ管理対象外（自動生成）です。

## 新規ノート作成・重複チェック

```bash
# 重複チェック（URL またはキーワード）
python scripts/check_duplicate.py "https://x.com/..." "キーワード"

# ローカルで静的サイトをビルド確認（dist/ に出力）
python scripts/build_site.py
```

- 新規ノートのファイル名は `YYYY-MM-DD-<platform>-<post_id>.md` とし、先頭に YAML Frontmatter を付与します。
- サムネイル画像は Base64 で HTML に埋め込まず、`<カテゴリ>/assets/<ノート名>.webp` として保存します。
