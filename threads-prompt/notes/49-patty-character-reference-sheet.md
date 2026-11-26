# 49. アップロード画像から作るキャラクター設定資料シート（Character Reference Sheet）のプロンプト（@p______patty）

- 元ネタ: https://www.threads.com/@p______patty/post/DgFJr-9ko_p （共有リンク https://www.threads.com/share/BAYYR1TV3X から解決）
- 投稿日: 2026-11-23
- 投稿者: MS. Patty 巴蒂小妹 @p______patty（AI 创作实验室。プロフィール表記は Prompt｜工具｜实测｜种草）
- 投稿本文: 「从人物五官、发型、服装,到不同角度和表情，一张图整理好，让AI 更容易保持角色一致，减少人物跑脸、造型乱变的问题! Save this prompt & try it yourself」（五官・髪型・服装から角度・表情までを1枚に整理し、AI がキャラの一貫性を保ちやすくして、顔崩れや造形のブレを減らす、という趣旨。中国語）
- プロンプト: 作者本人の直接返信（https://www.threads.net/t/DgFJvmskksh ）に掲載。コメント取得では返信本文が空で返ったため、作者の投稿一覧の native_features（SNIPPET）から全文を復元（コピーボタン対象）
- 添付画像: 作例のキャラクターシート1枚（画像そのものは取得できなかったため、見た目はキャプションとプロンプト原文からの読み取り）

## プロンプトの構成（要旨）

- 全体: アップロードした画像を唯一の参照として、プロ仕様の「Character Reference Sheet」（キャラクター設定資料シート）を1枚生成させる英語プロンプト
- IDENTITY LOCK: 全パネルで同一人物を厳守。顔の形・五官の比率・目・眉・鼻・口・肌色・髪色・髪型・髪の長さ・体型・身長比・年齢感・ほくろやタトゥー等の特徴点まで同一に保ち、顔・性別・年齢・民族の変更や特徴の追加・削除を禁止
- STYLE LOCK: 元画像の画風を検出して全体に統一。実写なら写実的な写真表現（自然光・肌の質感・髪の毛流れ）、3D なら同じレンダリング調、アニメ／イラストなら同じ線と塗りを維持し、スタイルの混在を禁止
- AUTO-ANALYSIS: 描画前に性別・年齢層・民族／種族・顔と目の形・髪・肌・体型・衣装・特徴を自動分析し、全パネルと Basic Profile のテキストに反映させる
- OUTFIT: 元画像の衣装を「Base Outfit」とする。顔や上半身だけの画像なら、キャラの雰囲気に合う簡素な衣装を補完して全パネルで統一
- LAYOUT: 白〜淡ベージュ背景のグリッド配置。ラベルは英語のみ（中国語等の混入禁止）、文字は読みやすく、要素の重なりなし
- SECTIONS（英語タイトル固定の9部構成）: 1. Basic Profile（名前プレースホルダ・性別・年齢層・身長・体型・髪・目・肌・性格とスタイルのキーワード）／2. Full-Body Angles（正面・側面・背面・前寄り3/4・後ろ寄り3/4）／3. Face Angles（正面・45°・横顔・やや上から・やや下から）／4. Expressions（無表情・優しい笑顔・真剣・驚き・困り顔）／5. Hair Details（前・横・後ろ）／6. Facial Features（目・眉・鼻・口・耳）／7. Skin Texture（顔・身体。非実写は陰影や素材感で代替）／8. Body Details（肩・腹部／胴・背中・脚・手）／9. Everyday Outfit & Scene Examples（部屋着・カジュアル・カフェ・仕事／学校・旅行）
- QUALITY／NEGATIVE: 自然で柔らかい光・正確な解剖学と比率・シャープな細部を要求し、ネガティブ指定として顔の変化・顔のドリフト・髪型や髪色の変更・体型変更・年齢の不一致・指の過多・手の歪み・スタイル混在・中国語や英語以外のテキスト・文字のぼやけや綴りミス・透かしを列挙

## 要点

- プロンプト配布そのものが主題（キャプション「Save this prompt & try it yourself」＋作者返信で全文配布）のため threads-prompt へ仕分け。写真の撮影・編集技法の解説ではないため ai-picture には入れない
- 核は「キャラ設定資料を先に1枚作らせる」ことで、漫画・動画・続編画像の生成時に顔や造形がブレる問題（跑脸）を抑えるワークフロー。プロンプト自体が IDENTITY LOCK／STYLE LOCK という2つの固定ルールと、分析→シート化の手順まで含む設計になっている
- コメント欄では Meta AI が「キャラを固定して生成ごとに変わらないようにするためのもの」と要約して解説しているほか、「一番下の行はあまり役に立たない、服装が不完全で結局キャラが一致しない。もっと細部を渡した方がいい」という批判的な利用者コメントもあり、万能ではない点も読み取れる（投稿内表記）

## プロンプト全文（原文ママ、作者本人の返信の SNIPPET より復元）

```text
Strictly use the uploaded image as the sole reference and create a professional "Character Reference Sheet".

CORE RULE – IDENTITY LOCK:
Every image on the sheet must show the exact same character as the uploaded image. Keep identical: face shape, facial feature proportions, eyes, eyebrows, nose, mouth, skin tone, hair color, hairstyle, hair length, body type, height proportions, age appearance, and any distinctive marks (moles, scars, freckles, tattoos, piercings, glasses, accessories, horns, ears, tail, etc.). Do not change the face, do not change gender, age, or ethnicity, and do not add or remove features.

STYLE LOCK:
Detect the art style of the uploaded image and keep it consistent across the whole sheet.

- If it is a real person: realistic photography, natural light, real skin texture, individual hair strands, realistic body proportions, no anime look, no CG look, no over-smoothing.
- If it is a 3D character: keep the same 3D render style, materials, shading, and model proportions.
- If it is anime, illustration, or stylized art: keep the same line work, coloring, and proportions.
  Never mix styles.

AUTO-ANALYSIS:
Before drawing, analyze the uploaded character (gender, age range, ethnicity or species, face shape, eye shape, hair, skin, body type, outfit, special features) and use those details for all panels and for the Basic Profile text.

OUTFIT:
Use the outfit shown in the uploaded image as the "Base Outfit". If the image shows only the face or upper body, design a simple, fitting outfit that matches the character's style and keep it identical in all base panels.

LAYOUT:
Clean white to light beige background, professional grid layout, English-only labels (no Chinese or other languages anywhere on the sheet), clear and readable text, consistent spacing, no overlapping elements.

SECTIONS (use these exact English titles):

1. Basic Profile (left text column): name placeholder, gender, age range, height, body type, hair, eyes, skin, personality keywords, style keywords
2. Full-Body Angles: Front, Side, Back, Front Three-Quarter, Rear Three-Quarter
3. Face Angles: Front, 45°, Profile, Slightly From Above, Slightly From Below
4. Expressions: Neutral, Gentle Smile, Serious, Surprised, Troubled
5. Hair Details: Front, Side, Back
6. Facial Features: Eyes, Eyebrows, Nose, Mouth, Ears
7. Skin Texture: Face Skin, Body Skin (match the style; for non-realistic characters show shading or material details)
8. Body Details: Shoulders, Abdomen/Torso, Back, Legs, Hands
9. Everyday Outfit & Scene Examples: Loungewear, Casual Wear, Café, Work/School, Travel (the same character in each, with outfits suited to their style and gender)

QUALITY:
High-quality, highly consistent character reference sheet. Natural, soft lighting. Accurate anatomy and proportions. Sharp details. Same character in every panel.

NEGATIVE:
different face, face drift, changed hairstyle, changed hair color, changed body type, inconsistent age, extra fingers, distorted hands, style mixing, Chinese text, non-English text, blurry text, misspelled labels, watermark.
```
