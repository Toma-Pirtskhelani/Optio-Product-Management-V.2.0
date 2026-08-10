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

| paste_id | date_received | url | source | requested_scope | visible_count | total_count | pagination | sort_order | filters_active | source_language | raw_file | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| _(empty — no research has been conducted)_ | | | | | | | | | | | | |
