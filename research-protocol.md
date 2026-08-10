# research-protocol.md — the standing method

Binding on every research pass in this repo. Read before starting one.
`CLAUDE.md` says what you must not do; this file says how the work is actually
performed.

---

## 1. The source ladder

Three rungs, attempted in strict order. **You may not start on a lower rung.**
Every recorded fact carries the rung that produced it.

| Rung | What it is | When you may use it |
|---|---|---|
| **R1** | Primary source fetched directly — the company's own site, an SEC/Companies House/registrar filing, a regulator, the analyst firm's own page, the marketplace listing itself. | Always try first. |
| **R2** | The same primary source retrieved via `web.archive.org`. | Only after R1 returned 403 / paywall / robots block / 404, and that response is logged. |
| **R3** | A secondary source — press coverage, an aggregator, a search-engine summary, a third-party database. | Only after **both** R1 and R2 have been attempted and logged as failed. |

Rules:

- **R3 requires two logged failures above it.** An R3 row whose `fetch-log`
  shows no R1 attempt is a protocol breach; the row is discarded and refetched.
- An R3 claim is marked secondary **permanently**. A later successful R1 fetch
  does not edit the old row — it adds a new row and supersedes it, and both stay
  visible.
- Snippets returned by a search engine are R3 evidence *about* a page, never
  evidence *from* it. If you have not fetched the page, you have not read it.
- Save every fetched page to `evidence/raw/` with the filename pattern
  `<pass_id>__<slug>__<retrieved_at>.<ext>`. A URL that 404s next month must not
  take the evidence with it.

### The fetch log is not optional

Every URL you touch gets a row in `evidence/fetch-log.md`, including failures,
including duplicates, including the ones that turned out to be useless.

```
| ts | pass_id | url | rung_attempted | http_status | outcome | archive_url | snapshot_date | raw_file |
```

`outcome` ∈ `OK` | `BLOCKED-403` | `PAYWALL` | `404` | `ROBOTS` | `TIMEOUT` |
`EMPTY` | `ARCHIVE-MISS`.

The log is how P3 and P6 are audited. If the log is thin, the pass is thin.

---

## 2. Confidence grades

This replaces any binary fact/assumption split. Ordered strongest to weakest.

| Grade | Definition | Test it must pass |
|---|---|---|
| **PRIMARY** | Fetched from the source of record via R1 or R2. | The organisation that owns the number published it. |
| **CORROBORATED** | Two **independent** secondary sources in agreement. | Would they still agree if one had never been published? If no — it's one source. |
| **SINGLE-SOURCE** | One secondary source, unconfirmed. | Someone reported it. Nobody checked it. |
| **MODELED** | A third-party estimate — Latka, Growjo, ZoomInfo, Owler, PitchBook ranges, "estimated revenue" widgets. | **Not a fact.** It is a vendor's algorithm guessing at a private number. |
| **UNKNOWN** | Nobody has established it. | Say this. Never fill the gap with reasoning. |

Hard rules:

- **Rung ≠ grade.** The rung is *how you got it*. The grade is *what it is
  worth*. R1 on a competitor's marketing page is `PRIMARY` for "they claim X",
  not for "X is true" — record the claim, not the implication.
- **R2 dating rule.** An archive snapshot is `PRIMARY` for stable facts
  (founding year, HQ country, incorporation) but drops to `SINGLE-SOURCE` for
  volatile facts (pricing, headcount, customer counts, feature sets) when the
  snapshot is **older than 24 months**. Always record `snapshot_date` alongside.
- **MODELED never combines upward.** Three estimate vendors agreeing is still
  `MODELED`; they scrape overlapping inputs. This is the single most common way
  a fake number gets promoted to a real one.
- **Every table cell carrying a number carries its grade.** No exceptions, no
  "grade applies to the whole table" shortcuts, no footnote-instead-of-column.
  Inline form: `142 [PRIMARY]`, `~$4.2M [MODELED]`, `— [UNKNOWN]`.
- **Numbers carry as-of dates, currency, and unit** or they are `UNKNOWN`.
  "500 customers" with no date is not a fact, it is a rumour with a number in it.

---

## 3. Failure sampling (P4)

**Any pass that studies successful companies must also identify companies that
attempted the same thing and failed.** A winners-only output is rejected and
rerun — not annotated, rerun.

Minimum bar per pass: a good-faith, *logged* search for the dead, using the
mechanisms in that pass's schema file (each schema names its own — e.g.
Crunchbase status filters, archived category pages, vendors dropped from a prior
year's analyst report, delisted marketplace apps).

Record every attempted-and-failed company in `outputs/failure-register.md`:

```
| company | normalized_name | what they attempted | outcome | outcome_date | evidence_url | rung | grade | how_found |
```

`outcome` ∈ `SHUT-DOWN` | `ACQUIHIRED` | `ACQUIRED-DISTRESSED` | `PIVOTED-AWAY` |
`DORMANT` | `INSOLVENT`. Distinguish these — a healthy acquisition is not a
failure and must not be counted as one.

If a genuine, logged search finds no failures in a category, that is itself a
finding: write it down with the queries you ran. **"I found no failures" is only
acceptable with the search log attached.** Absent that log, the pass is
incomplete.

Why this is non-negotiable: a category where twenty companies died is a
different business proposition from one where none did, even when the survivor
lists look identical. V1 could not tell those two markets apart.

---

## 4. Conflicts

When two sources disagree — on a number, a category boundary, a founding date, a
vendor's presence in a market:

1. Record **both**, each with its own URL, rung, and grade.
2. Add a row to `evidence/conflicts.md`.
3. Do **not** pick one. Do **not** average. Do **not** quietly prefer the
   higher-rung source without saying so.
4. If the conflict blocks a decision, escalate it to the user as a conflict, not
   as a resolved answer with a caveat.

```
| conflict_id | subject | claim_a | src_a | grade_a | claim_b | src_b | grade_b | status | why_it_matters |
```

`status` ∈ `OPEN` | `RESOLVED-BY-PRIMARY` (only when a new R1 fetch settles it,
with its log row) | `IRRECONCILABLE` | `DEFINITIONAL` (the sources are measuring
different things — usually the most valuable kind).

---

## 5. Language protocol (P5)

For any market outside the anglophone world:

- Run queries in the market's dominant business language(s), not just English.
- Record the **exact query strings**, in-language, in the pass file.
- Fetch and cite the local-language source directly. Do not cite an English
  article *about* a local-language source when the source itself is fetchable —
  that is an R3 masquerading as an R1.
- Record `source_lang` on every row. A market whose rows are 100% `en` has not
  been researched; it has been googled.
- Local company registries, local review sites, and local marketplace storefronts
  outrank global aggregators for local presence. Prefer them.

---

## 6. Pass lifecycle

1. **Declare.** State the `pass_id` (`<SOURCE>-<YYYY-MM-DD>-<nn>`), the
   governing schema in `schemas/`, the scope, and the stop condition.
2. **Enumerate.** Pull the source's own list. Never your memory's list (P1).
   Record the enumeration URL and the count the source itself states.
3. **Capture.** One row per item, spine columns filled, per the schema.
4. **Normalize.** Map each `raw_name` through `industry-registry.md`. No match →
   append a new registry entry (P2 protects you here; a forced match destroys the
   evidence).
5. **Sample failures.** § 3. Not optional, not deferrable to a later pass.
6. **Self-reject.** Run the checklist in § 7 against your own output.
7. **Write.** `passes/<source>/<pass_id>.md`, plus fetch-log, conflict, and
   registry appends.

Every pass file opens with a header block:

```
pass_id:        G2-2026-08-09-01
schema:         schemas/g2.md
scope:          <what was and was not covered>
enumeration_url:<where the list came from>
stated_count:   <count the source itself claims> [grade]
captured_count: <rows actually captured>
languages:      <codes>
queries:        <every query string run, verbatim>
failures_found: <n>  (0 requires the search log below)
started / completed: <ts>
```

---

## 7. Rejection checklist

Run this on your own output before writing it. Any `NO` rejects the pass.

- [ ] Every numeric cell has a grade.
- [ ] Every row has its own URL, not a pass-level one.
- [ ] Every row has a rung, and every R3 has two logged failures above it.
- [ ] Every blocked fetch shows a logged `web.archive.org` attempt.
- [ ] Failure sampling ran, with results or an attached search log.
- [ ] Conflicts are recorded as conflicts, not silently resolved.
- [ ] Non-anglophone scope has non-English queries logged.
- [ ] No `raw_name` was edited to fit the registry.
- [ ] `captured_count` vs `stated_count` gap is explained, not ignored.
- [ ] No grade in this file is higher than the grade in the file it came from.
- [ ] Nothing in the output came from model memory. Anything that did is deleted
      or refetched.

## 8. What "done" is not

Not: a table that looks complete. Not: coverage of the companies that were easy
to fetch. Not: a confident narrative.

Done is a table where a reader can see, per row, exactly how much to trust it —
and where the rows nobody could verify say `UNKNOWN` in plain sight.
