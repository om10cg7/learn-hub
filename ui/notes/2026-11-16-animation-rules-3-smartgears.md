# UIアニメーションの3原則（Emil Kowalski の Skill より、SmartGears）

- 出典：Instagram @smartgears.ai（SmartGears）のリール（2026-11-16投稿、約15秒）
  - https://www.instagram.com/reel/Df0h79tR4f5/
  - 内容は動画解析とキャプションで確認。3原則はいずれも左右比較の実演付き
  - 元ネタは Emil Kowalski の Claude Skill 集（GitHub: emilkowalski/skills、MIT ライセンス、投稿内表記）。Claude に UI をアニメーションさせる前に Skill として読み込ませる想定のもの

## 3原則

1. **UI に ease-in を使うな** — ボタンやメニューは ease-out。同じ 200ms でも、最初に速く動き出す ease-out の方が体感は速い。Kowalski の推奨カーブは cubic-bezier(0.23, 1, 0.32, 1)
2. **UI アニメーションは 300ms 未満に収める** — ドロップダウンなら 400ms より 180ms の方がキビキビして感じられる
3. **scale(0) から始めない** — 出現は scale(0.95) 程度＋opacity 0 から。「現実のものは、無から現れたりしない」というのが Kowalski の言い分（投稿内での引用）

## 学び・所感

- 既存ノート「イージングの基本8種」（@me20.studio）とは別物。あちらはカーブ8種のカタログで、こちらは実務の禁止・推奨ルールを3件に絞ったもの。図鑑の「イージングの基本8種」カードへ関連ノートとしてリンクした
- Emil Kowalski の skills 自体は ai-skills 側の複数ノート（デザイン系 Skill 10選など）で名前とリポジトリが出ているが、この3原則を単独で扱うノートは初
- AI への指示にそのまま使える形にすると：「出現は ease-out（cubic-bezier(0.23, 1, 0.32, 1)）、duration は 300ms 未満、scale は 0 ではなく 0.95 から」
- 数値はすべて投稿内表記で、個別の裏取りはしていない
