# ヘッドトラッキング＋Gaussian Splattingで「実物みたい」になるサイト「BORING」（Dominik Fojcik）

- 出典：Instagram @_fojciko（Dominik Fojcik、Creative Technologist）のリール（2026-10-09投稿、いいね37,521、コメント約2万）
  - https://www.instagram.com/reel/DeRTIdJhAmf/
  - キャプション要旨：「Webサイトが実物みたいに感じ始めたら。ヘッドトラッキング＋Gaussian Splatting をサイトで実験中。SPLAT とコメントすればリンクを送る」。ハッシュタグは #webdesign #vfx #gaussiansplatting。使用音源は SEVER「Marcus」
  - 動画オーバーレイ：「POV: Your website start feeling a little too real...」
  - 重複確認：同URL・同作者の既存ノートなし。Gaussian Splatting の語は ai-skills の別投稿（モーション用リポジトリ20選）のリスト内に一度出るだけで、本投稿とは別物

## 内容

- 実写は暗い部屋のノートPCを斜め前から撮った画角。画面の Chrome（シークレット）でデモサイトが開かれ、Webカメラの作動ランプが点灯している。アドレスバーには「…-mediapipe-splat…workers.dev/splat-mediapipe-splat/」と読める文字列があり、MediaPipe 系の顔／頭部検出を使っていることがうかがえる（前半はぼやけて全文は未確定）
- サイトの中身は、廃墟風の廊下を Gaussian Splatting で再現した3Dシーン：錆びた配管とケーブル、吊りランプ、下半分が緑に塗られた壁、がれきの床、奥のドア。左下に大きな白太字で「BORING」、右に小さな段落（冒頭「Literally the most boring…」程度までしか判読できず）
- 動き：頭の動きに合わせて視点が大きく左右に動き、「BORING」全体が見える正面構図→「RING」だけ→「ING」だけ、と廊下の見える範囲が変わる。前景の配管・壁と奥のドア・窓のずれ方が違う視差（パララックス）が確認できた。上下の視点移動もサムネイルからは示唆されるが、頭の動き方向と視点の対応、前後移動でのズームはこの再生では未確認。人物自体は画面に映っていない

## 学び・所感

- マウスやスクロールではなく「見る人の頭の位置」を入力にして、画面を窓のように覗き込めるサイトにする実験。2Dのパララックスと違い、Gaussian Splatting の実写3Dだからこそ「窓の向こうに実空間がある」感覚になる
- 題材をあえて「最も退屈なはずの廃墟の廊下」にして、タイトルも「BORING」と名付ける逆張りも効いている。退屈な被写体ほど、視点が動く驚きだけが純粋に伝わる
- 実装の手がかりは URL の mediapipe-splat という文字列くらいで、コードや手順の解説はない Web 実験のショーケースのため、図鑑カードは追加せずノートのみ。ui の index.html（図鑑専用）も変更なし
