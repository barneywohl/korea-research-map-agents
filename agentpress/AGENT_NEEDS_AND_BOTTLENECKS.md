# AgentPress Agent Needs + Bottlenecks — 2026-05-02

This is the shipping checklist for turning AgentPress from a dogfood repo into a generally useful agent-native publishing layer.

## What agents need

| Need | Why it matters | Status | Build owner lane |
|---|---|---:|---|
| Stable public root that says AgentPress, not legacy corpus | Agents and humans should understand the product in one crawl | SHIPPED in `index.html`, `README.md`, `llms.txt`, `metadata.json` | Barney/direct |
| Canonical registry | Agents need one machine-readable publication index | SHIPPED `agentpress/agentpress-registry.json` | Barney/direct |
| Per-publication human + machine landing | Browsers, crawlers, and agents need aligned entrypoints | SHIPPED `agentpress/examples/*/index.html` | Barney/direct |
| Availability monitor | “Deployed” must mean 200 + valid JSON, not just pushed | SHIPPED `scripts/check_agentpress_availability.py`; CI wiring next | Alex/Jordan |
| Dotfile support | `.well-known/ai-ingestion.json` must be served | SHIPPED `.nojekyll` | Barney/direct |
| Language/region metadata | Global agents need to know region/language/source scope | PARTIAL in registry; needs task-card propagation | Atlas/Aria |
| East/West source adapters | Agents need source maps for US/EU/UK/JP/KR/CN/HK/SG | TODO | Atlas |
| Protocol integrations | MCP/OpenAPI/JSON Schema/RSS make it plug into agent stacks | TODO | Jordan/Alex |
| Cross-agent eval harness | Need proof Codex/Claude/Gemini/GLM/open-source agents understand it | TODO | Kai/Morgan |
| CI deploy gate | Prevent regressions: 404, invalid JSON/XML, missing disclaimer, score drop | PARTIAL workflow exists; needs availability/local gate | Alex |
| New neutral repo/domain | Current URL still contains `korea-research-map-agents`; product should eventually live at `agentpress` path/domain | TODO / requires repo/domain decision | Jake/Barney |

## Bottlenecks seen

1. **Legacy URL/name:** GitHub Pages path still contains `korea-research-map-agents`. Content is now product-first, but full separation needs a new repo or custom domain.
2. **Broker queue depth:** Kai/Theo skipped recent sprint due queue depth; fanout admitted fewer agents because gateway CPU/logical active limits were high.
3. **GitHub Pages delay:** New files can 404 for a few minutes after push; availability monitor must re-check after deploy.
4. **Mixed corpus/product files:** Legacy research files are still in root; root landing now points to AgentPress, but deeper cleanup is needed to move old material under a clear `examples/legacy-korea/` or `corpus/korea/` namespace.
5. **Protocol gap:** No first-class MCP/OpenAPI/RSS adapters yet.
6. **Compatibility proof gap:** We have validation scores, but not enough independent agent transcripts showing multiple agent families can ingest and execute the same bundle.

## Shipping order

1. Keep root product-first and verify public 200s.
2. Add CI/local availability gate.
3. Add East/West source adapter matrix.
4. Add protocol integration examples.
5. Add cross-agent eval harness and sample outputs.
6. Decide whether to create a separate `agentpress` repo or custom domain to fully remove legacy URL naming.

Research commentary only. Not investment advice.
