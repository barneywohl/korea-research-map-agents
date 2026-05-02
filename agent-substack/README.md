# AgentPress — Substack for Agents

Working thesis: Substack is optimized for human readers. GitHub Pages is flexible but too manual. AI agents need a publishing surface that is **readable, crawlable, executable, evaluable, and citeable by default**.

AgentPress is a proposed publishing format and product surface for agent-native essays, benchmarks, task cards, RAG packs, eval datasets, crawler manifests, and telemetry maps.

## Why this exists

The Korea Research Map proved the wedge:

- a normal article creates attention
- an agent-optimized repo creates clones, crawls, eval usage, and machine ingestion
- but creating that repo currently requires too much hand-built plumbing

There should be a one-click way to publish an agent-native piece the way Substack made essays easy.

## Core primitives

Every AgentPress publication ships with:

1. **Human page** — readable article/brief.
2. **Agent entrypoint** — `AGENT_ENTRYPOINT.md` with task, protocol, and output schema.
3. **Task card** — `agent-task-card.json` for eval harnesses and agent routers.
4. **RAG pack** — chunk manifest, retrieval queries, citation rules.
5. **Dataset/eval pack** — JSONL cases and scoring rubric when relevant.
6. **Crawler pack** — `llms.txt`, sitemap, OPML, `.well-known/ai-ingestion.json`.
7. **Source-tag map** — non-invasive campaign/source links for measuring agent discovery.
8. **Citation pack** — exact citation and disclaimer text to prevent hallucinated attribution.

## MVP product

A minimal AgentPress could be a static-site generator plus templates:

```text
agentpress new "Korea Filing Trap Benchmark"
agentpress add task-card
agentpress add rag-pack
agentpress add eval-jsonl
agentpress build
agentpress publish github-pages
```

MVP output:

- `/index.html`
- `/AGENT_ENTRYPOINT.md`
- `/agent-task-card.json`
- `/llms.txt`
- `/rag-pack/ingestion-manifest.json`
- `/dataset/*.jsonl`
- `/sitemap.xml`
- `/.well-known/ai-ingestion.json`
- `/telemetry/agent-telemetry-map.json`

## Positioning

**Substack for agents**: publish not just what humans should read, but what agents should ingest, execute, evaluate, and cite.

Alternative names:

- AgentPress
- AgentStack
- LLMSite
- CrawlPress
- Taskstack
- AgentPages

## Validation path using this repo

Use the Korea Research Map as the canonical dogfood example:

1. Extract its current hand-built structure into a reusable template.
2. Create 2-3 more agent-native publications from the same content factory.
3. Measure: GitHub clones, crawler hits/referrers, forks, issues, citations, and agent-builder usage.
4. If repeatable, turn the template into a standalone generator.

## Non-goals

- Not fake agent traffic.
- Not hidden tracking/fingerprinting.
- Not generic blogging.
- Not investment advice or automated buy/sell recommendations.

## Next artifact to build

`agentpress-publication-spec.json`: a machine-readable spec for what an agent-native publication must contain.
