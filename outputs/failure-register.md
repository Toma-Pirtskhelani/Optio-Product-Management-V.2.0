# outputs/failure-register.md

Companies that attempted the same thing and did not survive.

Required by P4. A pass that studies successful companies without producing rows
here — or an attached search log proving a good-faith search found none — is
rejected and rerun.

`outcome` ∈ `SHUT-DOWN` | `ACQUIHIRED` | `ACQUIRED-DISTRESSED` | `PIVOTED-AWAY` |
`DORMANT` | `INSOLVENT`

Coding rules:

- **A healthy acquisition is not a failure.** Do not pad this register with good
  exits; it destroys the register's only use.
- **Being too small for an analyst report is not a failure.** That belongs in
  `coverage-report.md`.
- **Leaving a marketplace is not a failure** until resolved at R1 against the
  vendor's own domain.
- Ambiguous outcomes are `UNKNOWN`, not guesses. An inflated failure count is the
  same class of error as V1's zero.

| company | normalized_name | what they attempted | outcome | outcome_date | evidence_url | rung | grade | how_found | notes |
|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | |

## Zero-result search logs

When a category genuinely yields no failures, the queries and archive diffs that
established it go here, verbatim, with dates. "I found no failures" is only a
result with this log attached.
