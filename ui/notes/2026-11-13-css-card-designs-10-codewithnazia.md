# CSSカードデザイン10種（codewithnazia）

- 出典：Instagram @codewithnazia（CodewithNazia）の単体画像「10 Beautiful CSS Card Designs — Modern / Responsive / Clean」（2026-11-13投稿）
  - https://www.instagram.com/p/Dfr1NZ5lZIX/
  - 全カードを画像から目視転記

## 10種

| # | スタイル | CSSの要点 |
|---|------|------|
| 1 | Classic Card | 白背景・角丸12px・柔らかい影。hoverで `translateY(-5px)` |
| 2 | Gradient Card | `linear-gradient(135deg, #667eea, #764ba2)` の面そのものが主役。白文字＋ピルボタン |
| 3 | Glassmorphism Card | `background: rgba(255,255,255,0.15)`＋`backdrop-filter: blur(12px)`＋1px半透明ボーダー |
| 4 | Neumorphism Card | 背景 `#e0e5ec` と同化させ、二重シャドウ（暗 `#c9d1d9`／明 `#ffffff`）で押し出し感 |
| 5 | Border Gradient Card | `border: 2px solid transparent`＋`background-clip: padding-box`、グラデーション枠は `::before` で敷く |
| 6 | Dark Card | 背景 `#1e1e1e` のダーク面＋上部に写真ヘッダー。hoverで浮く |
| 7 | Hover Lift Card | 持ち上がり専用設計：hoverで `translateY(-10px)` と影の拡大、`transition: all 0.3s ease` |
| 8 | Split Card | `display: flex` で左右分割。左は色面＋商品画像、右はテキストと価格・ボタン |
| 9 | Blog Card | 記事カード型：画像＋日付バッジ＋タイトル＋抜粋。hover lift 付き |
| 10 | Minimal Card | 影は `rgba(0,0,0,0.06)` まで薄く、余白と中央寄せで見せる |

Pro Tip（シート末尾）：モダンな CSS テクニックでカードを印象的に。

## 学び

- カードの「スタイル」はほぼ box-shadow・背景・角丸・hover の translateY の組み合わせで決まる、という分解ができるシート。1・7・9 は同じ浮き上がりでも度合い（-5px／-10px）と影の広げ方が違う
- グラスモーフィズムとニューモーフィズムは図鑑収録済みの質感用語だが、ここでは「カードという部品への当て方」として並ぶ。背景と同化させる（ニュー）／背景を透かす（グラス）という対比が1枚で掴める
- Border Gradient は `border-image` を使わず、透明ボーダー＋background-clip＋擬似要素で枠だけにグラデーションを回す実務テクニックとして拾える
