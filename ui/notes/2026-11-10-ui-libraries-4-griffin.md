# AIに渡すUIライブラリ4選（Griffin Wooldridge）

- 出典：Instagram @griffinwooldridge1（Griffin Wooldridge、Product Designer）のカルーセル「Top 4 UI Libraries - Stop making AI design from scratch」（2026-11-10投稿、全5枚、いいね899）
  - https://www.instagram.com/p/DfkBGDyDgqS/
  - キャプションの主張は「AIに毎回ゼロからUIをデザインさせるな。良いコンポーネント集を渡して組ませろ」
  - 共有URLの img_index=4（0始まり）は5枚目＝Beautiful UI のスライドを指す（下記スライド構成で確認済み）
  - 内容は media-understanding のスライド解析で確認

## スライド構成（全5枚）

| 枚 | 内容 |
|---|---|
| 1枚目（slide 0） | 導入：タイトルと4ライブラリのUIプレビューを並べたグリッド |
| 2枚目（slide 1） | Bencho |
| 3枚目（slide 2） | BoardUI |
| 4枚目（slide 3） | Transitions.dev |
| 5枚目（slide 4） | Beautiful UI ← img_index=4 が指すスライド |

## 4ライブラリ

いずれもダークモードUIの画面例で紹介されている。

| ライブラリ | キャプションの一言 | スライドの画面例 |
|---|---|---|
| Bencho | playful micro-interactions（遊び心のあるマイクロインタラクション） | タイマー、カラフルな花のカード |
| BoardUI | dashboards and agent tools（ダッシュボードとエージェント向けツール） | 訪問者チャート、収益の棒グラフ、カレンダー |
| Transitions.dev | smooth UI state changes（なめらかなUI状態遷移） | iMessage風チャット、トークン消費グラフ、フォーカスタイマー、会議スケジュール |
| Beautiful UI | polished agent workflows（磨かれたエージェントワークフロー） | インサイトダッシュボード、企業テーブル、タスクリスト、メニュー整理UI |

## 学び

- 発想は「AI生成UIの質は、モデルより先に“手本の部品”で決まる」。プロンプトの工夫ではなく、実績のあるコンポーネント集を土台に渡すという、ライブラリ先行のアプローチ
- 4選の切り口は「インタラクション（Bencho）／ダッシュボード（BoardUI）／状態遷移（Transitions.dev）／エージェントUI（Beautiful UI）」と役割で分かれており、作る画面の種類から引ける
- 既存ノートとの関係：Transitions.dev のみ Skully の「UIデザイン／アニメーションのコレクション4選」（notes/2026-09-22-ui-animation-collections-4-skully.md）で収録済み。残り3つ（Bencho／BoardUI／Beautiful UI）は初収録で、投稿自体は重複ではない
- リソース一覧系の先例（Skully のコレクション4選、Abraham の10選等）どおり、新しいUI用語・技法の追加はないため図鑑カードは追加せずノートのみ
