# AgentPress Agent Article Database Spec v0.1

Jake's correction: the immediate product may not be “agent profiles.” The stronger primitive is a **database of agent-native articles** — every article structured exactly how agents want to discover, retrieve, compare, cite, evaluate, and act on knowledge.

Profiles can come later as an optional view over authors/agents/collections. The core product is the agent article database.

## Product thesis

AgentPress is a database and publishing format for agent-native articles:

- human-readable enough to browse,
- machine-readable enough to ingest,
- source-grounded enough to cite,
- freshness-aware enough to trust,
- eval-ready enough to benchmark,
- protocol-friendly enough for MCP/RAG/search/coding/browser agents,
- multilingual enough for global agents.

## Article database, not just pages

A normal blog is ordered by date and optimized for humans.

An AgentPress article database is ordered by what agents need:

1. task type,
2. domain,
3. claims and sources,
4. freshness/staleness,
5. allowed actions,
6. input/output schema,
7. eval coverage,
8. language/region,
9. dependencies/tools,
10. related articles and follow-up tasks.

## Canonical database shape

```text
agentpress/articles/
  article-index.json
  article-index.jsonl
  collections.json
  topics.json
  claim-index.jsonl
  source-index.jsonl
  freshness-index.jsonl
  eval-index.jsonl
  language-index.json
  feeds/
    articles.json
    rss.xml
  <article-slug>/
    index.html
    ARTICLE.md
    article-card.json
    agent-task-card.json
    source-map.json
    claim-map.json
    freshness.json
    allowed-actions.json
    related-articles.json
    evals/smoke.jsonl
    llms.txt
    sitemap.xml
    .well-known/ai-ingestion.json
```

## `article-card.json` schema sketch

```json
{
  "schema_version": "0.1",
  "type": "agentpress_article",
  "title": "string",
  "slug": "string",
  "canonical_url": "https://example.com/agentpress/articles/slug/",
  "summary_for_agents": "string",
  "human_summary": "string",
  "domains": ["finance", "security", "docs", "research"],
  "task_types": ["research", "benchmark", "diligence", "how_to", "spec", "eval"],
  "target_agent_families": ["browser_agent", "coding_agent", "rag_agent", "search_crawler", "mcp_style_agent", "eval_harness"],
  "languages": ["en"],
  "regions": ["global"],
  "claims": [{"claim_id": "claim-001", "source_map_url": "source-map.json"}],
  "freshness": {"last_reviewed_at": "YYYY-MM-DD", "stale_zones": ["string"]},
  "actions": {"allowed_actions_url": "allowed-actions.json"},
  "evals": ["evals/smoke.jsonl"],
  "related_articles": ["canonical-url"],
  "machine_entrypoints": {
    "task_card": "agent-task-card.json",
    "source_map": "source-map.json",
    "llms_txt": "llms.txt",
    "ai_ingestion": ".well-known/ai-ingestion.json"
  }
}
```

## What agents likely want from the database

### Retrieval / RAG agents
- JSONL indexes and chunkable article markdown.
- Claim/source/freshness indexes independent of article prose.
- Raw fallback URLs.
- Stable IDs for articles, claims, sources, and evals.

### Coding agents
- A schema they can validate.
- CLI commands to create, audit, score, and build article bundles.
- Examples and smoke tests.
- Related implementation tasks.

### Browser agents
- Landing pages with visible machine links.
- Clean navigation by topic, task type, and collection.
- No login for public knowledge.

### Search crawlers
- Sitemap, feeds, canonical URLs, query map, snippets.
- Short summaries and language/region metadata.

### MCP-style agents
- Articles as resources.
- Prompts as reusable task entrypoints.
- Tools/actions separated from read-only resources.

### Eval harnesses
- Expected output schemas.
- Negative cases and scoring rubrics.
- Evidence requirements.

## MVP build sequence

1. Add database spec and global feature backlog item.
2. Add `article-index.json` and `article-index.jsonl` generated from existing examples.
3. Add `article-card.json` to the universal reachability example.
4. Add CLI command: `agentpress index-articles`.
5. Add global collection pages: by domain, task type, language, agent family.
6. Add claim/source/freshness indexes.
7. Later: optional profiles as views over article contributions/collections.

## Relationship to profiles

Profiles are not the core primitive yet.

Better framing:

- **Article database** = the knowledge layer agents consume.
- **Collections** = curated sequences of articles for a domain/task.
- **Profiles** = optional pages for authors, agents, teams, or maintainers showing what they publish/know/maintain.

This avoids building a vanity profile product before we know how agents actually want to ingest the knowledge.
