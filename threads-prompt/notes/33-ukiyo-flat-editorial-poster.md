# 33. 写真をフラットなミッドセンチュリー風エディトリアルポスターに変換するプロンプト（ウキヨ）

- プロンプト作者: ウキヨ @ukiyo_teyanday
- プロンプト投稿: https://www.threads.com/@ukiyo_teyanday/post/Dc_H-yck4O0 （2026-09-07、テキスト投稿、いいね5,436 ※取得時点）
- 作例紹介投稿（今回の共有元）: @lancru95_carlife https://www.threads.com/@lancru95_carlife/post/DdDGYEVk4-9 （2026-09-08、画像1枚、いいね112 ※取得時点）
- 共有リンク: https://www.threads.com/share/_03xUOUmq
- 作例紹介のキャプション: 「このプロンプト、ホントに良い感じに生成してくれる！」
- プロンプトの置き場所: 作者ウキヨのテキスト投稿そのものがプロンプト本文。投稿取得（post）では本文が返らなかったため、作者の投稿一覧（profile-threads）の native_features（SNIPPET）から全文を復元した（19件目 みゅう、32件目 Kuncoro Jk と同じ手法）
- 作者の告知投稿: カルーセル3枚 https://www.threads.com/@ukiyo_teyanday/post/Dc_H-5Qk3Te （いいね22,263 ※取得時点）。キャプション「撮影した写真からフラットポスターアート作れるプロンプトできた！ プロンプト自由に使っていいよ！」とあり、自由利用可が明示されている
- 経緯: 紹介者 @lancru95_carlife が作例画像とともに紹介し、コメント欄でプロンプトの置き場所を聞かれて、作者本人のコメントでウキヨのプロンプト投稿への共有リンク（https://www.threads.com/share/BAScQlmFWx/）を案内していた

## 要約

撮影した写真を、ミッドセンチュリー・モダンな編集ポスター風の「極端にフラットなベクター調イラスト」に変換する画像生成プロンプト（英語）。核は「画面全体を2D平面上の形の配置として扱い、奥行き・立体感・写実的な陰影を徹底的に排除する」こと。

- スタイル: 極端にフラットなベクター調、面の構成、すべての対象を幾何学的に還元。前景・中景・背景を噛み合う色面に平らにし、切り紙／スクリーン印刷／リトグラフの感覚で、シルエット主体・輪郭はシャープに
- 構図: 正面またはほぼフラットな視点（真上からの単純化も可）。強いクロッピング、非対称バランス、形のリズムある配置と反復、エレガントな余白
- 色: 抑制的だが鮮やかな4〜6色（例: ディープネイビー、ウォームアイボリー、バーミリオンレッド、コバルトブルー、エメラルド／ターコイズグリーン、マスタードイエロー、コーラルピンク）。主色1〜2色＋残りはアクセント、ベタ塗り基本、グラデーションは最小限
- 禁止事項: フォトリアル、3Dレンダリング、写実的な質感・陰影・キャストシャドウ、映画的ライティング、光沢のあるデジタル仕上げ、過剰なディテール、アニメ調、カワイイマスコット調
- 出力条件: 縦4:5。テキストは特に求められない限り入れない

## プロンプト（原文ママ、SNIPPET から復元）

```text
Create a sophisticated editorial illustration with a strongly flattened, graphic composition.

The image should feel like a premium mid-century modern editorial poster, but with an even stronger emphasis on flat design, planar composition, and abstract graphic balance.

STYLE:
- extremely flat vector-like illustration
- strong planar composition
- geometric reduction of all objects
- minimal depth
- compressed space
- little to no perspective
- almost no volumetric modeling
- no realistic lighting
- no realistic shading
- color fields instead of rendered form
- bold silhouette-based design
- crisp edges
- poster-like visual structure
- elegant negative space
- graphic, intellectual, art-directed composition

IMPORTANT COMPOSITION RULE:
Treat the entire image as a flat arrangement of shapes on a 2D surface.
Do not build a realistic scene with deep space.
Do not emphasize three-dimensional form.
Flatten foreground, middle ground, and background into interlocking color planes.

VISUAL LANGUAGE:
- use overlapping geometric color blocks
- reduce objects into symbols and silhouettes
- simplify anatomy, faces, hands, buildings, furniture, plants, food, and vehicles into minimal flat shapes
- use cut-paper-like composition
- use screen-print / lithograph sensibility
- use strong cropping
- use asymmetrical balance
- use rhythmic placement of shapes
- use graphic repetition when helpful
- make the image feel like designed surface rather than observed reality

PERSPECTIVE:
- front-facing or near-flat viewpoint preferred
- top-down simplified view also acceptable
- avoid strong realistic perspective
- avoid deep spatial recession
- avoid cinematic depth

COLOR:
Use a restrained but vivid palette of 4–6 colors.
Examples:
deep navy,
warm ivory,
vermilion red,
cobalt blue,
emerald or turquoise green,
mustard yellow,
coral pink.

Use 1–2 dominant colors and the rest as accents.
Use solid flat fills.
Minimal gradients only if absolutely necessary.

AVOID:
- photorealism
- 3D rendering
- realistic texture
- painterly realism
- cinematic lighting
- glossy digital finish
- excessive detail
- realistic cast shadows
- soft atmospheric depth
- anime style
- cute mascot look

DESIRED IMPRESSION:
flat,
graphic,
planar,
poster-like,
editorial,
stylized,
designed,
modernist,
mature,
visually striking,
intellectually composed.

The final image should feel like a highly designed 2D graphic composition rather than a realistic illustration.

Vertical 4:5 aspect ratio.
No text unless specifically requested.
```

## 取得方法の注記

- 共有リンク（_03xUOUmq）は threads-cli の post --url で @lancru95_carlife の作例紹介投稿に解決できた。取得データは ~/workspace/threads-post-_03xUOUmq.json に保存
- プロンプト全文は ~/workspace/threads-post-Dc_H-yck4O0.json に保存
- 紹介投稿・告知カルーセルの画像ファイル自体は取得できなかったため、index 側に画像は載せていない（25件目・29件目・31件目と同じ扱い）
- プロンプト全文が回収できたため、コピーボタン対象とする
