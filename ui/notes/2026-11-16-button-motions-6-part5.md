# ボタンの押した感触6種 Part 5（ui_motion_prompts）

- 出典：Instagram @ui_motion_prompts のリール「Button Part 5 — one button, six ways it feels when you press it.」（ボタンの演出 その5、2026-11-16投稿）
  - https://www.instagram.com/reel/Dfy_Cf2h4fo/
  - 内容は動画解析とサムネイル（全パネルの英字説明）で確認。各パネルのラベルと説明はサムネイル表記ママ
  - このチャット（振り分け）経由で受領し、仕分けルール（url_repo_router）で learn-ui 行きと判定して作成
- 関連：notes/2026-10-31-button-motions-6-part1.md（Part 1、図鑑85種目）、notes/2026-11-02-button-microinteractions-6.md（Part 2）。Part 4 は Part 2 の6種を鉛筆描き風に再描画したもので要約のみ

## 6種

1. **Soft Inset** — 浮いていた影が内側に反転し、ピルが沈んでからポンと戻る。「Its raised shadow flips inside: the pill sinks in, then pops back out.」
2. **Finger Dent** — 指の下で表面がへこみ、ゴムのように震えて戻る。「The surface dents under the finger, then wobbles back like rubber.」
3. **Tilt Press** — 押した側へ3Dで傾き、水平に揺り戻る。「It tilts in 3D toward the pressed side, then rocks back level.」
4. **Haptic Buzz** — 短い電話のバイブのような震えで揺れ、両側に振動のアークが出る。「A short phone-like buzz shakes it, with vibration arcs on both sides.」
5. **Pogo Bounce** — 押し込むとボールのように跳ね上がり、2回着地する。「Pressed down, it bounces up like a ball and lands twice.」
6. **Spring Pop** — 指の下で縮み、大きめにバネで戻って落ち着く。「It shrinks under the finger, then springs back bigger and settles.」

## 学び・所感

- Part 1（Press Down／Ripple／Glow Pulse／Jelly Bounce／Load & Success／Expand Morph）、Part 2（Hold to Confirm／Paper Plane／Confetti Burst／Copy Feedback／Shine Sweep／Slide to Confirm）のいずれとも効果名の重なりはなく、新規6種。Part 4 のような再描画ではない
- 6種はすべて「指の下で何が起きるか」という触感の違いで分かれている：影の反転（1）、表面のへこみ（2）、3Dの傾き（3）、振動の可視化（4）、二段着地（5）、オーバーシュート（6）
- 近いものとの区別：1 Soft Inset は影が外→内へ反転するニューモーフィズム系の沈みで、Part 1 の Press Down（濃い土台へ沈む）とは別物。5 Pogo Bounce は「2回着地」が本体で、Jelly Bounce のゼリー状の震えとも違う。6 Spring Pop は戻りで一瞬大きくなるオーバーシュートが本体
- 4 Haptic Buzz は触覚フィードバック（バイブレーション）を目に見える形にしたもの。実際の振動と連動させれば「押した」感が最も強まるが、振動なしだとただの小刻みな揺れに見えるので、実装では haptics とセットで使うのが前提
- キャプションは「Which one would you use? Comment 1–6」と1〜6の投票を呼びかける構成。プロンプトとコードはプロフィールのリンク先で配布（無料プロンプトあり）
