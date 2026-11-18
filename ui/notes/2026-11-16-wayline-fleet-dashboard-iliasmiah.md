# エージェント提案の承認インボックス型フリート管理ダッシュボード「Wayline」（Md Ilias Miah）

- 出典：Threads @ui.iliasmiah000（Md Ilias Miah）の動画投稿（2026-11-16投稿、いいね約80）
  - https://www.threads.com/@ui.iliasmiah000/post/Df1WHAuCXdB
  - 作者はプロダクトデザイナー（プロフィール文「Design the product. Build the site that sells it. Ship both.」）
  - 動画解析は取得できなかったため、内容はサムネイル（メイン画面「Command」のモックアップ）とキャプションで確認。数値類はすべて画面内モック表記
  - コメント欄にプロンプト等の配布はなし。反応は「顧客へ新しい到着時刻を即座に知らせるなら自動リルートを任せてもよい。当面はワンタップ承認を残すべき」という承認モデルの是非が中心

## 中身

- テーマは「Wayline」というトラック輸送チーム向けのエージェンティック（自律エージェント型）フリート管理プラットフォームのUIコンセプト。キャプションの設定は「I-35（州間高速）の閉鎖で荷物が14分遅延し、配車担当が最後に気づく」という課題に対し、Route agent が TX-6 への迂回路を見つけ、担当が1回承認するだけでドライバーと顧客の両方へ更新が届く、という流れ
- 画面は3ペイン構成。左は「Needs you（要対応）」インボックスで、未処理のエージェント提案が3件バッジ付きで並ぶ。各提案カードには担当エージェント名（Route agent／Maintenance agent／Dispatch agent）、提案内容、影響の数値（到着時刻・追加距離・コスト等）、根拠の一文（「I-35 is closed near Waco until 9 AM」等）、Review／Edit のリンクと黒い「Approve reroute」「Approve plan」の承認ボタンが入る
  - Route agent: 「T-214 を I-35 閉鎖の迂回路へ」到着1:36 PM（+14分）・+14 mi、費用は据え置き表示
  - Maintenance agent: 「T-118 を整備工場へ回し、荷物を T-131 へ載せ替え」$640
  - Dispatch agent: 「LD-48213（Dallas→Memphis）を Elena Ortiz へ割り当て」9h 40m・$310
- 中央は地図。車両マーカー、実線の現在ルートと点線の迂回路、「I-35 closed near Waco」の警報ピン、選択中車両の吹き出し（T-214／Marcus Reed／ETA 1:36 PM）、「via TX-6, saves 38 min」のタグ、目的地（Bluebonnet Foods DC）を表示。上部に All 98／Moving 48／Stopped 19／At risk 3／Traffic のフィルタチップ、下部に稼働台数・定時率94.2%・リスク3件・荷物128件などのKPIストリップ
- 右は選択中車両 T-214 の詳細パネル。トラック写真、ドライバー（Marcus Reed）、積荷番号、区間（Fort Worth, TX → Austin, TX）、ETA、残り運転時間10h 30m、燃料64%、トレーラー温度36.4°F、速度61 mph。「承認すれば Customer agent が顧客へ新しいETAを送り、ドライバーへナビ指示が届く」という注記と、エージェントの行動履歴タイムライン、「Message driver」「Open load」ボタン

## 学び・所感

- AIエージェントの自律実行を「提案→人間が承認→実行」の形にし、承認待ちの提案をインボックスとして左ペインに集約したダッシュボード作例。承認前に影響（遅延・距離・コスト）と根拠をカード内に並べることで、ワンタップ承認でも判断材料が足りる構成になっている。地図と詳細パネルは選択車両に連動し、承認対象の文脈をその場で確認できる
- 新しい用語・技法の提示はないダッシュボードUIショーケースのため、図鑑カードは追加せずノートのみ（ダッシュボード作例の先例どおり）
