# SaaSダッシュボード「Crestway Air & Heat」（nizam.design）

- 出典：Threads @nizam.design（Saas & AI Product Designer）の投稿（2026-09-28投稿、単一画像）
  - https://www.threads.com/@nizam.design/post/Dd0prmPn7kV
  - キャプションは「SAAS UXUI Design.」のみ。コメント欄（6件）は「How did you do it?」等の感想のみで、作者による技法解説・プロンプト配布・設定値の共有はない。内容は投稿画像を目視して記録する
  - 共有リンク https://www.threads.com/share/BAYc-a0IXhE 経由で受領し、仕分けルール（url_repo_router）で learn-ui 行きと判定して作成

## 内容

複数拠点ビジネスの買収・統合（ボルトオン）計画を管理する SaaS ダッシュボードの画面デザイン作例。白基調フラットで、角丸カードと淡いグレーの背景。

画面構成（画像より）:

- **左端アイコンレール** — ロゴ、グリッド、メッセージ（バッジ3）、ビル（選択中）、タスク（バッジ17）、グラフ、ドキュメント、ベル、設定ギア
- **ツリー型サイドバー** — Search（⌘K）。FAVORITES（Crestway ★／Merritt／Bluestem）と BOLT-ONS の2セクション。BOLT-ONS 配下は企業リストで、Crestway（バッジ2、選択中）を展開すると拠点ツリー（Charlotte HQ／Concord／Gastonia／Rock Hill、各行にチェックボックス）。各企業行には色付きの図形マーカー（橙・緑・赤の ○△□）で状態を併記。Merritt にはバッジ1
- **メインエリア** — タイトル「Crestway Air & Heat」にアンバー色の「At risk」ステータスピル。拠点のパンくず（Charlotte HQ / Concord / Gastonia / Rock Hill、チェックボックス付き）
- **タブ** — Overview／Plan（アクティブ）／Financials／Issues 7（件数付き）／People
- **タイムライン（Plan）** — 表示切替は Weeks／Months／Gates／Today のセグメント。Day 0（Jun 30）→Day 30（Jul 30）のガント風バーで、ワークストリームごとにカテゴリチップ＋担当者を付けて整理：
  - Financial（緑チップ、Michael Lee）— Bank and data access（Done）、First close on Intacct、5-day month-end close
  - People（紫チップ、Hannah Price）— Offers and retention（Done）、Payroll migration（行ハイライト）、Pay policy harmonized
  - Operations（橙チップ、Ray Castillo）— Price book alignment、Dispatch consolidation
  - Technology（青チップ、担当者あり）

## 学び・所感

- 統合計画の進捗を「カテゴリチップ×担当者×ガントバー」で1画面に圧縮した情報設計が主題。ツリー側は「図形＋色」の状態マーカーと件数バッジで、展開しなくても全体の異常（At risk、Issues 7）が読める
- 新しい用語・技法の提示はないダッシュボード作例のため、先例（Admin Dashboard V7／Glassy Dashboard V30／Ember Dashboard V29／Furniture CRM）どおり図鑑カードは追加せずノートのみ
