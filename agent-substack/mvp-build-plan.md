# AgentPress MVP Build Plan

## Goal

Turn this Korea Research Map repo into a reusable publishing template for agent-native content.

## Phase 1 — Template extraction

- Freeze current repo structure as a reference implementation.
- Define required/recommended files in `agentpress-publication-spec.json`.
- Create starter templates for:
  - `AGENT_ENTRYPOINT.md`
  - `agent-task-card.json`
  - `llms.txt`
  - `.well-known/ai-ingestion.json`
  - `telemetry/agent-telemetry-map.json`

## Phase 2 — Generator

Build a simple local CLI:

```bash
agentpress init my-agent-publication
agentpress add benchmark
agentpress add rag-pack
agentpress validate
agentpress build
```

Validation checks:

- required files exist
- JSON parses
- sitemap includes required URLs
- disclaimers/citation present
- agent output schema exists

## Phase 3 — Dogfood publications

Create 3 AgentPress examples:

1. Korea Filing Trap Agent Benchmark
2. Korea Liquidity Trap Agent Benchmark
3. Theme-to-Cash-Flow Agent Benchmark

## Phase 4 — Distribution

Submit the AgentPress format to AI/RAG/dev communities as a technical standard, not a marketing post.

## Success metrics

- repeatable publication creation under 10 minutes
- GitHub clone/referrer lift after each artifact
- external forks or issues from builders
- agent/RAG tools can ingest the publication without custom instructions
