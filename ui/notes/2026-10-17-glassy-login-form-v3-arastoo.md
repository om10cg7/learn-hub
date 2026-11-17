# グラスモーフィズムのログインフォーム V3（Arastoo）

- 出典：Instagram @code.xr（Arastoo）のリール「Glassy Login Form V3 — Premium Glassmorphism UI」（2026-10-17投稿）
  - https://www.instagram.com/reel/DeoGCPlzKOs/
  - 内容は動画解析で確認。実装は React.js / CSS / JavaScript / Framer Motion（キャプション表記）、ソースコードは「Code」コメントで配布の形式
- 関連：notes/2026-11-12-lamp-login-v5-arastoo.md（同じ作者のログインフォームだが、ランプの光でフォームが現れる演出が主役で別物）

## 中身

- 暗い抽象背景に青い光の筋が流れる画面の中央に、半透明のガラスカードを置いた認証 UI
- ログイン面「Welcome Back」：Email Address、Password、「Remember me」チェックボックス、「Forgot password?」リンク、青い「Sign In」ボタン、Google / Apple のソーシャルログイン
- 「Sign Up」をクリックするとカードが滑らかにフリップ（反転）して、新規登録面「Create Account」に切り替わる：Full Name、Email、Password、Confirm Password、規約チェックボックス、「Create Account」ボタン。反転してもう一度ログイン面へ戻る
- 画面下部には React / TypeScript のコードエディタが常時表示される、この作者のシリーズ共通の型（lucide-react の import が見える）

## 学び・所感

- ログインと新規登録を別ページに分けず、1枚のカードの表裏で切り替える構成。フリップという物理的な動きが「同じ場所で状態だけ変わる」ことを直感的に伝える
- ガラス質感は、暗くて情報量のある背景（光の筋）があって初めて透け感が読める、というこの作者のグラス系作例に共通する前提がここでも効いている
- グラスモーフィズムは図鑑収録済みの用語で、新しい用語・技法の提示はないため、図鑑カードは追加せずノートのみ（同作者のダッシュボード／サイドバー変種の先例どおり）
