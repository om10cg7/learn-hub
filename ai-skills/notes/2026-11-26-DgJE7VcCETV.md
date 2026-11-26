# Claude Skill 25選 — 5フロアの「オフィス」構成（Charlie Hills）

- 日付: 2026-11-24
- 作者: Charlie Hills @charliehills
- カテゴリ: Skill集
- 元ネタ: https://www.instagram.com/p/DgJE7VcCETV/（カルーセル、内容はメディア理解で確認）

## 要約

「白紙のチャットから始めるのをやめて、Claude にオフィスごと持たせる」という比喩で、工程ごとに1フロア、計5フロア×5 Skill＝25 Skill を並べた回。Skill は「指示の入った小さなフォルダで、仕事が来たら Claude が読み込むので、同じ説明を二度しなくて済む」という説明付き。全25個は無料 GitHub リポジトリ4つ（anthropic/skills、obra/superpowers、marketingskills、remotion-dev/skills）からで、6行のコマンドで全部入る。25個全部は不要で、自分が一番いるフロアから始めるのが推奨。インストール行と各 Skill の最初の一言は「OFFICE」コメントで送付（未回収、コピーボタン対象外）。

| フロア | 段階 | Skill 5つ |
|---|---|---|
| 1 | Design it（設計） | Frontend Design、Canvas Design、Algorithmic Art、Theme Factory、Remotion Create |
| 2 | Package it（文書化） | DOCX、PPTX、XLSX、PDF、Doc Coauthoring |
| 3 | Market it（マーケ） | Copywriting、SEO Audit、CRO、Emails、Social |
| 4 | Build it（構築） | Writing Plans、Subagent-Driven Development、Git Worktrees、MCP Builder、Skill Creator |
| 5 | Verify it（検証） | Webapp Testing、Systematic Debugging、Test-Driven Development、Requesting Code Review、Verification Before Completion |

## 学び・所感

- 並べ方の要点は「作る前に描く（Design）→ 形にする（Package）→ 売る（Market）→ 計画してから書く（Build）→ 終わりと言う前に証明する（Verify）」という工程の癖を Skill で固定すること。特に4階の「Writing Plans（コードの前に計画）」と5階の「Verification Before Completion（完了宣言の前に検証）」は、ツール紹介というより作業規律の話
- 出所が公式 anthropic/skills と著名どころの superpowers 等に寄っていて、出所不明の Skill まとめとは一線を画す構成
