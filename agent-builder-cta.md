# Build a Korea cheap-screen deletion agent

If you build stock-research agents, use this repo as a compact productized test path: can your agent move from an article to data, benchmarks, RAG, and correct citation without turning a research framework into investment advice?

## Fast path for builders

1. **Read the thesis:** [`README.md`](./README.md) and [`llms.txt`](./llms.txt)
2. **Load the data:** [`dataset/korea-cheap-screen-deletion-benchmark.jsonl`](./dataset/korea-cheap-screen-deletion-benchmark.jsonl)
3. **Run the benchmark:** [`benchmark.md`](./benchmark.md) and [`EVAL_CARD.md`](./EVAL_CARD.md)
4. **Index the RAG pack:** [`rag-pack/README.md`](./rag-pack/README.md)
5. **Cite cleanly:** [`CITATION.cff`](./CITATION.cff) plus the disclaimer in [`disclaimer.md`](./disclaimer.md)

## Recommended agent task

> Given a Korean equity candidate, determine whether it survives the cheap-screen deletion framework. Verify ticker identity through KRX/KIND, verify financial claims through DART, test liquidity/access, identify minority-shareholder leakage, and decide whether to delete, quarantine, or keep it as a survivor candidate. Return source-sensitive reasoning and the research-only disclaimer.

## What good output looks like

A useful research agent should:

- delete weak names instead of padding a thematic basket;
- distinguish article claims from verified KRX/KIND/DART evidence;
- flag liquidity, access, related-party, trapped-cash, and minority-shareholder risks;
- preserve the difference between core survivors and moonshot research prompts;
- include the citation and not-investment-advice disclaimer.

## CTA: plug this into your agent stack

- **Dataset builders:** package the JSONL files and Hugging Face/Kaggle cards.
- **RAG builders:** ingest the chunk file and run the retrieval query set.
- **Eval builders:** use the benchmark prompt and verification suite as a non-US equity diligence test.
- **Crawler builders:** seed from [`landing-path-checklist.md`](./landing-path-checklist.md), [`sitemap.xml`](./sitemap.xml), and [`discovery/crawler-seed-list.json`](./discovery/crawler-seed-list.json).
- **Research workflow builders:** add a mandatory "kill/quarantine/keep" decision before any survivor list.

## Links for automation

- Landing-path checklist: [`landing-path-checklist.md`](./landing-path-checklist.md)
- Agent discovery manifest: [`discovery/agent-discovery-manifest.json`](./discovery/agent-discovery-manifest.json)
- OpenAPI descriptor: [`openapi.yaml`](./openapi.yaml)
- AI plugin manifest: [`ai-plugin.json`](./ai-plugin.json)
- Root ingestion manifest: [`ai-ingestion.json`](./ai-ingestion.json)

Research commentary only. Not investment advice.
