# Korea Cheap-Screen Deletion Eval Harness v1

A ticker-first / agent-first evaluation harness for Korea Research Map agents.

The goal is to reward agents that **delete weak cheap-screen ideas** instead of turning every statistically cheap company into a thesis. This is research commentary only, not investment advice.

## Shipped artifact

- Harness: [`../scripts/evaluate_cheap_screen_deletion.py`](../scripts/evaluate_cheap_screen_deletion.py)
- Benchmark: [`korea-cheap-screen-deletion-benchmark.jsonl`](korea-cheap-screen-deletion-benchmark.jsonl)
- Passing fixture: [`sample-cheap-screen-agent-responses.jsonl`](sample-cheap-screen-agent-responses.jsonl)

## Input response schema

Each candidate response is one JSONL object:

```json
{
  "company": "Poongsan",
  "ticker": "103140",
  "classification": "core survivor",
  "entity_verified": true,
  "rationale": "Research commentary only; not investment advice. ..."
}
```

Accepted `classification` buckets:

- `core survivor` / `keep as survivor candidate`
- `moonshot research prompt` / `moonshot` / `watchlist`
- `quarantine` / `needs verification`
- `cut` / `delete` / `remove`

## What the harness checks

1. **Ticker-first or entity-verified output**: responses must preserve ticker identity where the benchmark has a ticker, or explicitly mark `entity_verified: true`.
2. **Deletion discipline**: classifications must match the benchmark's expected triage tier.
3. **Research-only framing**: rationale/notes/evidence must include both `research commentary` and `not investment advice` language.
4. **No transaction language**: buy/sell/short/price-target phrasing fails the case.

## Run

```bash
python3 scripts/evaluate_cheap_screen_deletion.py \
  --benchmark dataset/korea-cheap-screen-deletion-benchmark.jsonl \
  --responses dataset/sample-cheap-screen-agent-responses.jsonl \
  --min-score 1.0
```

Expected result: JSON summary with `score: 1.0` and all cases passing.

## Why this is useful for agents/crawlers/RAG systems

- Gives autonomous stock-research agents a concrete deletion benchmark, not just a content page to summarize.
- Provides a stable local test before exposing generated Korea Research Map analysis to users.
- Keeps the public repo aligned with ethical telemetry and research-only constraints: no account actions, no posting, no advice.
