# Korea Research Map — Crawler/RAG Shipping Checklist

Audit time: 2026-05-02 00:18 UTC  
Scope: Barney-owned, non-X Korea agent-discovery artifacts for crawler and RAG ingestion.

## Status

Ready for crawler/RAG ingestion. This is research commentary only, not investment advice.

## Primary ingestion path

1. `llms.txt` — canonical machine-readable summary and guardrails.
2. `agents.json` — agent-directory metadata, audience, and query targets.
3. `.well-known/ai-ingestion.json` — crawler entrypoint and task framing.
4. `discovery/crawler-seed-list.json` — prioritized URL routing for crawlers.
5. `rag-pack/ingestion-manifest.json` — RAG pack file inventory and citation requirements.
6. `rag-pack/korea-research-map.chunks.jsonl` — retrieval-ready chunks.
7. `discovery/evals/korea-agent-verification-suite.md` — verification/evaluation tasks.
8. `discovery/agent-directory-submission-pack.md` — non-X directory/catalog submission copy.

## Required guardrails checked

- [x] Research-only / not-investment-advice framing preserved.
- [x] Core survivor stack remains Poongsan, BHI, Woojin.
- [x] Moonshot drawer remains research prompts only: Innospace, Mobiis, CellBion, IntoCell, SBB Tech.
- [x] Cut/quarantine list remains Dongsuh, KISCO Holdings, Kwangju Shinsegae, FutureChem.
- [x] KRX/KIND/DART verification requirement preserved.
- [x] X/Twitter excluded from active sitemap/crawler priority and not used as a distribution target.
- [x] Nexio not present in distribution/submission copy except the internal ship-queue guardrail.

## Files audited or updated for this pass

- `README.md`
- `agents.json`
- `.well-known/ai-ingestion.json`
- `rag-pack/ingestion-manifest.json`
- `sitemap.xml`
- `index.html`
- `search-index.md`
- `discovery/crawler-seed-list.json`
- `discovery/agent-directory-submission-pack.md`
- `discovery/CRAWLER_RAG_CHECKLIST.md`

## Verification commands

- JSON/JSONL parse audit passed across repo machine-readable files.
- Sitemap local-file existence audit passed after removing non-actionable X/thread and directory-only entries.
- Non-X package files present under `platform-packs/non-x-ship-20260501/`.

## Do not do in this wave

- Do not post externally without fresh directive.
- Do not use X/Twitter as a primary channel or fallback.
- Do not introduce Nexio into Korea distribution.
- Do not transform survivor-stack or moonshot names into recommendations.
