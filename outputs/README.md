# outputs/ — merged tables and findings

Everything here is **derived**. Nothing is entered directly. Every value traces to a row in
`passes/`, which traces to a capture in `sources/raw/`, which carries its URL and date.

## The rule that governs this directory

**A claim's confidence grade is never upgraded by restating it in a second file.**

Every number here carries the same grade it had in its origin row, plus a pointer to that row.
A derived file may hold a grade **equal to or weaker than** its source — never stronger. If a
summary shows a number more confidently than the table it came from, **the summary is wrong**;
fix the summary, not the table.

This is the failure mode that makes bad studies persuasive: a number becomes a fact by being
repeated. It does not get to happen here.

## Required on every merged output

| Element | Requirement |
|---|---|
| Coverage matrix | Per `schemas/merged-table.md` §3. Not an appendix |
| `NOT-CHECKED` rate | Stated on the face of the table |
| Self-declared share | What share of rows rests on `SELF-DECLARED` sources alone |
| Corroboration share | Share with `corroborated: yes` — which requires two **different** source classes |
| Boundary-ruling count | How many rows are `BOUNDARY-IN`/`BOUNDARY-OUT`, so the count's sensitivity to the definition is visible |
| Competitor-class coverage | Which of classes 1–7 appear, which are `NOT-CHECKED`, and what source class would be needed |
| Language coverage | Row counts by `source_language`, and which required languages are missing |
| Failure coverage | Decline markers found; or the mechanism that looked and found none |
| Taxonomy separation | No count compared across `taxonomy_id` values |

## Presentation rules

- **`ABSENT-IN-VISIBLE-PAGE` and `NOT-CHECKED` are never rendered as zero.** Not in a table,
  not in a chart, not in a sentence. A chart that does this is rejected.
- **`UNKNOWN` stays visible.** It is a finding. It is never dropped to make a table look
  complete, and never replaced with an inferred range.
- **`MODELED` is never called a fact** and is never averaged with a `PRIMARY` number.
- **Funding, amount raised, and investor data are `UNKNOWN`** and stay that way. Capital
  efficiency is unanswerable from our sources (`CLAUDE.md` §7.1).
- **Category counts are not comparable across taxonomies.** The category cluster is the unit
  of analysis.

## Blinding

Every output is written blind. No finding is shaped by, ordered by, or filtered for relevance
to the commissioning company. **An industry that turns out to be enormous and unservable by
the client is a finding of the highest value** — outputs must be capable of producing it, and
any structure that would suppress it is wrong.

Unblinding happens only on the user's explicit instruction, after the research passes are
complete and committed.
