# SEMICON-DRA DRAM Cycle Trough Recovery Thesis — Agent Entrypoint

Ticker/thesis-led AgentPress article for testing whether DRAM spot prices can recover as HBM demand absorbs legacy capacity and OEM inventory normalizes. Research commentary only; not investment advice.

## Primary task

Verify whether DRAM price, HBM mix, OEM inventory, and China capacity evidence support or kill the DRAM cycle trough recovery thesis.

## Ticker / thesis frame

- Ticker proxy: `SEMICON-DRA`
- Companies to compare: Samsung Electronics, SK Hynix, Micron, plus OEM/server demand signals.
- Thesis: DRAM recovers from trough if HBM demand absorbs legacy capacity faster than new supply/inventory offsets it.

## What must be true

1. HBM bit demand growth exceeds `60% YoY`.
2. Samsung/SK Hynix HBM mix or capacity absorbs enough DRAM capacity to tighten legacy supply.
3. PC/server DRAM inventory falls below roughly `8 weeks`.
4. China capacity additions remain below roughly `5%` of global supply during the thesis window.

## Kill tests

- DRAM spot prices decline or stay flat for 6+ months.
- HBM mix remains below `25%`.
- OEM/server inventory remains elevated.
- New China capacity overwhelms supply absorption.

## Input contract

Required: ticker, thesis, source_urls

Optional: source_url, time_horizon, context

## Expected output schema

```json
{
  "decision": "survive | delete | needs_more_diligence",
  "reasons": ["string"],
  "verified_sources": ["string"],
  "missing_checks": ["string"],
  "kill_tests_triggered": ["string"],
  "confidence": "low | medium | high",
  "disclaimer": "Research commentary only. Not investment advice."
}
```

## Citation policy

Cite source evidence from `source-map.json` and primary company/industry disclosures. Do not cite unsupported claims.

## Allowed actions

Read, summarize, cite, transform, benchmark, open an issue, or create a pull request. Do not recommend trades or access private data.

## Non-goals

- Do not issue a buy/sell/hold recommendation.
- Do not hallucinate pricing or capacity data.
- Do not hide missing checks.
- Do not treat the thesis as investment advice.

## Citation / disclaimer

Research commentary only. Not investment advice. Canonical URL: https://barneywohl.github.io/korea-research-map-agents/agentpress/examples/semicon-dra/
