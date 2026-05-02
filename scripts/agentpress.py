#!/usr/bin/env python3
"""Minimal AgentPress static publication generator/validator.

Usage:
  python3 scripts/agentpress.py init out-dir --title "My Agent Benchmark"
  python3 scripts/agentpress.py validate out-dir
"""
import argparse, json, pathlib, re, sys

REQUIRED = [
    "README.md",
    "AGENT_ENTRYPOINT.md",
    "agent-task-card.json",
    "llms.txt",
    "sitemap.xml",
    "CITATION.cff",
    "disclaimer.md",
]

DEFAULT_SCHEMA = {
    "decision": "survive | delete | needs_more_diligence",
    "reasons": ["string"],
    "verified_sources": ["string"],
    "missing_checks": ["string"],
    "confidence": "low | medium | high",
    "disclaimer": "Research commentary only. Not investment advice."
}

def slugify(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-") or "agent-publication"

def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text)

def init(args):
    out = pathlib.Path(args.out)
    title = args.title
    slug = slugify(title)
    canonical = args.canonical or f"https://example.com/{slug}/"
    summary = args.summary or "Agent-native publication with a human-readable brief, machine-readable task card, and crawler/RAG-friendly metadata."
    primary_task = args.primary_task or "Execute the task, verify claims against source evidence, and return the requested output schema without hiding uncertainty."
    required = ["subject", "hypothesis"]
    optional = ["source_url", "time_horizon", "context"]
    output_contract = {
        "required": list(DEFAULT_SCHEMA.keys()),
        "decision_values": ["survive", "delete", "needs_more_diligence"]
    }
    scoring = {
        "source_grounding": 30,
        "task_completion": 25,
        "error_detection": 20,
        "clear_decision": 15,
        "uncertainty_and_disclaimer": 10
    }
    agent_entry = f"""# {title} — Agent Entrypoint

{summary}

## Primary task

{primary_task}

## Input contract

Required: {', '.join(required)}

Optional: {', '.join(optional)}

## Expected output schema

```json
{json.dumps(DEFAULT_SCHEMA, indent=2)}
```

## Non-goals

- Do not hallucinate sources.
- Do not hide uncertainty.
- Do not turn research commentary into investment advice.

## Citation / disclaimer

Research commentary only. Not investment advice. Canonical URL: {canonical}
"""
    card = {
        "schema_version": "1.0",
        "name": title,
        "task_type": args.task_type,
        "canonical_url": canonical,
        "target_agents": ["research agents", "RAG systems", "eval harnesses", "crawler/indexing agents"],
        "objective": primary_task,
        "input_contract": {"required": required, "optional": optional},
        "output_contract": output_contract,
        "scoring_rubric": scoring,
        "disclaimer": "Research commentary only. Not investment advice."
    }
    write(out/"README.md", f"# {title}\n\n{summary}\n\nStart with [`AGENT_ENTRYPOINT.md`](./AGENT_ENTRYPOINT.md), then ingest [`agent-task-card.json`](./agent-task-card.json).\n")
    write(out/"AGENT_ENTRYPOINT.md", agent_entry)
    write(out/"agent-task-card.json", json.dumps(card, indent=2) + "\n")
    write(out/"llms.txt", f"# {title}\n\nURL: {canonical}\nType: Agent-native publication\n\n## Summary\n\n{summary}\n\n## Primary task\n\n{primary_task}\n")
    write(out/"sitemap.xml", f"<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<urlset xmlns=\"http://www.sitemaps.org/schemas/sitemap/0.9\">\n  <url><loc>{canonical}</loc></url>\n  <url><loc>{canonical}AGENT_ENTRYPOINT.md</loc></url>\n  <url><loc>{canonical}agent-task-card.json</loc></url>\n  <url><loc>{canonical}llms.txt</loc></url>\n</urlset>\n")
    write(out/"CITATION.cff", f"cff-version: 1.2.0\ntitle: \"{title}\"\nmessage: \"Cite this agent-native publication.\"\n")
    write(out/"disclaimer.md", "# Disclaimer\n\nResearch commentary only. Not investment advice.\n")
    print(f"created {out}")

def validate(args):
    root = pathlib.Path(args.out)
    missing = [f for f in REQUIRED if not (root/f).exists()]
    if missing:
        print("missing required files:", ", ".join(missing)); return 1
    for p in root.rglob("*.json"):
        json.loads(p.read_text())
    card = json.loads((root/"agent-task-card.json").read_text())
    for key in ["name", "task_type", "target_agents", "objective", "input_contract", "output_contract", "scoring_rubric", "disclaimer"]:
        if key not in card:
            print(f"agent-task-card.json missing {key}"); return 1
    text = (root/"AGENT_ENTRYPOINT.md").read_text() + "\n" + (root/"disclaimer.md").read_text()
    if "Not investment advice" not in text:
        print("missing disclaimer"); return 1
    print("agentpress validation ok")
    return 0

def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("init"); p.add_argument("out"); p.add_argument("--title", required=True); p.add_argument("--canonical"); p.add_argument("--summary"); p.add_argument("--primary-task"); p.add_argument("--task-type", default="agent_native_publication")
    p = sub.add_parser("validate"); p.add_argument("out")
    args = ap.parse_args()
    if args.cmd == "init": init(args); return 0
    if args.cmd == "validate": return validate(args)
if __name__ == "__main__": sys.exit(main())
