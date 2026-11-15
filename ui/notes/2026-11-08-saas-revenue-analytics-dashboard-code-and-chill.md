# SaaS収益分析ダッシュボード（_code_and_chill_）

- 出典：Instagram @_code_and_chill_（Code & Chill）のリール（2026-11-08投稿、動画約5秒、いいね5,870、コメント329）
  - https://www.instagram.com/reel/DffBnb2vlUn/
  - キャプションは「SaaS revenue analytics dashboard 📈 #dashboard #dataviz #analytics #uidesign #Frontend」のみ。作者による技法解説・設定値の共有はなく、テンプレート製品のデモ／販促動画。内容は動画の内容解析とカバーフレームの目視で記録する
  - 仕分けルール（url_repo_router）で learn-hub の ui 行きと判定して作成。同作者のダッシュボード作例「Corbel Supply Co.」（2026-10-23、別ノート）「Cirrel」（2026-11-03、別ノート）とは別投稿・別デザイン

## 内容

SaaSの収益分析ダッシュボードの画面デザイン作例（動画デモ）。ダーク基調のWeb分析アプリを、左サイドバーをカーソルで切り替えながら見せる構成。

カバーフレーム（販促カバー）:

- 「REVENUE DASHBOARD ANIMATION／REACT + TYPESCRIPT」のタイトルと、「Watch MRR grow!」の吹き出し
- 「Live」バッジ付きの収益カード「$48,785」＋波形のレイヤードエリアチャート（黄→水色→青のグラデーション）
- 訴求バッジ4つ：CLEAN CODE（Well Structured）／SMOOTH ANIMATION／MODERN UI（Frosted Glass）／FULLY RESPONSIVE

動画本編で切り替わる3ビュー:

- **Funnels** — コンバージョン指標とファネルチャート
- **Campaigns** — キャンペーン実績カードと収益データ（$10,096）
- **Cohorts** — リテンション表とコホート分析グラフ
- 画面下にはコードエディタも映り、`src/animation.ts` の GSAP を使ったスライドアニメーション関数（slideFit）が見える。実装は React + TypeScript

## 学び・所感

- 分析ダッシュボードの情報設計の型：左サイドバーで Funnels／Campaigns／Cohorts と「集客→施策→定着」の分析軸ごとにビューを分け、各ビューは指標カード＋チャート／表に統一している
- カバー側は「MRR の伸び」を1枚の収益カードと波形チャートで象徴させる販促構成で、Frosted Glass やスムーズアニメーションを売りにしている（コメント欄では見た目の評価が高い一方、実用性や価格への言及もあり）
- 新しい用語・技法の提示はないダッシュボード作例のため、先例（Corbel／Cirrel／Crestway／Morphin／Admin Dashboard V7／Glassy Dashboard V30／Ember Dashboard V29／Furniture CRM）どおり図鑑カードは追加せずノートのみ
