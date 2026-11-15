# UXの法則5選（Vamshi）

- 出典：Threads @vamshi.work（Vamshi | Product Designer）のカルーセル「5 UX laws every designer should know!」（2026-11-08投稿、全7枚、いいね55）
  - https://www.threads.com/@vamshi.work/post/DfewBdOH_zn
  - 内容は全スライド（表紙＋法則5枚＋締め）を目視で確認。各法則に「✗ 悪い例／✓ 良い例」の画面モックを並べる構成
  - このチャット（振り分け）経由で受領し、仕分けルール（url_repo_router）で learn-ui 行きと判定して作成
- 関連：同じ作者の notes/2026-11-08-loader-types-8-vamshi.md、notes/2026-11-08-bottom-nav-styles-8-vamshi.md、notes/2026-11-05-designer-websites-54-vamshi.md

## 5つの法則（スライド順）

1. **Fitts's Law（フィッツの法則）** — "The bigger and closer a button is, the faster people hit it. Make key actions easy to reach."
   - 例：イヤホンの商品カードで、小さな「Buy」ボタンだけの案（✗）に対し、幅いっぱいの「Buy now」＋「Add to cart」を縦に置く案（✓）
2. **Hick's Law（ヒックの法則）** — "Every extra choice adds time to decide. Fewer options means faster decisions."
   - 例：プランが6つ並ぶ選択画面（✗）に対し、3プラン＋「Continue」に絞る案（✓）
3. **Law of Proximity（近接の法則）** — "Things placed close together look related. Use spacing to show what belongs together."
   - 例：アカウント作成フォームで、ラベルと入力欄の間隔が空いて対応が分かりにくい案（✗）に対し、ラベルを各入力欄に寄せた案（✓）。ゲシュタルト原則のひとつ
4. **Von Restorff Effect（フォン・レストルフ効果）** — "The one thing that looks different gets noticed first. Save it for the action that matters."
   - 例：プラン一覧が全部白で並ぶ案（✗）に対し、推したい「Pro」だけを青く塗り「Popular」バッジを付ける案（✓）
5. **Doherty Threshold（ドハーティの閾値）** — "If a response takes longer than 0.4 seconds, people notice. Show something instantly."
   - 例：注文一覧が「Loading...」の空白で待たせる案（✗）に対し、スケルトンUIで即座に形を見せる案（✓）

## 学び・所感

- 定番5法則を「1法則＝1画面の✗／✓対比」で見せる型。言葉の定義ではなく「画面のどこを直すか」で覚えられるのが良い
- 5つは効く場所で整理できる：操作の速さ（1 フィッツ）／決断の速さ（2 ヒック）／反応の速さ（5 ドハーティ）、グルーピングの読み取り（3 近接）、注意の誘導（4 レストルフ）
- 既存の「UIとUXの違い」ノート（2026-11-12-ui-vs-ux-basics.md）の表紙ではヒック／フィッツ等が「デザイン心理学」の名前だけ挙がっていたが、本投稿は各法則の実例編にあたる。図鑑には本件を「UXの法則5選」のカードとして追加した
- 4 のプラン強調は同作者のヒックの法則の例（同じプラン選択画面）と画面素材が共通で、法則ごとに同じ画面を使い回して対比を作っている点も教材として上手い
