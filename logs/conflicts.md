# conflicts.md

**When two sources disagree, record BOTH and flag it. Never silently pick one.**

A conflict is not a data-quality problem to be cleaned. It is usually the most informative
thing on the page: two taxonomies disagreeing about a vendor tells you where the category
boundary actually is, and a vendor's domestic and English sites disagreeing tells you how it
presents itself to two different audiences.

Append-only. Governed by `research-protocol.md` §7.

## Columns

| Field | Meaning |
|---|---|
| `conflict_id` | `C-0001`, sequential. Merged rows cite this |
| `date` | ISO date recorded |
| `subject` | Vendor, product, or category the conflict is about |
| `dimension` | What they disagree on: `count` / `price` / `category-placement` / `ownership` / `status` / `product-depth` / `customer-list` / `market-definition` / other |
| `value_a` | Side A's value, verbatim |
| `source_a` | URL + `paste_id` |
| `class_a` | `SELF-DECLARED` / `REVEALED-BEHAVIOR` |
| `grade_a` | Confidence grade of side A |
| `lang_a` | ISO language code |
| `value_b` | Side B's value, verbatim |
| `source_b` | URL + `paste_id` |
| `class_b` | `SELF-DECLARED` / `REVEALED-BEHAVIOR` |
| `grade_b` | Confidence grade of side B |
| `lang_b` | ISO language code |
| `resolution` | `UNRESOLVED — both carried` (default) / `judgment: <which side, why>` / `resolved by <new source>` |
| `effect_on_grade` | Grade the merged row carries as a result |

## Rules

- **Default resolution is `UNRESOLVED — both carried`.** Resolving is the exception and
  requires a stated reason.
- **A conflict resolved by judgment never raises the merged row's grade.** If judgment
  picked a side, the row says judgment picked, and why. Judgment is not a source.
- **Domestic-language vs. English disagreement on the same vendor** — pricing, product
  depth, customer lists — is logged here, not reconciled. Per `CLAUDE.md` §6 the
  domestic-language version is primary and the English version is marketing collateral, but
  both values stay in the row.
- **Two SELF-DECLARED sources agreeing is not corroboration** (`research-protocol.md` §5) —
  and by the same logic, two SELF-DECLARED sources *disagreeing* is a strong signal, because
  their errors are supposed to correlate. Flag those explicitly in `resolution`.
- A conflict about a **category's market definition or inclusion criteria** is logged here
  *and* reflected in `industry-registry.md`, which keeps both raw names rather than merging
  them into one normalized entry.

## Log

| conflict_id | date | subject | dimension | value_a | source_a | class_a | grade_a | lang_a | value_b | source_b | class_b | grade_b | lang_b | resolution | effect_on_grade |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| _(empty — no research has been conducted)_ | | | | | | | | | | | | | | | |
