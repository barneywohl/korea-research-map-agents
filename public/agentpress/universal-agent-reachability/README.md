# Universal Agent Reachability Benchmark

A neutral AgentPress example for testing whether *many different kinds of agents* can discover, ingest, cite, transform, evaluate, and safely act on one static publication bundle.

This is intentionally **not** a market-research corpus. It is a universal compatibility target for browser agents, coding agents, RAG indexers, search crawlers, MCP-style agents, eval harnesses, and open-source model agents.

## Start here

- [`AGENT_ENTRYPOINT.md`](./AGENT_ENTRYPOINT.md) — agent task instructions
- [`agent-task-card.json`](./agent-task-card.json) — machine task contract
- [`source-map.json`](./source-map.json) — claim/source map
- [`freshness.json`](./freshness.json) — staleness policy
- [`allowed-actions.json`](./allowed-actions.json) — safe boundaries
- [`.well-known/ai-ingestion.json`](./.well-known/ai-ingestion.json) — discovery manifest
- [`llms.txt`](./llms.txt) — compact crawler/LLM brief

## Goal

No agent should be turned away because it prefers a different entrypoint. The same bundle should be reachable via HTML, markdown, JSON, JSONL evals, sitemap, `llms.txt`, and well-known manifests.

## Expected output from an agent

A compatibility report with:

1. files discovered,
2. task card parsed,
3. sources cited,
4. allowed/prohibited actions understood,
5. unsupported assumptions flagged,
6. runtime family identified,
7. pass/fail recommendation for global agent reachability.
