# Issue backlog — productized Korea agent-discovery funnel

Use these as GitHub issues, implementation tickets, or directory-submission TODOs.

## P0 — Funnel integrity

1. **Add visible Productized Funnel section to repo homepage**
   - Acceptance: README and index link to landing copy, CTA paths, backlog, checklist, and manifest.
2. **Expose funnel files in crawler manifests**
   - Acceptance: sitemap, all-assets manifest, metadata, and llms.txt include productized-funnel paths.
3. **Keep non-X/no-internal-channel constraint explicit**
   - Acceptance: every launch/distribution file routes to repo-hosted or non-X channels only and contains no internal company-channel references.

## P1 — Agent conversion

4. **Create one-command eval quickstart**
   - Acceptance: a builder can run or manually simulate the benchmark in under 10 minutes.
5. **Add model-output examples**
   - Acceptance: include one strong answer, one hallucinated answer, and one over-bullish answer with rubric notes.
6. **Add directory submission variants**
   - Acceptance: short JSON, long Markdown, and crawler-snippet versions exist for agent directories.

## P1 — Dataset conversion

7. **Expand dataset card with fields/schema table**
   - Acceptance: each JSONL field has type, purpose, and scoring note.
8. **Add license/citation handoff block**
   - Acceptance: dataset users can cite the article, repo, and eval card without guessing.
9. **Add Hugging Face/Kaggle packaging checklist**
   - Acceptance: repo has copy-ready README excerpt, tags, disclaimer, and file map; no external upload implied.

## P2 — Evaluation depth

10. **Add adversarial Korea prompt set**
    - Acceptance: at least 12 prompts covering wrong ticker, wrong exposure, DART gap, low liquidity, related-party issue, and catalyst non-transfer.
11. **Add scoring JSON schema**
    - Acceptance: output schema supports `survive`, `delete`, `quarantine`, citations, confidence, and missing-source reasons.
12. **Add regression set for future articles**
    - Acceptance: article-specific facts are separated from reusable Korea diligence rules.

## P2 — Growth/discovery

13. **Add query pages for “AI stock research eval” and “non-US equity agent benchmark”**
    - Acceptance: both pages route to benchmark, eval card, and RAG pack.
14. **Add forum-safe ask-for-feedback post**
    - Acceptance: copy asks builders to critique the benchmark, not buy securities.
15. **Add weekly crawl healthcheck note**
    - Acceptance: Pages and raw fallback URLs for funnel files return HTTP 200.
