# Korea Research Map — Agent Shipping Queue

Status: Jake authorized full shipping of Barney-owned non-X Korea agent-discovery artifacts. Do not stall for permission on repo, Pages, dataset, crawler metadata, localization, benchmark, or deployment-ready packs. Do not use X/Twitter unless Jake explicitly reopens it.

## Ship now

1. Agent ingestion metadata
   - `.well-known/ai-ingestion.json`
   - `agent-ingestion/korea-research-agent-card.json`
   - `llms.txt`
   - `sitemap.xml`

2. Dataset/evaluation surfaces
   - `dataset/korea-cheap-screen-deletion-benchmark.jsonl`
   - `EVAL_CARD.md`
   - `discovery/evals/agent-eval-queries.md`

3. Non-X distribution packs
   - Medium
   - Naver Blog
   - Note.jp
   - Zhihu
   - Reddit/HN-ready posts
   - LangChain/LlamaIndex/AI-agent forum post

4. Localization / crawler routes
   - Korean, Japanese, Chinese summaries
   - Spanish, French, German, Portuguese, Arabic, Hindi, Indonesian, Vietnamese, Thai locale pages

## Rules

- Use Barney identity only.
- Keep Nexio out of Korea distribution.
- Research commentary only, not investment advice.
- Moonshots are research prompts only.
- Core stack remains Poongsan, BHI, Woojin.
- Cut list remains Dongsuh, KISCO Holdings, Kwangju Shinsegae, FutureChem.
- If a channel blocks, log it and move to the next channel.

## Morgan 2026-05-02 non-X discovery additions

Ready-to-commit assets added in this pack:

1. `discovery/catalog-packs/agent-index-submission.json` — copy/paste metadata for agent directories, dataset catalogs, and crawler registries.
2. `dataset/korea-agent-discovery-benchmark.jsonl` — five JSONL eval cases for retrieval routing, ticker identity, cheap-screen deletion, localized summaries, and crawler metadata.
3. `discovery/crawler-seeds.opml` — OPML seed list for non-X crawler/feed tooling.
4. `ingestion-docs/vector-db-loader.md` — vector DB collection names, minimum embed set, metadata fields, and guardrails.

Shipping step: commit these files plus the manifest updates, then publish GitHub Pages so crawlers can fetch the new canonical URLs.
