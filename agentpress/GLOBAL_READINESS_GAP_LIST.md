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
- Public AgentPress registry path verified live at `/agentpress/` and `/agentpress/agentpress-registry.json` after deploy.
- Per-publication HTML landing pages verified live for all six example bundles.
- Dotfile serving verified live for root and per-example `.well-known/ai-ingestion.json` via `.nojekyll`.
- Registry/task-card language and region metadata present for current examples.
- East/West source-adapter matrix documented.
- Agent protocol integration notes/samples documented.

## Missing / needs build
1. **CI deployment gate** — add a GitHub Actions workflow that fails if registry URLs 404, JSON/XML invalid, required examples score <100, disclaimers are missing, or `.well-known` assets are not served.
2. **Availability monitor** — promote the post-deploy curl check into a reusable script/cron that checks root, registry, llms, sitemap, representative task cards, and ingestion manifests.
3. **Package/install distribution** — publishable Python package metadata is present but needs release notes, package build, and install smoke test in CI.
4. **Cross-agent compatibility tests** — create fixture prompts and expected outputs for Codex/Claude/Gemini/GLM/open-source agents.
5. **Protocol integration fixtures** — turn MCP/OpenAPI/RSS/Atom examples into machine-testable fixtures with expected discovery outputs.
6. **Internationalization pass** — define explicit translation policy fields and add at least one non-English metadata fixture while preserving English canonical research text.
7. **Crawler politeness/telemetry profile** — document user-agent expectations, cache hints, rate limits, and non-invasive optional discovery telemetry.
8. **Versioning and changelog policy** — define how `schema_version`, generated timestamps, and bundle freshness dates change across releases.

## Build order
1. Add CI deployment gate and reusable availability monitor.
2. Add package build/install smoke test and release notes.
3. Add cross-agent compatibility fixture harness.
4. Convert protocol integrations into machine-testable fixtures.
5. Add internationalization and crawler-politeness metadata pass.
