# Industries served — unique list and per-industry analytics

Generated 2026-08-12 by `scripts/industries.py` from `outputs/companies.jsonl` → `enrichment.industries_served`. Regenerate, never hand-edit.

## What this counts, and what it does not

Every row below counts **vendors that published an industry block on their own website and whose block the enrichment pass captured within its four-fetch budget**. That is a count of self-declaration, not of market coverage, revenue, customers or wins.

| Denominator | Companies |
|---|---:|
| In the store | 237 |
| Declared ≥1 industry (the base for every number here) | **53** (22.4% of the store) |
| `industries_served` present but UNKNOWN — no block found in budget | 158 |
| Field absent — paste-only, third-party-only or unreachable records | 26 |

**The declaring base is Gartner-shaped** — 44 Gartner-only, 7 in both sources, 2 G2-only. G2 coverage in this study is 65 of 1,810 listings (3.6%), and that limit propagates straight into every count below.

**A vendor absent from an industry row is not evidence it does not serve that industry.** 184 of 237 companies never had an industry block read at all.

**Grade.** Every cell is `PRIMARY` / Rung 1 / `SELF-DECLARED` — read off the vendor's own page. Two self-declared sources agreeing is not corroboration, so **no industry row here is `CORROBORATED`, and none can be** without a revealed-behaviour source.

**Standing statement.** Demand-side evidence exists for none of competitor classes 2–7. Nothing here counts buyers; it counts vendors' claims about who they sell to.

**Ranking is within this source only** — the vendor-website population. It is never comparable with G2 or Gartner category counts, which have different bar heights.

---

## 1 · The unique industry list — 81 industries

Each named once. The label is the **most frequently published spelling** of that industry among the vendors, not a name invented here.

| # | Industry | Vendors | Also spelled as |
|---:|---|---:|---|
| 1 | **Financial Services** | 31 | finance, financial |
| 2 | **Retail** | 25 | retail stores |
| 3 | **Healthcare** | 21 | health |
| 4 | **Ecommerce** | 18 | e-commerce |
| 5 | **Travel** | 17 | tourism |
| 6 | **Hospitality** | 16 | — |
| 7 | **Insurance** | 14 | — |
| 8 | **Media** | 13 | news, publishers, publishing |
| 9 | **Banking** | 12 | bank, banks |
| 10 | **Telecommunication** | 12 | communications, telco, telecom, telecommunications |
| 11 | **Automotive** | 9 | automobile |
| 12 | **Entertainment** | 9 | — |
| 13 | **Manufacturing** | 9 | — |
| 14 | **Education** | 8 | — |
| 15 | **Government** | 8 | public sector, public services |
| 16 | **Restaurants** | 8 | restaurant |
| 17 | **CPG** | 7 | consumer goods, consumer packaged goods, fmcg |
| 18 | **Gaming** | 6 | social games, social gaming |
| 19 | **Technology** | 6 | hi tech, high tech, tech |
| 20 | **Utilities** | 6 | — |
| 21 | **Energy** | 5 | — |
| 22 | **Nonprofits** | 5 | ngos, non-profit |
| 23 | **Fintech** | 4 | — |
| 24 | **iGaming** | 4 | — |
| 25 | **Life Sciences** | 4 | — |
| 26 | **Logistics** | 4 | — |
| 27 | **Real Estate** | 4 | — |
| 28 | **Beauty** | 3 | cosmetics |
| 29 | **Credit Unions** | 3 | credit union |
| 30 | **Legal** | 3 | — |
| 31 | **SaaS** | 3 | — |
| 32 | **Aerospace** | 2 | — |
| 33 | **Airline** | 2 | — |
| 34 | **Capital Markets** | 2 | — |
| 35 | **EdTech** | 2 | — |
| 36 | **Food & Beverage** | 2 | food and beverage |
| 37 | **Higher Education** | 2 | — |
| 38 | **Home Services** | 2 | — |
| 39 | **Hotels** | 2 | — |
| 40 | **IT** | 2 | it services |
| 41 | **Sports** | 2 | — |
| 42 | **Wellness** | 2 | — |
| 43 | **Advertising and Marketing** | 1 | — |
| 44 | **Agriculture** | 1 | — |
| 45 | **Airports** | 1 | — |
| 46 | **Auto Services** | 1 | — |
| 47 | **Aviation** | 1 | — |
| 48 | **Fiber** | 1 | broadband |
| 49 | **Business Services** | 1 | — |
| 50 | **Car Dealerships** | 1 | — |
| 51 | **Churches** | 1 | — |
| 52 | **Coffee Shops** | 1 | — |
| 53 | **D2C** | 1 | — |
| 54 | **Defense** | 1 | — |
| 55 | **Distribution** | 1 | — |
| 56 | **Financial Advisors** | 1 | — |
| 57 | **Fuel Retail** | 1 | — |
| 58 | **Education (K-12)** | 1 | — |
| 59 | **Last-Mile Delivery** | 1 | — |
| 60 | **Lending** | 1 | — |
| 61 | **Luxury** | 1 | — |
| 62 | **Mixed-Use** | 1 | — |
| 63 | **Mortgage** | 1 | — |
| 64 | **Mutual Funds** | 1 | — |
| 65 | **Oil & Gas** | 1 | — |
| 66 | **Online Trading** | 1 | — |
| 67 | **Pet Services** | 1 | — |
| 68 | **Pharma** | 1 | — |
| 69 | **Pharmacy** | 1 | — |
| 70 | **Prediction Markets** | 1 | — |
| 71 | **Private Equity** | 1 | — |
| 72 | **PropTech** | 1 | — |
| 73 | **Salons** | 1 | — |
| 74 | **Satellite** | 1 | — |
| 75 | **Shopping Centers** | 1 | — |
| 76 | **Smart Cities** | 1 | — |
| 77 | **Software** | 1 | — |
| 78 | **Spas** | 1 | — |
| 79 | **Supply Chain** | 1 | — |
| 80 | **Ticketing** | 1 | — |
| 81 | **Transportation** | 1 | — |

### Shape of the list

| Measure | Value |
|---|---:|
| Industries named | 81 |
| Industry claims (vendor × industry pairs) | 358 |
| Declaring vendors | 53 |
| Industries per vendor — median / max | 7.5 / 15 |
| Industries claimed by exactly one vendor | 39 (48%) |
| Share of all claims held by the top 10 industries | 50% |

**The list is a short head and a long tail.** 39 of 81 industries rest on a single vendor's website — `SINGLE-SOURCE` in substance, and each one would disappear if that one vendor rewrote its nav. The top 10 hold 50% of all claims.

**Broadest claimers** (they inflate the tail): Tech Mahindra (15), HCLTech (14), Medallia (14), indigitall (12), EZ Texting (12).

---

## 2 · Per-industry analytics

`Both` = present in G2 **and** Gartner. `Median reviews` is the vendor's largest product review count — a measure of review-solicitation effort as much as customer volume. `Breadth` is the median number of industries those vendors each declare: low means the industry is claimed by focused vendors, high means it is claimed in passing by generalists.

| Industry | Vendors | Both | G2 | Gartner | Median reviews | Median categories | Breadth | Most-common co-claim |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| **Financial Services** | 31 | 5 | 5 | 31 | 37.5 | 1 | 8 | Retail (18) |
| **Retail** | 25 | 3 | 5 | 23 | 47.0 | 1 | 8 | Financial Services (18) |
| **Healthcare** | 21 | 2 | 3 | 20 | 10 | 1 | 9 | Financial Services (16) |
| **Ecommerce** | 18 | 2 | 3 | 17 | 9 | 2.0 | 8.0 | Financial Services (14) |
| **Travel** | 17 | 4 | 4 | 17 | 35 | 2 | 9 | Financial Services (15) |
| **Hospitality** | 16 | 3 | 4 | 15 | 56.0 | 2.0 | 9.0 | Travel (13) |
| **Insurance** | 14 | 0 | 1 | 13 | 42.0 | 1.0 | 11.0 | Healthcare (10) |
| **Media** | 13 | 3 | 3 | 13 | 36 | 2 | 9 | Financial Services (12) |
| **Banking** | 12 | 1 | 1 | 12 | 37.5 | 1.0 | 9.5 | Healthcare (10) |
| **Telecommunication** | 12 | 4 | 4 | 12 | 49 | 2.0 | 10.0 | Financial Services (10) |
| **Automotive** | 9 | 1 | 1 | 9 | 45 | 1 | 9 | Financial Services (9) |
| **Entertainment** | 9 | 3 | 3 | 9 | 75.0 | 3 | 9 | Financial Services (9) |
| **Manufacturing** | 9 | 0 | 0 | 9 | 39 | 1 | 10 | Financial Services (6) |
| **Education** | 8 | 0 | 0 | 8 | 7.0 | 2.0 | 8.0 | Healthcare (5) |
| **Government** | 8 | 0 | 0 | 8 | 5 | 1.0 | 9.0 | Healthcare (7) |
| **Restaurants** | 8 | 2 | 4 | 6 | 146 | 1.0 | 8.0 | Retail (6) |
| **CPG** | 7 | 1 | 1 | 7 | 60 | 1 | 10 | Retail (5) |
| **Gaming** | 6 | 1 | 1 | 6 | 45 | 2.0 | 6.0 | Financial Services (5) |
| **Technology** | 6 | 0 | 0 | 6 | 9 | 1.0 | 11.0 | Retail (5) |
| **Utilities** | 6 | 0 | 0 | 6 | 9 | 1.0 | 10.0 | Healthcare (6) |
| **Energy** | 5 | 0 | 0 | 5 | 24.0 | 1 | 10 | Healthcare (5) |
| **Nonprofits** | 5 | 1 | 3 | 3 | 445.0 | 1 | 10 | Retail (4) |
| **Fintech** | 4 | 1 | 1 | 4 | 119 | 2.0 | 4.5 | Healthcare (2) |
| **iGaming** | 4 | 0 | 0 | 4 | 128 | 1.5 | 5.5 | Financial Services (2) |
| **Life Sciences** | 4 | 0 | 0 | 4 | 24.0 | 1.0 | 14.0 | Financial Services (4) |
| **Logistics** | 4 | 0 | 0 | 4 | 1 | 1.0 | 10.5 | Travel (3) |
| **Real Estate** | 4 | 0 | 0 | 4 | 35 | 1.0 | 9.0 | Education (3) |
| **Beauty** | 3 | 1 | 1 | 3 | 712.5 | 1 | 8 | Financial Services (3) |
| **Credit Unions** | 3 | 0 | 0 | 3 | 60 | 1 | 8 | Banking (3) |
| **Legal** | 3 | 0 | 1 | 2 | 10 | 1 | 8 | Healthcare (3) |
| **SaaS** | 3 | 1 | 1 | 3 | 449.0 | 2 | 5 | Healthcare (2) |
| **Aerospace** | 2 | 0 | 0 | 2 | 63.5 | 1.0 | 8.5 | Advertising and Marketing (1) |
| **Airline** | 2 | 1 | 1 | 2 | 125.5 | 2.0 | 4.5 | Hospitality (1) |
| **Capital Markets** | 2 | 0 | 0 | 2 | 119 | 1.0 | 8.0 | Automotive (1) |
| **EdTech** | 2 | 1 | 1 | 2 | 465.0 | 3.0 | 6.0 | Healthcare (2) |
| **Food & Beverage** | 2 | 0 | 0 | 2 | 5 | 1.5 | 10.5 | Education (2) |
| **Higher Education** | 2 | 0 | 1 | 1 | 372.5 | 1.0 | 10.0 | Ecommerce (2) |
| **Home Services** | 2 | 0 | 0 | 2 | 10 | 1.0 | 9.0 | Financial Services (2) |
| **Hotels** | 2 | 0 | 1 | 1 | 1398 | 1.0 | 6.0 | Airports (1) |
| **IT** | 2 | 0 | 0 | 2 | — | 1.0 | 9.5 | Financial Services (2) |
| **Sports** | 2 | 1 | 1 | 2 | 887.5 | 4.0 | 9.0 | Entertainment (2) |
| **Wellness** | 2 | 0 | 0 | 2 | 5.5 | 1.0 | 10.0 | Financial Services (2) |
| **Advertising and Marketing** | 1 | 0 | 0 | 1 | 8 | 1 | 3 | Aerospace (1) |
| **Agriculture** | 1 | 0 | 0 | 1 | 35 | 1 | 9 | Automotive (1) |
| **Airports** | 1 | 0 | 0 | 1 | — | 1 | 6 | Hotels (1) |
| **Auto Services** | 1 | 0 | 0 | 1 | 10 | 1 | 8 | Home Services (1) |
| **Aviation** | 1 | 1 | 1 | 1 | 227 | 2 | 4 | Financial Services (1) |
| **Fiber** | 1 | 0 | 0 | 1 | — | 1 | 10 | Home Services (1) |
| **Business Services** | 1 | 0 | 0 | 1 | 60 | 1 | 12 | Pharma (1) |
| **Car Dealerships** | 1 | 0 | 1 | 0 | 744 | 1 | 12 | Nonprofits (1) |
| **Churches** | 1 | 0 | 1 | 0 | 744 | 1 | 12 | Nonprofits (1) |
| **Coffee Shops** | 1 | 0 | 0 | 1 | — | 1 | 6 | Airports (1) |
| **D2C** | 1 | 0 | 0 | 1 | — | 2 | 5 | Ecommerce (1) |
| **Defense** | 1 | 0 | 0 | 1 | 119 | 1 | 14 | Automotive (1) |
| **Distribution** | 1 | 0 | 0 | 1 | 2 | 2 | 3 | Retail (1) |
| **Financial Advisors** | 1 | 0 | 0 | 1 | 100 | 2 | 7 | Credit Unions (1) |
| **Fuel Retail** | 1 | 0 | 0 | 1 | 24 | 2 | 5 | Hospitality (1) |
| **Education (K-12)** | 1 | 0 | 1 | 0 | 744 | 1 | 12 | Nonprofits (1) |
| **Last-Mile Delivery** | 1 | 0 | 0 | 1 | 1 | 1 | 12 | Automotive (1) |
| **Lending** | 1 | 0 | 0 | 1 | — | 2 | 5 | D2C (1) |
| **Luxury** | 1 | 1 | 1 | 1 | 1688 | 6 | 9 | Gaming (1) |
| **Mixed-Use** | 1 | 0 | 0 | 1 | — | 1 | 6 | Airports (1) |
| **Mortgage** | 1 | 0 | 0 | 1 | 60 | 1 | 12 | Pharma (1) |
| **Mutual Funds** | 1 | 0 | 0 | 1 | — | 2 | 5 | D2C (1) |
| **Oil & Gas** | 1 | 0 | 0 | 1 | 9 | 3 | 15 | Media (1) |
| **Online Trading** | 1 | 0 | 0 | 1 | 128 | 2 | 9 | Gaming (1) |
| **Pet Services** | 1 | 0 | 0 | 1 | 10 | 1 | 8 | Home Services (1) |
| **Pharma** | 1 | 0 | 0 | 1 | 60 | 1 | 12 | Credit Unions (1) |
| **Pharmacy** | 1 | 0 | 0 | 1 | 1 | 1 | 8 | Higher Education (1) |
| **Prediction Markets** | 1 | 0 | 0 | 1 | 128 | 2 | 9 | Gaming (1) |
| **Private Equity** | 1 | 0 | 0 | 1 | 9 | 3 | 15 | Media (1) |
| **PropTech** | 1 | 0 | 0 | 1 | 9 | 1 | 10 | Government (1) |
| **Salons** | 1 | 0 | 1 | 0 | 1398 | 1 | 6 | Hotels (1) |
| **Satellite** | 1 | 0 | 0 | 1 | 8 | 1 | 3 | Advertising and Marketing (1) |
| **Shopping Centers** | 1 | 0 | 0 | 1 | — | 1 | 6 | Airports (1) |
| **Smart Cities** | 1 | 0 | 0 | 1 | — | 1 | 6 | Airports (1) |
| **Software** | 1 | 0 | 0 | 1 | — | 1 | 10 | Home Services (1) |
| **Spas** | 1 | 0 | 1 | 0 | 1398 | 1 | 6 | Hotels (1) |
| **Supply Chain** | 1 | 0 | 0 | 1 | 9 | 1 | 10 | Government (1) |
| **Ticketing** | 1 | 0 | 0 | 1 | 63 | 1 | 7 | Automotive (1) |
| **Transportation** | 1 | 0 | 0 | 1 | 60 | 1 | 12 | Pharma (1) |

### Channel and commercial posture, by industry

Each cell shows the count **over the vendors in that industry for whom the field is known** — the denominator is printed, because these fields are far from complete and a bare percentage would hide that.

| Industry | Vendors | Channels declared by | Top channels | Publishes price | Free tier | HQ published |
|---|---:|---:|---|---:|---:|---|
| **Financial Services** | 31 | 29 | email (26), sms (14), push (11), whatsapp (10) | 7/14 | 6 | US 5, IN 1 |
| **Retail** | 25 | 21 | email (18), sms (13), push (9), whatsapp (8) | 4/11 | 3 | US 5 |
| **Healthcare** | 21 | 19 | email (17), sms (6), voice (5), push (4) | 6/9 | 4 | US 4, IN 1 |
| **Ecommerce** | 18 | 18 | email (17), whatsapp (11), sms (10), push (10) | 4/7 | 5 | US 2 |
| **Travel** | 17 | 16 | email (15), sms (10), whatsapp (10), push (8) | 2/9 | 4 | US 4 |
| **Hospitality** | 16 | 15 | email (14), sms (11), whatsapp (8), push (8) | 3/9 | 4 | US 4 |
| **Insurance** | 14 | 11 | email (8), sms (5), voice (4), chat (4) | 3/6 | 2 | US 1, IN 1 |
| **Media** | 13 | 13 | email (11), sms (9), push (8), whatsapp (7) | 1/7 | 2 | US 2, IN 1 |
| **Banking** | 12 | 9 | email (8), sms (4), push (4), whatsapp (4) | 1/3 | 0 | IN 1 |
| **Telecommunication** | 12 | 10 | email (8), sms (7), push (5), whatsapp (4) | 0/3 | 0 | US 1, IN 1 |
| **Automotive** | 9 | 9 | email (7), sms (3), push (2), rcs (2) | 3/5 | 2 | US 1 |
| **Entertainment** | 9 | 9 | email (8), sms (7), push (5), whatsapp (4) | 1/5 | 1 | US 2, IN 1 |
| **Manufacturing** | 9 | 6 | email (3), chat (2), voice (1) | 2/4 | 0 | IN 1 |
| **Education** | 8 | 8 | email (7), whatsapp (4), chat (4), sms (3) | 3/3 | 2 | IN 1 |
| **Government** | 8 | 7 | email (6), voice (2), sms (2), chat (2) | 1/2 | 1 | US 1 |
| **Restaurants** | 8 | 7 | email (6), sms (5), push (3), rcs (3) | 4/7 | 3 | US 2 |
| **CPG** | 7 | 5 | email (5), sms (3), whatsapp (2), push (1) | 0/2 | 0 | US 2 |
| **Gaming** | 6 | 5 | email (4), sms (4), push (4), whatsapp (3) | 2/4 | 2 | US 1 |
| **Technology** | 6 | 5 | email (3), voice (2), sms (2), chat (2) | 0/3 | 0 | US 2, IN 1 |
| **Utilities** | 6 | 4 | email (3), chat (2), sms (1) | 0/0 | 0 | IN 1 |
| **Energy** | 5 | 3 | email (2), chat (1) | 0/0 | 0 | IN 1 |
| **Nonprofits** | 5 | 5 | email (5), sms (2), voice (2), rcs (1) | 2/2 | 2 | US 1 |
| **Fintech** | 4 | 4 | email (4), sms (3), push (3), in-app (2) | 3/3 | 1 | US 1 |
| **iGaming** | 4 | 4 | email (4), whatsapp (4), push (3), sms (3) | 2/3 | 1 | US 1 |
| **Life Sciences** | 4 | 3 | email (1), voice (1), chat (1) | 0/1 | 0 | IN 1 |
| **Logistics** | 4 | 3 | email (3), voice (2), sms (1), push (1) | 2/3 | 2 | US 1 |
| **Real Estate** | 4 | 4 | email (4), direct-mail (1), sms (1), whatsapp (1) | 2/2 | 1 | — |
| **Beauty** | 3 | 3 | email (3), push (2), whatsapp (2), sms (1) | 1/2 | 1 | US 1 |
| **Credit Unions** | 3 | 2 | email (2), sms (1), push (1), in-app (1) | 1/2 | 0 | — |
| **Legal** | 3 | 3 | email (3), sms (1), rcs (1), voice (1) | 2/2 | 2 | US 2 |
| **SaaS** | 3 | 3 | email (3), whatsapp (2), voice (2), sms (1) | 3/3 | 2 | US 1 |
| **Aerospace** | 2 | 1 | email (1) | 0/0 | 0 | — |
| **Airline** | 2 | 1 | email (1), sms (1), push (1), web-push (1) | 0/0 | 0 | — |
| **Capital Markets** | 2 | 2 | email (2), sms (1), whatsapp (1), voice (1) | 1/1 | 1 | US 1 |
| **EdTech** | 2 | 2 | email (2), sms (2), push (2), in-app (2) | 1/1 | 0 | US 1 |
| **Food & Beverage** | 2 | 2 | email (2), voice (2), sms (1), push (1) | 1/1 | 1 | — |
| **Higher Education** | 2 | 2 | email (2), sms (1), rcs (1), voice (1) | 1/1 | 1 | US 1 |
| **Home Services** | 2 | 2 | email (2), direct-mail (1), ads (1) | 1/1 | 1 | US 1 |
| **Hotels** | 2 | 2 | email (2), sms (2), push (1), voice (1) | 1/2 | 1 | — |
| **IT** | 2 | 2 | email (2), direct-mail (1), voice (1) | 1/1 | 1 | — |
| **Sports** | 2 | 2 | email (2), sms (2), push (2), rcs (2) | 0/2 | 1 | — |
| **Wellness** | 2 | 2 | email (2), ads (1) | 2/2 | 2 | US 1 |
| **Advertising and Marketing** | 1 | 0 | — | 0/0 | 0 | — |
| **Agriculture** | 1 | 1 | email (1) | 0/0 | 0 | — |
| **Airports** | 1 | 1 | email (1), sms (1) | 0/1 | 0 | — |
| **Auto Services** | 1 | 1 | email (1), ads (1) | 1/1 | 1 | US 1 |
| **Aviation** | 1 | 1 | email (1), sms (1), push (1), web-push (1) | 0/0 | 0 | — |
| **Fiber** | 1 | 1 | email (1), direct-mail (1) | 0/0 | 0 | — |
| **Business Services** | 1 | 0 | — | 0/1 | 0 | — |
| **Car Dealerships** | 1 | 1 | email (1), sms (1), rcs (1), voice (1) | 1/1 | 1 | US 1 |
| **Churches** | 1 | 1 | email (1), sms (1), rcs (1), voice (1) | 1/1 | 1 | US 1 |
| **Coffee Shops** | 1 | 1 | email (1), sms (1) | 0/1 | 0 | — |
| **D2C** | 1 | 1 | email (1), sms (1), push (1), whatsapp (1) | 0/0 | 0 | — |
| **Defense** | 1 | 1 | email (1) | 0/0 | 0 | — |
| **Distribution** | 1 | 1 | chat (1) | 0/0 | 0 | — |
| **Financial Advisors** | 1 | 1 | email (1) | 1/1 | 0 | — |
| **Fuel Retail** | 1 | 0 | — | 0/0 | 0 | — |
| **Education (K-12)** | 1 | 1 | email (1), sms (1), rcs (1), voice (1) | 1/1 | 1 | US 1 |
| **Last-Mile Delivery** | 1 | 1 | email (1) | 1/1 | 1 | — |
| **Lending** | 1 | 1 | email (1), sms (1), push (1), whatsapp (1) | 0/0 | 0 | — |
| **Luxury** | 1 | 1 | email (1), sms (1), push (1), whatsapp (1) | 0/1 | 1 | — |
| **Mixed-Use** | 1 | 1 | email (1), sms (1) | 0/1 | 0 | — |
| **Mortgage** | 1 | 0 | — | 0/1 | 0 | — |
| **Mutual Funds** | 1 | 1 | email (1), sms (1), push (1), whatsapp (1) | 0/0 | 0 | — |
| **Oil & Gas** | 1 | 1 | chat (1) | 0/0 | 0 | IN 1 |
| **Online Trading** | 1 | 1 | email (1), sms (1), push (1), whatsapp (1) | 0/0 | 0 | — |
| **Pet Services** | 1 | 1 | email (1), ads (1) | 1/1 | 1 | US 1 |
| **Pharma** | 1 | 0 | — | 0/1 | 0 | — |
| **Pharmacy** | 1 | 1 | email (1) | 0/0 | 0 | — |
| **Prediction Markets** | 1 | 1 | email (1), sms (1), push (1), whatsapp (1) | 0/0 | 0 | — |
| **Private Equity** | 1 | 1 | chat (1) | 0/0 | 0 | IN 1 |
| **PropTech** | 1 | 1 | email (1), sms (1), chat (1) | 0/0 | 0 | — |
| **Salons** | 1 | 1 | email (1), sms (1), push (1), voice (1) | 1/1 | 1 | — |
| **Satellite** | 1 | 0 | — | 0/0 | 0 | — |
| **Shopping Centers** | 1 | 1 | email (1), sms (1) | 0/1 | 0 | — |
| **Smart Cities** | 1 | 1 | email (1), sms (1) | 0/1 | 0 | — |
| **Software** | 1 | 1 | email (1), direct-mail (1) | 0/0 | 0 | — |
| **Spas** | 1 | 1 | email (1), sms (1), push (1), voice (1) | 1/1 | 1 | — |
| **Supply Chain** | 1 | 1 | email (1), sms (1), chat (1) | 0/0 | 0 | — |
| **Ticketing** | 1 | 1 | email (1), sms (1), push (1), rcs (1) | 1/1 | 0 | — |
| **Transportation** | 1 | 0 | — | 0/1 | 0 | — |

### Vendors behind each industry

**Financial Services** (31) — Acoustic, Act-On, Airship, Appier, Blueshift, Braze, Epsilon, EVAM, HCLTech, Insider One, iPresso, LeadSquared, Medallia, Meiro, Netmera, OneSignal, Optimove, Pitney Bowes, Piwik PRO, Postalytics, Precisely, Pyze, Radar, Sprinklr, Tech Mahindra, Thryv, Tidio, Treasure AI, Vibes, Woosmap, WorksBuddy

**Retail** (25) — Acoustic, Airship, Appier, Blueshift, BSI Software, Capillary Technologies, Creatio, Epsilon, EZ Texting, indigitall, Insider One, Medallia, Meiro, Netmera, Optimove, Pitney Bowes, Postalytics, Precisely, Radar, Rapidops, Sprinklr, Textedly, Treasure AI, Vibes, Woosmap

**Healthcare** (21) — Act-On, Blueshift, BSI Software, Customer.io, Epsilon, EZ Texting, HCLTech, indigitall, L-Soft, LeadSquared, Medallia, Meiro, Pitney Bowes, Piwik PRO, Precisely, Pyze, Tech Mahindra, Thryv, Treasure AI, Woosmap, WorksBuddy

**Ecommerce** (18) — Acoustic, Appier, Blueshift, EZ Texting, indigitall, Insider One, iPresso, Meiro, Netmera, Nvecta, OneSignal, Optimove, Pitney Bowes, Piwik PRO, Postalytics, Tidio, Woosmap, ZEPIC

**Travel** (17) — Acoustic, Airship, Braze, Epsilon, indigitall, Insider One, iPresso, LeadSquared, Medallia, Netmera, Optimove, Radar, Sprinklr, Tidio, Treasure AI, Woosmap, ZEPIC

**Hospitality** (16) — Acoustic, Airship, Braze, Capillary Technologies, EZ Texting, indigitall, Insider One, LeadSquared, Medallia, Netmera, Optimove, Sprinklr, Treasure AI, Vibes, Woosmap, ZEPIC

**Insurance** (14) — Act-On, Airship, Appier, BSI Software, Creatio, EZ Texting, HCLTech, indigitall, Medallia, Nvecta, Precisely, Pyze, Tech Mahindra, Woosmap

**Media** (13) — Acoustic, Airship, Blueshift, Braze, Epsilon, indigitall, iPresso, Medallia, Meiro, Netmera, OneSignal, Tech Mahindra, Treasure AI

**Banking** (12) — Act-On, Blueshift, BSI Software, Creatio, HCLTech, indigitall, Meiro, Netmera, Piwik PRO, Precisely, Pyze, Tech Mahindra

**Telecommunication** (12) — Airship, Creatio, Epsilon, EVAM, indigitall, Insider One, Medallia, Netmera, Precisely, Pyze, Sprinklr, Tech Mahindra

**Automotive** (9) — Appier, HCLTech, Insider One, LeadSquared, Medallia, Treasure AI, Vibes, Woosmap, WorksBuddy

**Entertainment** (9) — Acoustic, Airship, Braze, Epsilon, iPresso, Netmera, Tech Mahindra, Treasure AI, Vibes

**Manufacturing** (9) — Act-On, Creatio, HCLTech, LeadSquared, Medallia, Pyze, Rapidops, SugarAI, Tech Mahindra

**Education** (8) — indigitall, iPresso, L-Soft, LeadSquared, Tech Mahindra, Tidio, Webmaxy, WorksBuddy

**Government** (8) — L-Soft, Medallia, Pitney Bowes, Piwik PRO, Precisely, Pyze, Sprinklr, Woosmap

**Restaurants** (8) — Braze, Epsilon, EZ Texting, Medallia, Radar, Textedly, Vibes, Webmaxy

**CPG** (7) — Capillary Technologies, Creatio, Epsilon, HCLTech, iPresso, Sprinklr, Treasure AI

**Gaming** (6) — Appier, Braze, OneSignal, OptiKPI, Optimove, Radar

**Technology** (6) — Creatio, Medallia, Postalytics, Sprinklr, Tech Mahindra, Treasure AI

**Utilities** (6) — BSI Software, HCLTech, Piwik PRO, Precisely, Pyze, Tech Mahindra

**Energy** (5) — BSI Software, HCLTech, Piwik PRO, Pyze, Tech Mahindra

**Nonprofits** (5) — Epsilon, EZ Texting, L-Soft, Postalytics, Textedly

**Fintech** (4) — Customer.io, HCLTech, OneSignal, OptiKPI

**iGaming** (4) — Meiro, OptiKPI, Optimove, Text

**Life Sciences** (4) — HCLTech, Medallia, Pyze, Tech Mahindra

**Logistics** (4) — indigitall, Radar, Woosmap, WorksBuddy

**Real Estate** (4) — LeadSquared, Postalytics, Webmaxy, WorksBuddy

**Beauty** (3) — Insider One, Meiro, Thryv

**Credit Unions** (3) — Act-On, Blueshift, Creatio

**Legal** (3) — EZ Texting, Pitney Bowes, Thryv

**SaaS** (3) — Customer.io, Tidio, WorksBuddy

**Aerospace** (2) — Amazon Web Services, HCLTech

**Airline** (2) — Capillary Technologies, EVAM

**Capital Markets** (2) — HCLTech, Text

**EdTech** (2) — Blueshift, Customer.io

**Food & Beverage** (2) — indigitall, WorksBuddy

**Higher Education** (2) — EZ Texting, Pitney Bowes

**Home Services** (2) — Postalytics, Thryv

**Hotels** (2) — Aislelabs, Textedly

**IT** (2) — Postalytics, WorksBuddy

**Sports** (2) — Airship, Braze

**Wellness** (2) — Thryv, Woosmap

**Advertising and Marketing** (1) — Amazon Web Services

**Agriculture** (1) — LeadSquared

**Airports** (1) — Aislelabs

**Auto Services** (1) — Thryv

**Aviation** (1) — EVAM

**Fiber** (1) — Postalytics

**Business Services** (1) — Creatio

**Car Dealerships** (1) — EZ Texting

**Churches** (1) — EZ Texting

**Coffee Shops** (1) — Aislelabs

**D2C** (1) — Nvecta

**Defense** (1) — HCLTech

**Distribution** (1) — Rapidops

**Financial Advisors** (1) — Act-On

**Fuel Retail** (1) — Capillary Technologies

**Education (K-12)** (1) — EZ Texting

**Last-Mile Delivery** (1) — Woosmap

**Lending** (1) — Nvecta

**Luxury** (1) — Braze

**Mixed-Use** (1) — Aislelabs

**Mortgage** (1) — Creatio

**Mutual Funds** (1) — Nvecta

**Oil & Gas** (1) — Tech Mahindra

**Online Trading** (1) — Optimove

**Pet Services** (1) — Thryv

**Pharma** (1) — Creatio

**Pharmacy** (1) — Pitney Bowes

**Prediction Markets** (1) — Optimove

**Private Equity** (1) — Tech Mahindra

**PropTech** (1) — Precisely

**Salons** (1) — Textedly

**Satellite** (1) — Amazon Web Services

**Shopping Centers** (1) — Aislelabs

**Smart Cities** (1) — Aislelabs

**Software** (1) — Postalytics

**Spas** (1) — Textedly

**Supply Chain** (1) — Precisely

**Ticketing** (1) — Vibes

**Transportation** (1) — Creatio

---

## 3 · Segments recorded but not counted as industries

These are real published claims, but they name an audience or a business model, not an industry. Counting them as industries would inflate the list with a different kind of thing.

| Claim | Vendors | Why not an industry |
|---|---:|---|
| enterprise | 2 | company size |
| agencies | 2 | competitor class 3 - services firms |
| on-demand | 1 | business model |
| marketplace | 1 | business model |
| mgmt. consulting | 1 | competitor class 3 - services firms |
| conglomerates | 1 | org type |
| mobile apps | 1 | product type |
| marketers | 1 | buyer role |
| startups | 1 | company stage |
| franchises | 1 | ownership model |
| franchisees | 1 | ownership model |
| operators | 1 | ownership model |
| b2b | 1 | go-to-market |
| digital native businesses | 1 | business model |
| business | 1 | too generic |
| in-house marketing | 1 | competitor class 2 - in-house build |
| in-house operations | 1 | competitor class 2 - in-house build |
| consultants | 1 | competitor class 3 - services firms |
| operations | 1 | buyer role |
| operations service providers | 1 | competitor class 3 - services firms |
| small business | 1 | company size |
| marketplaces | 1 | business model |
| startups & scaleups | 1 | company stage |
| technical | 1 | buyer role |
| cx teams | 1 | buyer role |
| customer service | 1 | buyer role |

Two of these are notable: **Agencies / Consultants** and **In-house marketing** appear as *target segments of software vendors* — supply-side self-declaration, competitor classes 2 and 3 showing up as buyers rather than as rivals. Neither is evidence any buyer chose that route.

---

## 4 · Disposition of every raw string

The field held **369 distinct raw strings**. The extractor that filled it was heading-anchored — it took the lines after an `Industries`/`Verticals` heading — so it swept in navigation, CTAs, product names, client names and Material-icon ligatures **at grade PRIMARY**. Every string is shown with its ruling; none is silently dropped.

| Raw string | Seen | Atom | Bucket | Ruling |
|---|---:|---|---|---|
| `Resources` | 18 | resources | REJECTED | site navigation, CTA, product or content label |
| `Resources` | 18 | resources | REJECTED | site navigation, CTA, product or content label |
| `Resources` | 18 | resources | REJECTED | site navigation, CTA, product or content label |
| `Resources` | 18 | resources | REJECTED | site navigation, CTA, product or content label |
| `Resources` | 18 | resources | REJECTED | site navigation, CTA, product or content label |
| `Resources` | 18 | resources | REJECTED | site navigation, CTA, product or content label |
| `Resources` | 18 | resources | REJECTED | site navigation, CTA, product or content label |
| `Resources` | 18 | resources | REJECTED | site navigation, CTA, product or content label |
| `Resources` | 18 | resources | REJECTED | site navigation, CTA, product or content label |
| `Resources` | 18 | resources | REJECTED | site navigation, CTA, product or content label |
| `Resources` | 18 | resources | REJECTED | site navigation, CTA, product or content label |
| `Resources` | 18 | resources | REJECTED | site navigation, CTA, product or content label |
| `Resources` | 18 | resources | REJECTED | site navigation, CTA, product or content label |
| `Resources` | 18 | resources | REJECTED | site navigation, CTA, product or content label |
| `Resources` | 18 | resources | REJECTED | site navigation, CTA, product or content label |
| `Resources` | 18 | resources | REJECTED | site navigation, CTA, product or content label |
| `Resources` | 18 | resources | REJECTED | site navigation, CTA, product or content label |
| `Resources` | 18 | resources | REJECTED | site navigation, CTA, product or content label |
| `Financial Services` | 15 | financial services | INDUSTRY | financial-services |
| `Financial Services` | 15 | financial services | INDUSTRY | financial-services |
| `Financial Services` | 15 | financial services | INDUSTRY | financial-services |
| `Financial Services` | 15 | financial services | INDUSTRY | financial-services |
| `Financial Services` | 15 | financial services | INDUSTRY | financial-services |
| `Financial Services` | 15 | financial services | INDUSTRY | financial-services |
| `Financial Services` | 15 | financial services | INDUSTRY | financial-services |
| `Financial Services` | 15 | financial services | INDUSTRY | financial-services |
| `Financial Services` | 15 | financial services | INDUSTRY | financial-services |
| `Financial Services` | 15 | financial services | INDUSTRY | financial-services |
| `Financial Services` | 15 | financial services | INDUSTRY | financial-services |
| `Financial Services` | 15 | financial services | INDUSTRY | financial-services |
| `Financial Services` | 15 | financial services | INDUSTRY | financial-services |
| `Financial Services` | 15 | financial services | INDUSTRY | financial-services |
| `Financial Services` | 15 | financial services | INDUSTRY | financial-services |
| `Retail` | 14 | retail | INDUSTRY | retail |
| `Retail` | 14 | retail | INDUSTRY | retail |
| `Retail` | 14 | retail | INDUSTRY | retail |
| `Retail` | 14 | retail | INDUSTRY | retail |
| `Retail` | 14 | retail | INDUSTRY | retail |
| `Retail` | 14 | retail | INDUSTRY | retail |
| `Retail` | 14 | retail | INDUSTRY | retail |
| `Retail` | 14 | retail | INDUSTRY | retail |
| `Retail` | 14 | retail | INDUSTRY | retail |
| `Retail` | 14 | retail | INDUSTRY | retail |
| `Retail` | 14 | retail | INDUSTRY | retail |
| `Retail` | 14 | retail | INDUSTRY | retail |
| `Retail` | 14 | retail | INDUSTRY | retail |
| `Retail` | 14 | retail | INDUSTRY | retail |
| `Healthcare` | 12 | healthcare | INDUSTRY | healthcare |
| `Healthcare` | 12 | healthcare | INDUSTRY | healthcare |
| `Healthcare` | 12 | healthcare | INDUSTRY | healthcare |
| `Healthcare` | 12 | healthcare | INDUSTRY | healthcare |
| `Healthcare` | 12 | healthcare | INDUSTRY | healthcare |
| `Healthcare` | 12 | healthcare | INDUSTRY | healthcare |
| `Healthcare` | 12 | healthcare | INDUSTRY | healthcare |
| `Healthcare` | 12 | healthcare | INDUSTRY | healthcare |
| `Healthcare` | 12 | healthcare | INDUSTRY | healthcare |
| `Healthcare` | 12 | healthcare | INDUSTRY | healthcare |
| `Healthcare` | 12 | healthcare | INDUSTRY | healthcare |
| `Healthcare` | 12 | healthcare | INDUSTRY | healthcare |
| `Insurance` | 10 | insurance | INDUSTRY | insurance |
| `Insurance` | 10 | insurance | INDUSTRY | insurance |
| `Insurance` | 10 | insurance | INDUSTRY | insurance |
| `Insurance` | 10 | insurance | INDUSTRY | insurance |
| `Insurance` | 10 | insurance | INDUSTRY | insurance |
| `Insurance` | 10 | insurance | INDUSTRY | insurance |
| `Insurance` | 10 | insurance | INDUSTRY | insurance |
| `Insurance` | 10 | insurance | INDUSTRY | insurance |
| `Insurance` | 10 | insurance | INDUSTRY | insurance |
| `Insurance` | 10 | insurance | INDUSTRY | insurance |
| `Manufacturing` | 9 | manufacturing | INDUSTRY | manufacturing |
| `Manufacturing` | 9 | manufacturing | INDUSTRY | manufacturing |
| `Manufacturing` | 9 | manufacturing | INDUSTRY | manufacturing |
| `Manufacturing` | 9 | manufacturing | INDUSTRY | manufacturing |
| `Manufacturing` | 9 | manufacturing | INDUSTRY | manufacturing |
| `Manufacturing` | 9 | manufacturing | INDUSTRY | manufacturing |
| `Manufacturing` | 9 | manufacturing | INDUSTRY | manufacturing |
| `Manufacturing` | 9 | manufacturing | INDUSTRY | manufacturing |
| `Manufacturing` | 9 | manufacturing | INDUSTRY | manufacturing |
| `Blog` | 8 | blog | REJECTED | site navigation, CTA, product or content label |
| `Blog` | 8 | blog | REJECTED | site navigation, CTA, product or content label |
| `Blog` | 8 | blog | REJECTED | site navigation, CTA, product or content label |
| `Blog` | 8 | blog | REJECTED | site navigation, CTA, product or content label |
| `Blog` | 8 | blog | REJECTED | site navigation, CTA, product or content label |
| `Blog` | 8 | blog | REJECTED | site navigation, CTA, product or content label |
| `Blog` | 8 | blog | REJECTED | site navigation, CTA, product or content label |
| `Blog` | 8 | blog | REJECTED | site navigation, CTA, product or content label |
| `Restaurants` | 8 | restaurants | INDUSTRY | restaurants |
| `Restaurants` | 8 | restaurants | INDUSTRY | restaurants |
| `Restaurants` | 8 | restaurants | INDUSTRY | restaurants |
| `Restaurants` | 8 | restaurants | INDUSTRY | restaurants |
| `Restaurants` | 8 | restaurants | INDUSTRY | restaurants |
| `Restaurants` | 8 | restaurants | INDUSTRY | restaurants |
| `Restaurants` | 8 | restaurants | INDUSTRY | restaurants |
| `Restaurants` | 8 | restaurants | INDUSTRY | restaurants |
| `Travel & Hospitality` | 8 | travel | INDUSTRY | travel |
| `Travel & Hospitality` | 8 | hospitality | INDUSTRY | hospitality |
| `Travel & Hospitality` | 8 | travel | INDUSTRY | travel |
| `Travel & Hospitality` | 8 | hospitality | INDUSTRY | hospitality |
| `Travel & Hospitality` | 8 | travel | INDUSTRY | travel |
| `Travel & Hospitality` | 8 | hospitality | INDUSTRY | hospitality |
| `Travel & Hospitality` | 8 | travel | INDUSTRY | travel |
| `Travel & Hospitality` | 8 | hospitality | INDUSTRY | hospitality |
| `Travel & Hospitality` | 8 | travel | INDUSTRY | travel |
| `Travel & Hospitality` | 8 | hospitality | INDUSTRY | hospitality |
| `Travel & Hospitality` | 8 | travel | INDUSTRY | travel |
| `Travel & Hospitality` | 8 | hospitality | INDUSTRY | hospitality |
| `Travel & Hospitality` | 8 | travel | INDUSTRY | travel |
| `Travel & Hospitality` | 8 | hospitality | INDUSTRY | hospitality |
| `Travel & Hospitality` | 8 | travel | INDUSTRY | travel |
| `Travel & Hospitality` | 8 | hospitality | INDUSTRY | hospitality |
| `Automotive` | 7 | automotive | INDUSTRY | automotive |
| `Automotive` | 7 | automotive | INDUSTRY | automotive |
| `Automotive` | 7 | automotive | INDUSTRY | automotive |
| `Automotive` | 7 | automotive | INDUSTRY | automotive |
| `Automotive` | 7 | automotive | INDUSTRY | automotive |
| `Automotive` | 7 | automotive | INDUSTRY | automotive |
| `Automotive` | 7 | automotive | INDUSTRY | automotive |
| `Education` | 6 | education | INDUSTRY | education |
| `Education` | 6 | education | INDUSTRY | education |
| `Education` | 6 | education | INDUSTRY | education |
| `Education` | 6 | education | INDUSTRY | education |
| `Education` | 6 | education | INDUSTRY | education |
| `Education` | 6 | education | INDUSTRY | education |
| `Travel` | 5 | travel | INDUSTRY | travel |
| `Travel` | 5 | travel | INDUSTRY | travel |
| `Travel` | 5 | travel | INDUSTRY | travel |
| `Travel` | 5 | travel | INDUSTRY | travel |
| `Travel` | 5 | travel | INDUSTRY | travel |
| `Company` | 4 | company | REJECTED | site navigation, CTA, product or content label |
| `Company` | 4 | company | REJECTED | site navigation, CTA, product or content label |
| `Company` | 4 | company | REJECTED | site navigation, CTA, product or content label |
| `Company` | 4 | company | REJECTED | site navigation, CTA, product or content label |
| `Gaming` | 4 | gaming | INDUSTRY | gaming |
| `Gaming` | 4 | gaming | INDUSTRY | gaming |
| `Gaming` | 4 | gaming | INDUSTRY | gaming |
| `Gaming` | 4 | gaming | INDUSTRY | gaming |
| `Government` | 4 | government | INDUSTRY | government |
| `Government` | 4 | government | INDUSTRY | government |
| `Government` | 4 | government | INDUSTRY | government |
| `Government` | 4 | government | INDUSTRY | government |
| `Hospitality` | 4 | hospitality | INDUSTRY | hospitality |
| `Hospitality` | 4 | hospitality | INDUSTRY | hospitality |
| `Hospitality` | 4 | hospitality | INDUSTRY | hospitality |
| `Hospitality` | 4 | hospitality | INDUSTRY | hospitality |
| `Industries` | 4 | industries | REJECTED | site navigation, CTA, product or content label |
| `Industries` | 4 | industries | REJECTED | site navigation, CTA, product or content label |
| `Industries` | 4 | industries | REJECTED | site navigation, CTA, product or content label |
| `Industries` | 4 | industries | REJECTED | site navigation, CTA, product or content label |
| `Nonprofits` | 4 | nonprofits | INDUSTRY | nonprofits |
| `Nonprofits` | 4 | nonprofits | INDUSTRY | nonprofits |
| `Nonprofits` | 4 | nonprofits | INDUSTRY | nonprofits |
| `Nonprofits` | 4 | nonprofits | INDUSTRY | nonprofits |
| `Support` | 4 | support | REJECTED | site navigation, CTA, product or content label |
| `Support` | 4 | support | REJECTED | site navigation, CTA, product or content label |
| `Support` | 4 | support | REJECTED | site navigation, CTA, product or content label |
| `Support` | 4 | support | REJECTED | site navigation, CTA, product or content label |
| `Telecommunication` | 4 | telecommunication | INDUSTRY | telecommunications |
| `Telecommunication` | 4 | telecommunication | INDUSTRY | telecommunications |
| `Telecommunication` | 4 | telecommunication | INDUSTRY | telecommunications |
| `Telecommunication` | 4 | telecommunication | INDUSTRY | telecommunications |
| `About` | 3 | about | REJECTED | site navigation, CTA, product or content label |
| `About` | 3 | about | REJECTED | site navigation, CTA, product or content label |
| `About` | 3 | about | REJECTED | site navigation, CTA, product or content label |
| `All Industries` | 3 | all industries | REJECTED | site navigation, CTA, product or content label |
| `All Industries` | 3 | all industries | REJECTED | site navigation, CTA, product or content label |
| `All Industries` | 3 | all industries | REJECTED | site navigation, CTA, product or content label |
| `Banking` | 3 | banking | INDUSTRY | banking |
| `Banking` | 3 | banking | INDUSTRY | banking |
| `Banking` | 3 | banking | INDUSTRY | banking |
| `Case Studies` | 3 | case studies | REJECTED | site navigation, CTA, product or content label |
| `Case Studies` | 3 | case studies | REJECTED | site navigation, CTA, product or content label |
| `Case Studies` | 3 | case studies | REJECTED | site navigation, CTA, product or content label |
| `Click for Demo` | 3 | click for demo | REJECTED | site navigation, CTA, product or content label |
| `Click for Demo` | 3 | click for demo | REJECTED | site navigation, CTA, product or content label |
| `Click for Demo` | 3 | click for demo | REJECTED | site navigation, CTA, product or content label |
| `Contact Us` | 3 | contact us | REJECTED | site navigation, CTA, product or content label |
| `Contact Us` | 3 | contact us | REJECTED | site navigation, CTA, product or content label |
| `Contact Us` | 3 | contact us | REJECTED | site navigation, CTA, product or content label |
| `CPG` | 3 | cpg | INDUSTRY | cpg |
| `CPG` | 3 | cpg | INDUSTRY | cpg |
| `CPG` | 3 | cpg | INDUSTRY | cpg |
| `Energy & Utilities` | 3 | energy | INDUSTRY | energy |
| `Energy & Utilities` | 3 | utilities | INDUSTRY | utilities |
| `Energy & Utilities` | 3 | energy | INDUSTRY | energy |
| `Energy & Utilities` | 3 | utilities | INDUSTRY | utilities |
| `Energy & Utilities` | 3 | energy | INDUSTRY | energy |
| `Energy & Utilities` | 3 | utilities | INDUSTRY | utilities |
| `Finance` | 3 | finance | INDUSTRY | financial-services |
| `Finance` | 3 | finance | INDUSTRY | financial-services |
| `Finance` | 3 | finance | INDUSTRY | financial-services |
| `Financial services` | 3 | financial services | INDUSTRY | financial-services |
| `Financial services` | 3 | financial services | INDUSTRY | financial-services |
| `Financial services` | 3 | financial services | INDUSTRY | financial-services |
| `Fintech` | 3 | fintech | INDUSTRY | fintech |
| `Fintech` | 3 | fintech | INDUSTRY | fintech |
| `Fintech` | 3 | fintech | INDUSTRY | fintech |
| `iGaming` | 3 | igaming | INDUSTRY | igaming |
| `iGaming` | 3 | igaming | INDUSTRY | igaming |
| `iGaming` | 3 | igaming | INDUSTRY | igaming |
| `Logistics` | 3 | logistics | INDUSTRY | logistics |
| `Logistics` | 3 | logistics | INDUSTRY | logistics |
| `Logistics` | 3 | logistics | INDUSTRY | logistics |
| `Retail & Ecommerce` | 3 | retail | INDUSTRY | retail |
| `Retail & Ecommerce` | 3 | ecommerce | INDUSTRY | ecommerce |
| `Retail & Ecommerce` | 3 | retail | INDUSTRY | retail |
| `Retail & Ecommerce` | 3 | ecommerce | INDUSTRY | ecommerce |
| `Retail & Ecommerce` | 3 | retail | INDUSTRY | retail |
| `Retail & Ecommerce` | 3 | ecommerce | INDUSTRY | ecommerce |
| `Solutions` | 3 | solutions | REJECTED | site navigation, CTA, product or content label |
| `Solutions` | 3 | solutions | REJECTED | site navigation, CTA, product or content label |
| `Solutions` | 3 | solutions | REJECTED | site navigation, CTA, product or content label |
| `Telecommunications` | 3 | telecommunications | INDUSTRY | telecommunications |
| `Telecommunications` | 3 | telecommunications | INDUSTRY | telecommunications |
| `Telecommunications` | 3 | telecommunications | INDUSTRY | telecommunications |
| `View Now` | 3 | view now | REJECTED | site navigation, CTA, product or content label |
| `View Now` | 3 | view now | REJECTED | site navigation, CTA, product or content label |
| `View Now` | 3 | view now | REJECTED | site navigation, CTA, product or content label |
| `Banking & Financial Services` | 2 | banking | INDUSTRY | banking |
| `Banking & Financial Services` | 2 | financial services | INDUSTRY | financial-services |
| `Banking & Financial Services` | 2 | banking | INDUSTRY | banking |
| `Banking & Financial Services` | 2 | financial services | INDUSTRY | financial-services |
| `Channels` | 2 | channels | REJECTED | site navigation, CTA, product or content label |
| `Channels` | 2 | channels | REJECTED | site navigation, CTA, product or content label |
| `E-commerce` | 2 | e-commerce | INDUSTRY | ecommerce |
| `E-commerce` | 2 | e-commerce | INDUSTRY | ecommerce |
| `eCommerce` | 2 | ecommerce | INDUSTRY | ecommerce |
| `eCommerce` | 2 | ecommerce | INDUSTRY | ecommerce |
| `Ecommerce` | 2 | ecommerce | INDUSTRY | ecommerce |
| `Ecommerce` | 2 | ecommerce | INDUSTRY | ecommerce |
| `EdTech` | 2 | edtech | INDUSTRY | edtech |
| `EdTech` | 2 | edtech | INDUSTRY | edtech |
| `Enterprise` | 2 | enterprise | SEGMENT | company size |
| `Enterprise` | 2 | enterprise | SEGMENT | company size |
| `Expand menu` | 2 | expand menu | REJECTED | site navigation, CTA, product or content label |
| `Expand menu` | 2 | expand menu | REJECTED | site navigation, CTA, product or content label |
| `Franchises` | 2 | franchises | SEGMENT | ownership model |
| `Franchises` | 2 | franchises | SEGMENT | ownership model |
| `Healthcare & Life Sciences` | 2 | healthcare | INDUSTRY | healthcare |
| `Healthcare & Life Sciences` | 2 | life sciences | INDUSTRY | life-sciences |
| `Healthcare & Life Sciences` | 2 | healthcare | INDUSTRY | healthcare |
| `Healthcare & Life Sciences` | 2 | life sciences | INDUSTRY | life-sciences |
| `Hotels` | 2 | hotels | INDUSTRY | hotels |
| `Hotels` | 2 | hotels | INDUSTRY | hotels |
| `Learn` | 2 | learn | REJECTED | site navigation, CTA, product or content label |
| `Learn` | 2 | learn | REJECTED | site navigation, CTA, product or content label |
| `Legal` | 2 | legal | INDUSTRY | legal |
| `Legal` | 2 | legal | INDUSTRY | legal |
| `Log In` | 2 | log in | REJECTED | site navigation, CTA, product or content label |
| `Log In` | 2 | log in | REJECTED | site navigation, CTA, product or content label |
| `Marketing` | 2 | marketing | REJECTED | site navigation, CTA, product or content label |
| `Marketing` | 2 | marketing | REJECTED | site navigation, CTA, product or content label |
| `Media & Entertainment` | 2 | media | INDUSTRY | media |
| `Media & Entertainment` | 2 | entertainment | INDUSTRY | entertainment |
| `Media & Entertainment` | 2 | media | INDUSTRY | media |
| `Media & Entertainment` | 2 | entertainment | INDUSTRY | entertainment |
| `Media and Entertainment` | 2 | media | INDUSTRY | media |
| `Media and Entertainment` | 2 | entertainment | INDUSTRY | entertainment |
| `Media and Entertainment` | 2 | media | INDUSTRY | media |
| `Media and Entertainment` | 2 | entertainment | INDUSTRY | entertainment |
| `Others` | 2 | others | REJECTED | site navigation, CTA, product or content label |
| `Others` | 2 | others | REJECTED | site navigation, CTA, product or content label |
| `Partners` | 2 | partners | REJECTED | site navigation, CTA, product or content label |
| `Partners` | 2 | partners | REJECTED | site navigation, CTA, product or content label |
| `Public Sector` | 2 | public sector | INDUSTRY | government |
| `Public Sector` | 2 | public sector | INDUSTRY | government |
| `Real Estate` | 2 | real estate | INDUSTRY | real-estate |
| `Real Estate` | 2 | real estate | INDUSTRY | real-estate |
| `Retail & eCommerce` | 2 | retail | INDUSTRY | retail |
| `Retail & eCommerce` | 2 | ecommerce | INDUSTRY | ecommerce |
| `Retail & eCommerce` | 2 | retail | INDUSTRY | retail |
| `Retail & eCommerce` | 2 | ecommerce | INDUSTRY | ecommerce |
| `Retail and E-commerce` | 2 | retail | INDUSTRY | retail |
| `Retail and E-commerce` | 2 | e-commerce | INDUSTRY | ecommerce |
| `Retail and E-commerce` | 2 | retail | INDUSTRY | retail |
| `Retail and E-commerce` | 2 | e-commerce | INDUSTRY | ecommerce |
| `Retail Stores` | 2 | retail stores | INDUSTRY | retail |
| `Retail Stores` | 2 | retail stores | INDUSTRY | retail |
| `SaaS` | 2 | saas | INDUSTRY | saas |
| `SaaS` | 2 | saas | INDUSTRY | saas |
| `Sign Up Now` | 2 | sign up now | REJECTED | site navigation, CTA, product or content label |
| `Sign Up Now` | 2 | sign up now | REJECTED | site navigation, CTA, product or content label |
| `Spas & Salons` | 2 | spas | INDUSTRY | spas |
| `Spas & Salons` | 2 | salons | INDUSTRY | salons |
| `Spas & Salons` | 2 | spas | INDUSTRY | spas |
| `Spas & Salons` | 2 | salons | INDUSTRY | salons |
| `Sports` | 2 | sports | INDUSTRY | sports |
| `Sports` | 2 | sports | INDUSTRY | sports |
| `Technology` | 2 | technology | INDUSTRY | technology |
| `Technology` | 2 | technology | INDUSTRY | technology |
| `Telco & Media` | 2 | telco | INDUSTRY | telecommunications |
| `Telco & Media` | 2 | media | INDUSTRY | media |
| `Telco & Media` | 2 | telco | INDUSTRY | telecommunications |
| `Telco & Media` | 2 | media | INDUSTRY | media |
| `Telecom` | 2 | telecom | INDUSTRY | telecommunications |
| `Telecom` | 2 | telecom | INDUSTRY | telecommunications |
| `Travel and Hospitality` | 2 | travel | INDUSTRY | travel |
| `Travel and Hospitality` | 2 | hospitality | INDUSTRY | hospitality |
| `Travel and Hospitality` | 2 | travel | INDUSTRY | travel |
| `Travel and Hospitality` | 2 | hospitality | INDUSTRY | hospitality |
| `About Us` | 1 | about us | REJECTED | site navigation, CTA, product or content label |
| `Academics` | 1 | academics | REJECTED | site navigation, CTA, product or content label |
| `account_balance` | 1 | account_balance | REJECTED | Material-icon ligature scraped from markup |
| `Advertising and Marketing` | 1 | advertising and marketing | INDUSTRY | advertising |
| `Aerospace and Defense` | 1 | aerospace | INDUSTRY | aerospace |
| `Aerospace and Defense` | 1 | defense | INDUSTRY | defense |
| `Aerospace and Satellite` | 1 | aerospace | INDUSTRY | aerospace |
| `Aerospace and Satellite` | 1 | satellite | INDUSTRY | satellite |
| `Agencies` | 1 | agencies | SEGMENT | competitor class 3 - services firms |
| `Agencies and Consultants` | 1 | agencies | SEGMENT | competitor class 3 - services firms |
| `Agencies and Consultants` | 1 | consultants | SEGMENT | competitor class 3 - services firms |
| `Agriculture` | 1 | agriculture | INDUSTRY | agriculture |
| `Airline` | 1 | airline | INDUSTRY | airlines |
| `Airline & Aviation` | 1 | airline | INDUSTRY | airlines |
| `Airline & Aviation` | 1 | aviation | INDUSTRY | aviation |
| `Airship guarantees results` | 1 | airship guarantees results | REJECTED | sub-label describing the row above, not an industry heading |
| `All Capabilities` | 1 | all capabilities | REJECTED | site navigation, CTA, product or content label |
| `All industries` | 1 | all industries | REJECTED | site navigation, CTA, product or content label |
| `Already a customer? Log in here.` | 1 | already a customer? log in here. | REJECTED | site navigation, CTA, product or content label |
| `approval_delegation` | 1 | approval_delegation | REJECTED | Material-icon ligature scraped from markup |
| `Audience monetization and retention` | 1 | audience monetization and retention | REJECTED | sub-label describing the row above, not an industry heading |
| `Auto Services` | 1 | auto services | INDUSTRY | auto-services |
| `auto_stories` | 1 | auto_stories | REJECTED | Material-icon ligature scraped from markup |
| `Automobile` | 1 | automobile | INDUSTRY | automotive |
| `Awards` | 1 | awards | REJECTED | site navigation, CTA, product or content label |
| `B2B` | 1 | b2b | SEGMENT | go-to-market |
| `Back` | 1 | back | REJECTED | site navigation, CTA, product or content label |
| `Bank & Insurance` | 1 | bank | INDUSTRY | banking |
| `Bank & Insurance` | 1 | insurance | INDUSTRY | insurance |
| `Banking & Finance` | 1 | banking | INDUSTRY | banking |
| `Banking & Finance` | 1 | finance | INDUSTRY | financial-services |
| `Banking & financial services` | 1 | banking | INDUSTRY | banking |
| `Banking & financial services` | 1 | financial services | INDUSTRY | financial-services |
| `Banking and Credit Unions` | 1 | banking | INDUSTRY | banking |
| `Banking and Credit Unions` | 1 | credit unions | INDUSTRY | credit-unions |
| `Banking and Finance` | 1 | banking | INDUSTRY | banking |
| `Banking and Finance` | 1 | finance | INDUSTRY | financial-services |
| `Banks & Credit Union` | 1 | banks | INDUSTRY | banking |
| `Banks & Credit Union` | 1 | credit union | INDUSTRY | credit-unions |
| `Beauty & Cosmetics` | 1 | beauty | INDUSTRY | beauty |
| `Beauty & Cosmetics` | 1 | cosmetics | INDUSTRY | beauty |
| `Beauty & Wellness` | 1 | beauty | INDUSTRY | beauty |
| `Beauty & Wellness` | 1 | wellness | INDUSTRY | wellness |
| `Blogs` | 1 | blogs | REJECTED | site navigation, CTA, product or content label |
| `Books` | 1 | books | REJECTED | site navigation, CTA, product or content label |
| `Books and reports` | 1 | books and reports | REJECTED | site navigation, CTA, product or content label |
| `Boost prof` | 1 | boost prof | REJECTED | site navigation, CTA, product or content label |
| `Business` | 1 | business | SEGMENT | too generic |
| `Business Services` | 1 | business services | INDUSTRY | business-services |
| `By organization type` | 1 | by organization type | REJECTED | site navigation, CTA, product or content label |
| `By Team` | 1 | by team | REJECTED | site navigation, CTA, product or content label |
| `By use case` | 1 | by use case | REJECTED | site navigation, CTA, product or content label |
| `By Use Case` | 1 | by use case | REJECTED | site navigation, CTA, product or content label |
| `Capabilities` | 1 | capabilities | REJECTED | site navigation, CTA, product or content label |
| `Capital Markets` | 1 | capital markets | INDUSTRY | capital-markets |
| `Car Dealerships` | 1 | car dealerships | INDUSTRY | car-dealerships |
| `Careers` | 1 | careers | REJECTED | site navigation, CTA, product or content label |
| `Case studies` | 1 | case studies | REJECTED | site navigation, CTA, product or content label |
| `Certification` | 1 | certification | REJECTED | site navigation, CTA, product or content label |
| `Churches` | 1 | churches | INDUSTRY | churches |
| `Clients` | 1 | clients | REJECTED | site navigation, CTA, product or content label |
| `Clinics, dental, chiro` | 1 | clinics, dental, chiro | REJECTED | sub-label describing the row above, not an industry heading |
| `Close Resources` | 1 | close resources | REJECTED | site navigation, CTA, product or content label |
| `Communications` | 1 | communications | INDUSTRY | telecommunications |
| `Communities` | 1 | communities | REJECTED | site navigation, CTA, product or content label |
| `Compare` | 1 | compare | REJECTED | site navigation, CTA, product or content label |
| `Compliant CDP for regulated sectors` | 1 | compliant cdp for regulated sectors | REJECTED | sub-label describing the row above, not an industry heading |
| `computer` | 1 | computer | REJECTED | site navigation, CTA, product or content label |
| `Conglomerates` | 1 | conglomerates | SEGMENT | org type |
| `Consumer Goods` | 1 | consumer goods | INDUSTRY | cpg |
| `Consumer packaged goods` | 1 | consumer packaged goods | INDUSTRY | cpg |
| `Contact` | 1 | contact | REJECTED | site navigation, CTA, product or content label |
| `Contact us – Netmera` | 1 | contact us – netmera | REJECTED | site navigation, CTA, product or content label |
| `Content library` | 1 | content library | REJECTED | site navigation, CTA, product or content label |
| `Convert More Customers` | 1 | convert more customers | REJECTED | site navigation, CTA, product or content label |
| `CPG/ FMCG` | 1 | cpg | INDUSTRY | cpg |
| `CPG/ FMCG` | 1 | fmcg | INDUSTRY | cpg |
| `Credit Unions` | 1 | credit unions | INDUSTRY | credit-unions |
| `Customer case studies` | 1 | customer case studies | REJECTED | site navigation, CTA, product or content label |
| `Customer Service` | 1 | customer service | SEGMENT | buyer role |
| `Customer Stories` | 1 | customer stories | REJECTED | site navigation, CTA, product or content label |
| `Customer stories` | 1 | customer stories | REJECTED | site navigation, CTA, product or content label |
| `Customers` | 1 | customers | REJECTED | site navigation, CTA, product or content label |
| `CX Teams` | 1 | cx teams | SEGMENT | buyer role |
| `Cybele` | 1 | cybele | REJECTED | named client or vendor, not an industry |
| `Developer Hub` | 1 | developer hub | REJECTED | site navigation, CTA, product or content label |
| `Digital certified mail` | 1 | digital certified mail | REJECTED | site navigation, CTA, product or content label |
| `Digital Native Businesses` | 1 | digital native businesses | SEGMENT | business model |
| `Direct Mail API` | 1 | direct mail api | REJECTED | site navigation, CTA, product or content label |
| `Direct Mail Editor` | 1 | direct mail editor | REJECTED | site navigation, CTA, product or content label |
| `Direct Mail Mailing Lists` | 1 | direct mail mailing lists | REJECTED | site navigation, CTA, product or content label |
| `Display` | 1 | display | REJECTED | site navigation, CTA, product or content label |
| `Distribution` | 1 | distribution | INDUSTRY | distribution |
| `Download` | 1 | download | REJECTED | site navigation, CTA, product or content label |
| `Drive Engagement` | 1 | drive engagement | REJECTED | site navigation, CTA, product or content label |
| `E-Commerce` | 1 | e-commerce | INDUSTRY | ecommerce |
| `Earthy Orgins` | 1 | earthy orgins | REJECTED | named client or vendor, not an industry |
| `eBooks` | 1 | ebooks | REJECTED | site navigation, CTA, product or content label |
| `Ebooks + Guides` | 1 | ebooks + guides | REJECTED | site navigation, CTA, product or content label |
| `eCommerce & D2C` | 1 | ecommerce | INDUSTRY | ecommerce |
| `eCommerce & D2C` | 1 | d2c | INDUSTRY | d2c |
| `Education (K-12)` | 1 | education (k-12) | INDUSTRY | k12-education |
| `Education Industry Solutions` | 1 | education | INDUSTRY | education |
| `Email` | 1 | email | REJECTED | site navigation, CTA, product or content label |
| `Email Marketing` | 1 | email marketing | REJECTED | site navigation, CTA, product or content label |
| `Energy & utilities` | 1 | energy | INDUSTRY | energy |
| `Energy & utilities` | 1 | utilities | INDUSTRY | utilities |
| `Energy and HVAC Optimization` | 1 | energy and hvac optimization | REJECTED | site navigation, CTA, product or content label |
| `Energy and Utilities` | 1 | energy | INDUSTRY | energy |
| `Energy and Utilities` | 1 | utilities | INDUSTRY | utilities |
| `English` | 1 | english | REJECTED | site navigation, CTA, product or content label |
| `Entertainment & Media` | 1 | entertainment | INDUSTRY | entertainment |
| `Entertainment & Media` | 1 | media | INDUSTRY | media |
| `Entertainment & Ticketing` | 1 | entertainment | INDUSTRY | entertainment |
| `Entertainment & Ticketing` | 1 | ticketing | INDUSTRY | ticketing |
| `Enthusiast Hotels` | 1 | enthusiast hotels | REJECTED | named client or vendor, not an industry |
| `Event` | 1 | event | REJECTED | site navigation, CTA, product or content label |
| `Explore industries` | 1 | explore industries | REJECTED | site navigation, CTA, product or content label |
| `Explore More` | 1 | explore more | REJECTED | site navigation, CTA, product or content label |
| `Explore our Solution Suite` | 1 | explore our solution suite | REJECTED | site navigation, CTA, product or content label |
| `FEATURED` | 1 | featured | REJECTED | site navigation, CTA, product or content label |
| `Features` | 1 | features | REJECTED | site navigation, CTA, product or content label |
| `Fiber/Broadband` | 1 | fiber | INDUSTRY | broadband |
| `Fiber/Broadband` | 1 | broadband | INDUSTRY | broadband |
| `Finance & insurance` | 1 | finance | INDUSTRY | financial-services |
| `Finance & insurance` | 1 | insurance | INDUSTRY | insurance |
| `Finance & Insurance` | 1 | finance | INDUSTRY | financial-services |
| `Finance & Insurance` | 1 | insurance | INDUSTRY | insurance |
| `Financial Advisors` | 1 | financial advisors | INDUSTRY | financial-advisors |
| `Financial Services and Banking` | 1 | financial services | INDUSTRY | financial-services |
| `Financial Services and Banking` | 1 | banking | INDUSTRY | banking |
| `Fintech/Financial` | 1 | fintech | INDUSTRY | fintech |
| `Fintech/Financial` | 1 | financial | INDUSTRY | financial-services |
| `FMCG` | 1 | fmcg | INDUSTRY | cpg |
| `Food & Beverage` | 1 | food & beverage | INDUSTRY | food-beverage |
| `For Airports` | 1 | airports | INDUSTRY | airports |
| `For Coffee Shops` | 1 | coffee shops | INDUSTRY | coffee-shops |
| `For Hotels` | 1 | hotels | INDUSTRY | hotels |
| `For Mixed-Use` | 1 | mixed-use | INDUSTRY | mixed-use |
| `For Shopping Centers` | 1 | shopping centers | INDUSTRY | shopping-centres |
| `For Smart Cities` | 1 | smart cities | INDUSTRY | smart-cities |
| `Franchisees & Operators` | 1 | franchisees | SEGMENT | ownership model |
| `Franchisees & Operators` | 1 | operators | SEGMENT | ownership model |
| `Fuel Retail` | 1 | fuel retail | INDUSTRY | fuel-retail |
| `German / Deutsch` | 1 | german / deutsch | REJECTED | site navigation, CTA, product or content label |
| `get started` | 1 | get started | REJECTED | site navigation, CTA, product or content label |
| `Glossary` | 1 | glossary | REJECTED | site navigation, CTA, product or content label |
| `Go to industry hub` | 1 | go to industry hub | REJECTED | site navigation, CTA, product or content label |
| `Government & public sector` | 1 | government | INDUSTRY | government |
| `Government & public sector` | 1 | public sector | INDUSTRY | government |
| `Grooming, boarding, vets` | 1 | grooming, boarding, vets | REJECTED | sub-label describing the row above, not an industry heading |
| `HCLTech` | 1 | hcltech | REJECTED | named client or vendor, not an industry |
| `Health` | 1 | health | INDUSTRY | healthcare |
| `Health & Beauty` | 1 | health | INDUSTRY | healthcare |
| `Health & Beauty` | 1 | beauty | INDUSTRY | beauty |
| `Health & Wellness` | 1 | health | INDUSTRY | healthcare |
| `Health & Wellness` | 1 | wellness | INDUSTRY | wellness |
| `Healthcare & HIPAA` | 1 | healthcare | INDUSTRY | healthcare |
| `Healthcare & HIPAA` | 1 | hipaa | REJECTED | site navigation, CTA, product or content label |
| `Help Portal` | 1 | help portal | REJECTED | site navigation, CTA, product or content label |
| `Hi Tech` | 1 | hi tech | INDUSTRY | technology |
| `High Tech` | 1 | high tech | INDUSTRY | technology |
| `Higher Education` | 1 | higher education | INDUSTRY | higher-education |
| `Higher education` | 1 | higher education | INDUSTRY | higher-education |
| `Home` | 1 | home | REJECTED | site navigation, CTA, product or content label |
| `Home Page Dropdown Resource` | 1 | home page dropdown resource | REJECTED | site navigation, CTA, product or content label |
| `Home Services` | 1 | home services | INDUSTRY | home-services |
| `In-House Marketing` | 1 | in-house marketing | SEGMENT | competitor class 2 - in-house build |
| `In-House Operations` | 1 | in-house operations | SEGMENT | competitor class 2 - in-house build |
| `Increase engagement` | 1 | increase engagement | REJECTED | site navigation, CTA, product or content label |
| `Industry solutions on AWS` | 1 | industry solutions on aws | REJECTED | site navigation, CTA, product or content label |
| `industry versions` | 1 | industry versions | REJECTED | site navigation, CTA, product or content label |
| `Insurance & Health` | 1 | insurance | INDUSTRY | insurance |
| `Insurance & Health` | 1 | health | INDUSTRY | healthcare |
| `Integration Partners` | 1 | integration partners | REJECTED | site navigation, CTA, product or content label |
| `Journey Designer` | 1 | journey designer | REJECTED | site navigation, CTA, product or content label |
| `Language` | 1 | language | REJECTED | site navigation, CTA, product or content label |
| `Last-Mile Delivery` | 1 | last-mile delivery | INDUSTRY | last-mile-delivery |
| `Law, accounting` | 1 | law, accounting | REJECTED | sub-label describing the row above, not an industry heading |
| `LEARN` | 1 | learn | REJECTED | site navigation, CTA, product or content label |
| `Learn about OptiKPI heritage and story` | 1 | learn about optikpi heritage and story | REJECTED | sub-label describing the row above, not an industry heading |
| `Learn more` | 1 | learn more | REJECTED | site navigation, CTA, product or content label |
| `Learn with Airship` | 1 | learn with airship | REJECTED | sub-label describing the row above, not an industry heading |
| `Legal & Finance` | 1 | legal | INDUSTRY | legal |
| `Legal & Finance` | 1 | finance | INDUSTRY | financial-services |
| `Lending` | 1 | lending | INDUSTRY | lending |
| `LET’S TALK RESULTS` | 1 | let's talk results | REJECTED | site navigation, CTA, product or content label |
| `Life Sciences` | 1 | life sciences | INDUSTRY | life-sciences |
| `Life Sciences and Healthcare` | 1 | life sciences | INDUSTRY | life-sciences |
| `Life Sciences and Healthcare` | 1 | healthcare | INDUSTRY | healthcare |
| `LISTSERV 101` | 1 | listserv 101 | REJECTED | site navigation, CTA, product or content label |
| `Local/Home Services` | 1 | local | REJECTED | site navigation, CTA, product or content label |
| `Local/Home Services` | 1 | home services | INDUSTRY | home-services |
| `Locations` | 1 | locations | REJECTED | site navigation, CTA, product or content label |
| `Loyalty and lifecycle marketing` | 1 | loyalty and lifecycle marketing | REJECTED | sub-label describing the row above, not an industry heading |
| `Luxury` | 1 | luxury | INDUSTRY | luxury |
| `Maestro 101` | 1 | maestro 101 | REJECTED | site navigation, CTA, product or content label |
| `Manage customer lifecycle` | 1 | manage customer lifecycle | REJECTED | site navigation, CTA, product or content label |
| `Marketers` | 1 | marketers | SEGMENT | buyer role |
| `Marketplace` | 1 | marketplace | SEGMENT | business model |
| `Marketplaces` | 1 | marketplaces | SEGMENT | business model |
| `Media & entertainment` | 1 | media | INDUSTRY | media |
| `Media & entertainment` | 1 | entertainment | INDUSTRY | entertainment |
| `Media & Publishers` | 1 | media | INDUSTRY | media |
| `Media & Publishers` | 1 | publishers | INDUSTRY | media |
| `Media & Publishing` | 1 | media | INDUSTRY | media |
| `Media & Publishing` | 1 | publishing | INDUSTRY | media |
| `Media and entertainment` | 1 | media | INDUSTRY | media |
| `Media and entertainment` | 1 | entertainment | INDUSTRY | entertainment |
| `Media&Entertainment` | 1 | media | INDUSTRY | media |
| `Media&Entertainment` | 1 | entertainment | INDUSTRY | entertainment |
| `Mgmt. Consulting` | 1 | mgmt. consulting | SEGMENT | competitor class 3 - services firms |
| `Mobile` | 1 | mobile | REJECTED | site navigation, CTA, product or content label |
| `Mobile App Marketing` | 1 | mobile app marketing | REJECTED | site navigation, CTA, product or content label |
| `Mobile apps` | 1 | mobile apps | SEGMENT | product type |
| `Mortgage` | 1 | mortgage | INDUSTRY | mortgage |
| `Mutual Funds` | 1 | mutual funds | INDUSTRY | mutual-funds |
| `New` | 1 | new | REJECTED | site navigation, CTA, product or content label |
| `News` | 1 | news | REJECTED | site navigation, CTA, product or content label |
| `News/Media` | 1 | news | INDUSTRY | media |
| `News/Media` | 1 | media | INDUSTRY | media |
| `NGOs` | 1 | ngos | INDUSTRY | nonprofits |
| `Non-profit` | 1 | non-profit | INDUSTRY | nonprofits |
| `Nurture Leads` | 1 | nurture leads | REJECTED | site navigation, CTA, product or content label |
| `Oil & Gas` | 1 | oil & gas | INDUSTRY | oil-gas |
| `Omnichannel Engagement` | 1 | omnichannel engagement | REJECTED | site navigation, CTA, product or content label |
| `On-Demand` | 1 | on-demand | SEGMENT | business model |
| `One pagers` | 1 | one pagers | REJECTED | site navigation, CTA, product or content label |
| `Online Trading` | 1 | online trading | INDUSTRY | online-trading |
| `Open Resources` | 1 | open resources | REJECTED | site navigation, CTA, product or content label |
| `Operations` | 1 | operations | SEGMENT | buyer role |
| `Operations Service Providers` | 1 | operations service providers | SEGMENT | competitor class 3 - services firms |
| `OPTIKPI FOR...` | 1 | optikpi for... | REJECTED | site navigation, CTA, product or content label |
| `Orchestrate Journeys` | 1 | orchestrate journeys | REJECTED | site navigation, CTA, product or content label |
| `Our Solutions` | 1 | our solutions | REJECTED | site navigation, CTA, product or content label |
| `Our Story` | 1 | our story | REJECTED | site navigation, CTA, product or content label |
| `Personalization` | 1 | personalization | REJECTED | site navigation, CTA, product or content label |
| `Personalization at purchase scale` | 1 | personalization at purchase scale | REJECTED | sub-label describing the row above, not an industry heading |
| `Pet Services` | 1 | pet services | INDUSTRY | pet-services |
| `Pharma` | 1 | pharma | INDUSTRY | pharma |
| `Pharmacy` | 1 | pharmacy | INDUSTRY | pharmacy |
| `Plans` | 1 | plans | REJECTED | site navigation, CTA, product or content label |
| `Prediction Markets` | 1 | prediction markets | INDUSTRY | prediction-markets |
| `Pricing` | 1 | pricing | REJECTED | site navigation, CTA, product or content label |
| `Private Equity` | 1 | private equity | INDUSTRY | private-equity |
| `Process Mining` | 1 | process mining | REJECTED | site navigation, CTA, product or content label |
| `PRODUCT FEATURES` | 1 | product features | REJECTED | site navigation, CTA, product or content label |
| `Product Tours` | 1 | product tours | REJECTED | site navigation, CTA, product or content label |
| `Products` | 1 | products | REJECTED | site navigation, CTA, product or content label |
| `PropTech` | 1 | proptech | INDUSTRY | proptech |
| `Public Services` | 1 | public services | INDUSTRY | government |
| `Pulse: iGaming’s Benchmark Tool` | 1 | pulse: igaming's benchmark tool | REJECTED | site navigation, CTA, product or content label |
| `Read the report` | 1 | read the report | REJECTED | site navigation, CTA, product or content label |
| `Real Estate Industry Solutions` | 1 | real estate | INDUSTRY | real-estate |
| `Real-time player context and activation` | 1 | real-time player context and activation | REJECTED | sub-label describing the row above, not an industry heading |
| `Reduce churn, boost loyal` | 1 | reduce churn, boost loyal | REJECTED | site navigation, CTA, product or content label |
| `Repair shops & detailing` | 1 | repair shops & detailing | REJECTED | sub-label describing the row above, not an industry heading |
| `Request a Demo` | 1 | request a demo | REJECTED | site navigation, CTA, product or content label |
| `Resource Center` | 1 | resource center | REJECTED | site navigation, CTA, product or content label |
| `Resource hub` | 1 | resource hub | REJECTED | site navigation, CTA, product or content label |
| `Resource Library -->` | 1 | resource library --> | REJECTED | site navigation, CTA, product or content label |
| `Resources and Events` | 1 | resources and events | REJECTED | site navigation, CTA, product or content label |
| `Restaurant Industry Solutions` | 1 | restaurant | INDUSTRY | restaurants |
| `Retail & E-Commerce` | 1 | retail | INDUSTRY | retail |
| `Retail & E-Commerce` | 1 | e-commerce | INDUSTRY | ecommerce |
| `Retail & E-commerce` | 1 | retail | INDUSTRY | retail |
| `Retail & E-commerce` | 1 | e-commerce | INDUSTRY | ecommerce |
| `Retail & ecommerce` | 1 | retail | INDUSTRY | retail |
| `Retail & ecommerce` | 1 | ecommerce | INDUSTRY | ecommerce |
| `Retail and ecommerce` | 1 | retail | INDUSTRY | retail |
| `Retail and ecommerce` | 1 | ecommerce | INDUSTRY | ecommerce |
| `Retail Leasing Metrics` | 1 | retail leasing metrics | REJECTED | site navigation, CTA, product or content label |
| `RFP/RFI` | 1 | rfp/rfi | REJECTED | site navigation, CTA, product or content label |
| `ROI Calcu` | 1 | roi calcu | REJECTED | site navigation, CTA, product or content label |
| `Salons, spas, fitness` | 1 | salons, spas, fitness | REJECTED | sub-label describing the row above, not an industry heading |
| `Schedule a Demo` | 1 | schedule a demo | REJECTED | site navigation, CTA, product or content label |
| `Schedule a demo` | 1 | schedule a demo | REJECTED | site navigation, CTA, product or content label |
| `Security and Compliance` | 1 | security and compliance | REJECTED | site navigation, CTA, product or content label |
| `See All Industries` | 1 | see all industries | REJECTED | site navigation, CTA, product or content label |
| `See product tour` | 1 | see product tour | REJECTED | site navigation, CTA, product or content label |
| `Service` | 1 | service | REJECTED | site navigation, CTA, product or content label |
| `Services` | 1 | services | REJECTED | site navigation, CTA, product or content label |
| `shopping_cart` | 1 | shopping_cart | REJECTED | Material-icon ligature scraped from markup |
| `Small business` | 1 | small business | SEGMENT | company size |
| `SMS Marketing` | 1 | sms marketing | REJECTED | site navigation, CTA, product or content label |
| `Social Games & Apps` | 1 | social games | INDUSTRY | gaming |
| `Social Games & Apps` | 1 | apps | REJECTED | site navigation, CTA, product or content label |
| `Social Gaming` | 1 | social gaming | INDUSTRY | gaming |
| `Social Media` | 1 | social media | REJECTED | site navigation, CTA, product or content label |
| `Solutions Library` | 1 | solutions library | REJECTED | site navigation, CTA, product or content label |
| `Solutions that drive business results` | 1 | solutions that drive business results | REJECTED | site navigation, CTA, product or content label |
| `Space Optimization` | 1 | space optimization | REJECTED | site navigation, CTA, product or content label |
| `Startups` | 1 | startups | SEGMENT | company stage |
| `Startups & Scaleups` | 1 | startups & scaleups | SEGMENT | company stage |
| `State of Direct Mail` | 1 | state of direct mail | REJECTED | site navigation, CTA, product or content label |
| `Success Story` | 1 | success story | REJECTED | site navigation, CTA, product or content label |
| `Supply Chain` | 1 | supply chain | INDUSTRY | supply-chain |
| `Switch from GA4` | 1 | switch from ga4 | REJECTED | site navigation, CTA, product or content label |
| `Switch from Matomo` | 1 | switch from matomo | REJECTED | site navigation, CTA, product or content label |
| `Teams` | 1 | teams | REJECTED | site navigation, CTA, product or content label |
| `Tech/Software/IT` | 1 | tech | INDUSTRY | technology |
| `Tech/Software/IT` | 1 | software | INDUSTRY | software |
| `Tech/Software/IT` | 1 | it | INDUSTRY | it-services |
| `Technical` | 1 | technical | SEGMENT | buyer role |
| `Technology & Services` | 1 | technology | INDUSTRY | technology |
| `Technology & Services` | 1 | services | REJECTED | site navigation, CTA, product or content label |
| `Telecom, media & entertainment` | 1 | telecom | INDUSTRY | telecommunications |
| `Telecom, media & entertainment` | 1 | media | INDUSTRY | media |
| `Telecom, media & entertainment` | 1 | entertainment | INDUSTRY | entertainment |
| `Testimonials` | 1 | testimonials | REJECTED | site navigation, CTA, product or content label |
| `Text - Customer service solution for capital markets` | 1 | capital markets | INDUSTRY | capital-markets |
| `Text - Customer service solution for iGaming` | 1 | igaming | INDUSTRY | igaming |
| `Toggle Menu` | 1 | toggle menu | REJECTED | site navigation, CTA, product or content label |
| `Tourism` | 1 | tourism | INDUSTRY | travel |
| `Tourism Fiji` | 1 | tourism fiji | REJECTED | named client or vendor, not an industry |
| `Trades & field work` | 1 | trades & field work | REJECTED | sub-label describing the row above, not an industry heading |
| `Training` | 1 | training | REJECTED | site navigation, CTA, product or content label |
| `Transportation` | 1 | transportation | INDUSTRY | transportation |
| `travel` | 1 | travel | INDUSTRY | travel |
| `Travel & hospitality` | 1 | travel | INDUSTRY | travel |
| `Travel & hospitality` | 1 | hospitality | INDUSTRY | hospitality |
| `Travel And Hospitality` | 1 | travel | INDUSTRY | travel |
| `Travel And Hospitality` | 1 | hospitality | INDUSTRY | hospitality |
| `Travel and hospitality` | 1 | travel | INDUSTRY | travel |
| `Travel and hospitality` | 1 | hospitality | INDUSTRY | hospitality |
| `Turn` | 1 | turn | REJECTED | site navigation, CTA, product or content label |
| `Use Cases` | 1 | use cases | REJECTED | site navigation, CTA, product or content label |
| `USE CASES` | 1 | use cases | REJECTED | site navigation, CTA, product or content label |
| `Utilities` | 1 | utilities | INDUSTRY | utilities |
| `Video Tutorials` | 1 | video tutorials | REJECTED | site navigation, CTA, product or content label |
| `View Blog` | 1 | view blog | REJECTED | site navigation, CTA, product or content label |
| `Vodafone Fiji` | 1 | vodafone fiji | REJECTED | named client or vendor, not an industry |
| `Webinar` | 1 | webinar | REJECTED | site navigation, CTA, product or content label |
| `Webinars` | 1 | webinars | REJECTED | site navigation, CTA, product or content label |
| `Webinars and events` | 1 | webinars and events | REJECTED | site navigation, CTA, product or content label |
| `Website` | 1 | website | REJECTED | site navigation, CTA, product or content label |
| `what we can do for you` | 1 | what we can do for you | REJECTED | site navigation, CTA, product or content label |
| `WHAT’S NEW?` | 1 | what's new | REJECTED | site navigation, CTA, product or content label |
| `White Papers & Guides` | 1 | white papers & guides | REJECTED | site navigation, CTA, product or content label |
| `Why iPresso?` | 1 | why ipresso | REJECTED | site navigation, CTA, product or content label |
| `Why Pyze` | 1 | why pyze | REJECTED | site navigation, CTA, product or content label |
| `Why SmartCOMM` | 1 | why smartcomm | REJECTED | site navigation, CTA, product or content label |
| `WorksBuddy for Automobile` | 1 | automobile | INDUSTRY | automotive |
| `WorksBuddy for Education` | 1 | education | INDUSTRY | education |
| `WorksBuddy for Finance` | 1 | finance | INDUSTRY | financial-services |
| `WorksBuddy for Food and Beverage` | 1 | food and beverage | INDUSTRY | food-beverage |
| `WorksBuddy for Healthcare` | 1 | healthcare | INDUSTRY | healthcare |
| `WorksBuddy for IT Services` | 1 | it services | INDUSTRY | it-services |
| `WorksBuddy for Logistics` | 1 | logistics | INDUSTRY | logistics |
| `WorksBuddy for Real Estate` | 1 | real estate | INDUSTRY | real-estate |
| `WorksBuddy for SaaS` | 1 | saas | INDUSTRY | saas |
