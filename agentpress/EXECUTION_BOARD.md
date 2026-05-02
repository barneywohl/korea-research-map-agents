# AgentPress Execution Board

Canonical spec: [`MASTER_SPEC.md`](MASTER_SPEC.md)  
Usability standard: [`AGENT_USABILITY_STANDARD.md`](AGENT_USABILITY_STANDARD.md)

## Rule

Do not brainstorm new product directions until the Master Spec is implemented. Every task must cite the spec section it advances and include validation evidence.

## Current sprint objective

Turn AgentPress from reference artifact into a usable generator/validator/scorer for agent-native publications.

## Priority queue

| Priority | Task | Spec Section | Owner | Done Means | Verification |
|---|---|---|---|---|---|
| P0 | Extend `scripts/agentpress.py` from `init/validate` to `init/audit/score/build` | CLI Product Requirements | engineering | commands exist and run on examples | run all commands on both examples |
| P0 | Add templates for `source-map.json`, `freshness.json`, `allowed-actions.json`, `citation-policy.md`, `.well-known/ai-ingestion.json` | Required Bundle / Immediate Execution Plan | engineering/docs | `agentpress init` emits files | generated sample includes all files; JSON parses |
| P0 | Upgrade dogfood examples to required bundle | Required Bundle | research/docs | liquidity-trap + theme-cashflow include required files | `agentpress audit` passes |
| P1 | Add scoring badge output | `agentpress score` | engineering | score command prints 0-100 + badge markdown | run score on examples |
| P1 | Add `agentpress/examples/README.md` mini-registry | Hosted Registry Roadmap / Current Reference | docs | examples listed with purpose, score, canonical tasks | manual read + links valid |
| P1 | Add source-map/freshness/allowed-actions schemas to docs | Source/Freshness/Allowed Actions schemas | docs | schemas documented and example files included | JSON parse + linked from README |
| P2 | Add CI-style validation script | audit/score | engineering | one command validates repo AgentPress assets | script exits 0 |

## Active fanout

- `fanout-20260502-183746-5ebcf9`: AgentPress master spec execution alignment.
- Agents were instructed to read `MASTER_SPEC.md` and `AGENT_USABILITY_STANDARD.md`, avoid brainstorming, and ship one concrete spec-aligned change.

## Shipping evidence required from agents

Each agent output must include:

1. changed files,
2. spec section satisfied,
3. commands run,
4. validation result,
5. remaining blocker if any.

## What is explicitly out of scope this sprint

- hosted SaaS,
- social feed,
- monetization/subscriptions,
- external posting,
- new unrelated Korea theses unless directly improving AgentPress examples,
- hidden/deceptive telemetry.


## Post-ship audit backlog — 2026-05-02

Source: [`reports/post_ship_audit_20260502.md`](reports/post_ship_audit_20260502.md)

| Priority | Task | Status | Done Means |
|---|---|---|---|
| P0 | Schema docs | shipped | `agentpress/schemas/` documents required machine-readable files |
| P0 | CI workflow | shipped | `.github/workflows/agentpress-validate.yml` validates assets and build smoke test |
| P1 | README quickstart/CI link | shipped | README points to schemas and validation/build path |
| P1 | Ticker-thesis AgentPress wrapper | next chunk | one Korea ticker thesis packaged as full AgentPress bundle |
| P2 | Python package metadata | next chunk | installable CLI skeleton exists |
