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
