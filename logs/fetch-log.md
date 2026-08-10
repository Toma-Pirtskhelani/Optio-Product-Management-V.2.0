# fetch-log.md

Every fetch attempt, **logged as it happens** — including failures, including refusals to
try. Retroactive logging is reconstruction, and reconstruction is what this study refuses to
accept from anyone else.

Append-only. Never edit a past row; add a new one and reference it.

Governed by `research-protocol.md` §1 and §9.

## Columns

| Field | Meaning |
|---|---|
| `date` | ISO date of the attempt (YYYY-MM-DD) |
| `url` | Full URL attempted |
| `source` | Source of record this belongs to (e.g. `g2`, `gartner`, marketplace name) |
| `rung` | Ladder rung attempted: `1` / `2` / `3` / `4` |
| `outcome` | `ok` / `403` / `404` / `timeout` / `blocked-by-environment` / `partial` / `skipped-by-judgment` / `paste-requested` / `paste-received` |
| `obtained` | What content was actually obtained — or the reason for skipping |
| `raw_file` | Path under `sources/raw/`, or `—` |
| `escalated_to` | Rung escalated to, and why. `—` if none needed |
| `source_language` | ISO code of the page's language (`en`, `ru`, `tr`, `zh`, `es`, `pt`, `ka`, …). **Mandatory on every row, including failures** |

## Measuring the language bias instead of suffering it

Rung 3 makes the user the throughput limit of this study, and **blocking is not
language-neutral**: non-English sources are more likely to block, to lack alternate paths, and
to be expensive to request. The language obligation (`CLAUDE.md` §6) therefore fails hardest
exactly where it matters most — and, unmeasured, it fails *looking like diligence*.

That constraint cannot be removed. It can be made visible with a number attached.

**`source_language` is recorded on every attempt, including every failure**, so the block rate
can be computed per language. Every pass reports:

> Attempts by language: `en` N (M blocked, X%) · `ru` N (M blocked, X%) · …

**If non-English sources block at several times the English rate, that is a measured bias, not
a silent one.** It is reported as a finding about the method, and any conclusion about
non-Anglophone market coverage carries the block rate beside it.

`skipped-by-judgment` rows count toward the denominator too. A source skipped because
requesting it was expensive is still a source this study did not see.

## Rules

- `skipped-by-judgment` **requires** a stated reason in `obtained` describing what the page
  would have decided and why that decision does not matter here. A skip with no reason is a
  silent omission — prohibition 6.
- A `403` or `blocked-by-environment` row **must** have a non-`—` `escalated_to`, or a
  `skipped-by-judgment` row immediately following it. A block with neither is an
  unfinished action, not a finished attempt.
- `web.archive.org` is `blocked-by-environment` at the tool level. Do not attempt it and do
  not design fallbacks around it.

## Log

| date | url | source | rung | outcome | obtained | raw_file | escalated_to | source_language |
|---|---|---|---|---|---|---|---|---|
| _(empty — no research has been conducted)_ | | | | | | | | |
