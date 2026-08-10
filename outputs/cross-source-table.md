# outputs/cross-source-table.md

**The deliverable.** Everything else in this repo is scaffolding for this file.

Schema: `schemas/merged-table.md`. Merge key: `normalized_name` from
`industry-registry.md`. Nothing is written here that is not already written in a
pass file with the same grade — the merge is a copy operation, never a
judgement (`CLAUDE.md`, grade-never-rises).

Ships with `coverage-report.md`. Not before it, not without it.

---

## Status

**Not started.** No research pass has run. The registry is empty, so there is
nothing to merge on.

## Table A — cross-taxonomy category matrix

_Empty. Populated after ≥2 source passes; a "merge" of one source is that
source's taxonomy wearing a different filename, which is exactly P2._

## Table B — vendor cross-listing

_Empty._

## Reading rules for whoever gets this table

1. `row_confidence` is the **weakest** grade in the row, not the average and not
   the best. A row reading `MODELED` is a row you may not spend money on.
2. `— [UNKNOWN]` means a source does not list it. **It never means zero.**
3. `SOLE-SOURCE` rows are the most interesting in the table and the least
   settled: either a real market three taxonomies are blind to, or an artifact of
   one taxonomy's commercial model.
4. `failures_found: 0` without a linked search log means the failure sampling did
   not run. Treat that row as incomplete, not as a market where nobody died.
5. Version history is kept. The delta between reruns is itself a result.
