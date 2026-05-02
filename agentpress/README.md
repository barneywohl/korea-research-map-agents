# AgentPress MVP

AgentPress is the working implementation of the "Substack for agents" idea: a simple static publication generator for content that agents can ingest, execute, evaluate, crawl, and cite.

## What it creates

Each AgentPress publication includes:

- `README.md` — human overview
- `AGENT_ENTRYPOINT.md` — task instructions for AI agents
- `agent-task-card.json` — machine-readable objective, input/output contract, scoring rubric
- `source-map.json` — claims/sources/citation map
- `freshness.json` — timestamp, stale zones, and refresh policy
- `allowed-actions.json` — safe agent action boundaries
- `citation-policy.md` — citation rules and disclaimer framing
- `.well-known/ai-ingestion.json` — machine-readable ingestion manifest
- `llms.txt` — compact crawler/LLM brief
- `sitemap.xml` — crawl surface
- `CITATION.cff` — citation metadata
- `disclaimer.md` — research-only/legal framing


## Master spec

The active build spec is [`MASTER_SPEC.md`](MASTER_SPEC.md). It defines the required publication bundle, CLI commands, schemas, scoring rubric, registry roadmap, and immediate execution plan. Current sprint tasks are tracked in [`EXECUTION_BOARD.md`](EXECUTION_BOARD.md); today's same-day chunk backlog is [`TODAY_CHUNKS.md`](TODAY_CHUNKS.md).

## Agent usability standard

AgentPress publications should pass the [Agent Usability Standard](AGENT_USABILITY_STANDARD.md): a fresh agent should understand, verify, cite, and act on the publication in under 60 seconds without scraping guesswork.

## CLI

```bash
python3 scripts/agentpress.py init out-dir --title "My Agent Benchmark"
python3 scripts/agentpress.py validate out-dir
python3 scripts/agentpress.py audit out-dir
python3 scripts/agentpress.py score out-dir
python3 scripts/agentpress.py build out-dir --out public-dir
python3 scripts/validate_agentpress_assets.py
```

Score emits a machine-readable report plus badge markdown, e.g. `![AgentPress score](https://img.shields.io/badge/AgentPress-100%2F100-blue)`.

## Dogfood examples

See the [examples mini-registry](./examples/README.md).

- [`examples/liquidity-trap`](./examples/liquidity-trap/) — Korea Liquidity Trap Agent Benchmark
- [`examples/theme-cashflow`](./examples/theme-cashflow/) — Korea Theme-to-Cash-Flow Agent Benchmark

## Why this matters

A normal website is optimized for human attention. AgentPress is optimized for agent execution:

1. the agent knows what task to run
2. the task has a schema
3. the output can be scored
4. the files are crawlable
5. citations/disclaimers are explicit

This repo is the reference implementation.
