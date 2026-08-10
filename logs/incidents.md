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
