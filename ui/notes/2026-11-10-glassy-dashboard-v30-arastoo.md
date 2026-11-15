# Glassy Dashboard V30（Arastoo / code.xr）

- 出典：Instagram @code.xr（Arastoo）のリール「Glassy Dashboard V30 — Premium Purple & White Design」（2026-11-10投稿）
  - https://www.instagram.com/reel/Dfj_FGsTAVB/
  - 内容は動画解析で確認
  - 同作者のダッシュボード系既存ノート：notes/2026-10-30-glassy-dashboard-v7-arastoo.md（Glassy V7）、notes/2026-11-08-dashboard-v22-arastoo.md（V22／V24）、notes/2026-11-09-dashboard-v25-arastoo.md（V25）、notes/2026-11-12-admin-dashboard-v7-arastoo.md（Admin V7）。いずれとも画面構成・数値が異なる別投稿
  - このチャット（振り分け）経由で受領し、仕分けルール（url_repo_router）で learn-ui 行きと判定して作成

## 内容

グラスモーフィズムの管理ダッシュボードの画面ツアー。キャプションは「Premium Purple & White」とうたうが、動画解析では背景はダークで、紫のグロー accents を効かせたガラスカード群という実画面だった（キャプションと実画面の食い違いは同作者の V22／V24／Admin V7 でもあったパターン）。技術は React.js／CSS3／HTML5 とされ、ソースは「Code」コメントで配布。

動画で切り替わる画面（解析より）:

- 上部タブ：Overview／Sales／Marketing／Support（サイドバーではなく上部ナビ型）
- Overview：Revenue $179k、四半期ターゲットのゲージ 46%、サマリーカード群
- Reports：$23.3k とチャート類
- Deal Pipeline：商談パイプラインのボード
- Customers：アバター付き顧客テーブル
- Products：カラフルなアプリアイコンのグリッド

画面下にはコードエディタが常時表示され、ガラスカード部品が framer-motion の motion と lucide-react を import している（シリーズ共通の見せ方）。

## 学び・所感

- 同作者のダッシュボード系では画面の種類が一番多い版：Overview の指標だけでなく、パイプラインボード／顧客テーブル／プロダクトグリッドまで一巡する。ただし部品と質感はシリーズ共通で、新しい用語・技法の追加はないため、Glassy Dashboard V7 や Admin Dashboard V7 の先例どおり図鑑カードは追加せずノートのみ
- ゲージ（四半期ターゲット46%）は @uxwoodytips「数字を見せる図の名前9種」の Gauge そのもので、ダッシュボード文脈での実例としてつながる
- 上部タブ型（Overview／Sales／Marketing／Support）は、左サイドバー型が続いた同作者の系譜では目先の違う構成
