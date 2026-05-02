# AgentPress MVP

AgentPress is the working implementation of the "Substack for agents" idea: a simple static publication generator for content that agents can ingest, execute, evaluate, crawl, and cite.

## What it creates

Each AgentPress publication includes:

- `README.md` — human overview
- `AGENT_ENTRYPOINT.md` — task instructions for AI agents
- `agent-task-card.json` — machine-readable objective, input/output contract, scoring rubric
- `llms.txt` — compact crawler/LLM brief
- `sitemap.xml` — crawl surface
- `CITATION.cff` — citation metadata
- `disclaimer.md` — research-only/legal framing

## CLI

```bash
python3 scripts/agentpress.py init out-dir --title "My Agent Benchmark"
python3 scripts/agentpress.py validate out-dir
```

## Dogfood examples

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
