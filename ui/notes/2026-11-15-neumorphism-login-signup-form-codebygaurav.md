# ニューモーフィズムのログイン／サインアップフォーム（CodeByGaurav）

- 出典：Instagram @clasyy.shop のリール（2026-11-15投稿、いいね約80、約8秒）
  - https://www.instagram.com/reel/DfwnQp5CaGt/
  - 内容は動画解析とサムネイル（img_index=0、動画のベストフレーム）の目視で確認
  - 注意：投稿アカウントはダッカの下着・水着ショップで、キャプションも店舗販促の定型文で動画内容と無関係。動画本体は CodeByGaurav の「Login & Sign Up Form UI」で、VS Code のタイトル表示とブラウザのブックマーク（@code_by_gaurav）から特定できる転載型の投稿のため、実画面ベースで記録した
- 関連：notes/2026-10-17-glassy-login-form-v3-arastoo.md（ログイン⇔新規登録を1枚のカードで切り替える同型の構成）、notes/2026-10-26-neumorphism-guideline.md（ニューモーフィズムの影の作り方）

## 中身

- 上半分はブラウザ（localhost）で表示した白基調のログインフォーム。背景に白い円が柔らかく浮き出すニューモーフィズム風の造形で、中央のカードに鍵アイコン、「Welcome／Login to continue your journey」、Email Address、Password（目のアイコン付き）、Remember me チェックボックス、Forgot Password? リンク、Login ボタン
- カード下部の「Don't have an account?」の横にある丸い「＋」ボタンを押すと、Create Account フォーム（Full Name／Email Address／Password／Confirm Password）にアニメーションで切り替わり、もう一度押すとログイン面へ戻る。メール欄ではオートコンプリートのドロップダウンも出る
- 下半分は VS Code の index.html（style.css／script.js のタブもあり）。bg-circle の div 群など背景の円の構造が見える。「Get the Complete Source Code / Check the Description!」のテロップで、完全なソースコードは説明欄へ誘導する形式
- BGM のみでナレーションなし

## 学び・所感

- ログインと新規登録を1枚のカードで切り替える発想は Glassy Login Form V3（フリップ反転）と同型。こちらは切り替えの合図が「＋」という最小の記号で、質感はニューモーフィズムの柔らかい影で統一している点が違い
- ニューモーフィズムは図鑑収録済みの用語で、新しい用語・技法の提示はないため、図鑑カードは追加せずノートのみ（ログインフォーム変種の先例どおり）
- キャプションと実画面が食い違う投稿だったので、仕分けと記録は実画面を優先した
