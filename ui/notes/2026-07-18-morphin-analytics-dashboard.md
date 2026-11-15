# 分析ダッシュボードのマイクロインタラクション作例（Morphin.dev）

- 出典：Threads @morphin.dev（Morphin.dev）の投稿（2026-07-18投稿、動画、いいね274）
  - https://www.threads.com/@morphin.dev/post/Da9Msx7gMPU
  - キャプションは「Dashboards don't have to be boring. Small interactions make analytics feel premium. React + Tailwind + shadcn/ui.」のみ。コメントは0件で、作者による技法解説・プロンプト配布・設定値の共有はない。内容は動画の代表フレーム（サムネイル）を目視して記録する。なおサムネイルはフェード遷移途中のフレームで全体が淡く写っており、細部は判読できた範囲に限る
  - 共有リンク https://www.threads.com/share/BAWg72ru7_ 経由で受領し、仕分けルール（url_repo_router）で learn-ui 行きと判定して作成

## 内容

自動化ワークフローの実行状況を追う分析ダッシュボードの画面デザイン作例（動画デモ）。白基調で余白を広く取ったミニマルな構成。主題はキャプションのとおり「小さなインタラクションで分析画面をプレミアムに見せる」こと。

画面構成（代表フレームより）:

- **Performance trend** — 月別（Jan〜Dec）の折れ線グラフ。ホバーで縦ガイド線＋ツールチップ（「Apr 30, 2026／328」）が出るインタラクションが見える。右上に「Executions」の切替ドロップダウン
- **KPIカード×4** — いずれも前月比の増減を小さく併記:
  - Prod executions 320（+5% vs last month）
  - Failed executions 28（-4.3% vs last month）
  - Failure rate 2.4%（+0.3% vs last month）
  - Time saved 18.4 hrs（-1.3% vs last month）
- 実装スタックは React + Tailwind + shadcn/ui（キャプション表記）

## 学び・所感

- グラフのホバーツールチップのような小さな反応を積み重ねて「退屈なダッシュボード」を上質に見せる方向性の作例。KPIカードは数値＋前月比だけの最小構成で、余白と淡い罫線で情報の階層を作っている
- 新しい用語・技法の提示はないダッシュボード作例のため、先例（Corbel／Crestway／Admin Dashboard V7／Glassy Dashboard V30／Ember Dashboard V29／Furniture CRM）どおり図鑑カードは追加せずノートのみ
