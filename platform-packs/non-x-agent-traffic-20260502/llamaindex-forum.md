# LlamaIndex forum submission pack

**Category:** Show and tell / RAG / evaluation
**Title:** Korea public-equity RAG benchmark: can the agent delete weak cheap-screen ideas?

## Body

I converted a Korean equities research note into a RAG/eval pack for stock-research agents.

The goal is not to ask an agent for “best stocks.” The goal is to test whether it can delete weak cheap-screen ideas after checking local sources: KRX/KIND entity identity, DART filings, liquidity/access, minority-shareholder economics, governance leakage, and whether a theme reaches revenue/profit/cash flow.

Potential LlamaIndex use cases:

- Index the RAG chunks and retrieval queries as a non-US public-equity source-discipline test.
- Build an evaluator that scores evidence-backed deletion versus unsupported thesis writing.
- Test whether citation coverage includes DART/KRX/KIND-style local sources before the final answer.

Canonical agent page: https://barneywohl.github.io/korea-research-map-agents/
GitHub repo: https://github.com/barneywohl/korea-research-map-agents
Benchmark JSONL: https://barneywohl.github.io/korea-research-map-agents/dataset/korea-cheap-screen-deletion-benchmark.jsonl
RAG pack: https://barneywohl.github.io/korea-research-map-agents/rag-pack/README.md
Full article: https://barneywohl.substack.com/p/the-korea-research-map-where-cheap?r=7xa6e3

Research commentary only. Not investment advice.

I would welcome feedback on the eval rubric and any additional non-US filing failure cases to add.
