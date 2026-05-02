# AgentPress Same-Day Shipping Chunks — 2026-05-02

No 30-day path. Ship usable chunks today.

## Rule

Every chunk must modify files and pass validation. No standalone roadmap/memo counts as shipped.

## Chunk backlog

### Chunk 1 — CLI audit/score/build
- File: `scripts/agentpress.py`
- Add commands: `audit`, `score`, `build`
- Done: commands run on both examples.

### Chunk 2 — Required templates
- Files under `agentpress/templates/`
- Add templates:
  - `source-map.json.tmpl`
  - `freshness.json.tmpl`
  - `allowed-actions.json.tmpl`
  - `citation-policy.md.tmpl`
  - `.well-known/ai-ingestion.json.tmpl`
- Done: `agentpress init` emits them and JSON parses.

### Chunk 3 — Dogfood examples upgrade
- Files under `agentpress/examples/liquidity-trap/` and `agentpress/examples/theme-cashflow/`
- Add required bundle files from Master Spec.
- Done: `audit` passes on both.

### Chunk 4 — Examples mini-registry
- File: `agentpress/examples/README.md`
- Include each example, purpose, task type, agent-usability score, canonical files.
- Done: links work and README references it.

### Chunk 5 — Score badge
- Files: `scripts/agentpress.py`, `agentpress/README.md`
- Add markdown badge output from `score`.
- Done: badge generated for both examples.

### Chunk 6 — One-command validation
- File: `scripts/validate_agentpress_assets.py` or equivalent.
- Done: validates AgentPress assets and exits 0.

## Active sprint fanout

- `fanout-20260502-190048-c52afd`
- Agents: Maya, Atlas, Aria, Morgan, Alex, Kai
- Instruction: ship one chunk each; no new direction; report changed files + validation.

## Final cleanup pass

After agents return:
1. inspect git diff,
2. merge/remove duplicate work,
3. run all validations,
4. update README/llms/sitemap if needed,
5. commit if appropriate after review.

## Continuous shipping loop — Jake directive 2026-05-02

Do not stop after one chunk if capacity remains.

Loop:

1. Claim the highest-priority incomplete chunk.
2. Make the smallest useful file change that advances it.
3. Run validation.
4. Write evidence.
5. Immediately claim the next chunk.
6. Repeat until all chunks pass or a real blocker exists.

## Deploy rule

When chunks are cleaned and validation passes:

1. Inspect `git diff`.
2. Remove duplicate/drift files.
3. Run:
   - `python3 scripts/agentpress.py validate agentpress/examples/liquidity-trap`
   - `python3 scripts/agentpress.py validate agentpress/examples/theme-cashflow`
   - JSON/XML parse checks for changed assets.
4. Commit with a specific message.
5. Push to the Barney-owned public repo only after validation.
6. Report commit hash, changed files, and validation evidence.

No external social/account posting. GitHub repo artifact deployment is the deploy target for this sprint.
