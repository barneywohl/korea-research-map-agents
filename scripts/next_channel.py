#!/usr/bin/env python3
import json, pathlib, datetime
root = pathlib.Path(__file__).resolve().parents[1]
queue = json.loads((root/'growth-system/channel-rotation-queue.json').read_text())['queue']
log = root/'growth-system/channel-attempt-log.jsonl'
seen_blocked=set(); seen_done=set()
if log.exists():
    for line in log.read_text().splitlines():
        if not line.strip(): continue
        rec=json.loads(line)
        if rec.get('result')=='blocked': seen_blocked.add(rec['channel'])
        if rec.get('result') in ('posted','live','done'): seen_done.add(rec['channel'])
for item in sorted(queue, key=lambda x:x['priority']):
    if item['channel'] not in seen_done and item['channel'] not in seen_blocked:
        print(json.dumps(item, indent=2, ensure_ascii=False)); break
else:
    print(json.dumps({'status':'all_channels_attempted','next':'refresh research and add new channels'}, indent=2))
