# 小売ストア売上ダッシュボード「Corbel Supply Co.」（_code_and_chill_）

- 出典：Threads @_code_and_chill_ の投稿（2026-10-23投稿、動画、いいね1,966）
  - https://www.threads.com/@_code_and_chill_/post/De13rnmiW-W
  - キャプションは「Retail store sales dashboard 📊 #dashboard #analytics #typescript #webdesign #frontend」のみ。コメント欄は感想・質問のみで、作者による技法解説・プロンプト配布・設定値の共有はない。内容は動画の代表フレーム（サムネイル）を目視して記録する
  - 共有リンク https://www.threads.com/share/_jtPIup5rX 経由で受領し、仕分けルール（url_repo_router）で learn-ui 行きと判定して作成

## 内容

小売店の売上を追うダッシュボードの画面デザイン作例（動画デモ）。白基調フラットで、角丸カード＋淡いグレーの背景。黒いカードを2枚だけ混ぜて引き締める構成。

画面構成（代表フレームより）:

- **上部ナビ** — 左にロゴ＋「Corbel Supply Co.」。中央に Dashboard（黒ピルでアクティブ）／Orders 14／Products／Customers／Messages 3／Analytics／Automations（件数バッジ付き）。右端に設定アイコン、アバター（MR）、「● 1,284 live now」のライブ指標
- **左端アイコンレール** — 黒い縦長ピル型に検索、グリッド、メッセージ、グラフ、設定ギア、ユーザー等のアイコンを集約
- **ヘッダー行** — タイトル「Dashboard」。タブは Overview／Online／In store（チャネル切替）。右に「October 2026, month to date」の期間表示と Full analytics／Export（黒）ボタン
- **KPIカード×4** — いずれも前月比の増減を併記し、カード下部に次の導線リンクを持つ:
  - Active sales $25,018（↑14.2% vs last month、ミニ棒グラフ付き、黒カード）→ See orders
  - Revenue $20,451（↑7.6%）→ See analytics
  - Units sold 1,989（↑6.4%、「+389」ピル）→ See products
  - Conversion rate 2.5%（↓0.2pt）→ See funnel
- **Sales performance（黒カード）** — 半円ゲージで「0 of 100 points（+3）」。見出し「Ahead of plan」に「Both channels beat last month. Online did most of the lifting」と、数値の背景を一文で添える
- **Revenue パネル** — 「Revenue $300,000 so far for the year」。右上に 2025／2026 の年切替

## 学び・所感

- KPIカードに「前月比＋次に見る画面への導線（See orders／See funnel）」をセットで埋め込み、指標から行動へそのまま流れる情報設計が主題。チャネル別タブ（Online／In store）と live now 表示で「小売の今」を切り取る構成
- 新しい用語・技法の提示はないダッシュボード作例のため、先例（Crestway／Admin Dashboard V7／Glassy Dashboard V30／Ember Dashboard V29／Furniture CRM）どおり図鑑カードは追加せずノートのみ
