# passes/ — per-pass working outputs

One directory per research pass: `passes/<NN>-<slug>/`.

A pass is a unit of work with a question, a source of record, a target schema, and a stated
failure condition — declared **before** it runs. A pass whose question was written after its
results arrived is a pass fitted to its results.

## Required contents of every pass directory

| File | Contents |
|---|---|
| `00-plan.md` | The question, the source of record, the target schema, what would make this pass fail, and which paste requests it expects to need |
| `rows.md` | Parsed rows conforming to the pass's schema in `schemas/` |
| `coverage.md` | The coverage statement (below) |
| `failures.md` | The failure-coverage statement (below) |

Raw captures do **not** live here — they live in `sources/raw/`, cited by filename.

## Coverage statement — required, no pass is finished without it

1. What was checked — sources, URLs, dates.
2. What was `ABSENT-IN-VISIBLE-PAGE` vs `ABSENT-ENUMERATED` vs `NOT-CHECKED`, with counts.
3. Which competitor classes (1–7) were unmeasurable here, and **which source class would be
   needed to measure each** — an unmeasured class is a stated hole, never an implied zero.
4. Which languages were covered, which required languages were not, and what was attempted.
5. What share of rows rests on `SELF-DECLARED` sources alone.
6. `NOT-CHECKED` rate for the pass as a whole.

## Failure-coverage statement — required

1. How many declining or failed entities were identified, and by what mechanism.
2. Which decline markers were available in this source and which were extracted.
3. Where failure could not be checked at all — which class, and why.

**"No failures found" is only acceptable alongside a description of the mechanism that looked
for them.** A winners-only output is rejected and rerun, not annotated
(`research-protocol.md` §6).

## Pass hygiene

- Every new category with no registry match is **appended** to `industry-registry.md` with its
  alias list — never force-matched.
- Every fetch, paste, boundary ruling, and conflict is logged in `logs/` **as it happens**.
- Every pass is committed when it completes. A pass left uncommitted did not happen.
