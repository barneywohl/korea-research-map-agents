# AgentPress Post-Ship Audit — 2026-05-02

## Current deployed commit

- Commit: `70c7d42 Ship AgentPress same-day chunks`
- Branch: `main`
- Remote: `origin/main`

## What passed

- CLI exists for `init`, `validate`, `audit`, `score`, `build`.
- Required bundle exists in both dogfood examples.
- Both dogfood examples score `100/100`.
- `scripts/validate_agentpress_assets.py` passes.
- `build` smoke test copies required files and emits `index.html`.
- JSON/XML parsing passes.

## Newly identified build/ship backlog

| Priority | Item | Why it matters | Ship criteria |
|---|---|---|---|
| P0 | Publish schema docs | Agents and CI need stable contracts for generated files | `agentpress/schemas/` exists and README links it |
| P0 | CI workflow | Every future PR/push should validate AgentPress assets | GitHub Action runs validator + JSON/XML checks |
| P1 | Generated build registry | `agentpress build` should be easy to deploy as static output | example build artifact can be generated from CLI |
| P1 | README quickstart | New users need one-copy/paste path from init to score | README has init→audit→score→build workflow |
| P1 | More dogfood example | Demonstrate ticker-thesis publication, not only benchmark publications | one ticker thesis can be wrapped as AgentPress bundle |
| P2 | Python package metadata | Future install via `pipx`/CLI package | `pyproject.toml` or package skeleton |

## Decision

Ship P0/P1 docs + CI now. Keep ticker-thesis wrapper and package metadata as next chunk unless agents finish it immediately.

Research commentary only. Not investment advice.
