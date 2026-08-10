# research-protocol.md — the standing method

The method is fixed before the evidence arrives. That is the point of writing it down
first: a method invented while looking at results is a method fitted to the results.

Governed by `CLAUDE.md`. Output shapes in `schemas/`. Merge key in `industry-registry.md`.

---

## 1. Source ladder

**Strict order. Every fact records the rung that produced it.** A fact with no rung is not
a fact yet.

### Rung 1 — Direct fetch of the source of record
Fetch the page that *is* the authority for the claim. A G2 category page is the source of
record for what G2 puts in that category. A vendor's own pricing page is the source of
record for that vendor's list pricing. A news article about either is not.

### Rung 2 — Alternate paths on the same source
When Rung 1 is blocked, the source is often still reachable. Before giving up on it, try:
- **Different subdomains.** A research, methodology, docs, or developer subdomain is
  frequently open while the main site blocks.
- **Sitemaps** — `/sitemap.xml`, `/sitemap_index.xml`, and the child sitemaps they list.
- **RSS / Atom feeds.**
- **Public API endpoints** — anything the site's own front end calls without a key.
- **Equivalent pages under different URL patterns** — print views, AMP variants, localized
  paths (`/de/`, `/tr/`, `/ru/`, `/pt-br/`), legacy path structures.
- **Localized domains.** A `.com.tr`, `.ru`, `.cn`, `.com.br` property may be a different
  server with different rules — and per `CLAUDE.md` §6 the domestic-language version is the
  primary one anyway.

Rung 2 is still the source of record. It grades as PRIMARY. Log which alternate path
worked — it will work again next time.

### Rung 3 — HUMAN TRANSPORT — mandatory before Rung 4
When a page is blocked and its content is genuinely needed, **stop and ask the user to open
it and paste it.**

- **Do not skip the source silently.** Prohibition 6.
- **Do not substitute a search-engine summary for a page you were told to read.**
- A blocked page that matters is a *request*, not a dead end.

Not everything blocked is needed. Before asking, state to yourself what the page decides.
If the answer is "nothing," don't ask — log it as skipped-by-judgment in the fetch log with
the reason, so the skip is auditable.

### Rung 4 — Secondary sources, explicitly marked
Only after 1–3 fail or 3 is declined. A secondary source is anything reporting on the
source of record rather than being it. Max grade for a Rung-4 fact is **SINGLE-SOURCE**
(or CORROBORATED if a second, different-class source agrees). It can never be PRIMARY,
however authoritative the outlet sounds.

### Environment constraint
**`web.archive.org` is blocked at the Claude Code tool level** — an environment
restriction, not a site 403. Retrying it is wasted effort. **Design no fallback around it.**
Any method step whose recovery path is "check the Wayback Machine" is broken and must be
rewritten to escalate to Rung 3 instead.

---

## 2. Asking for a paste

Rung 3 costs the user's attention, which is the scarcest input to this study. Spend it
precisely.

**Every paste request must state, per URL:**
1. **The exact URL** — full, clickable, no "search for X".
2. **What to copy** — whole page, or a named section ("the table under *Products*", "the
   block beginning *To qualify for inclusion*"). Say which.
3. **Whether pagination is involved** — if the list is paginated, say how many pages to
   step through, or say explicitly that page 1 is enough for this purpose and why.
4. **What it decides** — one line on what this page resolves. If it decides nothing, don't
   ask for it.

**Batch requests.** A single message with 6 URLs, each with its instruction, beats six
messages. Never trickle requests one at a time.

**While waiting:** continue any work that does not depend on the blocked page. Do not
guess the page's contents as a placeholder. A placeholder written in the shape of a result
will be read as a result.

---

## 3. Grading pasted content

**Pasted content grades as PRIMARY.** It is the source of record; only the transport is
human. But two failure modes are introduced by human transport, and **both are recorded
every single time.**

### Failure mode A — pagination is invisible
A paste captures one screen. If a listing says *"Products 1–20 of 122"*, you have 20 of
122 and you know it. If it says nothing, you do not know what you have.

**Therefore, absence is typed. Never write bare "absent".**

| Absence type | Meaning | When to use |
|---|---|---|
| `ABSENT-ENUMERATED` | The full list was visible and the item is not in it | Total count seen and matched what was captured |
| `ABSENT-IN-VISIBLE-PAGE` | Not in the captured screen; more pages exist or may exist | Default whenever pagination is present or unknown |
| `NOT-CHECKED` | This source was never consulted for this item | Coverage gap, not evidence |

`ABSENT-IN-VISIBLE-PAGE` and `NOT-CHECKED` are **not** evidence of absence and must never be
summarized as "not present in the market." Every capture records `visible_count` and
`total_count` (or `total_count: UNKNOWN`) so this distinction survives into the merge.

### Failure mode B — human selection is sampling
Which pages the user pastes determines what this study can see. That is a sampling frame,
and an unlogged sampling frame is indistinguishable from a neutral one — which it is not.

**Every pasted page is logged in `logs/paste-log.md`:** URL, date received, what was
visible (`visible_count` / `total_count`), source language, sort order if the page showed
one, filters active if the page showed any, and the file in `sources/raw/` holding the
verbatim content.

The paste log is read as a sample description at write-up time. Any finding whose support
comes disproportionately from one requested page says so.

### Verbatim capture is mandatory
Pasted content goes into `sources/raw/` **unedited** — no summarizing, no reformatting, no
"cleaning". The parsed row is derived from it and points back to it. If the two ever
disagree, the raw file wins.

---

## 4. Confidence grades

Replaces any binary fact/assumption split. **Every table cell carrying a number carries its
grade. No exceptions.** Non-numeric claims carry one too wherever they are contestable.

| Grade | Definition | Hard rule |
|---|---|---|
| `PRIMARY` | From the source of record — fetched (Rung 1/2) or human-transported (Rung 3) | Transport being human does not reduce it |
| `CORROBORATED` | Two independent sources agree — **and they are of different source classes** | Two SELF-DECLARED sources agreeing is not this |
| `SINGLE-SOURCE` | One secondary source, unconfirmed | Rung 4's ceiling absent corroboration |
| `MODELED` | A third-party estimate | **Never called a fact.** Never averaged with a PRIMARY number |
| `UNKNOWN` | Not established | **Say this.** Never fill a gap with reasoning |

**UNKNOWN is a finding.** It is written into the cell, kept in the output, and counted in
coverage. It is never quietly dropped so a table looks complete, and it is never replaced by
an inference dressed as a range.

### Grades are read per cell. `row_grade` is advisory only.

**Every substantive claim is governed by the grade of the cell it comes from, not by the
grade of the row it sits in.**

`row_grade` remains the weakest grade among the row's populated cells (`merged-table.md` §4),
but it is **a flag meaning "this row contains something weak" — not the row's verdict.**

The reason is mechanical: with weakest-wins as the verdict, a single `UNKNOWN` cell — and
early rows will have several — drags every row to `UNKNOWN`. A signal that never varies stops
being a signal, and a grade everyone learns to ignore is worse than no grade, because it still
occupies the column where the real one should be.

So:
- **Cite the cell's grade** when making a claim from a cell. `product_count: 122 (PRIMARY)` is
  the claim, regardless of the row's `UNKNOWN` funding column.
- **Use `row_grade` to triage**, not to conclude — it tells you which rows have a hole in
  them, which is what it is good for.
- **Never use `row_grade` to suppress a well-graded cell.** A `PRIMARY` count inside an
  `UNKNOWN`-graded row is still `PRIMARY`.
- Reject condition 3 in `merged-table.md` §7 still stands: `row_grade` may never be *stronger*
  than the weakest contributing cell.

**No grade laundering.** A grade is never upgraded by restating the claim in a second file.
Every restatement carries the same grade plus a pointer to its origin row, and a derived
file may hold a grade only **equal to or weaker than** its source.

---

## 5. Source class — mandatory on every source

| Class | Definition |
|---|---|
| `SELF-DECLARED` | The entity appears because it **invested in appearing** — vendor site, directory listing, review-platform profile, marketplace listing, press release, sponsored placement |
| `REVEALED-BEHAVIOR` | The entity appears because **an action left a trace regardless of intent** — company/tax registries, procurement and tender records, court filings, job postings naming a stack, tech-stack detection, DNS/MX/CDN records, app-store install or review counts generated by users |

**The rule: two SELF-DECLARED sources agreeing is NOT corroboration. Their errors
correlate** — both reward marketing spend, both undercount vendors who never bothered to
list. **CORROBORATED requires two sources of different classes.**

This is the study's main defense against its own source set. Per `CLAUDE.md` §7, all three
planned sources are largely SELF-DECLARED and several are pay-to-play; cross-checking them
against each other cannot detect that bias, because it is their shared bias. Only a
REVEALED-BEHAVIOR source can.

**Consequence to accept, not engineer around:** most rows in the first passes will top out
at SINGLE-SOURCE or PRIMARY-but-uncorroborated. That is the honest state of the evidence.
Do not promote a row to CORROBORATED by finding a second directory that copied the first.

**Per-class ceiling reporting.** Every output states what share of its rows rests on
SELF-DECLARED sources alone. A pass at 100% is reported as such on its face.

---

## 6. Failure sampling — no winners-only output

Prohibition 4. **Any pass studying successful companies must also identify companies that
attempted the same thing and failed.** A winners-only output is **rejected and rerun** —
not annotated, rerun.

### Primary failure-detection mechanism: Gartner decline markers
Gartner marks decline explicitly. Nothing else in our source set can. **Extract all three
as first-class fields, never footnotes:**

| Marker | Applies to | Meaning | Why it matters |
|---|---|---|---|
| `(Legacy)` | A product name | Managed decline; ratings intact | A product still scoring well while being labelled legacy is a live warning that the ratings do not price in |
| `(Retired)` | A category name | **A market that failed or dissolved** | Stronger signal than any single dead company. Nothing else we have produces it |
| `(Transitioning to X)` | A category name | The taxonomy itself is moving | Tells you the category boundary is in motion — record source and target names both |

A `(Retired)` category is retained in `industry-registry.md` with its retirement recorded.
**Deleting retired categories would rebuild survivorship bias inside the merge key itself.**

### Secondary failure signals — used, but graded honestly
Wherever encountered in-source, not hunted from memory: profiles removed between captures,
acquisition notices, listings marked discontinued/unsupported, marketplace apps delisted
between captures, categories whose product count drops sharply between captures.

**Capture-to-capture comparison requires two dated captures of the same URL in
`sources/raw/`.** Without both, "it disappeared" is UNKNOWN, not a finding — an absent row
may be pagination (§3A), not death.

### Failure-coverage statement
Every pass output ends with a failure-coverage statement: how many declining/failed entities
were identified, by what mechanism, and — where a class could not be checked for failure at
all — which class and why. "No failures found" is only acceptable alongside a description of
the mechanism that looked for them.

---

## 7. Conflicts

**When two sources disagree, record BOTH and flag it. Never silently pick one.**

- The row keeps both values, each with its own grade, class, rung, URL, and language.
- The disagreement is logged in `logs/conflicts.md` with both sides and the specific
  dimension of disagreement (count, price, category placement, ownership, status).
- The merged row's grade is **not** upgraded by a conflict being resolved through judgment.
  If judgment picked, the row says judgment picked, and why.
- **Domestic-vs-English disagreement on the same vendor** (pricing, product depth, customer
  lists) is logged as a conflict, not reconciled. It is a finding about how the vendor
  presents itself to two audiences.

Taxonomy boundary disagreements are logged the same way — see `CLAUDE.md` §1. Two sources
disagreeing about whether a vendor belongs in a category is information about the category,
not noise to be cleaned.

---

## 8. Category inclusion criteria — recorded per category

Categories differ enormously in how hard they are to enter. **Raw counts across categories
are therefore not comparable and must never be presented as if they were.**

For every category captured, record **that source's own inclusion criteria or
mandatory-feature list, verbatim** — G2's "To qualify for inclusion in the X category, a
product must:" block, Gartner's market definition, a marketplace's listing requirements.

Where criteria are not published, record `inclusion_criteria: UNKNOWN` and treat that
category's count as **non-comparable to any other**, including to itself over time.

---

## 9. Fetch logging

**Every fetch attempt is logged in `logs/fetch-log.md` as it happens**, including failures.
Retroactive logging is reconstruction, and reconstruction is exactly the thing this study
does not accept from anyone else.

Recorded per attempt: date, URL, rung attempted, outcome (`ok` / `403` / `404` / `timeout`
/ `blocked-by-environment` / `partial`), what was obtained, the `sources/raw/` file, and —
when escalating — the rung escalated to and why.

**A blocked source is a logged event with a next action, never a silent omission.**

---

## 10. Pass discipline

Every research pass, before it starts, writes down: its question, its source of record, its
target schema, and what would make it fail. Every pass, when it ends, produces:

1. Raw captures in `sources/raw/`, verbatim.
2. Parsed rows conforming to the pass's schema in `schemas/`.
3. New `industry-registry.md` entries for every unmatched category — **appended with alias
   lists, never force-matched to a near-neighbor.**
4. Log entries: fetch, paste, boundary rulings, conflicts.
5. A **coverage statement**: what was checked, what was `ABSENT-IN-VISIBLE-PAGE`, what was
   `NOT-CHECKED`, which competitor classes were unmeasurable and what source class would be
   needed, which languages were covered, and what share of rows rests on SELF-DECLARED
   sources alone.
6. A **failure-coverage statement** (§6).

A pass missing 5 or 6 is not finished, regardless of how good its table looks.
