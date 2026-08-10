# industry-registry.md — the merge key

**This registry starts empty and is built only by evidence.** It is not pre-populated from
anyone's knowledge of the market, including the model's. Pre-populating it would be
prohibition 1 — a brainstormed list mistaken for the universe — committed at the single
point where it would contaminate every downstream table at once.

If you are reading this file looking for the list of industries this study covers, the
answer today is: **none yet, because no evidence has been gathered.** That is correct, not
incomplete.

---

## 1. What this file is for

Sources name the same industry differently. G2, Gartner, and a marketplace will describe one
economic activity with three different strings, at three different levels of granularity,
under three different theories of what a category is. Merging on the string produces
nonsense. Merging on a normalized key produces a study.

So every pass records **both**:

- **`raw_name`** — the category name **exactly as its source states it**, character for
  character, in the source's own language and capitalization. Never cleaned, never
  translated in place, never singular/plural-normalized.
- **`normalized_name`** — a key drawn from this registry.

`raw_name` is evidence. `normalized_name` is a decision. Keeping them in separate columns is
what makes the decision reversible when a later pass proves it wrong.

---

## 2. The append rule

**A pass meeting a category with no registry match appends a new entry with its alias list.
It does not force a bad match.**

Forcing a near-match is the single most damaging thing that can happen in this repository,
because it is invisible afterward: two genuinely different market definitions collapse into
one row, the disagreement between the taxonomies disappears, and the resulting count looks
more solid than either source alone. A forced match manufactures corroboration.

When in doubt, **append**. Two registry entries later found to be the same thing are trivial
to merge, and the merge is recorded. One entry that was secretly two is undetectable.

---

## 3. Entry format

Every registry entry is a block in this shape. Nothing in it is optional; missing values are
written `UNKNOWN`.

```
### <normalized_name>

- registry_id:        R-0001
- normalized_name:    <the merge key — a name this study assigns, stable forever once assigned>
- status:             ACTIVE | RETIRED-BY-SOURCE | TRANSITIONING | MERGED-INTO <registry_id> | PROVISIONAL
- first_seen:         <ISO date> via <source> <url> (paste_id if human-transported)
- definition_basis:   <which source's definition this key was created from — and the fact
                       that this key is OUR construct, not that source's property>
- scope_verdict:      IN | OUT | BOUNDARY-IN | BOUNDARY-OUT | UNRULED  (ruling_id in logs/boundary-rulings.md)

- aliases:
  | raw_name (verbatim) | source | source_url | language | date_seen | paste_id | granularity | notes |
  |---|---|---|---|---|---|---|---|

- inclusion_criteria:
  | source | criteria_verbatim | source_url | date | grade |
  |---|---|---|---|---|
  <the source's OWN inclusion criteria or mandatory-feature list, quoted, per source.
   UNKNOWN where unpublished — and see §5.>

- source_boundary_notes: <where a source's stated boundary differs from this study's
                          functional definition, quoted verbatim. Never normalized away.
                          Cross-reference conflict_id.>

- decline_markers:
  | marker | applied_by | value_verbatim | date_seen | source_url | grade |
  |---|---|---|---|---|---|
  <(Retired) / (Transitioning to X) as stated by the source. See §6.>

- merge_history: <appends, splits, merges — each with date and reason. Append-only.>
```

---

## 4. Naming rules for `normalized_name`

1. **English is a working convention here, not a claim.** The key is an internal identifier;
   it does not assert that the English name is the real one. `raw_name` in the source's own
   language remains the evidence, and per `CLAUDE.md` §6 the domestic-language name is
   primary wherever a vendor or market has one.
2. **Never invent a name more general than the evidence supports.** If one source says
   *"Retail — Grocery"* and another says *"Retail"*, those are two entries with a recorded
   relationship, not one entry. Granularity differences are recorded in the `granularity`
   column, never flattened.
3. **A key is stable once assigned.** Renaming breaks every table that cites it. To change a
   name, append a new entry and mark the old `MERGED-INTO`.
4. **A key is never created from model memory** — only from a `raw_name` that appeared in a
   fetched or pasted source. If you find yourself typing an industry name you did not read
   somewhere, stop: that is prohibition 1.

---

## 5. Inclusion criteria are part of the key

Recorded per source, per category, **verbatim**. Not paraphrased — the wording is the thing.

Categories differ enormously in how hard they are to enter. A category requiring six
mandatory features and a category requiring one are not comparable, and their product counts
are not comparable either. **Raw counts across categories must never be presented as if they
were.**

Where a source does not publish inclusion criteria, record `UNKNOWN` and treat that
category's count as **non-comparable to any other, including to itself over time** — an
unpublished criterion can change silently between captures.

This is also why `CLAUDE.md` §7 makes the **category cluster** the unit of analysis: a single
vendor may occupy many categories at once, and how many depends on the taxonomy's rules
rather than on the vendor.

---

## 6. Retired categories stay

A category marked `(Retired)` by its source is **kept**, with `status: RETIRED-BY-SOURCE` and
the marker recorded verbatim.

Deleting retired categories would rebuild survivorship bias inside the merge key itself —
the exact failure this study exists to avoid, planted at the root where every table inherits
it. A retired category is a **market that failed or dissolved**, and per
`research-protocol.md` §6 that is a stronger signal than any single dead company.

`(Transitioning to X)` gets `status: TRANSITIONING`, with **both** the source and target
names recorded as aliases. The taxonomy moving is itself a finding about the market.

---

## 7. Registry hygiene

- **Append-only.** Entries are added, merged, or marked; never deleted, never silently
  edited. Every change carries a date and a reason in `merge_history`.
- **Every entry traces to a URL and a date.** An entry with no source is a mistake to be
  investigated, not tidied away.
- **`PROVISIONAL`** marks an entry created from a single ambiguous sighting. Provisional
  entries may not anchor a finding until confirmed by a second capture.
- **A registry entry is not a claim that the industry matters.** It is a claim that a source
  named it. Whether it matters is decided in the outputs, on evidence, blind to the client.

---

## 8. Registry

_(empty — no research has been conducted. Entries are appended by evidence, per §2.)_

| registry_id | normalized_name | status | alias_count | scope_verdict | first_seen |
|---|---|---|---|---|---|
| _(none)_ | | | | | |
