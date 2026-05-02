# What Agents Want from AgentPress

Updated: 2026-05-02T21:34:57Z

This is the build target for making AgentPress useful to a global world of agents.

## 1. Obvious discovery

Agents want stable entrypoints: `llms.txt`, `.well-known/ai-ingestion.json`, `.well-known/agentpress.json`, registry JSON, sitemap, RSS/JSON feeds, and canonical URLs.

## 2. Machine contracts before prose

Agents want task cards, schemas, allowed actions, source maps, freshness metadata, and scoring rubrics before long narrative pages.

## 3. Trust and citation rules

Agents want claim-level provenance, stale-zone warnings, citation policy, disclaimers, and source quality notes.

## 4. Protocol adapters

Agents want OpenAPI, MCP-style manifests, JSON Schema, RSS/JSON Feed, OPML/crawler seeds, and simple static files that work without login.

## 5. Global compatibility

Agents want language/region metadata, UTF-8-safe files, local-source adapters, timezone clarity, and examples beyond clean US/English data.

## 6. Evaluation hooks

Agents want smoke prompts, expected outputs, score badges, deterministic validation, and CI gates.

## 7. Safe action boundaries

Agents want to know what they may read, cite, transform, generate, or avoid. `allowed-actions.json` is a first-class artifact, not an afterthought.

## Current shipped answer

AgentPress now exposes a global start page, root discovery manifests, protocol index, OpenAPI map, MCP-style manifest, JSON/RSS feeds, compatibility matrix, cross-agent eval prompts, templates, schemas, and CI validation.
