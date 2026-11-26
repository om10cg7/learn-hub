# 紙の漁村が折りたたまれる — papercraft Skill製のthree.jsミニチュア世界「Lantern Cove」

- 日付: 2026-11-25
- 作者: Terry Djony @terrydjony
- カテゴリ: クリエイティブコーディング／3D
- 元ネタ: https://www.threads.com/@terrydjony/post/DgKeu9UDvA7
- ブラウザデモ: https://awesomeslop.terrydjony.com/art/019-lantern-cove
- ギャラリーのリポジトリ: https://github.com/terryds/awesomeslop

## 要約

Threads の動画投稿。小さな紙の漁村が、カメラが通り過ぎるのに合わせて折りたたまれていくミニチュア世界の作例。全てのパーツが紙のカードでできており、three.js 上で Claude の papercraft Skill を使って構築したという。使用モデルは「Claude Opus 5.5」と投稿内表記（モデル名は作者の表記のまま）。

作者の自己返信で、この作品をブラウザでそのまま試せるデモ（awesomeslop.terrydjony.com の /art/019-lantern-cove、作品名は「Lantern Cove」）と、作者のギャラリープロジェクト「awesomeslop」の GitHub リポジトリが案内されている。

awesomeslop は「AIエージェントが作ったアートのギャラリー。1作品につき1プロンプト」というコンセプトの個人プロジェクトで、リポジトリを裏取りした内容（2026-11-26確認）: 公開リポジトリ、スター5、2026-11-12作成。Cloudflare Worker（Hono、サーバーレンダリングJSX）＋D1 で構築され、各作品は arts/ フォルダに art.json（タイトル・使用モデル・エージェント・媒体・タグ等）・prompt.md（その作品を作った1プロンプト）・README・実体（index.html 等）を入れる形式。作品ページにはプロンプトのコピーボタンもある。

papercraft Skill そのものの紹介は、別作者 @aiadventureryt の投稿を ai-skills に収録済み（2026-11-22-DgEuYVtBdr6）。本投稿はその Skill を使って作られた作品そのものの提示が主題で、作者も作品も別のため重複ではなく、作例として etc に収録した。

## 学び・所感

- Skill の紹介投稿だけでなく「そのSkillで実際に作られた作品＋ブラウザで触れるデモ＋作ったプロンプトの公開」まで揃うと、再現可能性の検証材料として価値が上がる
- 「1作品1プロンプト」をギャラリーの単位にする awesomeslop の形式は、AIエージェント製アートの記録方法として素直で追いやすい
