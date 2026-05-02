# AgentPress Schemas

These are lightweight JSON Schema contracts for the required AgentPress bundle. They are intentionally stable, readable, and strict enough for CI validation without blocking useful prose.

Required machine-readable files:

- [`agent-task-card.schema.json`](./agent-task-card.schema.json)
- [`source-map.schema.json`](./source-map.schema.json)
- [`freshness.schema.json`](./freshness.schema.json)
- [`allowed-actions.schema.json`](./allowed-actions.schema.json)
- [`ai-ingestion.schema.json`](./ai-ingestion.schema.json)

Validation entrypoint:

```bash
python3 scripts/validate_agentpress_assets.py
```

Research commentary only. Not investment advice.
