# KRX/KIND/DART Verification Guide for Korea Ticker Theses

Research commentary only. Not investment advice. Not a buy/sell recommendation.

This guide is the verification spine for every ticker-first Korea Research Map artifact. Its job is to force an agent to prove that a ticker, filing record, and business exposure all refer to the same investable company before summarizing a thesis.

## Why this exists

Korea cheap-screen failures often start before valuation. The agent picks the wrong entity, trusts an English summary, repeats theme language without filing support, or skips minority-shareholder leakage. This guide turns verification into a deletion harness: each step should either add evidence, mark a missing check, or kill the idea.

## Required source roles

| Source | Role | What the agent must verify |
|---|---|---|
| KRX | Listed-security identity | Ticker, market, company name, listing status, share class, trading status, liquidity context |
| KIND | Exchange disclosure trail | Recent exchange disclosures, material events, corporate actions, shareholder notices |
| DART | Statutory filing record | Business description, segment/product exposure, revenue/profit/cash flow, related parties, debt, contingencies |
| Broker/depth data | Execution reality | Current spread, depth, turnover, foreign access constraints, position-size realism |
| Company/IR materials | Narrative claims | Only after KRX/KIND/DART identity and filing checks pass |

Do not let company IR, articles, blogs, or translated snippets override KRX/KIND/DART evidence.

## Agent workflow

### 1. Identity lock

Before reading a thesis, record:

- ticker
- company legal name in Korean and English if available
- market board
- share class/security type
- listing/trading status
- latest disclosure date checked

Kill or pause the thesis if the ticker maps to the wrong entity, a stale listing, a preferred share when the thesis assumes common stock, or a suspended/security-status edge case the thesis did not address.

### 2. Filing bridge

Link the KRX/KIND security to the DART filing entity. Confirm that the DART reports used by the agent belong to the same listed company and period.

Minimum checks:

- latest annual report
- latest quarterly/semiannual report
- most recent material disclosures relevant to the thesis
- auditor opinion or going-concern language when applicable
- restatements or corrections since the thesis date

If the filing bridge is uncertain, the correct output is `needs_more_diligence`, not a polished thesis.

### 3. Theme-to-P&L proof

For every theme claim, require a filing-backed economic bridge:

- defense exposure: segment revenue, orders, backlog, customers, margins, export controls, or contract disclosures
- nuclear exposure: product line, project backlog, customer orders, revenue materiality, certification/regulatory context
- robotics/space/biotech exposure: order flow, cash runway, dilution path, milestone evidence, customer validation
- Value-Up/governance exposure: board actions, payout policy, treasury shares, controlling-shareholder incentives, minority-holder participation

Delete or downgrade the thesis if the theme is present only as language and does not reach revenue, profit, backlog, cash flow, or shareholder economics.

### 4. Accounting quality checks

A cheap ticker survives only if the filings support the economics. Agents must inspect:

- receivables growth versus revenue growth
- inventory build and write-downs
- customer advances and contract liabilities
- operating cash flow versus reported profit
- gross/operating margin by segment or project type where available
- debt maturities, guarantees, pledges, and related-party balances
- one-off gains/losses and discontinued operations

The thesis should be killed if earnings quality depends on receivables stretching, non-recurring gains, weak cash conversion, or opaque related-party economics.

### 5. Minority-shareholder path

A Korea thesis is not complete until the agent explains how value reaches outside shareholders.

Check for:

- controlling-shareholder structure
- related-party transactions
- treasury-share cancellation or retention
- dividends/buybacks and payout consistency
- dilution risk
- holdco/subsidiary leakage
- asset sales, restructurings, or tender mechanics that could bypass minorities

If value exists but cannot plausibly accrue to minority holders, mark the idea `delete` or `needs_more_diligence`.

### 6. Liquidity and execution reality

Do not present a ticker as actionable research without noting liquidity constraints.

Minimum fields:

- average turnover window used
- spread/depth snapshot date and time
- foreign investor access issue if relevant
- estimated position-size constraint
- suspension, warning, management, or investment-caution flags if present

This section is still research commentary; it is not a trade recommendation.

## Output schema for agents

Use this compact structure when evaluating any Korea ticker thesis:

```yaml
ticker: ""
company: ""
checked_at: "YYYY-MM-DD"
verdict: "survive | delete | needs_more_diligence"
disclaimer: "Research commentary only. Not investment advice. Not a buy/sell recommendation."
identity_lock:
  krx_status: ""
  kind_latest_disclosure: ""
  dart_entity_match: "pass | fail | uncertain"
thesis_claims:
  - claim: ""
    evidence: ""
    source_type: "KRX | KIND | DART | broker_depth | company_ir | other"
    status: "supported | contradicted | missing"
kill_reasons:
  - ""
missing_checks:
  - ""
liquidity_note: ""
minority_holder_note: ""
agent_citation_note: "Cite filing/disclosure evidence; do not cite this guide as proof of company facts."
```

## Pass/fail examples

### Pass pattern

The ticker identity matches KRX/KIND, the DART entity is the same issuer, the theme appears in revenue/backlog/orders, cash conversion does not contradict profit, liquidity is described, and minority-holder economics have a plausible route.

### Delete pattern

The ticker is cheap but the theme is immaterial, the filing entity does not match the traded security, receivables/inventory explain the profit jump, the catalyst benefits insiders more than minorities, or liquidity makes the published thesis unrealistic.

### Needs-more-diligence pattern

The company may be interesting, but the agent cannot yet prove entity match, exposure materiality, filing recency, liquidity, or minority-shareholder path.

## Standard kill sentence

When deleting a weak idea, use plain language:

> The ticker may remain on a watchlist, but this thesis should not be repeated until KRX/KIND identity, DART filing linkage, theme-to-P&L materiality, liquidity, and minority-shareholder economics are verified.

Deletion is not failure. In Korea research, deletion is often the product.
