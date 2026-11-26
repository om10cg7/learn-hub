# Gen AIエンジニアになるための24ツール（datasciencebrain）

- 日付: 2026-11-23
- 作者: Deepak Jose | Data Science & Gen AI @datasciencebrain
- カテゴリ: AI開発
- 元ネタ: https://www.instagram.com/reel/DgG-xmfvmLt/

## 要約

リール動画（約19秒、内容はキャプションで確認）。「Gen AI エンジニアになりたいなら学ぶべき24ツール」を4カテゴリ×6で示すリスト。全ツールは書籍『Gen AI: Zero to Hero』で実働コード付きで教えているという構成で、本のリンクは「HERO」コメントで DM 送付（未回収）。

| カテゴリ | ツール |
|---|---|
| LLMアプリ＆エージェント構築 | OpenAI SDK、Claude SDK、LiteLLM、Ollama、LangGraph、MCP |
| RAG構築 | PyMuPDF、RapidOCR、sentence-transformers、pgvector、LangChain、LlamaIndex |
| AIのテスト＆セキュリティ | Ragas、DeepEval、promptfoo、OpenTelemetry、Arize Phoenix、Presidio |
| ファインチューニング＆出荷 | PEFT、TRL、bitsandbytes、vLLM、FastAPI、Azure AI Foundry |

開始前の2つの助言が実務的：

1. すでに Postgres を運用しているなら、まず pgvector から。専用のベクトルDBが要るのは具体的な理由があるときだけ
2. 各部品は一度手で作ってからフレームワークに移る。LangChain や LlamaIndex が悪い答えを返したとき、どのデフォルトを確認すべきか分かるようになる

## 学び・所感

- 24個の並べ方が「作る→検索を繋ぐ→測って守る→鍛えて出す」という Gen AI アプリの工程順になっていて、ツールの暗記ではなく工程の地図として読める
- pgvector の助言は「新しい専用DBを足す前に既存資産で足りるか」という判断の提示で、リスト系投稿には珍しい抑制の効いた内容。手組み→フレームワークの順序も同種の実務感
