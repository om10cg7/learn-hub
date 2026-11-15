# 通知UIのスタイル8種（ale.uiux）

- 出典：Instagram @ale.uiux（Ale • UX/UI Design • AI）のリール「Notification Styles: 8 ways to tell users something happened」（2026-11-14投稿、12秒）
  - https://www.instagram.com/reel/DfuRU7Zko1C/
  - 「DESIGN NOTES / UI」シリーズ。暗背景に8種の通知をスマホ画面のグリッドで並べ、カーソルで1つずつハイライトしながら下に説明文が出る構成。内容は動画解析で確認
  - 関連：同作者の「モバイルナビゲーションのパターン8種」（Dfr0Ws7D98x）、「ページ遷移アニメーション8種」（Dftu2zGj6i2）、「トグルスイッチのスタイル8種」（DfsK5dcihXy）、「ボタンスタイル8種」（DfuxovhkyaE）と同じ「8種カタログ」の型。既存の「通知のモーション6種」シリーズ（@ui_motion_prompts、Part 1〜3）は通知の「動き・アニメーション」が主題で、こちらは通知の「形式と使い分け」が主題なので別件

## 8種

| # | 名称 | 向く場面（動画・キャプションの定義） |
|---|------|------|
| 1 | Toast | 素早い確認＋取り消し（Undo）付き。例：「Message archived」 |
| 2 | Push banner | アプリの外からの更新を知らせる |
| 3 | Live pill | 進行中のアクティビティを常時表示する |
| 4 | Badge | 未読数などを邪魔にならず（割り込みゼロで）示す |
| 5 | Inline alert | 起きた場所その場で返すフィードバック（フォーム入力など） |
| 6 | Dialog | 本当に重要な判断・決断にだけ使う（削除確認など） |
| 7 | Stacked | ロック画面などで多数の通知をまとめて積む |
| 8 | Progress toast | 長い処理をバックグラウンドで進捗表示する（アップロードなど） |

## 学び

- 通知選びの軸は「ユーザーの流れ（フロー）をどれだけ止めるか」。良い通知は、知らせるべきことを伝えつつ操作を中断させない
- 割り込み度のグラデーションで整理できる：Badge（割り込みゼロ）→ Toast／Inline alert（その場・一時的）→ Push banner／Live pill／Stacked（画面の外・常時系）→ Dialog（判断を強制するので最後の手段）
- 形式ごとに役割が固定されている：確認＋Undo は Toast、フォームのフィードバックは Inline alert、未読数は Badge、重要な決断だけ Dialog、長時間タスクは Progress toast
- AI への指示でも「Progress toast でアップロードを表示」「Stacked でロック画面通知」など名前で指定できる、同作者の名前シリーズ共通の効用
