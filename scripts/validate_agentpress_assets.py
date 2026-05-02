#!/usr/bin/env python3
"""Validate all AgentPress example assets in one command."""
import json
import pathlib
import subprocess
import sys
import xml.etree.ElementTree as ET

ROOT = pathlib.Path(__file__).resolve().parents[1]
EXAMPLES_ROOT = ROOT / 'agentpress/examples'


def discover_examples() -> list[pathlib.Path]:
    if not EXAMPLES_ROOT.exists():
        return []
    return sorted(
        p for p in EXAMPLES_ROOT.iterdir()
        if p.is_dir() and (p / 'agent-task-card.json').exists()
    )


def parse_repo_json_xml() -> None:
    for p in ROOT.rglob('*.json'):
        if '.git' in p.parts:
            continue
        json.loads(p.read_text(encoding='utf-8'))
    for p in ROOT.rglob('*.xml'):
        if '.git' in p.parts:
            continue
        ET.parse(p)


def run(cmd):
    print('+', ' '.join(str(c) for c in cmd))
    subprocess.run(cmd, cwd=ROOT, check=True)


def main() -> int:
    examples = discover_examples()
    if not examples:
        print('no AgentPress examples found', file=sys.stderr)
        return 1
    for ex in examples:
        rel = ex.relative_to(ROOT)
        run(['python3', 'scripts/agentpress.py', 'validate', str(rel)])
        run(['python3', 'scripts/agentpress.py', 'audit', str(rel)])
        run(['python3', 'scripts/agentpress.py', 'score', str(rel)])
    parse_repo_json_xml()
    print(f'agentpress asset validation ok ({len(examples)} examples)')
    return 0


if __name__ == '__main__':
    sys.exit(main())
