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
