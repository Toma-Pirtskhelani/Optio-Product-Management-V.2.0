# paste-log.md — the sampling record

Every human-transported page. This file exists because **which pages get pasted determines
what this study can see**, and an unlogged sampling frame is indistinguishable from a
neutral one — which it is not.

This is not bookkeeping. At write-up time, this file is read as a **sample description**,
and any finding whose support comes disproportionately from one requested page has to say so.

Append-only. Governed by `research-protocol.md` §2 and §3.

## Columns

| Field | Meaning |
|---|---|
| `paste_id` | `P-0001`, sequential. Rows in `passes/` and `outputs/` cite this |
| `date_received` | ISO date the paste arrived |
| `url` | Exact URL the user opened |
| `source` | Source of record (`g2`, `gartner`, marketplace name) |
| `requested_scope` | What was asked for: whole page / named section / page N of M |
| `visible_count` | Items actually visible in the pasted content, or `n/a` |
| `total_count` | Total the page itself declared (e.g. "of 122"), or `UNKNOWN` |
| `pagination` | `none` / `page X of Y` / `unknown` |
| `sort_order` | Sort the page displayed, if shown (`default`, `relevance`, `rating`, …) or `UNKNOWN` |
| `filters_active` | Filters visible as applied, or `none` / `UNKNOWN` |
| `source_language` | ISO code of the page's language. **Mandatory** — feeds the block-rate-by-language measurement in `logs/fetch-log.md` |
| `raw_file` | Path under `sources/raw/` holding the verbatim paste |
| `notes` | Anything visibly truncated, ad-marked, "sponsored", or otherwise not what was asked for |

## Rules

- **`total_count: UNKNOWN` is not `total_count: visible_count`.** If the page did not
  declare a total, absence from the paste is `ABSENT-IN-VISIBLE-PAGE`, never
  `ABSENT-ENUMERATED`.
- `sort_order` and `filters_active` are recorded because a "top 20" is a *ranked* sample,
  not a random one. A finding drawn from a rating-sorted first page is a finding about
  highly-rated vendors, and must say so.
- **Sponsored / promoted placements are recorded in `notes`.** A pay-to-play position at the
  top of a list is SELF-DECLARED evidence at its strongest, and its position carries no
  information about the market.
- The raw paste goes into `sources/raw/` **verbatim**. If a parsed row and the raw file ever
  disagree, the raw file wins.

## Log

### Pass 01 — requests pre-registered 2026-08-10, pastes not yet received

**Recorded before the content arrives, deliberately.** If the sampling frame is only written
down after seeing what came back, it is a description of the result rather than of the
sample. These four requests, and the reasoning for choosing exactly these URLs, are in
`outputs/source-taxonomies.md` §8.

| paste_id | date_received | url | source | requested_scope | visible_count | total_count | pagination | sort_order | filters_active | source_language | raw_file | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| P-0001 | **awaiting** | https://www.gartner.com/reviews/markets | gartner | whole page, every market name incl. (Legacy)/(Retired)/(Transitioning to X) suffixes; **page through to the end** | — | — | expected, unknown depth | — | — | en | — | Highest value in the study: the only denominator Gartner can have, and the only failure-detection mechanism our source set contains |
| P-0002..P-0013 | **awaiting** | 12 × https://www.g2.com/categories/{marketing-automation, email-marketing, sms-marketing, push-notification, mobile-marketing, customer-communications-management, customer-data-platform-cdp, loyalty-management, proactive-notification, patient-engagement, citizen-engagement, political-campaign} | g2 | definition paragraphs + **entire** "To qualify for inclusion" bullet list + declared product count line. Page 1 only — the product list is not needed | — | — | not required | — | — | en | — | **Sampling frame declared: I chose these twelve.** 6 functional core, 2 named boundary classes, 1 framing test, 3 verticals. The user was asked to pick the next twelve so the frame is not mine alone |
| P-0014 | **awaiting** | https://www.gartner.com/reviews/market/marketing-automation-platforms | gartner | market definition + mandatory capabilities + declared vendor count + any decline marker | — | — | — | — | — | en | — | Shapes schemas/gartner.md against a real page instead of an assumed one |
| P-0015 | **awaiting** | Shopify app listing requirements + HubSpot app certification requirements | shopify-app-store, hubspot-ecosystem | requirements list verbatim | — | — | — | — | — | en | — | Bar height for both marketplaces, currently UNKNOWN — which is what makes their counts non-comparable to anything |


### Pass 02 — pastes RECEIVED 2026-08-10

**Purposive sample, user-selected.** Seven of the twelve G2 URLs pre-registered as P-0002..P-0013
were not supplied; Gartner market pages were supplied instead — a different, and better, set for
establishing what Gartner thinks it catalogues. The substitution is recorded rather than
smoothed over: what arrived is not what was requested, and the sampling frame is therefore the
user's, not mine.

| paste_id | date_received | url | source | requested_scope | visible_count | total_count | pagination | sort_order | filters_active | source_language | raw_file | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| P-0016 | 2026-08-10 | /reviews/market/multichannel-marketing-hubs | gartner | whole page | 122 | **122** | none — full enumeration | Number of Ratings, High to Low | none | en | `sources/raw/web pages/gartner/…` | 5 (Legacy) products; Gartner states MMH overlaps CDP and personalization engines |
| P-0017 | 2026-08-10 | /reviews/market/email-marketing | gartner | whole page | 100 | **100** | none | Number of Ratings, High to Low | none | en | idem | category marked (Transitioning to Email Marketing Platforms) |
| P-0018 | 2026-08-10 | /reviews/market/customer-data-platforms | gartner | whole page | 71 | **71** | none | idem | none | en | idem | activation defined as sending segments to engagement tools |
| P-0019 | 2026-08-10 | /reviews/market/personalization-engines | gartner | whole page | 64 | **64** | none | idem | none | en | idem | highest bar in sample (8); recipient definition includes employees |
| P-0020 | 2026-08-10 | /reviews/market/b2b-marketing-automation-platforms | gartner | whole page | 59 | **59** | none | idem | none | en | idem | 3 (Legacy) |
| P-0021 | 2026-08-10 | /reviews/market/mobile-marketing-platforms | gartner | whole page | 45 | **45** | none | idem | none | en | idem | lowest bar (3, all "Basic"); Market Guide only, no Magic Quadrant |
| P-0022 | 2026-08-10 | /reviews/market/location-based-marketing-software | gartner | whole page | 15 | **15** | none | idem | none | en | idem | **control case** — Peer Insights Category, no mandatory features, no analyst document |
| P-0023 | 2026-08-10 | /reviews/faq | gartner | whole page | n/a | n/a | none | n/a | n/a | en | idem | governance; language eligibility list excludes ru/tr/ka |

**Sampling note carried into every output built on these:** seven Marketing markets out of an
**unknown** branch total. `total_count` is `PRIMARY` *within* each market — every page
enumerates fully — and `UNKNOWN` at branch level. The first supports `ABSENT-ENUMERATED`
inside a market; the second forbids any statement about how many such markets exist.

### Pass 03 — 36 vendor pages, human-transported, received 2026-08-11

**A purposive sample: the user chose which pages to send.** That is a sampling decision and is
logged as one. Every row records what the paste actually was, because four classes arrived and
they are not interchangeable.

`Preamble` counts unattributed prose lines above the pasted URL. Those lines were **discarded** —
they are of unknown authorship, and two acquisition claims found in them were rejected (`C-0009`).

| paste_id | date | company | url supplied | classification | identity | lines | preamble | how it was used |
|---|---|---|---|---|---|---|---|---|
| P-101 | 2026-08-11 | Amazing Mail | https://www.amazingmail.com/ | VENDOR_SITE | ✅ | 53 | 0 | re-fetched from this URL — record is HTML-derived |
| P-102 | 2026-08-11 | AT Internet | https://developers.piano.io/analytics/ | THIRD_PARTY | ❌ | 29 | 0 | **not used** |
| P-103 | 2026-08-11 | Beaconsmind | https://www.gartner.com/reviews/product/beaconsmind | THIRD_PARTY | ✅ | 247 | 0 | Rung-4 existence evidence only |
| P-104 | 2026-08-11 | BrandOps | https://brandops.work/ | VENDOR_SITE | ✅ | 172 | 0 | re-fetched from this URL — record is HTML-derived |
| P-105 | 2026-08-11 | BSI Software | https://www.bsi-software.com/en | VENDOR_SITE | ✅ | 216 | 0 | re-fetched from this URL — record is HTML-derived |
| P-106 | 2026-08-11 | Capillary Technologies | https://www.capillarytech.com/ | VENDOR_SITE | ✅ | 148 | 0 | re-fetched from this URL — record is HTML-derived |
| P-107 | 2026-08-11 | Cisco Systems | https://www.cisco.com/c/dam/en/us/products/conferencing/Cisco_WebEx_Marketing_Automation.pdf | VENDOR_SITE | ✅ | 80 | 0 | paste is the only evidence — paste-derived fields |
| P-108 | 2026-08-11 | ClickDimensions | https://clickdimensions.com/ | VENDOR_SITE | ✅ | 190 | 0 | paste is the only evidence — paste-derived fields |
| P-109 | 2026-08-11 | Datorama | https://funnel.io/what-is-datorama | THIRD_PARTY | ✅ | 178 | 0 | Rung-4 existence evidence only |
| P-110 | 2026-08-11 | Ecomail | https://ecomail.app/ | VENDOR_SITE | ✅ | 146 | 0 | re-fetched from this URL — record is HTML-derived |
| P-111 | 2026-08-11 | Emailidea | *none supplied* | VENDOR_PAGE_NO_URL | ✅ | 205 | 0 | paste is the only evidence — paste-derived fields |
| P-112 | 2026-08-11 | FollowAnalytics | https://mmaglobal.com/sponsors/followanalytics | THIRD_PARTY | ✅ | 62 | 0 | Rung-4 existence evidence only |
| P-113 | 2026-08-11 | Free Stand Sampling Solutions | https://freestand.in/ | VENDOR_SITE | ✅ | 149 | 0 | re-fetched from this URL — record is HTML-derived |
| P-114 | 2026-08-11 | Fresh Relevance | https://dotdigital.com/personalization/ | THIRD_PARTY | ✅ | 198 | 1 | Rung-4 existence evidence only |
| P-115 | 2026-08-11 | Hewlett Packard Enterprise | https://www.hpe.com/emea_europe/en/home.html | VENDOR_SITE | ✅ | 130 | 0 | paste is the only evidence — paste-derived fields |
| P-116 | 2026-08-11 | IBM | https://www.ibm.com/products/watsonx | VENDOR_SITE | ✅ | 234 | 0 | re-fetched from this URL — record is HTML-derived |
| P-117 | 2026-08-11 | inConcert | https://www.inconcertcx.com/en | VENDOR_SITE | ✅ | 170 | 0 | re-fetched from this URL — record is HTML-derived |
| P-118 | 2026-08-11 | Intense Technologies | https://www.in10stech.com/ | VENDOR_SITE | ✅ | 175 | 0 | paste is the only evidence — paste-derived fields |
| P-119 | 2026-08-11 | Lob | https://www.lob.com/ | VENDOR_SITE | ✅ | 129 | 0 | re-fetched from this URL — record is HTML-derived |
| P-120 | 2026-08-11 | Longtail UX | https://au.linkedin.com/company/longtail-ux | THIRD_PARTY | ✅ | 86 | 0 | Rung-4 existence evidence only |
| P-121 | 2026-08-11 | Mindmatrix | https://www.mindmatrix.net/ | VENDOR_SITE | ✅ | 289 | 0 | re-fetched from this URL — record is HTML-derived |
| P-122 | 2026-08-11 | NewZapp | *none supplied* | VENDOR_PAGE_NO_URL | ✅ | 169 | 0 | paste is the only evidence — paste-derived fields |
| P-123 | 2026-08-11 | PAR | https://www.salesforce.com/marketing/b2b-automation/ | THIRD_PARTY | ❌ | 159 | 1 | **not used** |
| P-124 | 2026-08-11 | Reachdesk | https://www.reachdesk.com/ | VENDOR_SITE | ✅ | 122 | 0 | re-fetched from this URL — record is HTML-derived |
| P-125 | 2026-08-11 | SAP | https://www.sap.com/products/crm/engagement-cloud.html | VENDOR_SITE | ✅ | 182 | 0 | paste is the only evidence — paste-derived fields |
| P-126 | 2026-08-11 | SAS | https://support.sas.com/en/software/marketing-automation-support.html | VENDOR_SITE | ✅ | 87 | 0 | re-fetched from this URL — record is HTML-derived |
| P-127 | 2026-08-11 | Spectrm | https://www.linkedin.com/company/spectrm | THIRD_PARTY | ✅ | 100 | 1 | Rung-4 existence evidence only |
| P-128 | 2026-08-11 | Striker Soft Solutions | https://se.linkedin.com/company/strikersoft | THIRD_PARTY | ✅ | 208 | 1 | Rung-4 existence evidence only |
| P-129 | 2026-08-11 | SwiftERM Hyper-Personalisation | https://swifterm.com/ | VENDOR_SITE | ✅ | 151 | 0 | re-fetched from this URL — record is HTML-derived |
| P-130 | 2026-08-11 | Treasure AI | https://www.treasure.ai/ | VENDOR_SITE | ✅ | 164 | 0 | re-fetched from this URL — record is HTML-derived |
| P-131 | 2026-08-11 | Veloxy IO | https://veloxy.io/ | VENDOR_SITE | ✅ | 204 | 0 | re-fetched from this URL — record is HTML-derived |
| P-132 | 2026-08-11 | Webmaxy | https://www.webmaxy.co/ | VENDOR_SITE | ✅ | 158 | 0 | re-fetched from this URL — record is HTML-derived |
| P-133 | 2026-08-11 | Wigzo | https://www.crunchbase.com/organization/wigzo-technologies | THIRD_PARTY | ✅ | 274 | 0 | Rung-4 existence evidence only |
| P-134 | 2026-08-11 | WILY | https://wilyglobal.com/ | VENDOR_SITE | ✅ | 69 | 0 | re-fetched from this URL — record is HTML-derived |
| P-135 | 2026-08-11 | xiQ | https://xiqinc.com/ | VENDOR_SITE | ✅ | 176 | 0 | re-fetched from this URL — record is HTML-derived |
| P-136 | 2026-08-11 | Zeta | https://www.zeta.tech/us/ | VENDOR_SITE | ✅ | 478 | 0 | re-fetched from this URL — record is HTML-derived |
