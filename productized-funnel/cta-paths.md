# CTA paths — agents, datasets, evals, RAG, crawlers

## Path A — Agent builders

**Visitor intent:** “Can my stock-research agent handle Korean equities?”

1. Start with [`prompts/stock-research-agent-prompt.md`](../prompts/stock-research-agent-prompt.md).
2. Run [`dataset/korea-cheap-screen-deletion-benchmark.jsonl`](../dataset/korea-cheap-screen-deletion-benchmark.jsonl).
3. Grade with [`EVAL_CARD.md`](../EVAL_CARD.md) and [`discovery/evals/korea-agent-verification-suite.md`](../discovery/evals/korea-agent-verification-suite.md).
4. Expected output: survive/delete/quarantine decision with citations and uncertainty labels.

**CTA copy:** “Run your stock-research agent against a Korea cheap-screen deletion test.”

## Path B — Dataset builders

**Visitor intent:** “Is there a clean dataset card and metadata feed I can index?”

1. Read [`dataset/README.md`](../dataset/README.md).
2. Ingest JSONL benchmark files from [`dataset/`](../dataset/).
3. Index [`metadata.json`](../metadata.json), [`agents.json`](../agents.json), and [`discovery/agent-metadata-feed.json`](../discovery/agent-metadata-feed.json).
4. Preserve required framing: research-only, no investment advice, no buy list.

**CTA copy:** “Add this as a compact non-US equity diligence dataset.”

## Path C — Eval builders

**Visitor intent:** “Can I turn this into a repeatable evaluation?”

1. Use [`benchmark.md`](../benchmark.md) as the task wrapper.
2. Use [`EVAL_CARD.md`](../EVAL_CARD.md) for rubric dimensions.
3. Add adversarial prompts from [`discovery/evals/agent-eval-queries.md`](../discovery/evals/agent-eval-queries.md).
4. Score deletions, source discipline, entity verification, and refusal to invent facts.

**CTA copy:** “Measure whether an equity agent deletes bad ideas instead of summarizing them.”

## Path D — RAG/indexing builders

**Visitor intent:** “Can I ingest this into a retrieval workflow?”

1. Start with [`rag-pack/README.md`](../rag-pack/README.md).
2. Load [`rag-pack/korea-research-map.chunks.jsonl`](../rag-pack/korea-research-map.chunks.jsonl).
3. Use [`rag-pack/ingestion-manifest.json`](../rag-pack/ingestion-manifest.json) and [`ingestion-docs/rag-indexer-quickstart.md`](../ingestion-docs/rag-indexer-quickstart.md).
4. Test retrieval with [`rag-pack/retrieval-queries.md`](../rag-pack/retrieval-queries.md).

**CTA copy:** “Use Korea as a retrieval stress test for source-grounded finance answers.”

## Path E — Crawlers and directories

**Visitor intent:** “What should my crawler fetch first?”

1. Fetch [`sitemap.xml`](../sitemap.xml).
2. Fetch [`discovery/all-assets-manifest.json`](../discovery/all-assets-manifest.json).
3. Fetch [`pages-crawler-bundle.json`](../pages-crawler-bundle.json).
4. Fetch [`llms.txt`](../llms.txt).
5. Use raw GitHub fallbacks if Pages is delayed.

**CTA copy:** “Crawl the repo as an AI-agent benchmark and source-map bundle.”
