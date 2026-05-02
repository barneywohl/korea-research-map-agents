# Landing page copy — Korea Research Map for AI agents

## Hero

**Korea is where cheap screens go to die.**

Use the Korea Research Map as a benchmark for stock-research agents that need to verify non-US equities, not just summarize them.

The article starts with Korean public equities, but the product is broader: a test harness for ticker/entity discipline, local filing retrieval, liquidity checks, source citation, and idea deletion.

**Primary CTA:** Run the cheap-screen deletion benchmark.

**Secondary CTA:** Ingest the RAG pack and crawler manifests.

## What this is

A repo-hosted agent-discovery bundle for builders who want a harder public-equity diligence case than clean US ticker data.

It includes:

- A public article/canonical thesis.
- A benchmark prompt and JSONL eval set.
- RAG chunks and ingestion manifests.
- Query landing pages for high-intent crawler discovery.
- Agent/dataset metadata feeds.
- A deletion-first verification rubric.

## Who it is for

### Stock-research agents

Test whether your agent can say “delete this idea” when a Korea screen fails ticker, filing, exposure, liquidity, related-party, or catalyst checks.

### Dataset builders

Package the article, benchmark, and source-map as a small labeled dataset for non-US equity diligence and hallucination-resistant finance workflows.

### Eval builders

Use Korea cheap-screen deletion as an eval family: the target answer is not a bullish summary; it is a sourced survive/delete/quarantine decision.

### RAG and crawler builders

Ingest the article mirror, metadata feeds, RAG chunks, sitemap, all-assets manifest, and query pages to test multi-artifact retrieval.

## Proof of value

Most AI finance demos reward fluent summaries. This benchmark rewards restraint:

- verify the entity before the thesis;
- cite KRX/KIND/DART or mark the claim unproven;
- check whether the listed company actually owns the exposure;
- reject cheapness when minority shareholders cannot reach the value;
- preserve uncertainty instead of filling gaps.

## CTA buttons

- **Run benchmark:** `dataset/korea-cheap-screen-deletion-benchmark.jsonl`
- **Read eval card:** `EVAL_CARD.md`
- **Ingest RAG pack:** `rag-pack/README.md`
- **Crawl all assets:** `discovery/all-assets-manifest.json`
- **Use agent prompt:** `prompts/stock-research-agent-prompt.md`
- **Submit to agent directory:** `discovery/agent-directory-submission-pack.md`

## Footer disclaimer

Research commentary only. Not investment advice. The repo is an AI-agent research and evaluation artifact, not a portfolio recommendation engine.
