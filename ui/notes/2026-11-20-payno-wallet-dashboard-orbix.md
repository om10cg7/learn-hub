# ウォレット概要ダッシュボード「Payno」作例（Orbix Studio）

- 出典：Instagram @orbixdashboard（Orbix Studio Dashboard）のカルーセル「Paymo: Wallet Overview Dashboard UI」（2026-11-20投稿、全5枚、いいね33）
  - https://www.instagram.com/p/Df-JT9vlKdz/
  - 製品名はキャプションでは「Paymo」だが、実画面のロゴ（左上・カード面とも）は「Payno」で、本ノートは実画面ベースで Payno と表記する
  - キャプションは設計内容の列挙（Balance and quick action card／Income and expense summaries／Monthly cash flow chart／Digital card and upcoming payments list）で、作者による技法解説・設定値の共有はない。末尾はウォレットダッシュボード制作の DM 営業。コメント4件は称賛のみで作者の補足なし。内容は media-understanding のスライド解析と1枚目の目視で確認
  - 同作者（Orbix Studio）の既存ノート「Coinly 支出分析ダッシュボード」（2026-10-29）、「HRアナリティクスダッシュボード」（2026-01-02）、「Deuce テニス選手ダッシュボード」（2026-11-14）とは別画面・別題材の作例であり、重複ではない

## 内容

個人向けウォレット（財布）の概要を1画面にまとめたフィンテック系ダッシュボードのコンセプト作例。白基調に淡いブルーのシェーディングで、全体に丸みを持たせた静かなトーン。上部にはブルーのグラデーション帯、左端にアイコンのみの細いナビを置く。

スライド構成（全5枚）:

- **1〜4枚目** — ダッシュボード画面（全体表示と別アングル／部分表示）。主な要素は次のとおり
  - Available Balance $56,751.23（Available Limit • $3,600 Left の併記）と Quick Actions（Send／Add Funds／Pay Bills／QR の円形ボタン4つ）
  - Total Income +$86,420.75、Total Expenses -$42,180.30（いずれも -2.4% の小さな変動バッジ付き）を残高カードの横に積む
  - Cash Flow: 月次バー（Jan〜Dec）はほぼ淡色で、選択中の Aug だけ濃紺＋斜線ハッチでハイライトし、Income +$12,412.91／Expenses -$5,215.10 のツールチップを添える
  - 右カラムに Credit Card（Visa のデジタルカードプレビュー）と Upcoming Payments（Electricity $85.00・期限明日／Internet $49.99・3日後／Water $35.00・5日後／Mobile Phone $45.00・10日後／Gas $15.19・10日後）を分離配置。定期支払いをチャート領域に入れず、独立リストとして常時見えるようにしている
  - 右上に Export CSV ボタン
- **5枚目（指定スライド、img_index=4）** — 問い合わせ用 CTA スライド。「次のプロジェクトについて相談しよう」という見出しに、無料15分コールの予約ボタン、WhatsApp の QR コード、電話・メール、Dribbble／Behance／X／LinkedIn へのリンクをまとめた営業スライドで、ダッシュボード画面そのものは含まれない

## 学び・所感

- バーチャートは「全部淡く、選択月だけ濃く＋ハッチ」という強調の付け方で、色数を増やさずに注目点を1か所に絞っている
- Upcoming Payments をチャートと混ぜず独立リストにした分離は、キャプションでも設計意図として明言されている。「定期支払いは時系列グラフとは別物」という情報の性質での切り分け
- 同作者の既存作例（Coinly／HR／Deuce）と同様、新しい用語・技法の提示はないダッシュボード作例のため、先例どおり図鑑カードは追加せずノートのみ。ui の index.html（図鑑専用）も変更なし
