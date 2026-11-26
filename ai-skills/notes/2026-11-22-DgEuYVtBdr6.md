# 紙の飛び出す世界をコードで作るClaude Skill「papercraft」

- 日付: 2026-11-22
- 作者: AI Adventurer @aiadventureryt
- カテゴリ: 動画・映像／Skill
- 元ネタ: https://www.instagram.com/reel/DgEuYVtBdr6/
- リポジトリ: https://github.com/xikhar/papercraft

## 要約

リール動画（約25秒）。タイトルは「Paper pop-up worlds, made with Claude」。印刷した紙のパーツがヒンジで立ち上がる「飛び出す絵本」風のミニチュア世界を、Claude Code の Skill でコードから生成し動画にレンダリングする仕組みの紹介。画像生成器は使わず全てコードで作る、という点が売り。

作例は3つで、いずれも同じ手順で作られたもの。

- 夜明けに目覚める灯台の町（作者が実際に依頼した例）
- 雪の村
- 砂漠の市場

手順は3ステップ。

1. GitHub リンクをコピーする
2. Claude Code を開いて貼り付け、「install this skill」と入力する（動画内の実演では URL の後に /install と続けていた）
3. 「紙で何か」を前置きして作りたいものを頼む（例: "Make something paper: a lighthouse town waking up at dawn, as a vertical reel."）

リンクは「PAPER」とコメントすると DM で送られる形式だが、動画内でリポジトリ（github.com/xikhar/papercraft）が画面表示されていたため特定できた。

リポジトリを裏取りした内容（2026-11-25確認）: 公開リポジトリで MIT ライセンス、スター661・フォーク71、2026-11-21作成。正式名称は小文字の「papercraft」で、ゲーム・インタラクティブシーン・Webページ・アニメーションを「手作りの飛び出すペーパークラフト様式」で作るためのエージェント Skill。three.js ベースで、紙の質感（薄い切り口のエッジ、層になった印刷、世界に色づく柔らかい影）、ヒンジの動き、ティルトシフトのマクロレンズ表現などの数値・手法を SKILL.md と references にまとめ、lib（paperkit-2d.js／paperkit-3d.js 等）と capture.py（静止画・MP4 のヘッドレス書き出し）を含む。インストールは `npx skills add xikhar/papercraft`、または skills/papercraft/ をスキルフォルダへコピー。Claude Code 以外の Agent Skills 対応エージェント（Codex、Cursor、Gemini CLI、OpenCode 等）でも使えるとしている。画像生成器は「頼んだときだけ」使う設計で、基本は全てコード生成という投稿側の説明とも一致する。

## 学び・所感

- 「紙の質感」を素材モデルとして数値化し、構造タイプ（差し込み十字、折り箱、ドーム等）のカタログと一緒に Skill 化している点が要点。見た目の再現をプロンプトの言い回しではなく、ライブラリ＋計測ループ（measure.py、盲検A/Bシート）で担保する作り
- 動画・Web・ゲームを同一の世界モデルから複数アスペクト（16:9／9:16／正方形／4K）で書き出せる設計で、リール作例はその一出力にすぎない
