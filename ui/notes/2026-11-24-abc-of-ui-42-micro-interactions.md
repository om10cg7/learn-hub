# The ABC of UI — マイクロインタラクション42種 Part 01（anside.design）

- 出典：Instagram @anside_design（Design studio、アスタナ）のリール「The ABC of UI」（2026-11-23投稿）
  - https://www.instagram.com/reel/DgFUOPxtOJK/
  - 6列×7行＝42カードの静止インフォグラフィックが、各要素だけ順にアニメーションする構成。内容は動画解析とサムネイル目視で確認し、42種すべてを転記
  - サブタイトルは「MICRO INTERACTIONS 01 — BUTTONS・TOGGLES・LOADERS・DOCS」、「Part 01 | UI Basics」

## 42種

| # | 名称 | # | 名称 | # | 名称 |
|---|---|---|---|---|---|
| 01 | Toggle | 15 | Search Expand | 29 | Stepper |
| 02 | Like Burst | 16 | Notification | 30 | Progress Ring |
| 03 | Spinner | 17 | Star Rating | 31 | Card Flip |
| 04 | Progress Bar | 18 | Range Slider | 32 | Drag to Sort |
| 05 | Checkbox | 19 | Tab Switch | 33 | Swipe Delete |
| 06 | Radio Group | 20 | Grid ↔ List | 34 | Typing... |
| 07 | Download | 21 | Ripple Tap | 35 | Float Label |
| 08 | Upload | 22 | Accordion | 36 | Carousel |
| 09 | Open Folder | 23 | Modal Pop | 37 | Connecting |
| 10 | Doc Preview | 24 | Toast | 38 | Unlock |
| 11 | Dot Loader | 25 | Avatar Stack | 39 | Trash |
| 12 | Skeleton | 26 | Charging | 40 | Copy |
| 13 | Send Button | 27 | Equalizer | 41 | Day / Night |
| 14 | Menu → Close | 28 | Play / Pause | 42 | Bar Chart |

## 学び・所感

- キャプションの主張は「うまくできていれば誰も気づかないが、欠けるとプロダクト全体が平板に感じる」。マイクロインタラクションを装飾ではなく「生きた感じ」の土台として並べた基礎カタログ
- 顔ぶれは入力（Toggle／Checkbox／Radio／Range Slider／Stepper）、フィードバック（Ripple Tap／Like Burst／Toast／Notification）、読み込み（Spinner／Dot Loader／Skeleton／Progress Bar／Progress Ring／Connecting）、状態変化（Menu → Close／Grid ↔ List／Day / Night／Play / Pause）に大別できる。既存の ale.uiux の8種シリーズ（トグル・ボタン等）と重なる要素は多いが、こちらは42種を1枚に集めた索引型
- 「Part 01 | UI Basics」表記なので続編前提のシリーズ。42番 Bar Chart はサムネイルでは線だけの最小表示だった

## 追記（2026-11-25）— 製品版の告知リール

- 同じ作者の別リール（2026-11-24投稿）https://www.instagram.com/reel/DgHiu_WhjZ2/ が、この42種を「そのまま貼れる」製品として告知していたため、別ノートにせずここへ追記
- 訴求点：「UIアニメーションをゼロから作るな」。42種は **Pure HTML + CSS、JavaScript ゼロ**、ワンクリックでコピーできるギャラリー形式、色は CSS 変数で一括変更可、React／Vue／Webflow／WordPress で動作。入手はプロフィールのリンク（価格は投稿内では未確認）
- つまり上の42種カタログは、無料の索引であると同時に、このコピペ用コード集への導線だった
