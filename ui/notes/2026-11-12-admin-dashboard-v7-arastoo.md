# Admin Dashboard V7（Arastoo / code.xr）

- 出典：Instagram @code.xr（Arastoo）のリール「Admin Dashboard V7」（2026-11-12投稿）
  - https://www.instagram.com/reel/Dfoqc5PzYZW/
  - 内容は動画解析で確認。キャプションは「Premium Purple & White Design」「Beautiful Glassmorphism Effects」をうたうが、動画解析ではダークテーマの画面として読み取れており、キャプションと実画面の配色が食い違う（同作者では V22／V24 でも同じ食い違いがあった）。動画内タイトルは「Admin Dashboard V7」
  - 既存の同名・近似ノートとは別物：notes/2026-10-30-glassy-dashboard-v7-arastoo.md（Glassy Dashboard V7。写真背景＋Revenue $99,560）、notes/2026-11-09-dashboard-v25-arastoo.md（V25。「Hi, James!」＋CRM パイプライン）。本作は挨拶の人物・数値・画面構成（Plans 画面）がいずれも異なる
  - このチャット（振り分け）経由で受領し、仕分けルール（url_repo_router）で learn-ui 行きと判定して作成

## 内容

管理ダッシュボードの画面ツアー。左サイドバー（Overview／Analytics／Customers／Products／Orders／Revenue／Settings）を持ち、技術は React.js／CSS3／HTML5 とされ、ソースは「Code」コメントで配布。

動画で巡る画面（解析より）:

- **Overview** — 「Good afternoon, Maya」の挨拶＋指標カード（Revenue $4,483、Orders 135、AOV $33.62、Conversion rate 0.33%）、売上チャート、月間ゴールゲージ 43%
- **Analytics** — Revenue $9,879、Orders 273、Visitors 72,255 と棒グラフ群
- **Plans** — $9／$29／$99（月額）の3段サブスクリプション料金表

画面下にはコードエディタが常時表示され、lucide-react と framer-motion の import が見える（シリーズ共通の StatCard テンプレートの型）。

## 学び・所感

- V22→V25 と続く同作者のダッシュボード量産シリーズの新バリエーション。差分は人物（Maya）と数値、Plans（料金表）画面が入った点程度で、新しい用語・技法の追加はないため、先例（Glassy Dashboard V7／V25）どおり図鑑カードは追加せずノートのみ
- 「V7」の名乗りが Glassy Dashboard V7 と重なるが中身は別物。番号とタイトルだけではシリーズ内の同一性が判定できない点は、作者の量産形式の特徴として記録する
- キャプションの配色表現（紫×白・グラスモーフィズム）と実画面（ダークテーマ）の食い違いも含め、宣伝文句ではなく映像の中身で記録するのがこの作者のノートの原則
