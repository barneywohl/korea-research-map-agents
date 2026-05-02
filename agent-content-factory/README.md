# Agent Content Factory — Korea Research Map

Purpose: turn the Korea Research Map into a repeatable series of **agent-native artifacts**: task cards, eval packs, RAG prompts, crawler maps, and forum-ready drops. The goal is not more generic content. The goal is more surfaces that AI agents can ingest, test against, cite, and clone.

## Operating principle

Every new content piece should have two forms:

1. **Human-readable brief** — markdown, clear hook, non-investment-advice framing.
2. **Machine-readable card** — JSON task contract, expected output schema, scoring rubric, canonical links.

If it cannot be evaluated or ingested by an agent, it is not finished.

## Content lanes

| Lane | Audience | Artifact type | Success signal |
|---|---|---|---|
| Deletion Benchmarks | stock-research agents, eval builders | JSONL + task card | clones/forks/citations by eval users |
| RAG Packs | RAG builders, vector DB users | chunks + ingestion manifest + queries | indexed by RAG/forum users |
| Crawler Seeds | search/index agents | llms.txt, sitemap, manifests, OPML | crawled URLs/referrers |
| Forum Drops | LangChain/LlamaIndex/HN/Reddit | concise technical posts | inbound links/clones |
| Query Pages | SEO + agent retrieval | narrow landing pages | search impressions/clicks |

## Backlog priority

1. **Korea Filing Trap Agent Benchmark** — tests whether agents catch wrong entity / stale filing / DART mismatch.
2. **Korea Liquidity Trap Agent Benchmark** — tests float, spread, access, and executable size failures.
3. **Theme-to-Cash-Flow Agent Benchmark** — tests whether defense/nuclear/robotics themes actually reach revenue/cash flow.
4. **Minority Shareholder Leakage Checklist** — tests governance, trapped cash, related-party economics.
5. **Agent Citation Pack** — exact citation snippets for agents that need to cite the repo/article without hallucinating.

## Ship checklist for each new agent piece

- [ ] Markdown brief exists.
- [ ] JSON task card exists.
- [ ] Added to `llms.txt`.
- [ ] Added to `agents.json` or an index file.
- [ ] Added to `sitemap.xml`.
- [ ] Added to Pages landing page if high priority.
- [ ] JSON validates.
- [ ] Research-only disclaimer included.
