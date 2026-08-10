# schemas/merged-table.md — the target

**Not a fifth source.** This is the deliverable the other four schemas are
designed backward from. Read this first; the source schemas only make sense as
inputs to it.

If a column here cannot be filled from the four source passes, one of those
schemas is wrong. Fix the schema before running the pass — not the table after.

---

## 1. The spine

Every row of every table in every pass carries these columns. They are what
makes the merge possible and what makes P3 (uneven depth, invisibly presented)
impossible.

| Column | Meaning |
|---|---|
| `pass_id` | `<SOURCE>-<YYYY-MM-DD>-<nn>`. Traces the row to its pass file. |
| `raw_name` | The category name **verbatim** from the source. Immutable. |
| `normalized_name` | Registry entry from `industry-registry.md`, or `IND-NEW:<proposed>` when the pass appended one. |
| `source_url` | **Row-level.** The exact URL this row came from. A pass-level URL is a rejected row. |
| `rung` | `R1` / `R2` / `R3`, per `research-protocol.md` § 1. |
| `retrieved_at` | ISO date of fetch. |
| `snapshot_date` | R2 only. Date of the archive snapshot. |
| `source_lang` | ISO code of the page actually fetched. |
| `grade` | `PRIMARY` / `CORROBORATED` / `SINGLE-SOURCE` / `MODELED` / `UNKNOWN`. |
| `notes` | Anything a reader would need to not misread the row. |

Numeric cells carry their grade inline regardless: `142 [PRIMARY]`,
`~$4.2M [MODELED]`, `— [UNKNOWN]`.

---

## 2. Table A — cross-taxonomy category matrix (primary deliverable)

One row per `normalized_name`. This is the artifact the whole phase exists to
produce. Its job is to show, at a glance, **where the four taxonomies disagree
about what the market is** — the correction V1 never applied to Gartner.

| Column | Notes |
|---|---|
| `normalized_name` | Merge key. |
| `registry_id` | `IND-nnn`. |
| `registry_status` | `ACTIVE` / `PROVISIONAL` / `SUPERSEDED`. |
| `g2_raw_name` | Verbatim, or `— [UNKNOWN]` if absent from G2. |
| `g2_vendor_count` | With grade. |
| `g2_url` / `g2_rung` / `g2_grade` | |
| `cb_raw_name` | Crunchbase category/group, verbatim. |
| `cb_org_count` | With grade. |
| `cb_url` / `cb_rung` / `cb_grade` | |
| `gtnr_raw_name` | Gartner market name, verbatim. |
| `gtnr_vendor_count` | With grade. |
| `gtnr_inclusion_criteria` | Summary + URL. **The most load-bearing cell in the table** — it states who was allowed in. |
| `gtnr_url` / `gtnr_rung` / `gtnr_grade` | |
| `mkt_raw_name` | Marketplace category, verbatim, per platform. |
| `mkt_platforms` | Which marketplaces carry it. |
| `mkt_listing_count` | With grade. |
| `mkt_url` / `mkt_rung` / `mkt_grade` | |
| **`sources_covering`** | 1–4. |
| **`coverage_flag`** | See below. |
| **`failures_found`** | Count from `outputs/failure-register.md` for this category. `0` is only valid with a logged search. |
| **`conflict_ids`** | Rows in `evidence/conflicts.md` touching this category. |
| **`row_confidence`** | The **weakest** grade among the populated source cells. Never the best. Never an average. |
| `lang_coverage` | Languages actually fetched for this category. All-`en` on a non-anglophone market is a P5 flag, not a result. |

`coverage_flag` values:

- `ALL-FOUR` — appears in every source.
- `PARTIAL` — 2–3 sources.
- `SOLE-SOURCE` — exactly one. **Investigate every one of these.** It is either a
  real market three taxonomies are blind to, or an artifact of one taxonomy's
  commercial model. Both are findings; guessing which is not.
- `DEFINITIONAL-SPLIT` — sources carve the boundary differently; see
  `conflict_ids`.

**`row_confidence` takes the weakest grade, always.** This is the mechanism that
kills P3. A row where three sources are `PRIMARY` and one is `MODELED` is a
`MODELED` row, and it must *look* like one to a reader skimming the table.

---

## 3. Table B — vendor cross-listing (secondary)

One row per (vendor × `normalized_name`). Shows which vendors each taxonomy
sees, and therefore which vendors each taxonomy structurally cannot see.

| Column | Notes |
|---|---|
| `vendor_name` | Legal or trading name, verbatim from source; variants in `vendor_aliases`. |
| `vendor_aliases` | All observed spellings, incl. local-language. |
| `normalized_name` / `registry_id` | |
| `listed_in` | Set: `g2` / `cb` / `gartner` / `<marketplace>`. |
| `hq_country` | With grade. |
| `founded` | With grade. |
| `status` | `ACTIVE` / `ACQUIRED` / `SHUT-DOWN` / `DORMANT` / `UNKNOWN`, with grade. |
| `primary_lang_of_web_presence` | The P5 detector. |
| `source_urls` | One per listing, with rung and grade each. |
| `row_confidence` | Weakest grade among populated cells. |

Vendors appearing in exactly one source get the same scrutiny as `SOLE-SOURCE`
categories, for the same reason.

---

## 4. Table C — method coverage (`outputs/coverage-report.md`)

Not a nice-to-have. This table is what stops the merged table from being read as
the market rather than as four catalogues of it.

| Column | Notes |
|---|---|
| `dimension` | e.g. non-anglophone vendors, bootstrapped vendors, on-prem incumbents, services substitutes, in-house builds, dead companies. |
| `covered_by` | Which sources, if any, can see it at all. |
| `structural_blindness` | Why the others cannot — mechanism, not vibes. |
| `evidence` | URL for the mechanism claim (e.g. published inclusion criteria, listing fees). |
| `mitigation_run` | What this phase actually did about it. |
| `residual_risk` | What a reader must not conclude from the merged table. |

---

## 5. Merge rules

1. Merge on `normalized_name` only. Never on `raw_name`, never on fuzzy string
   match, never on "obviously the same thing".
2. A source absent from a category is `— [UNKNOWN]`, never blank and never `0`.
   **Absent ≠ zero.** That single substitution is how a taxonomy's blind spot
   becomes a finding about the market.
3. No cell in the merged table may carry a grade higher than the pass file it
   came from. The merge is a copy operation on grades, not a judgement.
4. Conflicts stay conflicts here too. If G2 and Gartner give different vendor
   counts for the same normalized category, both counts appear, both cited.
5. Re-running a source pass appends a new dated version of Table A. Old versions
   are kept. The delta between them is itself a result.
