# AgentPress Global Readiness Gap List — 2026-05-02

Purpose: make AgentPress understandable and usable by any autonomous agent, crawler, RAG system, or human team across East/West markets.

## Already present
- Human landing pages and README docs.
- Agent entrypoints (`AGENT_ENTRYPOINT.md`).
- Machine task cards (`agent-task-card.json`).
- Source maps, freshness policy, allowed-actions, citation policy, disclaimers.
- `.well-known/ai-ingestion.json`, `llms.txt`, and `sitemap.xml` per bundle.
- CLI validation/audit/score/list/build-all commands.
- Six validated example publications scoring 100/100.
- Public GitHub Pages root available.

## Missing / needs build
1. **Public AgentPress registry path** — `/agentpress/` and `/agentpress/agentpress-registry.json` must be served directly, not only under `/public/agentpress/`.
2. **Per-publication HTML landing pages** — each bundle needs `index.html` for human/browser discovery plus links to machine assets.
3. **Dotfile serving** — GitHub Pages needs `.nojekyll` so `.well-known/ai-ingestion.json` is available.
4. **Global language metadata** — add `languages`, `regions`, and `translation_policy` to registry/task cards; start with English but explicit global readiness.
5. **East/West source adapters** — document source families for Korea/Japan/China/HK/Singapore and US/UK/EU: DART/KRX/KIND, EDINET/TDnet, HKEX/SGX, SEC EDGAR, Companies House, ESMA/issuer sites.
6. **Agent protocol integrations** — add examples for MCP resource, OpenAPI endpoint, JSON Schema, RSS/Atom feed, and optional ActivityPub-style discovery.
7. **Package/install distribution** — publishable Python package metadata is present but needs release notes and package smoke test in CI.
8. **Cross-agent compatibility tests** — create fixture prompts and expected outputs for Codex/Claude/Gemini/GLM/open-source agents.
9. **Availability monitor** — cron/check script should curl root, registry, llms, sitemap, and representative ingestion manifests after deploy.
10. **Deployment gate** — CI should fail if registry URLs 404, JSON/XML invalid, score <100 for required examples, or disclaimer missing.

## Build order
1. Fix public availability paths and `.nojekyll`.
2. Add global registry metadata and per-example `index.html`.
3. Add source-adapter matrix for East/West markets.
4. Add agent-protocol integration docs/samples.
5. Add compatibility eval harness and CI deploy gate.
