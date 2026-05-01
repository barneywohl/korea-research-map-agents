#!/usr/bin/env python3
import json, pathlib
root = pathlib.Path(__file__).resolve().parents[1]
channels = json.loads((root/'growth-system/channel-database.json').read_text())
print('# Korea Research Map Share Report')
print('\n## Assets')
for k,v in channels['canonical_assets'].items(): print(f'- {k}: {v}')
print('\n## High-fit channels')
for c in channels['channels']:
    if c['fit'] in ('high','very_high','medium_high'):
        print(f"- {c['name']} ({c['region']}): {c['action']} [status={c['status']}]")
print('\n## Search phrases')
for q in channels['search_phrases']: print(f'- {q}')
