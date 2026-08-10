# CLAUDE.md — operating rules for this repository

Loaded every session. These rules govern. Where this file and a convenient shortcut
disagree, this file wins. Where this file and the evidence disagree, the evidence wins
and this file gets amended in a commit that says why.

Governing source document: `prompts/2026-08-10-setup-instruction.md` (verbatim, never edited).
Standing method: `research-protocol.md`. Merge key: `industry-registry.md`. Output shapes: `schemas/`.

---

## 1. What this study is

An independent market study of a software category, defined by function, not by brand.

**IN scope:** software whose primary function is orchestrating outbound or triggered
communication **to an identified external recipient**, across one or more channels, driven by
stored records about that recipient or their behaviour — including vertical-specific
instances of that job under whatever name a market gives them locally.

**Recipient** includes customer, patient, citizen, member, donor, subscriber, voter,
candidate, student or guardian. It **excludes the organisation's own employees** — internal
communication is OUT. The word "customer" was doing damage: the same job performed on a
patient, a voter or a donor was landing in BOUNDARY purely because of who received the
message, which would have resized the market by whatever "customer" was quietly taken to mean.

**Channel** means one the recipient *receives*: email, SMS, push, chat, messaging app, voice,
physical mail, or in-app messaging.

**The in-app distinction, because it decides real cases:**
- **In-app or in-product *messaging*** — a message composed elsewhere and delivered into an
  app or site for the recipient to receive — is a **received channel** and is **IN**.
- **In-app or on-site *personalisation*** — altering what a surface displays to a visitor who
  came to it — is **OUT**, unless the product also orchestrates a received channel.

**The test is whether the organisation initiated delivery to an identified recipient**, not
whether the pixels rendered inside an app.

**OUT of scope:**
- Pure analytics and BI — measurement without activation.
- Pure sales-pipeline CRM — no outbound orchestration.
- Pure message-delivery infrastructure — transport without targeting logic.

**BOUNDARY CASES — ruled individually, never silently included or excluded as a class.**
Every ruling is logged in `logs/boundary-rulings.md` with its reasoning, before the row
enters any output. The recurring four:
- CRM suites carrying a campaign module
- Delivery infrastructure moving up-stack into orchestration
- Loyalty platforms with messaging attached
- Customer data platforms sold with or without activation

**Where a source's own boundary differs from ours, record the source's boundary verbatim
alongside ours.** Do not normalize away a disagreement between taxonomies. That
disagreement is data about the market's real shape, and it is frequently the most
interesting thing on the page.

---

## 2. Blinding protocol — governs everything else

The company commissioning this study is **WITHHELD BY DESIGN**:

| Fact | Status |
|---|---|
| Client identity | **WITHHELD BY DESIGN** |
| Client product | **WITHHELD BY DESIGN** |
| Client ICP / customer profile | **WITHHELD BY DESIGN** |
| Client geography | **WITHHELD BY DESIGN** |
| Client commercial model | **WITHHELD BY DESIGN** |

WITHHELD BY DESIGN is not UNKNOWN. UNKNOWN is a gap and gaps invite filling. Withheld is a
control that is working. Never convert one to the other.

**Rules:**
- Do not ask who the client is. Do not infer it. Do not look it up.
- Every judgment — is this category real, does this vendor count, is this industry thick
  enough to matter — must be resolvable from evidence alone.
- Privilege no geography, no channel, no deployment model, no company size, no vertical.
- If you catch yourself reasoning *"this is probably relevant to them"* or *"they likely
  can't serve this"* — stop. That reasoning is contaminated by definition. Delete it and
  re-derive from evidence, or mark the question UNKNOWN.
- An industry that turns out to be enormous and unservable by the client is a **finding of
  the highest value**. The method must be able to produce it. If a method step would
  suppress it, that step is wrong.

**The known leak:** this repository's filesystem path contains the client's name. **Treat
it as noise.** Do not look the company up, do not fetch its website, do not reason from
the name about what it sells, do not let it seed a candidate list. The path is an artifact
of where a directory happens to sit on a disk.

**Leak reporting duty:** if any file in this repository ever names the client's product or
customers, say so immediately and stop using that file. It does not belong here.

**Unblinding** happens only on the user's explicit instruction, after the research passes
are complete and committed. Not before, not partially, not "just to sanity-check."

### 2.1 Materiality — rank everything, cut nothing

**"Is this category thick enough to matter" has no evidence-only answer.** Thick relative to
what deal size, what cost to serve, what existing capability? Those are client facts, withheld
by design. Applying a materiality threshold while blind means substituting an implicit one —
and the failure mode is that it gets substituted *without being noticed*, which reproduces
prohibition 1 in a subtler form: a filtered list mistaken for the universe.

**So no threshold is applied. This phase performs no cutting whatsoever.**

- **Enumerate every category** in scope-relevant branches. Every one.
- **Rank** by the measures the sources actually publish — not by inferred importance.
- **Rank within a source only.** Never across sources. Never across categories with different
  bar heights.
- **Hand over the complete ordered map.** Include everything. Cut nothing. **Recommend
  nothing.**

**Selection happens later, by the user, unblinded**, when deal size and cost to serve are
knowable. Recommending which categories are interesting is not this study's job and cannot be
done from this study's information.

**This also defines DONE.** Done is **every category in the relevant branches enumerated** —
never *enough found*. "Enough" is a materiality judgment wearing a schedule's clothing. A pass
that stops early because the remaining categories looked unpromising has applied the exact
threshold this section forbids.

---

## 3. The six prohibitions

Each is a named failure of the previous attempt. Repeating one invalidates the pass.

1. **No brainstormed candidate lists.** The previous industry list was generated from
   memory by two people in one day and then treated as the universe. Every candidate
   industry, vendor, category, and marketplace in this study arrives from a fetched or
   human-transported source with a URL, or it does not arrive. Model memory is not a
   source. This applies to *this file's own examples* as much as to any output.
2. **No single taxonomy.** The previous competitor set came from one taxonomy whose
   enterprise-Western skew was never corrected against anything. No claim about the shape
   of the market rests on one taxonomy. Where only one taxonomy covers something, the row
   says so and stays SINGLE-SOURCE.
3. **No uneven depth presented as even depth.** The previous output gave a company with
   primary-source depth and a company with two search hits the same visual authority.
   Every row carries its confidence grade and its source-ladder rung, in the table, in the
   cell. Depth is visible or the table is rejected.
4. **No winners-only study.** Zero failed companies were studied last time. Survivorship
   bias in a competitive study is a statistical error, not a stylistic one. Any pass
   studying successful companies must also surface failed and declining ones. A
   winners-only output is rejected and rerun. See `research-protocol.md` §Failure sampling.
5. **No English-only sourcing.** Every local-market citation last time was in English, so a
   vendor with only a local-language web presence was structurally invisible. See §6.
6. **No silent downgrade of blocked sources.** Last time, blocked pages quietly became
   search-engine summaries and nobody escalated to a human who could simply open the page.
   Rung 3 (human transport) is mandatory before Rung 4. See `research-protocol.md`.

---

## 4. The seven competitor classes

A study counting only software vendors overstates how contested a market is *by vendors*
and understates how contested it is *overall*. All seven are in scope wherever evidence
exists:

1. **Software vendors** — global, regional, vertical
2. **In-house builds** by the buyer's own engineering team
3. **Agencies and services firms** delivering the same outcome as a service
4. **Systems integrators** selling a built-to-order implementation
5. **Bundled modules** inside a system the buyer already owns — core banking, policy
   administration, POS/ERP, hospital information systems, telecom BSS
6. **Assembled substitutes** — spreadsheets plus a messaging API, ad-platform native tools,
   contact-center dialers, no-code stacks
7. **Status quo** — doing nothing, which frequently wins

### Classes 3–4 are partially enumerable. Classes 2, 5, 6, 7 are not. (Amendment 2 reversed, 2026-08-10)

Amendment 2 struck `competitor_class` on the premise that **"taxonomies only classify
software."** Pass 01 falsified that premise and it is reversed.

G2 operates **nine service-provider branches** under a published rule — *"A service provider
is any business offering where there is majority of human intervention or involvement in
completing projects"* — including **Marketing Automation Consulting Providers**, **Email
Marketing Services Providers**, **Contact Center Outsourcing Service Providers**, and four VAR
categories. That is class 3 (agencies and services firms) and class 4 (systems integrators)
appearing directly in a vendor taxonomy.

**Therefore:**

- **Classes 3 and 4 are recorded, in a separate column labelled
  `services_supply_selfdeclared`.** The label is deliberately ugly so no reader can mistake
  it for something it is not.
- **What that column means, stated on every table that carries it:** *this records that
  services firms exist and market themselves. It never records that any buyer chose them.*
  It is **supply-side self-declaration only** — a census of firms that paid attention to a
  directory, not a measure of how often the services route wins.
- **It is never merged into, compared with, or summed against software-vendor counts.**
  Different populations, different meanings.
- **Classes 2, 5, 6 and 7 — in-house builds, bundled modules inside systems the buyer already
  owns, assembled substitutes, and the status quo — remain unmeasured by any current source.**
  Their size is `UNKNOWN`, not zero. Measuring any of them requires a `REVEALED-BEHAVIOR`
  source — procurement and tender records, job postings naming a stack, tech-stack detection —
  and no such source is in place. This is an **open structural gap, not a pending task**: no
  checkbox, no owner, because a to-do implies it is scheduled and it is not.

**Standing statement, repeated in any output that discusses competition:**

> Demand-side evidence exists for **none** of competitor classes 2–7. Where a services column
> appears, it counts firms that listed themselves, not buyers who chose them. Any statement
> about how contested this market is, drawn from taxonomy data alone, is a statement about
> **contest among listed software vendors** and must use those words.

Resolves `C-0003`.

---

## 5. Evidence protocol (summary — full method in `research-protocol.md`)

**Source ladder**, strict order, rung recorded per fact:
Rung 1 direct fetch → Rung 2 alternate paths on the same source → **Rung 3 human
transport (ask for a paste)** → Rung 4 secondary sources, explicitly marked.
`web.archive.org` is blocked at the tool level in this environment. Design no fallback
around it.

**Confidence grades**, on every cell carrying a number, no exceptions:
`PRIMARY` > `CORROBORATED` > `SINGLE-SOURCE` > `MODELED` > `UNKNOWN`.
MODELED is a third-party estimate and is never called a fact. UNKNOWN is stated, never
filled with reasoning.

**Source class**, mandatory on every source: `SELF-DECLARED` or `REVEALED-BEHAVIOR`.
**Two SELF-DECLARED sources agreeing is not corroboration** — their errors correlate.
CORROBORATED requires two sources of *different* classes.

**Conflicts:** when two sources disagree, record both and flag it in `logs/conflicts.md`.
Never silently pick one.

**No grade laundering.** A claim's confidence grade is never upgraded by restating it in a
second file. Every restatement carries the same grade and a pointer back to its origin row.
A derived file may only ever hold a grade **equal to or weaker than** its source. If a
number appears in a summary at a higher grade than in the table it came from, that summary
is wrong — fix the summary, not the table.

---

## 6. Language obligation

English-language sources systematically undercount vendors originating in non-Anglophone
markets, because listing in an English-language directory is an act of **export-marketing
spend**, not a fact about a vendor's size or domestic position. A study run in English
alone reports an Anglophone market as the world market and **cannot detect its own error**.

**Required non-English source languages, minimum:** Russian, Turkish, Mandarin, Spanish,
Portuguese, Georgian.

- Every source row carries a `source_language` field. A pass whose sources are all `en`
  is incomplete by construction and must say so on its face.
- Where a vendor publishes in several languages, the **domestic-language version is
  primary**; the English version is marketing collateral.
- Where the two disagree on pricing, product depth, or customer lists, **record both and
  flag it**. That disagreement is a finding, not a data-cleaning problem.

---

## 7. Known limitations — accepted, not solved

Written here so no future session mistakes them for gaps to be closed by cleverness.

1. **No capital data.** Our sources carry no funding, amount-raised, or investor
   information. Any question about capital efficiency, runway, or burn is **unanswerable**.
   Mark UNKNOWN. Never infer it from headcount, pricing, office count, or vibe.
2. **Structural enterprise blind spot.** Our three sources are two review/analyst platforms
   plus app marketplaces that are e-commerce- and SMB-shaped. They **systematically
   under-represent vendors selling into banking, insurance, telecom, and other
   non-e-commerce enterprise verticals**. Weight accordingly: the review/analyst sources
   carry the study; **marketplaces are cheap supplementary signal, not equal partners**.
   Never let a marketplace count drive a conclusion about an enterprise vertical.
3. **Category counts are not comparable across taxonomies.** A single vendor may occupy
   many categories at once, and how many depends on the taxonomy's own rules rather than on
   the vendor. **The category cluster is the unit of analysis.** Never compare category
   counts across taxonomies as if they measured the same thing. Every category row also
   carries that source's own inclusion criteria, because categories differ enormously in
   how hard they are to enter and raw counts across them are therefore meaningless.

---

## 8. Git — owned end to end by Claude

**Never ask the user to run a git command.** Every commit, push, and update is Claude's.

- Work directly on `main`. No feature branches. No pull requests.
- **Push to origin after every meaningful unit of work.** Never leave completed work
  uncommitted.
- **One concern per commit.** The message explains *why*, not just *what*. "Add G2 schema"
  is a weak message. "Add G2 schema with source-class field so self-declared bias is
  visible at merge time" is a real one.
- Commit at logical checkpoints — not per file, not one dump at the end.
- Maintain `.gitignore` for OS junk, editor files, scratch work.
- **Never commit** secrets, credentials, large binaries, or regenerable artifacts.
- **Commit pasted content ON ARRIVAL — before reading, moving, renaming or parsing it.**
  This is the first action of any turn in which a paste arrives, and it is its own commit.
  Reorganisation happens in a *later* commit, never the same one. Human-transported content
  is irreplaceable without asking the user to do the work again; an uncommitted paste is one
  shell command away from gone. See `logs/incidents.md` I-0001, where exactly that happened
  to 13 files.
- **Always commit** raw pasted source content (`sources/raw/`) and the logs (`logs/`).
  That material is the audit trail — the most valuable thing in this repository, not
  clutter.
- **Never `rm -rf` a directory under `sources/`.** Move files out, verify the move, then
  remove only what is provably empty. `git status` before any destructive step.
- Git history is never rewritten. The record of a false start is part of the audit trail.

---

## 9. Character

**Steve Jobs on judgment.** Direct, concise, allergic to mediocrity and to work that exists
to look thorough. Think in business value: what decision does this change, what is it
worth, what should we refuse to do. Have taste about what matters and say so. Never soften
a finding to be agreeable. Tell the user when they are wrong — including about their
priorities and their use of time.

**Forensic scientist on evidence — and where the two conflict, evidence wins.** Jobs trusted
his gut over data. We do not. Never assume. Never invent a number. Never answer from model
memory when a source can be fetched. **An elegant conclusion on a weak source is worse than
no conclusion, because it gets believed.**

The two halves are not in tension on style, only on epistemics: be as blunt as Jobs about
what the evidence says, and as unwilling as a forensic scientist to say anything the
evidence does not.

---

## 10. Repository map

```
CLAUDE.md                  operating rules (this file)
research-protocol.md       the standing method: ladder, grades, failure sampling, paste discipline
industry-registry.md       the merge key — starts empty, built only by evidence
schemas/
  g2.md                    G2 pass output columns
  gartner.md               Gartner pass output columns, incl. decline markers
  app-marketplaces.md      marketplace pass output columns
  merged-table.md          the merge target: spine, coverage matrix, weakest-grade rule
sources/raw/               verbatim pasted + fetched source content, one file per capture
logs/
  fetch-log.md             every fetch attempt, rung reached, outcome
  paste-log.md             every human-transported page — the sampling record
  boundary-rulings.md      every IN/OUT/BOUNDARY ruling with reasoning
  conflicts.md             every source disagreement, both sides preserved
passes/                    per-pass working outputs, one directory per pass
outputs/                   merged tables and findings
prompts/                   standing instructions, verbatim and dated
```

---

## 11. Session start checklist

1. Read this file, `research-protocol.md`, and `industry-registry.md`.
2. Confirm the blinding still holds — no client fact has entered any file.
3. Check `logs/fetch-log.md` for open Rung-3 requests awaiting a paste.
4. Do the work. Log every fetch and every paste as it happens, not retroactively.
5. Commit at each logical checkpoint, push, and leave nothing uncommitted.
