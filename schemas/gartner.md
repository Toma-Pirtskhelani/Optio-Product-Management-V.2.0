# schemas/gartner.md — analyst-firm taxonomy pass

**Governs:** `passes/gartner/<pass_id>.md`
**Merges into:** `schemas/merged-table.md` Table A (categories) and Table B
(vendors), on `normalized_name`.

**This is the source that broke V1.** Its taxonomy was taken as the market, and
its enterprise-Western skew was never corrected. It is included here as *one of
four*, never as the frame. Any output where Gartner's category boundaries
silently became the study's boundaries is rejected on P2.

Two rules apply to this source and no other:

1. **Capture the inclusion criteria before capturing the vendor list.** The
   criteria — revenue floors, customer-count minimums, geographic presence
   requirements, vendor participation — *are* the skew, stated in the source's
   own words. Without them the vendor list is uninterpretable. A pass that
   captures vendors without criteria is rejected.
2. **A market Gartner does not name still exists.** Absence from Gartner is
   recorded as `— [UNKNOWN]` in the merged table, never as `0`, never as
   evidence a category isn't real.

Column availability is an assumption until the first fetch. Most Gartner content
is gated; § 2 governs.

---

## 1. Spine

Every row carries the spine from `schemas/merged-table.md` § 1.

## 2. Access protocol (P6, hardest case here)

1. R1 on the public market/definition page or Peer Insights market page.
2. `403` / paywall / login wall → **log it**, then R2 via `web.archive.org` with
   `snapshot_date`. Analyst content is heavily archived; this rung frequently
   works and V1 never tried it.
3. R3 only after both are logged, and permanently marked. A vendor's own press
   release announcing its placement is `R1` for *"the vendor claims placement"*
   and `SINGLE-SOURCE` for the placement itself — vendors reprint favourable
   analyst content selectively, so this route is structurally biased toward
   leaders. Note that bias on the row.
4. Reproduction of the report on a vendor's site is R3 for content and is
   recorded with the hosting vendor named, because the choice of who hosts it is
   itself information.

## 3. Table A — markets

| Column | Definition |
|---|---|
| *spine* | § 1 |
| `market_name` | Verbatim (`raw_name`). |
| `artifact_type` | `Magic Quadrant` / `Peer Insights` / `Market Guide` / `Critical Capabilities` / `Hype Cycle` / other — verbatim. Different artifacts have different inclusion rules; do not pool them. |
| `publication_date` | With grade. Analyst markets are renamed and retired often; date every row. |
| `prior_year_market_name` | If renamed, the previous name verbatim — a rename is a `SUPERSEDE` in `industry-registry.md`. |
| `stated_definition` | Gartner's market definition, quoted verbatim. |
| **`inclusion_criteria`** | Quoted verbatim, in full. Revenue floors, customer minimums, geographic requirements, participation requirements. **The single most load-bearing cell in this pass.** |
| `inclusion_criteria_url` | Row-level. |
| `vendor_count` | With grade. |
| `reviewer_geography` | Peer Insights reviewer distribution if published, with grade. Direct measurement of the Western skew. |
| `reviewer_org_size` | If published, with grade. Direct measurement of the enterprise skew. |
| `excluded_by_criteria` | Any vendor the criteria demonstrably exclude, where determinable. `UNKNOWN` is an acceptable answer; invention is not. |

## 4. Table B — vendors

| Column | Definition |
|---|---|
| *spine* | § 1 |
| `vendor_name` / `vendor_aliases` | Verbatim. |
| `placement` | Verbatim label (quadrant, rating, tier) — never paraphrased. |
| `placement_year` | |
| `prior_year_placement` | Enables § 5. |
| `review_count` / `rating` | With grade. |
| `vendor_own_site` | Fetched separately at R1. |
| `hq_country` | With grade. |
| `meets_criteria_note` | Which stated criterion admitted them, where determinable. |

## 5. Failure sampling (P4) — mechanisms for this source

Analyst reports are annual snapshots of survivors, which makes their **deltas**
unusually good failure detectors:

1. Fetch the prior-year artifact (R1, else R2 via archive). Diff the vendor
   lists. Every vendor present then and absent now is a candidate.
2. Resolve each candidate at R1 against its own domain: shut down, acquired,
   dropped below a revenue floor, declined to participate, or market renamed.
   These are five different outcomes and must not be collapsed into one.
3. Where a vendor was dropped for failing an inclusion criterion rather than for
   dying, record it in `outputs/coverage-report.md`, not in the failure register.
   **Being too small for Gartner is not a business failure** — treating it as one
   would import the exact bias this schema exists to expose.
4. Repeat across ≥2 prior years where archived versions exist.

## 6. Language protocol (P5)

Record `reviewer_geography` and the language of every artifact fetched. If scope
includes a non-anglophone market, check for regional analyst coverage from local
firms and record what exists — Gartner's silence on a region is a fact about
Gartner. Do not present a Gartner market as global unless the source itself
states global scope, quoted.

## 7. Rejection

Standard checklist, `research-protocol.md` § 7, plus:

- [ ] `inclusion_criteria` captured verbatim for every market, before vendors.
- [ ] Every gated fetch shows a logged `web.archive.org` attempt.
- [ ] Vendor-hosted reproductions marked R3 with the hosting vendor named.
- [ ] Prior-year diff run for ≥1 year; ≥2 where archives allow.
- [ ] Dropped-for-criteria separated from dropped-for-death.
- [ ] Nothing in this pass silently became the study's category frame.
