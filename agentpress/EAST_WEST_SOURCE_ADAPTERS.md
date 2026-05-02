# AgentPress East/West Source Adapter Matrix

AgentPress should work globally by making source expectations explicit per market/region. This file defines the first adapter map for agent bundles.

| Region | Primary filing / disclosure sources | Market data sources | Agent failure modes to guard against | Required metadata |
|---|---|---|---|---|
| US | SEC EDGAR, company IR, exchange notices | Nasdaq/NYSE/IEX/Polygon/Yahoo/FMP | ticker/entity mismatch, stale 10-K/10-Q, non-GAAP misuse | `jurisdiction=US`, `filing_system=SEC_EDGAR`, accession/date |
| UK | Companies House, RNS, LSE issuer notices | LSE, FCA, company IR | share-class confusion, AIM liquidity, old filings | `jurisdiction=UK`, company number, RNS IDs |
| EU | ESMA, national regulators, issuer IR | Euronext/Deutsche Börse/Borsa/etc. | multilingual filing mismatch, IFRS segment ambiguity | `jurisdiction=EU-*`, language, regulator URL |
| Korea | DART, KIND, KRX, company IR | KRX, broker/depth/spread checks | theme-vs-entity mismatch, minority-shareholder leakage, liquidity | `jurisdiction=KR`, ticker, DART corp code, KIND links |
| Japan | EDINET, TDnet, JPX, company IR | JPX, broker/depth/spread checks | translation loss, cross-shareholding, segment names | `jurisdiction=JP`, EDINET code, TDnet links |
| Hong Kong | HKEXnews, SFC, company IR | HKEX | share-class/entity mismatch, related-party transactions | `jurisdiction=HK`, stock code, HKEX links |
| Singapore | SGXNet, ACRA, company IR | SGX | issuer-action timing, thin liquidity | `jurisdiction=SG`, SGX code, announcement IDs |
| China A-shares | SSE/SZSE/BSE filings, CSRC, company IR | SSE/SZSE/BSE | language/translation ambiguity, state ownership, trading halts | `jurisdiction=CN`, exchange, stock code, filing URL |
| India | NSE/BSE filings, MCA, SEBI, company IR | NSE/BSE | promoter pledges, related-party, share-class | `jurisdiction=IN`, exchange, ISIN, filing URL |
| Global crypto/Bitcoin credit | on-chain explorer, custodian attestations, legal agreements, risk reports | mempool/chain APIs, exchange market data | address ownership mismatch, confirmation policy, oracle lag | `network`, address, txid, confirmation threshold |

## Adapter contract for future bundles

Add to `agent-task-card.json` or companion metadata:

```json
{
  "regions": ["global", "east_asia", "west"],
  "languages": ["en"],
  "source_adapters": [
    {
      "region": "KR",
      "filing_system": "DART",
      "exchange_disclosure": "KIND",
      "market_data": "KRX",
      "required_identifiers": ["ticker", "corp_code", "filing_url"]
    }
  ],
  "translation_policy": "Preserve source-language titles and cite machine translations as secondary only."
}
```

Research commentary only. Not investment advice.
