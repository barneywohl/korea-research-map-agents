# KB-FINRATE Korean Bank NIM Compression Thesis

Ticker/thesis-led AgentPress article for Korean bank net-interest-margin compression under a BOK rate-cut transmission scenario. Research commentary only; not investment advice.

## Thesis

Korean major bank net-interest margins compress by roughly `15–25 bps` over four quarters if Bank of Korea cuts transmit through deposit repricing faster than loan-yield recovery.

## What must be true

1. Bank of Korea cuts the base rate by at least `25 bps` within the next 6 months.
2. Time-deposit / interest-bearing deposit funding remains material for KB Financial, Shinhan Financial Group, and Hana Financial Group.
3. Deposit repricing moves faster than loan-yield repricing for at least two quarters.
4. Fee income, credit costs, and trading gains do not fully offset the NIM compression.

## Kill tests

- BOK holds or raises rates for two consecutive quarters after article publication.
- Bank disclosures show deposit beta or funding mix is too small for meaningful margin pressure.
- Quarterly filings show stable/improving NIM despite the expected rate path.
- Fee income/credit-cost improvements offset the thesis at the pre-provision-profit level.

## Agent verification checklist

- Fetch BOK base-rate history and latest monetary policy statement.
- Pull quarterly NIM/net-interest-income data from KB, Shinhan, and Hana disclosures.
- Check FSS/bank-statistics funding mix and deposit repricing data where available.
- Compare loan-yield lag vs deposit-cost lag.
- Return `survive`, `delete`, or `needs_more_diligence` with citations and missing checks.

Start with [`AGENT_ENTRYPOINT.md`](./AGENT_ENTRYPOINT.md), then ingest [`agent-task-card.json`](./agent-task-card.json).
