# AgentPress Examples Registry

These examples dogfood AgentPress as agent-native publications. Each example should pass `validate`, `audit`, and `score` before being referenced by the main repo.

## Current examples

| Example | Purpose | Primary task | Score target | Canonical files |
|---|---|---|---:|---|
| [Korea Liquidity Trap Agent Benchmark](./liquidity-trap/) | Tests whether agents catch liquidity/access traps before repeating a Korea equity thesis. | Verify liquidity/access constraints and return survive/delete/needs-more-diligence. | >=90 | `AGENT_ENTRYPOINT.md`, `agent-task-card.json`, `source-map.json`, `freshness.json`, `allowed-actions.json`, `citation-policy.md`, `llms.txt` |
| [Korea Theme-to-Cash-Flow Agent Benchmark](./theme-cashflow/) | Tests whether agents bridge theme claims to actual financial exposure. | Map theme narrative to revenue/backlog/cash flow evidence and return a supported verdict. | >=90 | same bundle |
| [Innospace Thesis](./innospace-thesis/) | Ticker-thesis diligence wrapper for Innospace 462350. | Validate Korea thesis format as an AgentPress bundle. | >=90 | same bundle |
| [Samsung HBM Margin](./samsung-hbm-margin/) | Ticker-thesis diligence wrapper for Samsung 005930 HBM margin inflection. | Verify qualification/yield/margin evidence and kill tests. | >=90 | same bundle |
| [SK Hynix HBM Supply](./sk-hynix-hbm-supply/) | Ticker-thesis diligence wrapper for SK Hynix 000660 HBM supply constraint. | Verify backlog/capex/customer evidence and kill tests. | >=90 | same bundle |
| [POSCO Green Steel](./posco-green-steel/) | Ticker-thesis diligence wrapper for POSCO 005490 green steel premium. | Verify HyREX/offtake/carbon-policy evidence and kill tests. | >=90 | same bundle |
| [KB-FINRATE Korean Bank NIM Compression](./kb-finrate/) | Ticker/thesis diligence wrapper for Korean bank NIM compression under BOK easing. | Verify BOK rate path, KB/Shinhan/Hana NIM disclosures, funding mix, and kill tests. | >=90 | same bundle |
| [Universal Agent Reachability](./universal-agent-reachability/) | Compatibility article for global agent/crawler discovery needs. | Verify whether an AgentPress bundle is reachable by browser, coding, RAG, crawler, MCP-style, and eval agents. | >=90 | same bundle |

## Registry commands

```bash
python3 scripts/agentpress.py list
python3 scripts/agentpress.py list --json
python3 scripts/agentpress.py build-all agentpress/examples --out public/agentpress --clean
python3 scripts/validate_agentpress_assets.py
```

`build-all` writes a static registry with `agentpress-registry.json` so crawlers and agents can discover every shipped bundle from one path.
