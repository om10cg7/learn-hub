# 本物のガラスは4要素：CSS blur との比較デモ（Alexander Tiler）

- 出典：Instagram @alexander.tiler（Alexander Tiler）のリール（2026-11-14投稿）
  - https://www.instagram.com/reel/Dfu1gt2N9Ei/
  - キャプションは「CSS blur has 1 setting. Real glass has 4.」
  - 内容は動画解析で確認。紹介されているエフェクト「Agentic Liquid Glass」は「GLASS」とコメントするとリンクが届く配布形式
- 関連：図鑑のリキッドグラス／グラスモーフィズム系カード、notes/2026-11-06-liquid-glass-footer-arastoo.md

## 中身

- ダークテーマの画面で「CSS BLUR」と「REAL GLASS」を左右に並べて比較するデモ
- CSS 側は backdrop-filter: blur(16px) の1設定のみで、調整できるのは「ぼかしの強さ」だけ
- REAL GLASS 側には4つのスライダーがあり、1つずつ動かして見せる
  - **Refraction（屈折）**：ガラスの背後の光・像が曲がって見える
  - **Rainbow（虹色の縁）**：エッジに色が分かれてにじむ（色収差）
  - **Frost（曇り）**：乳白色に曇った質感
  - **Light（リムライト）**：光の縁が動きに追随する
- 終盤で価格 $49 → $33（33%オフ）を表示する販促構成（投稿内表記・裏取りなし）

## 追記：続編リール「Zoom in」（2026-11-20投稿）

- https://www.instagram.com/reel/Df_FuVUtM6n/
- 同じ Agentic Liquid Glass の販促続編のため、新規ノートは作らずここに追記する（価格 $33、GLASS コメントでリンク送付は前回と同じ）
- 今回の切り口は「拡大すると差が出る」：左の backdrop-filter: blur は拡大すると灰色のムラと細い輪郭線だけが残り、右の本物のガラスは縁が鋭いまま、背後を曲げ、光を虹色に分ける
- 20倍まで拡大するとレイトレーシングの3Dレンズになると主張。画面ではアプリ「FERRITE」の通知風カードを題材に、"CSS BLUR" 側は硬い縁、"REAL GLASS" 側は「No edge. Just a blur.」と表示し、Refraction／Dispersion のラベルと球状レンズの屈折を見せる。締めは「Every card. Real glass.」
- 前回の4要素（屈折・虹・曇り・リムライト）のうち、今回は屈折と色分散に絞った拡大デモ

## 学び

- CSS の blur だけでは「すりガラス」止まりで、本物のガラスらしさは屈折・色収差・曇り・リムライトの4要素の組み合わせでできている、という分解が要点
- グラス系 UI を作るときのチェックリストとして使える：ぼかしの量だけでなく、縁の屈折と光の回り方まで作るかどうかで質感が変わる
