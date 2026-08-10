# boundary-rulings.md

Every IN / OUT / BOUNDARY ruling, with its reasoning, **logged before the row enters any
output**. Per `CLAUDE.md` §1: boundary cases are ruled individually and never silently
included or excluded as a class.

A ruling made in a chat message and not written here did not happen. Append-only — a
reversed ruling gets a new row citing the old `ruling_id`, and the old row stays.

## Columns

| Field | Meaning |
|---|---|
| `ruling_id` | `B-0001`, sequential |
| `date` | ISO date of the ruling |
| `subject` | Vendor, product, or category being ruled on |
| `subject_type` | `vendor` / `product` / `category` / `class` |
| `verdict` | `IN` / `OUT` / `BOUNDARY-IN` / `BOUNDARY-OUT` |
| `test_applied` | Which part of the functional definition decided it |
| `reasoning` | Why. Specific to this subject — not a restatement of the definition |
| `evidence` | Source URL(s) + `paste_id` the ruling rests on |
| `grade` | Confidence grade of the evidence the ruling rests on |
| `source_boundary_verbatim` | The source's own category boundary, quoted, where it differs from ours |
| `supersedes` | Prior `ruling_id` this reverses, or `—` |

## The test

**IN:** primary function is orchestrating outbound or triggered customer communication,
across one or more channels, driven by stored customer data or behavior — including
vertical-specific instances of that job under whatever local name.

**OUT:** pure analytics/BI (measurement without activation); pure sales-pipeline CRM (no
outbound orchestration); pure message-delivery infrastructure (transport without targeting
logic).

**The recurring four**, each ruled per instance and never as a class:
1. CRM suites carrying a campaign module
2. Delivery infrastructure moving up-stack into orchestration
3. Loyalty platforms with messaging attached
4. Customer data platforms sold with or without activation

## Rules

- **`BOUNDARY-IN` / `BOUNDARY-OUT` are distinct from `IN` / `OUT`.** They mark rows a
  reasonable analyst could rule the other way. Every output states how many of its rows are
  boundary rulings, so a count's sensitivity to the definition is visible rather than hidden
  inside it.
- A ruling made on `MODELED` or `UNKNOWN` evidence is not a ruling. Mark the subject
  `UNRULED — evidence insufficient` and keep it out of counts until evidence arrives.
- **Where a source's boundary differs from ours, quote the source's boundary verbatim.**
  Do not normalize the disagreement away — it is data about the market's shape and belongs
  in `logs/conflicts.md` as well.
- Blinding applies here hardest. A ruling that reads "this is adjacent to what the client
  does" is contaminated and void. The test is functional, not commercial.

## Log

| ruling_id | date | subject | subject_type | verdict | test_applied | reasoning | evidence | grade | source_boundary_verbatim | supersedes |
|---|---|---|---|---|---|---|---|---|---|---|
| _(empty — no research has been conducted)_ | | | | | | | | | | |
