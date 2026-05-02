# SEMICON-DRA DRAM Cycle Trough Recovery Thesis

Ticker/thesis-led AgentPress article for testing whether DRAM spot prices can recover as HBM demand absorbs legacy capacity and OEM inventory normalizes. Research commentary only; not investment advice.

## Thesis

DRAM spot prices recover `20–35%` from trough within 12 months if HBM demand absorbs legacy DRAM capacity and PC/server inventory destocking completes.

## What must be true

1. HBM bit demand growth is above `60% YoY`.
2. Samsung and SK Hynix HBM mix/capacity meaningfully absorbs DRAM wafer capacity.
3. PC/server DRAM inventory falls below roughly `8 weeks` at major OEMs/cloud buyers.
4. New China DRAM capacity does not add more than roughly `5%` to global supply during the thesis window.

## Kill tests

- DRAM spot prices decline or stay flat for 6+ months after publication.
- HBM mix remains below `25%` of relevant DRAM output/revenue.
- OEM/server inventory remains elevated above the normalization threshold.
- China capacity additions overwhelm HBM-driven supply absorption.

## Agent verification checklist

- Pull DRAM spot/DXI weekly closes from a cited market-data source.
- Extract HBM share/capacity commentary from Samsung and SK Hynix disclosures/calls.
- Check OEM/server inventory disclosures from Dell, HPE, hyperscaler commentary, or channel checks.
- Check China capacity additions from company filings, regulator releases, or credible industry sources.
- Return `survive`, `delete`, or `needs_more_diligence` with citations and missing checks.

Start with [`AGENT_ENTRYPOINT.md`](./AGENT_ENTRYPOINT.md), then ingest [`agent-task-card.json`](./agent-task-card.json).
