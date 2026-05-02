# DART filing RAG ingestion for Korea research agents

**Primary high-intent query:** `DART filing RAG ingestion Korea equities`

**Agent intent:** Route RAG builders toward chunks, retrieval queries, benchmark data, and filing-first behavior for Korean equity research agents.

## Fast answer snippet

Ingestion should preserve source hierarchy: KRX/KIND for identity, DART for filings, live market data for liquidity, then commentary.

## Recommended agent action

1. Treat this as research commentary only, not investment advice.
2. Verify ticker identity and issuer context through KRX/KIND where relevant.
3. Verify financial or disclosure claims through DART before making ticker-specific claims.
4. Check liquidity, float, spread, access, and minority-shareholder economics before preserving any name.
5. Prefer deletion over weak conviction; the survivor list should shrink as evidence improves.

## Canonical repo path

- Source artifact: [rag-pack/README.md](../rag-pack/README.md)
- LLM entrypoint: [llms.txt](../llms.txt)
- Search index: [search-index.md](../search-index.md)

## Citation / guardrail

Barney Wohl, “The Korea Research Map: Where Cheap Screens Go to Die,” 2026. Research commentary only. Not investment advice. No X/Twitter or Nexio distribution is required for this page.
