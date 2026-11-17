# Claude Codeで作る自分専用JARVIS 5ステップ

- 日付: 2026-11-14
- 作者: Nitin Chougale @classified.ai
- カテゴリ: パーソナルAI
- 元ネタ: https://www.instagram.com/p/DfuwCvUjkE5/

## 要約

カルーセル（全9枚、内容は解析で確認）。『AIにタイピングで話しかけるのはやめて、Claude Codeで自分のJARVISを作ろう』と題し、ノートPC上でローカルに動く音声操作パーソナルAIの構築を5ステップで示す。導入部では通常のチャットボット（打つ・忘れる・ブラウザの中だけ）との対比を置く。Step 1 Skills＝繰り返し作業を /morning-brief、/reel-script、/weekly-report、/study-notes、/reply-drafts、/plan-my-day のようなスキルとして覚えさせる。Step 2 Memory＝Obsidian VaultにCLAUDE.mdで249ノートをリンクさせて記憶を持たせる。Step 3 Voice＝Whisper（音声認識）とKokoro（音声合成）で、音声は端末内処理。Step 4 Router＝依頼をInstant／Quick／Deepの3段階に振り分ける。Step 5 Dashboard＝localhost:3000/jarvis のWebダッシュボードにワンタップのスキルボタンを並べ、ターミナル不要で使えるようにする。締めは1日の使い方（音声コマンド4例）の紹介で、構築ガイド全文は『JARVIS』とコメントするとDMで送られる配布形式。指定スライド img_index=3（4枚目）は Step 2 Memory のスライドと推定される（スライド単体画像は取得できないため、カルーセル解析の並びからの推定）。既存ノートとの関係: JARVIS構築は @ibraviz.ai（2026-10-30、4パーツ構成）、@juanbertorello.ia『JARVIS OS 2.0』（2026-11-02）、@techwith.ram『Build your own JARVIS』（2026-11-05）が同型で収録済み。本投稿はRouterの3段階分け（Instant／Quick／Deep）、スキルの具体例、CLAUDE.mdで249ノートをリンクする点など細部が新しいため、先行ノートの先例に倣い別作者の構成として新規収録した。
