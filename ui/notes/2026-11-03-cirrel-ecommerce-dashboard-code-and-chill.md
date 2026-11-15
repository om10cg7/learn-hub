# ECストア管理ダッシュボード「Cirrel」（_code_and_chill_）

- 出典：Threads @_code_and_chill_ の投稿（2026-11-03投稿、動画、いいね906）
  - https://www.threads.com/@_code_and_chill_/post/DfR0jrCCZBt
  - キャプションは「E-commerce store admin dashboard 🛒 #ecommerce #javascript #uianimation #webdesign #frontend」のみ。コメント0件で、作者による技法解説・プロンプト配布・設定値の共有はない。内容は動画の代表フレーム（サムネイル）を目視して記録する
  - 共有リンク https://www.threads.com/share/BAYSj2R9qO 経由で受領し、仕分けルール（url_repo_router）で learn-ui 行きと判定して作成
  - 同作者の小売ダッシュボード作例「Corbel Supply Co.」（2026-10-23、別ノート）とは別投稿・別デザイン

## 内容

ECストアの管理ダッシュボードの画面デザイン作例（動画デモ）。ダーク基調のUIで、背景にオレンジ／グリーン／ブルーの大きなグラデーション球体（オーロラ状のぼかし）を浮かせ、半透明のダークカードを重ねる構成。

画面構成（代表フレームより）:

- **左サイドバー** — ロゴ「Cirrel」＋検索欄。セクション見出しで機能を分類：SHOP（Dashboard／Orders バッジ3／Products／Analytics）、MONEY（Customers／Finances／Invoices／Discounts）、TALK（Chats／Email ほか）
- **ヘッダー行** — 「Good morning, Noor」＋「Sunday, November 1 · Dashboard」。右に検索・通知アイコンと「+ Create」ボタン（青ピル）
- **売上サマリーカード** — 「Today so far $207（+138% vs last Sunday）」「Last 7 days $4,946（+9.8% vs the week before）」など、指標ごとに対比相手を明示する見せ方
- **Sales studio** — 「$212,316 in this range（+28% on the same stretch before）」。期間切替ピル Last year／12M／6M／30D／7D と月次エリアチャート
- **右カラム** — 「November goal」カード：進捗リング「1% of $244」、Booked $244／Daily pace needed $792／October finished $24,477 と、目標までのペースを数値で示す。「Live store」カード：「38 on the site」の大数字＋バー表示、Carts open／Converting 30 days 2.5%／Top page「Ceremonial Matcha」、「Checkout healthy」の緑ステータス表示

## 学び・所感

- 指標の見せ方が主題：売上は「前週同曜日比」「前期間比」と対比相手を必ず添え、目標カードは達成率だけでなく「1日あたり必要なペース（Daily pace needed）」まで出す。ライブ来訪者数（38 on the site）と決済の健全性（Checkout healthy）で「今の店の状態」を右カラムに集約している
- 同作者の Corbel（白基調フラット）とは対照的なダーク＋グラデーション球体の世界観で、同じEC/小売ダッシュボードでもトーンの振り幅を見せる作例
- 新しい用語・技法の提示はないダッシュボード作例のため、先例（Corbel／Crestway／Morphin／Admin Dashboard V7／Glassy Dashboard V30／Ember Dashboard V29／Furniture CRM）どおり図鑑カードは追加せずノートのみ
