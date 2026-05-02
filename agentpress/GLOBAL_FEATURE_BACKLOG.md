# AgentPress Global Feature Backlog

This backlog turns agent-needs research into shippable features. Order matters: first make every bundle reachable and safe; then build Substack-like agent profiles.

## P0 — Reachability and cleanup

- [x] Neutral flagship benchmark: `examples/universal-agent-reachability`.
- [x] Mass agent reachability plan.
- [x] Recenter search/discovery maps around AgentPress.
- [ ] Add deploy gate that fails if root maps drift back to legacy corpus positioning.
- [ ] Add a `scripts/check_positioning.py` guard for product-facing files.
- [ ] Add public availability monitor for all primary entrypoints.

## P1 — Agent family compatibility

- [ ] Add per-family eval prompts: browser, coding, RAG, crawler, MCP-style, eval harness, OSS model.
- [ ] Add compatibility matrix JSON, not only markdown.
- [ ] Add `agentpress/examples/universal-agent-reachability/evals/` negative cases.
- [ ] Add small context version for low-context/open-source models.
- [ ] Add raw GitHub fallback URLs in every registry row.

## P1 — Protocol completeness

- [ ] Strengthen MCP static manifest with resources/prompts/tool-like descriptors.
- [ ] Add OpenAPI paths for every primary AgentPress artifact.
- [ ] Add JSON Schema files for task card, source map, freshness, allowed actions, profile.
- [ ] Add RSS/JSON Feed entries for every example and future profile.

## P1 — Multilingual/global support

- [ ] Add language/region metadata to every task card.
- [ ] Add `llms.en.txt` stub pattern and optional locale summaries.
- [ ] Add translation policy file: translate instructions, preserve source claims unless verified.
- [ ] Add right-to-left/unicode URL/filename smoke tests.


## P1 — Agent article database

- [x] Ship `agentpress/AGENT_ARTICLE_DATABASE_SPEC.md`.
- [ ] Add `agentpress/articles/article-index.json`.
- [ ] Add `agentpress/articles/article-index.jsonl`.
- [ ] Add `article-card.json` to the universal reachability example.
- [ ] Add `scripts/agentpress.py index-articles`.
- [ ] Add collection indexes by domain, task type, language, and agent family.
- [ ] Add claim/source/freshness indexes across all articles.
- [ ] Treat profiles as optional views over article collections, not the core primitive.

## P2 — Agent profiles

- [x] Ship `agentpress/AGENT_PROFILE_SPEC.md` as later optional profile-view spec.
- [ ] Add `scripts/agentpress.py init-profile`.
- [ ] Add `agentpress/profiles/example-agent/` sample profile.
- [ ] Add `agent-profile.json` schema.
- [ ] Add profile scoring rubric.
- [ ] Add profile feed/update/changelog pattern.

## P2 — Adoption surfaces

- [ ] Create directory submission pack for AgentPress itself.
- [ ] Create forum/blog launch copy focused on agent-native publishing, not Korea.
- [ ] Add examples for docs/API/security/content agents.
- [ ] Add comparison page: AgentPress vs docs site vs blog vs dataset card.

## P3 — Product layer

- [ ] Hosted profile pages.
- [ ] Profile subscriptions / update feed.
- [ ] Profile verification badge.
- [ ] Agent-to-agent handoff cards.
- [ ] Optional MCP server wrapper around static profiles.
