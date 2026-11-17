# テニス選手プロフィールダッシュボード「Deuce」作例（Orbix Studio）

- 出典：Instagram @orbixdashboard（Orbix Studio Dashboard）のカルーセル「Deuce: Tennis Player Profile Dashboard」（2026-11-14投稿、全5枚、いいね133）
  - https://www.instagram.com/p/Dfus5sWFAov/
  - キャプションは設計内容の列挙（Player profile and match overview／Win rate and surface charts／Upcoming match pairings／Tournament comparison and tactic map）で、作者による技法解説・設定値の共有はない。末尾はスポーツダッシュボード制作の DM 営業。内容は media-understanding のスライド解析で確認
  - 同作者（Orbix Studio）の既存ノート「Coinly 支出分析ダッシュボード」（2026-10-29）と「HRアナリティクスダッシュボード」（2026-01-02）とは別画面・別題材の作例であり、重複ではない

## 内容

テニス選手のプロフィールと成績を1画面にまとめたスポーツアナリティクス系ダッシュボードのコンセプト作例。題材の選手は Carlos Alcaraz（スペイン、21歳、世界ランク2位という設定）。白基調にグリーンのアクセント1色で、ナビ・推移グラフ・選択中コントロールを統一している。

スライド構成（全5枚）:

- **1〜4枚目** — ダッシュボード画面。選手プロフィールの横に Match Overview（勝率 72.34%）を置き、緑の折れ線チャートと小型のスタットカードで成績の詳細を整理
  - 左カラム: Upcoming Matches（Sinner／Djokovic／Medvedev との対戦予定）と小さなタクティクスマップ
  - Surface Performance（サーフェス別成績）: 下段で異なるチャート形状を使い、単調さを回避
  - Win Rate over Time（時期別の勝率推移、2026年5〜6月にピーク）、Season Summary（48試合・36勝12敗・賞金 $2.85M）、Recent Matches、Shot Distribution、Player Strengths のレーダーチャート
- **5枚目** — 問い合わせ用 CTA スライド（無料相談ボタンや SNS リンク集）

## 学び・所感

- 「選手その人の顔」と「数字」を同居させるレイアウト: プロフィールを起点に、概要→推移→内訳（サーフェス別・ショット分布・強みレーダー）と詳細へ降りていく情報の階層が分かりやすい
- チャート形状をパネルごとに変える（折れ線／レーダー／分布）一方、色はグリーン1色に抑えて全体を締める、ダッシュボード作例として同作者 Coinly／HR と一貫した手法
- 新しい用語・技法の提示はないダッシュボード作例のため、先例（同作者の HR アナリティクス、Corbel／Crestway／Cirrel ほか）どおり図鑑カードは追加せずノートのみ
