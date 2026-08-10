# evidence/fetch-log.md

Every URL touched by every pass. Including failures. Including duplicates.
Including the ones that turned out to be useless.

This log is how P3 (uneven depth) and P6 (silent downgrade) are audited. **A
thin log means a thin pass**, regardless of how the output table looks.

Append-only. Newest at the bottom.

`outcome` ∈ `OK` | `BLOCKED-403` | `PAYWALL` | `404` | `ROBOTS` | `TIMEOUT` |
`EMPTY` | `ARCHIVE-MISS`

An `R3` row with no preceding `R1` **and** `R2` attempt for the same URL is a
protocol breach: the row it produced is discarded and refetched.

| ts | pass_id | url | rung_attempted | http_status | outcome | archive_url | snapshot_date | raw_file |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |
