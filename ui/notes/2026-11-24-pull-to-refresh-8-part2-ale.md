# プル・トゥ・リフレッシュのデザイン8種 Part 2（ale.uiux）

- 出典：Instagram @ale.uiux（Ale • UX/UI Design • AI）のリール「Pull to refresh design, part 2: 8 more ways to update a feed」（2026-11-23投稿）
  - https://www.instagram.com/reel/DgFS9m0B7Uh/
  - 全パターンが実際に動くライブ見本で提示される構成。内容は動画解析とキャプションで確認
  - 関連：同作者の Part 1「ページ更新のスタイル8種」（2026-11-15）は Pull down／Auto-load／Load more など「更新の方式」全体のカタログ。本 Part 2 は引いて更新する際のインジケータ表現に絞った続編で、8種とも重複なし

## 8種

| # | 名称 | 向く場面（キャプションと動画内の定義） |
|---|------|------|
| 1 | iOS spokes | 純正スピナー。学習コストゼロ（native, calm, users already know it） |
| 2 | Progress ring | 「いつ離せばいいか」を正確に見せる |
| 3 | Arrow flip | 矢印の反転で離すタイミングを示す |
| 4 | Logo fill | ブランドマーク自体をローダーにする |
| 5 | Three dots | 軽い印象。チャットアプリに |
| 6 | Skeleton | データ再読み込み中もレイアウトを保つ |
| 7 | Stretchy header | 伸びるヘッダー。プロフィールやコミュニティに |
| 8 | Toast | 「3 new posts」のトーストで、読んでいるものを動かさず静かに更新 |

## 学び

- Part 1 が「更新を誰が主導するか」の方式論だったのに対し、Part 2 は同じプル操作の中の「合図と状態表示」の設計。特に離すタイミングの伝達（Progress ring、Arrow flip）が独立した設計要素として扱われている
- Toast 型はプル操作すら不要にする到達点で、「更新したこと」と「読む位置を守ること」を両立させる。新着ピル（Part 1）と同じ問題意識の別解
- Logo fill はローダーをブランド体験に変える手で、待ち時間の無味乾燥さを消す
