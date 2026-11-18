# 19. Mac Photo Booth風ウェブカメラ・セルフィー（The webcam diaries）

- 投稿者: XOXO ♡ @xohesox
- 投稿: https://www.threads.com/@xohesox/post/Dfrh8RuGKzY （2026-11-13、キャプション「The webcam diaries 📷💻」、カルーセル16枚、いいね約2,055 ※取得時点、音楽は Fergie「Clumsy」）
- 共有リンク: https://www.threads.com/share/BAXfjcloQ4
- プロンプトは投稿本文ではなく、作者本人のピン留め返信（ https://www.threads.net/t/Dfrh8B-GAXV ）に全文掲載（英語）
- 作例16枚はすべて同じ女性の Mac「Photo Booth」風スクリーンショット。画像は代表として1枚目を取得し、残り15枚は目視確認のうえ要約に反映した

## 要約

「写真」ではなく「アプリ画面のスクリーンショット」そのものを生成させるプロンプトの配布。核は、Mac の Photo Booth の UI を丸ごと指定すること:

- **UI の指定**: 白いタイトルバー（左に赤・黄・緑の信号ボタン、中央に「Photo Booth」の文字）、下部に小さなサムネイル7枚が並ぶ帯、赤い丸いカメラボタン（作例では右下に「Effects」の文字も再現されている）
- **MAIN FRAME**: 接写・ややハイアングルのノートPCウェブカメラ・セルフィー。柔らかく低解像度で、わずかな粒子感のある画質まで指定
- **HAIR -OUTFIT-MAKEUP DETAIL**: ロングで滑らかなチョコレートブラウンの髪（センター分け）、べっ甲の丸いクリアレンズ眼鏡（画面の反射入り）、太めの眉、スモーキーブラウンの跳ね上げアイライナー、バラ色の頬、つやのあるヌードピンクのぽってりした唇、クリスタルのフラワーイヤリング。黒いストラップレストップス（片肩が見える）、濃いネイビーのネイル、ソファやベッドにもたれてウェブカメラへ寄る姿勢、視線は画面の外へ
- **LIGHTING & MOOD**: ノートPCの画面の明かりだけが灯る薄暗い部屋。暖かい肌色と暗いグレイグリーンの背景、柔らかいハイライト、浅い被写界深度、わずかなビネット、やや彩度を落とした色で、親密でくつろいだウェブカメラの空気を作る

作例16枚は、眼鏡あり／なし、歯を見せた笑顔、唇を突き出す、指先で下唇に触れる、あごに手を添える等のバリエーション。プロンプト本文では眼鏡が標準指定だが、作例には眼鏡なしのカットも多い。作者はコメント欄で「Gemini で使う場合は 4:3 のアスペクト比指定を足すとよい」と補足している。返信は110件あり、多くが同じプロンプトで作った利用者の作例で、参加型の配布として回っている。

## プロンプト（原文ママ、本人のピン留め返信より）

```text
Ultra-realistic nostalgic 2010s Mac Photo Booth screenshot, featuring a white window title bar labeled “Photo Booth,” seven small thumbnail previews along the bottom, and a camera button.

MAIN FRAME: A close-up, slightly high-angle laptop webcam selfie with soft, low-resolution, subtly grainy quality.

HAIR -OUTFIT-MAKEUP DETAIL:
A young woman with long, sleek, chocolate-brown hair and a clean center part, wearing round tortoiseshell clear-lens glasses with visible screen reflections. Defined thick brows, soft smoky-brown winged eyeliner, glowing rosy cheeks, glossy nude-pink pouty lips, and sparkling crystal flower earrings.
She wears a black strapless top, with one bare shoulder visible, casually leaning close to the webcam while resting on a couch or bed. Dark navy nail polish, relaxed off-camera gaze, effortlessly chill expression.

LIGHTING & MOOD: Dim room illuminated only by the laptop screen glow, warm skin tones against a dark grey-green background. Soft creamy highlights, shallow depth of field, subtle vignette, slightly desaturated colors, and an intimate, cozy, candid webcam aesthetic.
```

## 取得方法の注記

- ピン留め返信は threads-cli のコメント取得では本文が空で返ったため、ブラウザで投稿ページを直接開き、表示テキストから全文を回収した（返信の冒頭には「✨prompt」の見出しが付く）
- 画像は投稿ページの PDF から代表1枚を抽出した。残り15枚はブラウザのメディアビューアで1枚ずつ目視確認した
