# schemas/merged-table.md — the merge target

**Designed first. The three source schemas are designed backward from this one.** A source
schema that cannot populate the spine is a schema that produces rows which cannot be merged,
and rows that cannot be merged get summarized instead — which is how the previous attempt
lost the distinction between a company it studied properly and a company it searched twice.

Governed by `CLAUDE.md` and `research-protocol.md`. Merge key defined in
`industry-registry.md`.

---

## 1. The unit of a row

**One row = one entity × one normalized category × one source.**

Source-level rows are the atoms and are never overwritten. The merged view is produced *from*
them, and every merged row carries pointers back to every atom that fed it. This is what
makes the weakest-grade rule (§4) checkable rather than asserted.

Per `CLAUDE.md` §7, the **category cluster is the unit of analysis** — a vendor occupying
nine categories in one taxonomy and two in another has told you about the taxonomies, not
about itself. Cluster fields are on the spine for exactly that reason.

---

## 2. The spine — every row carries all of it

Missing values are written `UNKNOWN`, never left blank. A blank is indistinguishable from a
value nobody looked for.

### Identity
| # | Field | Values / notes |
|---|---|---|
| 1 | `row_id` | `<source>-<NNNN>`, stable |
| 2 | `entity_name_raw` | **Verbatim as the source states it**, original language and casing |
| 3 | `entity_name_canonical` | This study's key for the entity. A decision, not evidence |
| 4 | `entity_aliases` | Every other observed spelling/name, with the source each came from |
| 5 | `entity_type` | `vendor` / `product` / `category` / `agency` / `integrator` / `module` / `substitute` / `in-house` / `status-quo` |
| 6 | ~~`competitor_class`~~ | **STRUCK from this phase.** Taxonomies only classify software, so classes 2–7 are not measurable here — and a column reading `NOT-CHECKED` on every row implies a gap was surveyed when it was not. See `CLAUDE.md` §4. Reinstated only when a `REVEALED-BEHAVIOR` pass exists to populate it |
| 7 | `origin_country` | Where the entity originates, per evidence. `UNKNOWN` is common and fine |
| 8 | `operating_geographies` | Only where a source states them. Never inferred from language or name |

### Category
| # | Field | Values / notes |
|---|---|---|
| 9 | `raw_name` | **Category name exactly as the source states it.** Evidence |
| 10 | `normalized_name` | Merge key from `industry-registry.md`. A decision |
| 11 | `registry_id` | `R-NNNN` |
| 12 | `taxonomy_id` | Which taxonomy this row's categories belong to. Counts never cross this |
| 13 | `category_cluster` | All normalized categories this entity occupies **within this taxonomy** |
| 14 | `cluster_size` | Count of #13. A property of the taxonomy, not of the entity |
| 15 | `inclusion_criteria_verbatim` | The source's own inclusion criteria / mandatory-feature list, quoted. `UNKNOWN` if unpublished |

### Scope
| # | Field | Values / notes |
|---|---|---|
| 16 | `scope_verdict` | `IN` / `OUT` / `BOUNDARY-IN` / `BOUNDARY-OUT` / `UNRULED` |
| 17 | `ruling_id` | `B-NNNN` in `logs/boundary-rulings.md`. Mandatory for any boundary verdict |
| 18 | `source_boundary_verbatim` | The source's own category boundary where it differs from ours. Never normalized away |

### Provenance — the part that cannot be skipped
| # | Field | Values / notes |
|---|---|---|
| 19 | `source` | `g2` / `gartner` / `<marketplace>` / other |
| 20 | `source_url` | **Per row.** Not per table, not per pass. The exact URL this row's values came from |
| 21 | `rung` | `1` / `2` / `3` / `4` — which ladder rung produced it |
| 22 | `source_class` | `SELF-DECLARED` / `REVEALED-BEHAVIOR`. Mandatory |
| 23 | `source_language` | ISO code. Mandatory |
| 24 | `capture_date` | ISO date the content was captured |
| 25 | `paste_id` | `P-NNNN` if human-transported, else `—` |
| 26 | `raw_file` | Path under `sources/raw/` holding the verbatim capture |

### Grading
| # | Field | Values / notes |
|---|---|---|
| 27 | `<field>_grade` | **Every cell carrying a number carries its own grade.** No exceptions. **These govern** — every substantive claim is read from the cell's grade |
| 28 | `row_grade` | Weakest grade among the row's populated cells (§4). **Advisory flag only** — "this row contains something weak," not the row's verdict |
| 29 | `corroborated` | `yes` / `no`. `yes` requires **two different source classes** (§5) |
| 30 | `corroborating_sources` | URLs + classes of the agreeing sources, or `—` |
| 31 | `conflict_ids` | `C-NNNN` list, or `—` |

### Status and decline
| # | Field | Values / notes |
|---|---|---|
| 32 | `decline_marker` | `none` / `legacy` / `retired` / `transitioning` (§6) |
| 33 | `decline_marker_verbatim` | The marker exactly as the source printed it, incl. the `X` in "Transitioning to X" |
| 34 | `entity_status` | `active` / `legacy` / `delisted` / `acquired` / `defunct` / `UNKNOWN` — **only where a source states or a two-capture comparison shows it** |

### Coverage
| # | Field | Values / notes |
|---|---|---|
| 35 | `presence` | `PRESENT` / `ABSENT-ENUMERATED` / `ABSENT-IN-VISIBLE-PAGE` / `NOT-CHECKED` (§3) |
| 36 | `visible_count` | Items visible in the capture this row came from |
| 37 | `total_count` | Total the source declared, or `UNKNOWN` |
| 38 | `sort_order` | Ranking the source displayed, or `UNKNOWN` |
| 39 | `promoted` | `yes` / `no` / `UNKNOWN` — sponsored or paid placement |

---

## 3. The coverage matrix

Produced alongside every merged table. **Not optional, not an appendix.**

One row per `entity_name_canonical` × `normalized_name`; one column per source; each cell one
of the four `presence` values.

| | g2 | gartner | marketplaces |
|---|---|---|---|
| `<entity> × <category>` | `PRESENT` | `ABSENT-IN-VISIBLE-PAGE` | `NOT-CHECKED` |

**The rules that make it worth producing:**

- **`ABSENT-IN-VISIBLE-PAGE` and `NOT-CHECKED` are never counted as absence.** They are
  never summarized as "not present in the market," and a chart that renders them as zero is
  rejected.
- **`ABSENT-ENUMERATED` requires a declared total that matched the captured count.** Without
  it, the value is `ABSENT-IN-VISIBLE-PAGE`. This is the pagination failure mode from
  `research-protocol.md` §3A, carried all the way into the output.
- Every merged table states its **`NOT-CHECKED` rate**. A table that is 60% unchecked is a
  coverage map, not a market map, and must present itself as one.
- **The coverage matrix covers software vendors only.** Competitor classes 2–7 are not rows
  here and are not columns here — they are outside what a taxonomy can describe
  (`CLAUDE.md` §4). Every table discussing competition carries the standing gap statement
  instead, in prose, where it cannot be mistaken for a measurement.

---

## 4. The weakest-grade rule

**A merged row inherits the WEAKEST grade among its inputs.**

Rank: `PRIMARY` 4 > `CORROBORATED` 3 > `SINGLE-SOURCE` 2 > `MODELED` 1 > `UNKNOWN` 0.
Merged grade = the **minimum rank** across the cells that fed it.

This is what makes prohibition 3 — uneven depth presented as even depth — **structurally
impossible rather than merely discouraged.** A company researched to primary-source depth and
a company with one secondary sighting cannot land in the same table looking equally solid,
because the merged row mechanically reports the weaker of what went into it. You cannot
average your way out and you cannot round up.

**`row_grade` is advisory. Per-cell grades govern.**

One `UNKNOWN` cell drags `row_grade` to `UNKNOWN`, and early rows will have several — so
`row_grade` would read `UNKNOWN` almost everywhere. A signal that never varies is not a
signal, and a grade everyone learns to ignore is worse than no grade because it occupies the
column where the real one should be.

So `row_grade` is **a flag meaning "this row contains something weak,"** used for triage. It
is **never** used to conclude, and **never** used to suppress a well-graded cell: a `PRIMARY`
product count inside an `UNKNOWN`-graded row is still `PRIMARY`, and is cited as `PRIMARY`.
Claims cite the cell.

**Consequences, all intended:**
- A merged **cell** is never stronger than its weakest input. Volume of weak evidence does not
  become strong evidence.
- The rule applies **across files.** A number restated in a summary carries the same grade and
  a pointer to its origin row; a derived file may hold a grade only equal to or weaker than
  its source. **No grade laundering** (`CLAUDE.md` §5).

**Design decision, stated because it is a real deviation and should be visible:** the grade
ladder ranks `PRIMARY` above `CORROBORATED`, so applying "weakest wins" naively would
*downgrade* two agreeing primary sources to `CORROBORATED` — punishing corroboration, which
is absurd. Therefore corroboration is carried as a **separate boolean** (spine #29) rather
than as a rung. A cell can be `PRIMARY` + `corroborated: yes`, which is the strongest state
this study can produce. The ladder is used for the weakest-wins minimum; the boolean is used
for the independence claim. They are different questions and are recorded separately.

---

## 5. Corroboration at merge time

**`corroborated: yes` requires two sources of DIFFERENT source classes.**

Two `SELF-DECLARED` sources agreeing is not corroboration — their errors correlate. Both
reward marketing spend; both undercount vendors who never bothered to list.

At merge time this bites hard and is supposed to: **G2, Gartner Peer Insights, and app
marketplace listings are all substantially `SELF-DECLARED`.** Three of them agreeing produces
`corroborated: no`. That is the correct answer, and it is the single most important thing
this schema does. Per `CLAUDE.md` §7 those sources cannot cross-check their own shared bias;
only a `REVEALED-BEHAVIOR` source can.

Every merged table therefore reports, on its face:
- share of rows resting on `SELF-DECLARED` sources alone;
- share with `corroborated: yes`;
- which `REVEALED-BEHAVIOR` sources, if any, were available.

---

## 6. Decline markers survive the merge

`decline_marker` and `decline_marker_verbatim` are **spine fields, not footnotes** — they
cannot be dropped when a merged view is generated.

| Marker | On | Meaning |
|---|---|---|
| `legacy` | Product name | Managed decline, ratings intact — a warning the ratings do not price in |
| `retired` | Category name | A market that failed or dissolved. Stronger than any single dead company |
| `transitioning` | Category name | The taxonomy itself is moving; record source **and** target names |

A merged table whose rows all show `decline_marker: none` must state **how many sources
capable of expressing a decline marker were consulted.** If the answer is zero, the table has
not looked for failure and is a winners-only output — **rejected and rerun**
(`research-protocol.md` §6).

---

## 7. Reject conditions

A merged table is **rejected**, not annotated, if any of these hold:

1. A numeric cell has no grade.
2. A row has no `source_url`, `rung`, `source_class`, or `source_language`.
3. `row_grade` is stronger than the weakest contributing cell.
4. `ABSENT-IN-VISIBLE-PAGE` or `NOT-CHECKED` is presented as absence.
5. A grade appears higher in a derived file than in its origin row.
6. `corroborated: yes` on two same-class sources.
7. No coverage matrix.
8. No failure-coverage statement, or a winners-only result with no mechanism described.
9. `normalized_name` was force-matched instead of appended to `industry-registry.md`.
10. Category counts compared across `taxonomy_id` values.
11. A row exists for a client-derived reason rather than an evidentiary one — **blinding
    breach**. Stop, report it, do not proceed.
