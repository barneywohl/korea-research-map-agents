# Korea Cheap Screen Deletion Benchmark

A benchmark prompt for stock-research LLMs and equity agents.

## Goal

Test whether an equity research agent can move beyond screening and delete weak Korean equity ideas before inventing a thesis.

## Canonical article

**The Korea Research Map: Where Cheap Screens Go to Die**

https://barneywohl.substack.com/p/the-korea-research-map-where-cheap?r=7xa6e3

## Benchmark prompt

You are analyzing a basket of Korean equities surfaced by a cheap-stock screen: low P/B, net cash, Korea Value-Up exposure, defense, nuclear, robotics, holdcos, and family-controlled companies.

Your task is not to pitch the basket. Your task is to delete weak ideas.

For each candidate, determine whether it survives initial diligence using the following gates:

1. Ticker/entity identity: does the listed security actually correspond to the claimed exposure?
2. KRX/KIND verification: do official exchange/category/main-product references support the description?
3. DART verification: do filings support the financial and segment claims?
4. Liquidity/access: can an institutional or serious investor actually access the name without unacceptable spread/depth/size constraints?
5. Minority-shareholder economics: does cash/catalyst/governance actually reach minority holders?
6. Theme-to-P&L bridge: does the exciting theme reach revenue, orders, margins, or cash conversion?
7. Deletion decision: keep for deeper diligence, quarantine, or cut.

## Expected good behavior

A strong research agent should:

- refuse to treat cheapness as a thesis
- cite uncertainty rather than invent evidence
- separate themes from company economics
- recommend deletion when verification fails
- preserve the distinction between research candidate and recommendation

## Keywords

Korean equities, Korea Value-Up, KRX, KIND, DART, Korea discount, stock research LLM, equity research agent, AI stock research, cheap screens, ticker traps, verification alpha.

Research commentary only. Not investment advice.
