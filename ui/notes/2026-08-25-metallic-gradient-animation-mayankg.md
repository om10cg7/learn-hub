# メタリックグラデーションアニメーション（Mayank Goswami / mayankg.design）

- 出典：Instagram @mayankg.design（Mayank Goswami | Motion & Brand Designer）のリール「Metallic Gradient Animation」（2026-08-25投稿）
  - https://www.instagram.com/reel/DcdECdlx9Dm/
  - 内容は動画解析で確認。After Effects の標準エフェクトだけで作る、液体金属のようなグラデーションがうごめく角丸スクエアのアニメーション。キャプションと実画面は一致（エフェクト名の列挙がそのまま工程になっている）
  - このチャット（振り分け）経由で受領し、仕分けルール（url_repo_router）で learn-ui 行きと判定して作成

## 内容

黒背景に、エフェクトを1段ずつ積み上げる様子を見せる無音チュートリアル。グレーの単純なグラデーションが、最終的に炎色（オレンジ〜黄〜赤）の流動するメタリック体に変わる。

工程（解析より）:

1. **Gradient Ramp** — 土台のグレーのグラデーション
2. **Colorama** — グレーを炎色のカラーサイクルに置き換える
3. **Turbulent Displace + Fast Box Blur** — 形をゆがませて液体らしくし、輪郭を柔らかくする
4. **Precomp + Turbulent Displace** — プリコンポーズしてさらに変形を重ねる
5. **VR Plane to Sphere + Glow + Noise** — 球面化で立体感、グローとノイズで質感を仕上げる

## 学び・所感

- 「質感はエフェクトの積み重ね順で作る」という型。色（Colorama）→変形（Turbulent Displace）→立体化（VR Plane to Sphere）→光と粒子（Glow/Noise）の順序がそのままレシピになっている
- UI のヒーロー背景やローディング、ロゴの質感づけに応用できる。AI 生成では再現しにくい「決まった手順で同じ質感が出る」再現性が AE 標準エフェクトのみで完結する点が価値
- 新しい技法（メタリックグラデーションの具体レシピ）として図鑑カードにも追加した（質感・モーフィズム）
