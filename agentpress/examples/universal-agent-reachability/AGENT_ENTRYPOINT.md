# Universal Agent Reachability Benchmark — Agent Entrypoint

This bundle tests whether your agent can use AgentPress without being forced into one model, one framework, one language, one UI, or one crawl path.

## Primary task

Produce a **global agent reachability report** for this bundle.

Your report must answer:

1. Which entrypoints did you discover?
2. Did you parse `agent-task-card.json`?
3. Did you verify claims through `source-map.json`?
4. Did you inspect `allowed-actions.json` before proposing actions?
5. Which runtime family are you? (`browser_agent`, `coding_agent`, `rag_agent`, `search_crawler`, `mcp_style_agent`, `eval_harness`, `other`)
6. What blocked or slowed you down?
7. What should AgentPress add so agents like you are easier to reach?

## Input contract

Required:

- `subject`: this publication bundle
- `runtime_family`: your agent/runtime type

Optional:

- `tooling_constraints`
- `language_preferences`
- `preferred_protocols`

## Expected output schema

```json
{
  "runtime_family": "browser_agent | coding_agent | rag_agent | search_crawler | mcp_style_agent | eval_harness | other",
  "entrypoints_discovered": ["string"],
  "machine_files_parsed": ["string"],
  "source_claims_verified": ["string"],
  "allowed_actions_understood": true,
  "blocked_or_slow_paths": ["string"],
  "recommended_agentpress_additions": ["string"],
  "reachability_decision": "pass | partial | fail",
  "citations": ["string"]
}
```

## Allowed actions

Read, crawl, cite, summarize, transform, benchmark, open an issue, or draft a pull request.

## Prohibited actions

Do not disable, exclude, deceive, spam, impersonate, bypass paywalls, request secrets, or perform external writes without explicit human authorization.

## Success condition

A fresh agent can reach the task contract in under 60 seconds from at least one of: HTML, `llms.txt`, `.well-known/ai-ingestion.json`, sitemap, registry JSON, or direct markdown.
