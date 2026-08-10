# schemas/crunchbase.md — funding-database taxonomy pass

**Governs:** `passes/crunchbase/<pass_id>.md`
**Merges into:** `schemas/merged-table.md` Table A (categories) and Table B
(vendors), on `normalized_name`.

This is the only one of the four sources that **retains the dead**. That makes it
the backbone of P4 failure sampling — and it also makes it the source most likely
to be over-trusted, because it looks like a database of companies when it is a
database of *fundraising events*. Companies that never raised are largely absent
by construction. Say so in every output that leans on it.

Column availability is an assumption until the first fetch. Fields behind the
paywall are `UNKNOWN` **and** logged as blocked — never substituted with an
estimate from another vendor.

---

## 1. Spine

Every row carries the spine from `schemas/merged-table.md` § 1.

## 2. Enumeration rule

Categories come from Crunchbase's own published category / category-group
listing, fetched at R1, with the stated organisation count recorded. Never from
recall (P1).

Access reality, handled explicitly, not silently (P6): much of Crunchbase is
gated. Attempt R1. On paywall → log `PAYWALL`, attempt R2 via
`web.archive.org` (record `snapshot_date`; apply the 24-month volatility rule in
`research-protocol.md` § 2). Only then R3, permanently marked. **Never** paper
over a gated field with a Growjo/Latka/ZoomInfo number and let it inherit the
row's grade — that number is `MODELED` in its own cell and does not touch the
neighbours.

## 3. Table A — categories

| Column | Definition |
|---|---|
| *spine* | § 1 |
| `category_group` | Crunchbase's parent grouping, verbatim. |
| `stated_definition` | Verbatim if published; else `UNKNOWN`. |
| `org_count_total` | Organisations in category, with grade. |
| `org_count_active` | With grade. |
| `org_count_closed` | With grade. **Directly feeds P4** — the ratio is a category-level survival signal available nowhere else in this source set. |
| `org_count_acquired` | With grade. |
| `top_hq_countries` | Distribution if published, with grade. Reveals this source's geographic skew as data, not as opinion. |
| `filter_url` | The exact query/filter URL used, so the count is reproducible. |

## 4. Table B — vendors

| Column | Definition |
|---|---|
| *spine* | § 1 |
| `vendor_name` / `vendor_aliases` | Verbatim; include former names. |
| `cb_permalink` | Stable identifier. |
| `vendor_own_site` | Fetched separately at R1. |
| `founded_year` | With grade. |
| `hq_country` / `hq_city` | With grade. |
| `operating_status` | Verbatim value (`Active` / `Closed` / …), with grade. |
| `status_normalized` | `ACTIVE` / `SHUT-DOWN` / `ACQUIRED` / `ACQUIRED-DISTRESSED` / `DORMANT` / `UNKNOWN`. |
| `closed_on` / `acquired_on` | Date + acquirer, with grade. |
| `last_funding_type` / `last_funding_date` / `last_funding_amount` | Each with grade and currency. |
| `total_raised` | With grade and currency. |
| `employee_range` | Crunchbase's banded estimate — **`MODELED`, always**. |
| `cb_categories_raw` | All category tags, verbatim, pipe-separated. |
| `primary_lang_of_web_presence` | From the vendor's own site, not from Crunchbase. |

Rung discipline: a Crunchbase profile is R1 for *"Crunchbase records X"* and R3
for the underlying fact. Funding amounts sourced to a company press release are
`PRIMARY` **only** when that release is fetched directly; sourced to Crunchbase
alone they are `SINGLE-SOURCE`. Two outlets reprinting the same release is one
source (`CLAUDE.md`, grade-never-rises).

## 5. Failure sampling (P4) — mechanisms for this source

This source carries the workload for the whole study. Minimum, per category:

1. Filter on closed / inactive operating status; capture **every** result, not a
   sample. Record the filter URL.
2. Filter on acquisitions and separate healthy exits from distressed ones —
   acquisition price relative to total raised, acquihire language in the
   announcement, team-only asset purchases. Where it cannot be determined, say
   `UNKNOWN`; do not code an ambiguous exit as a failure to inflate the count.
3. Capture companies whose last funding is >48 months old and that are still
   listed active: candidate `DORMANT`. Resolve at R1 against their own site
   before coding.
4. Every result lands in `outputs/failure-register.md` with `how_found`.

**Known limit, stated in every output using it:** companies that never raised
outside capital are largely invisible here, so this source undercounts both the
survivors and the dead in bootstrapped segments. That is a `coverage-report.md`
row, not a footnote.

## 6. Language protocol (P5)

`hq_country` distribution is the cheapest available test of this source's
geographic skew — capture it and report it. For any non-anglophone market in
scope, cross-check the local company registry directly at R1; Crunchbase's
coverage of non-US registrations is not assumed either way, it is measured and
reported.

## 7. Rejection

Standard checklist, `research-protocol.md` § 7, plus:

- [ ] Every count has its reproducible `filter_url`.
- [ ] Closed/acquired/dormant sampling ran on **every** category in scope.
- [ ] No paywalled field silently replaced by a third-party estimate.
- [ ] `employee_range` and any revenue estimate graded `MODELED`.
- [ ] The never-raised blind spot is stated in the pass file, not just here.
