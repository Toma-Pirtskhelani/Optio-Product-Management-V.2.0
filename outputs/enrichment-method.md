# Company enrichment — method and parked fields

Governs the enrichment of `outputs/companies.jsonl`. Read with `CLAUDE.md` and
`research-protocol.md`; where this file differs from them, the differences are stated below
and are deliberate.

---

## 1. Storage

| File | Role |
|---|---|
| `outputs/companies.jsonl` | **Canonical store.** One complete company object per line |
| `outputs/companies-meta.json` | File-level metadata — coverage, merge rules, limits. JSONL has no place for it, so it sits beside rather than being smuggled into record 0 |
| `outputs/companies-index.md` | **Generated view.** Never edit; regenerate with `scripts/build_index.py` |
| `outputs/companies-IN.json` | Superseded snapshot, kept for the audit trail |

One line per record means a single company is retrievable by `grep` without parsing the file,
and **a changed field produces a one-line git diff instead of rewriting the whole file.** In a
single-object JSON the audit trail dies on the first edit, and provenance is the point of this
project.

---

## 2. Fixed effort budget — four fetches per company

**Every company gets the same budget. No depth tiers, no exceptions for interesting companies.**

1. `/llms.txt` — cheap probe; where it exists it maps the documentation set and points the
   remaining fetches at the right pages
2. Homepage — description, value proposition, HQ hints, client logos, often channels
3. Product or features page — functionality, `channels[]`
4. One discretionary fetch — whichever page closes the largest remaining gap; usually
   `/pricing`, sometimes `/customers` or `/about`

After four, stop. Remaining fields are `UNKNOWN`.

**This is a comparability control, not just a cost control.** With a fixed budget, `UNKNOWN`
means *not findable in four fetches of the company's own site* — a consistent statement about
the company. With variable effort it would mean *nobody looked hard enough*, and nothing
downstream could tell the two apart. `fetches_used` is recorded on every record so the
uniformity is auditable rather than asserted.

---

## 3. Failure handling — deliberately different from the standing protocol

**The stop-at-Rung-3 rule does not apply to this pass** and would deadlock it: pausing for a
human paste on each of 237 companies is not a workflow.

- **Rungs 1 and 2 only.**
- Unreachable page → `unreachable: true` with the reason, affected fields `UNKNOWN`, move on.
- **Never request a paste in this pass.** Blocked domains accumulate for a later deep-dive.
- **Never substitute a search-engine summary** for a page that would not open. `UNKNOWN` is a
  finding; an invented value is a defect.
- A company that is entirely unreachable **is recorded as such**, never silently dropped.

---

## 4. `solution_type` — the inference rule

Where a vendor states its deployment model, in descending reliability: a security or trust page
(data residency, single-tenancy, SOC 2); the enterprise tier of a pricing page; installation or
deployment sections of documentation. Marketing homepages rarely say.

**If no statement is found, record `unknown`. Do not default to `saas-multi-tenant`.** A modern
vendor probably is SaaS — but "probably" is not evidence, and a silent default would erase the
exact distinction this field exists to capture. Where real indirect evidence exists (documented
installation steps, a published data-residency choice), record the value at grade `INFERRED`
and cite what it was inferred from in `solution_type_evidence`.

---

## 5. Parked fields — excluded by decision, not missed

Each failed one test: *is this reliably obtainable from the company's own website within a
fixed small fetch budget?* Half-filling them here would produce a column of noise that looks
like data.

| Parked field | Why it is not collected now | Where it will come from |
|---|---|---|
| `revenue` | No source in this study carries it | A financial source, or nowhere |
| `headcount` | Not reliably published; LinkedIn blocked | Same |
| `tech_stack` | Rarely published by any vendor | **Job postings** — a `REVEALED-BEHAVIOR` source, and stronger evidence than any marketing page |
| `top_requested_features` | Needs roadmap, changelog or feature-portal mining | Public roadmaps and feature-request portals |
| `top_complaints` | Needs review mining; both review sites block automated access | Review sites via human transport, small set only |

**An absent field with a recorded reason is honest. An absent field with no explanation looks
like an oversight.** That is why this table is in the repository rather than in a chat message.

---

## 6. Grading

Every field carries `value`, `source_url`, `rung`, `grade`, `retrieved_date`. **Per-cell
grading governs; a company is never graded as a whole.**

`PRIMARY` — stated on the company's own site · `INFERRED` — real indirect evidence, cited ·
`UNKNOWN` — not found within the budget.

`vertical_focus` is **computed, never researched**: `vertical` for 1–2 stated industries,
`mixed` for 3–5, `horizontal` for 6+ or any explicit any-industry claim. It is derived from
`industries_served`, so it costs no fetches and is reproducible from the record itself.
