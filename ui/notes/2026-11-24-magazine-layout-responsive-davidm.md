# レスポンシブ・マガジンレイアウト（David Mráz）

- 出典：Instagram @davidm_ai（David Mráz）のリール「Responsive magazine layout built for agentic coding」（2026-11-24投稿）
  - https://www.instagram.com/reel/DgI8bu8A9SQ/
  - 内容は動画解析で確認。Atheros AI Builder の無料コンポーネント「Magazine Layout」のデモで、下部クレジットは「AI Builder Components」（builder.atheros.ai）。コンポーネントは「Code」コメントでリンク配布
  - このチャット（振り分け）経由で受領し、仕分けルール（url_repo_router）で learn-hub の ui 行きと判定して作成

## デモの内容

- 幅スライダーをドラッグすると、ブレークポイント（Mobile 480px／Tablet 768px／Laptop／Desktop 1024px+）に応じてグリッドレイアウトがリアルタイムに組み替わるプレビュー
- グリッドのエリアは header／nav／left／main／right／footer の6区画。幅が狭くなるにつれて左右カラムが main の下へ回り込むマガジン式の再配置を見せる
- プレビュー下の CSS パネルが連動して更新され、各ブレークポイントの @media クエリと grid-template-areas の定義がそのまま読める

## 学び・所感

- エリア名（header/nav/left/main/right/footer）でレイアウトを宣言する grid-template-areas 方式は、カラム数ではなく「意味の区画」で組み替えを考えるのが要点。ブレークポイントごとにエリアの並びだけを差し替えれば、要素側の指定は変えずに済む
- 「幅をドラッグするとコードも一緒に変わる」見せ方は、レスポンシブの挙動と実装を同時に理解させる教材として効率が良い。ページネーション8種など同作者の部品カタログと同じく、エージェントに生成させる前提のコンポーネント紹介という位置づけ
