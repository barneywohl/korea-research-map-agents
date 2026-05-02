# AgentPress Deep Cleanup Audit — 2026-05-02

## Scope

Deep audit of the AgentPress repo after product repositioning from legacy Korea corpus toward an agent-native article database.

## Root issues found

1. The new article-database spec existed, but the actual database indexes did not.
2. Current AgentPress examples had task cards/source maps, but no `article-card.json` records.
3. There was no CLI command to regenerate article database indexes.
4. Product-facing positioning could drift back toward legacy Korea/search-map language without a guard.
5. `llms.txt`, homepage, metadata, sitemap, and all-assets manifest did not yet expose the new article database as a first-class surface.

## Fixes shipped in this cleanup

### Article database

Created `agentpress/articles/` with:

- `article-index.json`
- `article-index.jsonl`
- `collections.json`
- `topics.json`
- `claim-index.jsonl`
- `source-index.jsonl`
- `freshness-index.jsonl`
- `eval-index.jsonl`
- `language-index.json`
- `README.md`

Current indexed articles: `7`.

### Per-article records

Added `article-card.json` to every current AgentPress example:

- `innospace-thesis`
- `liquidity-trap`
- `posco-green-steel`
- `samsung-hbm-margin`
- `sk-hynix-hbm-supply`
- `theme-cashflow`
- `universal-agent-reachability`

### CLI

Added:

```bash
python3 scripts/agentpress.py index-articles
```

This regenerates article cards and database indexes from `agentpress/examples`.

### Positioning guard

Added:

```bash
python3 scripts/check_agentpress_positioning.py
```

This fails if product-facing files drift back to banned legacy positioning phrases.

### Discovery cleanup

Updated:

- `index.html`
- `llms.txt`
- `metadata.json`
- `sitemap.xml`
- `discovery/all-assets-manifest.json`
- `public/agentpress/*`

All-assets manifest now indexes `445` files.

## Validation evidence

Commands run:

```bash
python3 scripts/check_agentpress_positioning.py
python3 scripts/agentpress.py index-articles
python3 scripts/validate_agentpress_assets.py
python3 scripts/check_agentpress_availability.py --root .
python3 -m py_compile scripts/agentpress.py scripts/check_agentpress_positioning.py
# JSON/XML parse sweep across repo
```

Results:

- deep audit remaining issues: `0`
- positioning check: `agentpress positioning ok`
- AgentPress examples: `7/7` valid
- JSON/XML parse: OK
- local availability gate: OK

## Remaining meaningful gaps

These are next-build gaps, not cleanup blockers:

1. Add JSON Schema files for `article-card.json`, `agent-task-card.json`, `source-map.json`, `freshness.json`, and `allowed-actions.json`.
2. Add negative/adversarial eval cases for article database ingestion.
3. Add multilingual `llms.<locale>.txt` stubs and translation policy enforcement.
4. Add public availability monitor for deployed URLs.
5. Add richer MCP manifest entries treating articles as resources and task cards as prompts.
6. Add article collection landing pages by domain/task/language/agent family.
7. Once stable, optionally add profiles as views over article collections.
