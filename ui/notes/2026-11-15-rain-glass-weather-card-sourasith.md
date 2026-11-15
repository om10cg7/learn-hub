# 曇りガラスを拭う天気カード「Rain Glass Weather Card」（sourasith.design）

- 出典：Instagram @sourasith.design（Pommy Sourasith、DesignCode の UI/UX デザイナー）のリール「RAIN GLASS WEATHER CARD」（2026-11-14投稿）
  - https://www.instagram.com/reel/DfuVhXGOrNr/
  - キャプション要旨：「次のプロジェクトに向けた変わったアイデアの実験。曇り窓そのものが天気カードで、カーソルでガラスを拭うと拭えて、放っておくとゆっくりまた曇る」。プロフィールのリンク先で実際に触れるデモあり。ハッシュタグは #uidesign #webgl #creativecoding #interactiondesign
  - 内容は動画解析とサムネイルで確認

## 画面の内容（2バリエーション）

| 編 | テーマ | 表示 |
|---|---|---|
| Lisbon | ライト | "Rainfall afternoon"、大きな 14° と "Light rain"、下部に時間別予報（NOW 14°／17H 14°／18H 13°／19H 12°／20H 12°） |
| Kyoto | ダーク | "Showers until dawn"、9°。ぼやけた街の明かりが背景 |

- どちらの編も、カード全面が雨粒のついた曇りガラスに覆われて気温などの情報が隠れている。カーソル（手のポインタ）で拭った部分だけ水滴が取れ、気温・天気テキスト・背景の街並みが現れる

## 学び

- 「曇り＝情報が隠れた状態」そのものが雨天の表現になっているのが要点で、状態表示と操作対象が一体化したインタラクション
- 拭うという身体的な操作を挟むことで、天気という日常データに触感と遊びが生まれる。放っておくと自動で曇り直すため、「また拭く」ループが続く
- 既存のガラス質感系（グラスモーフィズム等）が「見た目」の質感なのに対し、こちらは「拭う」操作と時間経過（再曇り）まで含めた動きの設計なので、質感ではなく動き・UX原則のカテゴリで収録
- AI への指示でも "rain glass / foggy window wipe interaction" のように名前で指定できる
