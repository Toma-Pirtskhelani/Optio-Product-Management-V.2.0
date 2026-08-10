# schemas/gartner.md — Gartner pass output columns

Populates the spine in `schemas/merged-table.md`. Every spine field is mandatory here.

**Gartner is this study's primary failure-detection mechanism.** It is the only source in our
set that marks decline explicitly, on the record, in its own taxonomy. `(Legacy)`,
`(Retired)`, and `(Transitioning to X)` are **first-class fields in this schema, never
footnotes** — extracting them is the main reason this pass exists, and a Gartner pass that
returns ratings but not decline markers has failed at its primary job.

---

## 1. What Gartner is the source of record for

- Its own market/category names, definitions, and **market status** — including retirement
  and transition.
- Which products it places in a market, and how it labels their lifecycle stage.
- Peer Insights ratings, review counts, and willingness-to-recommend **as Gartner computes
  them**.

**Not the source of record for:** vendor size, revenue, funding, or customer counts. Funding
is `UNKNOWN` and stays `UNKNOWN` (`CLAUDE.md` §7.1) — never inferred from analyst coverage.

---

## 2. Decline markers — extracted first, dropped never

| Field | Notes |
|---|---|
| `decline_marker` | `none` / `legacy` / `retired` / `transitioning` |
| `decline_marker_verbatim` | **Exactly as printed**, parentheses and all: `(Legacy)`, `(Retired)`, `(Transitioning to Customer Communications Management)` |
| `decline_marker_applies_to` | `product` / `category` |
| `transition_target_raw` | The `X` in "Transitioning to X", verbatim → **appended to `industry-registry.md` as its own entry with the alias relationship recorded** |
| `marker_capture_date` | ISO date the marker was seen — markers change, and when they change is a finding |
| `marker_url` | Exact URL where the marker appeared |
| `marker_grade` | Normally `PRIMARY` (Gartner's own label about Gartner's own taxonomy) |

**Reading rules:**

- **`(Legacy)` on a product** — managed decline with ratings intact. This is the highest-value
  single row type in the study: a product still scoring well **while its own analyst source
  labels it legacy** is a warning the ratings do not price in. Record the rating *and* the
  marker on the same row so the contradiction is visible in one line.
- **`(Retired)` on a category** — a market that failed or dissolved. **Stronger than any
  single dead company, and nothing else in our source set can produce it.** The registry entry
  is kept with `status: RETIRED-BY-SOURCE`; deleting it would rebuild survivorship bias inside
  the merge key (`industry-registry.md` §6).
- **`(Transitioning to X)` on a category** — the taxonomy itself is moving. Record **both**
  names. A boundary in motion invalidates count comparisons across captures, and the pass
  must say so.

A Gartner pass output that contains **zero** decline markers must state how many category and
product pages were actually inspected for them. Zero markers across three pages is not a
finding about the market; it is a finding about the sample.

---

## 3. Market / category rows

`entity_type: category`.

| Field | Notes |
|---|---|
| `raw_name` | **Gartner's market name exactly as printed**, including any parenthetical marker |
| `raw_name_stripped` | Same name with the marker removed — for matching only. **Never replaces `raw_name`** |
| `normalized_name` / `registry_id` | From `industry-registry.md`. Append, never force-match |
| `market_definition_verbatim` | Gartner's full market definition, quoted. This is its inclusion criteria |
| `mandatory_features_verbatim` | Required/core capabilities list, quoted, where published. `UNKNOWN` otherwise |
| `market_status` | `active` / `retired` / `transitioning`, from the marker |
| `document_type` | `peer-insights-market` / `magic-quadrant` / `market-guide` / `critical-capabilities` / `hype-cycle` / other, **verbatim** |
| `document_date` | Publication or "as of" date. Analyst content ages, and an undated claim is undated |
| `vendor_count_declared` + `_grade` | Count Gartner states |
| `vendor_count_visible` | Count actually captured |
| `pagination`, `sort_order`, `filters_active` | Sampling metadata |
| `scope_verdict` / `ruling_id` | Ruled explicitly |
| `source_boundary_verbatim` | Where Gartner's boundary differs from ours — quoted, logged as a conflict |
| Spine provenance | `source_url`, `rung`, `source_class`, `source_language`, `capture_date`, `paste_id`, `raw_file` |

**Gartner's market definition frequently disagrees with G2's category definition for
overlapping ground. That disagreement is a finding** and goes to `logs/conflicts.md` with
`dimension: market-definition`. Do not resolve it by picking the more familiar one; both
names stay in the registry as separate entries with the relationship recorded.

---

## 4. Product / vendor rows

One row per product **per market**.

| Field | Notes |
|---|---|
| `entity_name_raw` | Product name exactly as printed — **including `(Legacy)` if present** |
| `vendor_name_raw` | Selling entity as printed |
| `entity_name_canonical` | This study's key |
| `product_url` | Exact URL |
| `entity_type` | `product` |
| `rating` + `_grade` | As printed |
| `review_count` + `_grade` | As printed |
| `willingness_to_recommend` + `_grade` | As printed, incl. the % sign |
| `mq_position_raw` | Leader / Challenger / Visionary / Niche Player, **verbatim**, with report name and year |
| `reviewer_segment_breakdown_raw` | Company-size / industry / region splits, verbatim where shown — the closest thing Gartner gives to a revealed buyer profile |
| `markets_listed_raw` | Every Gartner market this product appears in → `category_cluster` |
| `cluster_size` | Within `taxonomy_id: gartner` only |
| `decline_marker` fields | §2. Mandatory on every product row, `none` where absent |
| `entity_status` | `active` / `legacy` / `acquired` / `defunct` / `UNKNOWN` — **only from a Gartner statement or a two-capture comparison** |
| `funding_any` | **Always `UNKNOWN`.** Present as a column so nobody quietly infers it later |
| `presence`, `visible_count`, `total_count`, `promoted` | Spine coverage fields |
| Spine provenance | Full set |

---

## 5. Source-class discipline specific to Gartner

- **Peer Insights reviews and ratings: `SELF-DECLARED`.** Vendors actively solicit Peer
  Insights reviews; presence in the market listing reflects vendor participation. Errors
  correlate with G2's.
- **Analyst placement (MQ position, market inclusion): `SELF-DECLARED`.** Vendors brief
  analysts, and inclusion criteria reward the kind of vendor that engages with analysts.
- **Decline markers: still `SELF-DECLARED` in class, but uniquely valuable** — because they
  are the one thing in our source set that runs *against* the source's commercial incentive.
  A source labelling its own category retired is not marketing. Record the class honestly as
  `SELF-DECLARED`, and note in the pass that this specific field is
  incentive-incompatible and therefore unusually credible.

**Gartner + G2 agreeing is not corroboration.** Both are `SELF-DECLARED` and both
systematically favor vendors who invest in analyst and review-platform presence. Any row
claiming `corroborated: yes` on that pair is a reject condition (`merged-table.md` §5).

---

## 6. Known blind spot to state in every Gartner pass

Gartner covers enterprise IT buying. It **under-covers** vendors selling regionally,
in non-Anglophone markets, at SMB price points, or through channels that never brief an
analyst. Per `CLAUDE.md` §6 and §7.2, that skew is the previous attempt's prohibition 2 —
one taxonomy's enterprise-Western bias treated as the market — and it is corrected by
*other sources*, not by reading Gartner more carefully.

Every Gartner pass output ends with a language and coverage line: how many rows are
`source_language: en`, and which of the required non-English languages this pass touched.

---

## 7. Reject conditions (in addition to `merged-table.md` §7)

1. Any product or category row missing `decline_marker` — `none` is a value, blank is not.
2. `raw_name` with the marker stripped out (markers live in `raw_name` **and** in their own
   field).
3. `(Transitioning to X)` recorded without `transition_target_raw` and without a registry
   entry for X.
4. A `(Retired)` category deleted from the registry rather than marked.
5. `market_definition_verbatim` paraphrased.
6. Any funding, revenue, or investor value that is not `UNKNOWN`.
7. `corroborated: yes` where the second source is G2 or a marketplace.
