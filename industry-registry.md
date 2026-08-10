# industry-registry.md — the merge key

**This registry is empty by design and stays empty until evidence fills it.**

Pre-populating it from model knowledge is failure mode P1, committed at the one
place in the repo where it would do the most damage — the key every other file
joins on. A wrong key does not produce a wrong row; it produces a wrong table.

Four sources will name the same industry four different ways, at four different
levels of granularity, with four different boundaries. This file is where that
gets reconciled — visibly, with the original wording preserved, so a reader can
always see what each source actually said.

---

## The discipline

Every research pass, for every category it encounters:

1. Record `raw_name` — the category name **exactly** as the source states it.
   Verbatim. Original casing, punctuation, language, ampersands, plurals,
   trailing qualifiers. `raw_name` is **immutable** once written.
2. Look for a matching registry entry via its alias list.
3. **Match found** → use that entry's `normalized_name`, and append the new
   `raw_name` to its alias table if it isn't already there.
4. **No match** → **append a new entry**, with this `raw_name` as its first
   alias. Do not force a bad match. Do not widen an existing entry's definition
   to swallow it.
5. **Uncertain match** → append the new entry *and* file a row in
   `evidence/conflicts.md` with `status: DEFINITIONAL`. Ambiguity is recorded,
   never guessed away.

A registry that grows fast in early passes is working correctly. A registry that
stays small because everything "basically fits" is being used to hide the
disagreement it exists to expose.

## Rules

- **Append-only.** Entries are never deleted and IDs are never reused.
- **Never rename** a `normalized_name` in place. Superseding requires a new
  entry plus a row in the merge log below; the old entry stays with
  `status: SUPERSEDED-BY IND-nnn`.
- **Merging two entries requires evidence** — a source that explicitly treats
  them as one thing, cited. "They feel like the same market" is not evidence.
  Log it in the merge log.
- **One `raw_name` → exactly one `normalized_name`.** If a source's category
  genuinely spans two registry entries, record it as a `SPLIT` (below) and flag
  it in `evidence/conflicts.md`. Do not pick the closer half.
- **The registry does not rank, size, or judge.** No market-size column, no
  relevance column. It maps names to names. Anything else belongs in
  `outputs/`.
- **Definitions are written from the evidence.** An entry's one-line definition
  is composed from the source definitions on record, with those sources cited —
  never from what you know a category to mean.
- Granularity conflicts are entries too. If source A has one category where
  source B has three, that is three registry entries plus a `PARENT-OF`
  relation, and it is a finding worth reporting.

---

## Entry format

Copy this block per entry. Keep entries in ID order.

```markdown
### IND-000 — <normalized_name>

- **definition:** <one line, composed from cited source definitions>
- **definition_sources:** <url> [rung] [grade]; <url> [rung] [grade]
- **status:** ACTIVE | PROVISIONAL | SUPERSEDED-BY IND-nnn
- **created_by_pass:** <pass_id>
- **not_this:** <boundaries — what a reader might wrongly file here, and where it goes instead>
- **relations:** PARENT-OF IND-nnn | CHILD-OF IND-nnn | OVERLAPS IND-nnn (with note)

| raw_name (verbatim) | source | source_url | source_lang | first_seen_pass | rung | notes |
|---|---|---|---|---|---|---|
| | | | | | | |
```

Field notes:

- `normalized_name` — lowercase kebab-case, descriptive, source-neutral. It must
  not be lifted from any one source's vocabulary; borrowing G2's or Gartner's
  wording as the canonical name reimports that source's frame into the key
  itself, which is P2 through the back door.
- `PROVISIONAL` — created from a single pass, not yet seen in a second source.
  Provisional entries are reported as provisional in the merged table.
- `not_this` — the most useful field in the entry, and the one that stops the
  registry silently drifting. Fill it.

### Split record

Used when one `raw_name` genuinely covers two or more registry entries.

```markdown
- **SPLIT:** "<raw_name>" (<source>, <url>) covers IND-00a + IND-00b.
  conflict_id: <id>. Evidence for the split: <url> [rung] [grade].
```

---

## Registry

<!-- EMPTY. Entries are appended by research passes only. Do not seed this
     section from model knowledge — that is P1 at the merge key. -->

_No entries yet. First pass to run appends IND-001._

---

## Merge log

Every merge, split, supersede, or relation change gets a row. This is the audit
trail for the key; without it, the merged table cannot be reproduced.

| date | pass_id | action | entries | evidence_url | rung | grade | rationale |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

`action` ∈ `CREATE` | `ALIAS-ADD` | `MERGE` | `SPLIT` | `SUPERSEDE` |
`RELATION-ADD` | `STATUS-CHANGE`.

---

## Coverage counter

Maintained at the end of every pass. A registry entry that only ever appears in
one source is the most interesting row in the whole study — it is either a real
market one taxonomy sees and the others are blind to, or an artifact of that
taxonomy's commercial model. Either way, name it.

| normalized_name | g2 | crunchbase | gartner | app-marketplaces | sources_covering |
|---|---|---|---|---|---|
| | | | | | |
