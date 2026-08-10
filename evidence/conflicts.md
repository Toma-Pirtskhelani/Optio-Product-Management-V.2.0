# evidence/conflicts.md

Source disagreements. Left unresolved on purpose.

When two sources disagree, both claims are recorded with their own URL, rung, and
grade. Never pick one. Never average. Never quietly prefer the higher rung
without saying so. If a conflict blocks a decision, it goes to the user **as a
conflict**, not as a resolved answer with a caveat.

`status` ∈
- `OPEN` — unresolved.
- `RESOLVED-BY-PRIMARY` — a new R1 fetch settled it. Requires its fetch-log row.
  Both original claims stay visible.
- `IRRECONCILABLE` — both stand, no primary source exists to settle it.
- `DEFINITIONAL` — the sources are measuring different things. **Usually the most
  valuable kind**, and the one V1 destroyed by picking a winner.

| conflict_id | subject | claim_a | src_a | rung_a | grade_a | claim_b | src_b | rung_b | grade_b | status | why_it_matters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | | |
