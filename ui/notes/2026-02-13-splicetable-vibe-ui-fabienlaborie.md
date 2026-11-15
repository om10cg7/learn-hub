# バイブコーディングで作った触感UIパネル「SPLICETABLE」（Fabien Laborie）

- 出典：Threads @fabienlaborie（Fabien Laborie (Inscience)）の投稿（2026-02-13投稿、動画、いいね676）
  - https://www.threads.com/@fabienlaborie/post/DUtI9PEEZQP
  - キャプションは「Vibe-coded UI candy. I feel like I'm designing with super-powers now. Figma is truly becaming the messy napkin sketch.」のみ。コメントは0件で、作者による技法解説・プロンプト配布・設定値の共有はない。内容は動画の代表フレーム（サムネイル）を目視して記録する
  - 共有リンク https://www.threads.com/share/BAcSzeiz4M 経由で受領し、仕分けルール（url_repo_router）で learn-ui 行きと判定して作成

## 内容

「SPLICETABLE」というツールの操作パネル画面の作例（動画デモ）。白〜オフホワイト基調で、物理的な機材のような質感（柔らかい影、押し込めるボタン、回転ノブ）を持つスキューモーフィック寄りのパネルUI。

画面構成（代表フレームより）:

- **ヘッダー** — 左にタイトル「SPLICETABLE」、右にライト／ダークの切替アイコン
- **Material** — セグメントコントロール「Image／Color」
- **Splicer** — セグメントコントロール「Stretch／Scatter」
- **Background** — 「3:4 (portrait)」のドロップダウン＋緑ドット付きの小トグル
- **ロータリーノブ×5** — Count／Radius／Chaos／Width／Height（Width と Height の間にロックアイコン＝縦横比ロック）
- **Strength** — 下部左にスライダー
- **出力まわり** — 下部右に「1」のドロップダウン＋「Export」ボタン

## 学び・所感

- ノブやセグメントの「触れる機材感」をWeb UIで再現した作例。キャプションはバイブコーディングでこの水準のUIが作れる時代になり、Figma は下書き（napkin sketch）程度の位置づけになったという作者の所感で、作り方そのものの解説はない
- 新しい用語・技法の提示はないUI作例のため、先例（Corbel／Crestway／Morphin ほか）どおり図鑑カードは追加せずノートのみ
