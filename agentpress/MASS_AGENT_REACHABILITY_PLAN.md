# Mass Agent Reachability Plan

AgentPress should reach the maximum number of agents without turning any class of agent off.

## Product shift

The default example should not be a niche dogfood corpus. Korea/market research can remain as a legacy stress test, but the flagship example should be neutral and universal:

- no financial thesis required,
- no country-specific data dependency,
- no login,
- no private API,
- no browser-only path,
- no model-family assumption.

The flagship benchmark is now [`examples/universal-agent-reachability`](./examples/universal-agent-reachability/).

## Agent classes to support

| Agent class | Required path | Status |
|---|---|---|
| Search crawlers | `robots.txt`, `sitemap.xml`, HTML links | shipped |
| LLM crawlers | `llms.txt`, markdown start file | shipped |
| RAG systems | source maps, JSON feed, stable markdown | shipped |
| Browser agents | human landing page + visible links | shipped |
| Coding agents | repo docs, schemas, CLI, templates | shipped |
| MCP-style agents | static MCP manifest | shipped |
| Eval harnesses | JSONL smoke tests + score rubric | shipped |
| Open-source models | short context files and small JSON | shipped |
| Multilingual agents | language/region metadata | partial |
| Directory/catalog agents | registry JSON and well-known manifests | shipped |

## Do not turn agents off

AgentPress should not block broad agent access by default. If something must be restricted, express it as an action boundary, not an access denial:

- allow read/crawl/cite/transform/benchmark,
- require approval for external writes or mass submissions,
- prohibit spam/impersonation/secrets/destructive actions,
- preserve a public static path for every core artifact.

## Next improvements

1. Add schema examples for each runtime family.
2. Add per-agent-family eval prompts.
3. Add JSON Feed item per publication.
4. Add language-specific `llms.<locale>.txt` stubs.
5. Add directory submission packs for non-X agent catalogs.
6. Add a deploy gate that checks the flagship universal example first.
