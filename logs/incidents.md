# incidents.md

Errors by the agent that affected the evidence base. Recorded because an audit trail that
omits its own damage is not an audit trail.

---

## I-0001 — 2026-08-10 — 13 human-transported captures destroyed by the agent

**What happened.** The user pasted 13 new pages (11 G2 category pages, the G2 marketing nav,
the Gartner Marketing branch list, and a Gartner Voice of the Customer market page) into
`sources/raw/web pages/`. Before committing them, the agent ran a directory reorganisation
whose final step was `rm -rf "web pages"`. The `mv` loop preceding it had a shell quoting bug
(`$s__r3` parsed as an undefined variable `s__r3`), so most files were never moved. The
`rm -rf` then deleted them.

**What was recoverable.** The 8 Gartner pages from pass 02 had been committed in `1837b75`
and were restored with `git checkout`.

**What was lost — not recoverable, needs re-pasting:**

| Source | File | Why it mattered |
|---|---|---|
| gartner | `/reviews/market/marketing` | **The Marketing branch denominator — 82 categories.** The single most-requested artefact in this study |
| gartner | `/reviews/market/voice-of-the-customer-platforms` | An 8th market, not yet extracted |
| g2 | `/marketing` | G2 marketing nav |
| g2 | `/categories/account-based-marketing` | parent category |
| g2 | `/categories/account-data-management` | criteria + count |
| g2 | `/categories/customer-data-platform-cdp` | criteria + count |
| g2 | `/categories/digital-analytics` | criteria + count |
| g2 | `/categories/email-marketing` | criteria + count |
| g2 | `/categories/lead-generation` | parent category |
| g2 | `/categories/marketing-account-intelligence` | criteria + count |
| g2 | `/categories/marketing-analytics` | criteria + count |
| g2 | `/categories/marketing-automation` | criteria + count |
| g2 | `/categories/personalization` | criteria + count |
| g2 | `/categories/sms-marketing` | criteria + count |

**Root cause — not the shell bug.** The bug was the trigger; the cause was **processing
pasted content before committing it.** `CLAUDE.md` §8 already says "always commit raw pasted
source content." The rule existed and was not followed, because it did not say *when*.

**Fix applied.** A new first-action rule in `CLAUDE.md` §8 and `research-protocol.md` §2:
**pasted content is committed on arrival, before it is read, moved, renamed or parsed.**
Reorganisation happens in a later commit, never the same one.

**Consequence for the evidence.** Content extracted from those files before the deletion is
preserved in `sources/derived/UNVERIFIED-extractions-2026-08-10.md`, graded
**`UNVERIFIED-EXTRACTION`** — below `SINGLE-SOURCE`, because the raw capture that would
adjudicate it no longer exists. It may not anchor any finding until a re-paste restores the
raw file. It is kept rather than deleted so the user's effort is not wasted twice, but it is
kept **clearly marked**, because an extraction whose source has been destroyed is exactly the
kind of thing that quietly becomes a fact by being repeated.

---

## I-0002 — 2026-08-17 — at least 7 enrichment records describe the wrong company

**What happened.** A user remark — *"Zeta Athena is quite ahead with its AI propositions"* —
did not match the store. Our `Zeta` record reads *"Launch Card Programs Your Customers Will
Love"* and *"next-gen instant card issuing and transaction processing for banks and FIs."*
The record's own Gartner products are **Selligent**, **Cheetah Digital** and **Zeta Marketing
Platform** — unambiguously **Zeta Global** (`zetaglobal.com`, whose platform is *Athena by
Zeta™*). The enrichment fetched **`zeta.tech`**, an unrelated banking-technology company.

**A systematic sweep of all 211 captures found six more:**

| Company | Fetched | What that site actually is |
|---|---|---|
| Zeta | `zeta.tech` | banking card-issuing platform |
| MINT | `mint.intuit.com` → `creditkarma.com` | consumer credit app — and the capture is an **error page** |
| Trueblue | `trueblue.com` | US workforce-staffing firm (our record's product is *AiDEA Marketing*) |
| CAKE | `cake.com` | productivity suite — Plaky, Pumble, Clockify (our record's product is *Journey by CAKE*) |
| Insightly | `insightly.co` | an AI desk-research tool; the CRM is `insightly.com` |
| Marigold | `marigold.com` | **parked placeholder**, 213 bytes, title "marigold nn" |
| Levitate | `levitate.com` | alternative-energy company; page is charset `windows-1251` |

**Why the identity gate passed all seven.** The gate requires the company name to appear in
`title` / `og:site_name` / JSON-LD. On every one of these it does — because **the name is
shared with a different company**. The gate tests that a name matches, which is precisely what
`LEARNINGS.md` #1 says never to rely on. The four-character minimum does not help: `Zeta`,
`CAKE`, `MINT` all clear it while being among the least distinctive strings in the file.

**Why 15 verification checks passed.** The suite asserts *"every enriched company has a
recorded identity chain."* The chain is recorded. It is simply wrong. A check on the presence
of provenance cannot detect false provenance.

**The disambiguator was on the record the whole time and unused.** Every one of these companies
carries G2/Gartner **product names** — `Selligent`, `Cheetah Digital`, `Journey by CAKE`,
`AiDEA Marketing`. None appears anywhere on the fetched site. A cross-check of source-declared
product names against the capture is cheap, offline, and would have caught all seven.

**Blast radius.** Every marketing-derived cell on these records — `description_own`,
`value_proposition`, `functionality`, `channels`, `industries_served`, `website` — describes the
wrong company. `outputs/industries.md` inherits this: Zeta's card-issuing vocabulary and
Trueblue's staffing copy fed the industry rollup. Counts there are affected but were not
recomputed in this commit, because the fix is a re-enrichment, not an edit.

**Not fixed here, deliberately.** Correcting them means re-running enrichment against the right
domains, which is a pass with its own budget and log. Recorded now so nothing downstream is
built on it in the meantime. **The count is "at least 7": the sweep detects only cases where the
wrong company is in an obviously different business.** A wrong company in the *same* business
would pass every check we currently have.
