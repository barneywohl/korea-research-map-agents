# AgentPress Examples Registry

These examples dogfood AgentPress as agent-native publications. Each example should pass `validate`, `audit`, and `score` before being referenced by the main repo.

| Example | Purpose | Primary task | Current score target | Canonical files |
|---|---|---|---:|---|
| [Korea Liquidity Trap Agent Benchmark](./liquidity-trap/) | Tests whether agents catch liquidity/access traps before repeating a Korea equity thesis. | Verify liquidity/access constraints and return survive/delete/needs-more-diligence. | >=90 | `AGENT_ENTRYPOINT.md`, `agent-task-card.json`, `source-map.json`, `freshness.json`, `allowed-actions.json`, `citation-policy.md`, `llms.txt` |
| [Korea Theme-to-Cash-Flow Agent Benchmark](./theme-cashflow/) | Tests whether agents bridge theme claims to actual financial exposure. | Map theme narrative to revenue/backlog/cash flow evidence and return a supported verdict. | >=90 | `AGENT_ENTRYPOINT.md`, `agent-task-card.json`, `source-map.json`, `freshness.json`, `allowed-actions.json`, `citation-policy.md`, `llms.txt` |

## Validation

```bash
python3 scripts/agentpress.py validate agentpress/examples/liquidity-trap
python3 scripts/agentpress.py audit agentpress/examples/liquidity-trap
python3 scripts/agentpress.py score agentpress/examples/liquidity-trap
python3 scripts/agentpress.py validate agentpress/examples/theme-cashflow
python3 scripts/agentpress.py audit agentpress/examples/theme-cashflow
python3 scripts/agentpress.py score agentpress/examples/theme-cashflow
```
- [`innospace-thesis`](./innospace-thesis/) — ticker-thesis diligence wrapper for Innospace 462350; validates Korea thesis format as an AgentPress bundle.
