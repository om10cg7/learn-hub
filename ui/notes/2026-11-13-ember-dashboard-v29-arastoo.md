# Ember Dashboard V29（Arastoo / code.xr）

- 出典：Instagram @code.xr（Arastoo）のリール「Ember Dashboard V29」（2026-11-13投稿）
  - https://www.instagram.com/reel/DfrtgFyTmOM/
  - 内容は動画解析で確認。動画内タイトルは「Dashboard V29」。キャプションは「Beautiful Coral & White Theme」「Modern Glassmorphism Design」をうたう。配色（白背景＋コーラル／赤のアクセントカード）は実画面とおおむね一致するが、グラスモーフィズム的な半透明表現は解析では目立たず、白基調のフラットなカード中心だったため、実画面ベースで記録する
  - 既存の同作者ダッシュボード群とは別物：V22（淡い緑×白、チーム／プロフィール画面）、V25（「Hi, James!」のCRM風）、Admin Dashboard V7（ダークテーマ＋Plans料金表）、Glassy Dashboard V30（上部タブ型）。本作は挨拶の人物（Daniel）・数値・画面構成（Tasks／Messages）がいずれも異なる
  - このチャット（振り分け）経由で受領し、仕分けルール（url_repo_router）で learn-ui 行きと判定して作成

## 内容

管理ダッシュボードの画面ツアー。黒背景のステージ上に画面が切り替わり、技術は React.js／CSS3／HTML5 とされ、ソースは「Code」コメントで配布。

動画で巡る画面（解析より）:

- **メイン（Overview相当）** — 「Good afternoon, Daniel」の挨拶＋指標（$470K closed、pipeline slope $454K）
- **Saved** — カードサムネイルの一覧
- **Tasks** — タスク件数とリスト
- **Messages** — 会話スレッド形式のメッセージ画面

画面下にはコードエディタが常時表示され、framer-motion と lucide-react の import が見える（シリーズ共通の型）。

## 学び・所感

- 同作者のダッシュボード量産シリーズの新バリエーション。今回の差分はコーラル×白の配色と Tasks／Messages 画面で、新しい用語・技法の追加はないため、先例（Admin Dashboard V7／Glassy Dashboard V30）どおり図鑑カードは追加せずノートのみ
- Saved 画面は V22 の「Saved for later」と響き合うが、レイアウト・数値は別物。シリーズ内の画面モジュールの使い回しと差し替えの組み合わせとして記録する
- キャプションと実画面の関係は、今回は配色についてはほぼ一致し、質感表現（グラスモーフィズム）だけが宣伝側に寄っていた。引き続き映像の中身で記録する
