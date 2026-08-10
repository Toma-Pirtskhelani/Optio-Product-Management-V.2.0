# Research log

Chronological. Newest at the bottom. One entry per meaningful step: what was done, what it
changed, what it cost. Updated every time the repository is.

Blinding status: **client identity, product, ICP, geography — WITHHELD BY DESIGN.** Unbroken.

---

**00 · 2026-08-10 · Prior attempt discarded**
Repository emptied, git history deliberately kept — the record of a false start is audit trail,
not embarrassment. Nothing salvaged from the old scaffold: it used a dropped source, a fallback
that does not work here, and no blinding protocol.

**01 · 2026-08-10 · Repository rebuilt**
Wrote `CLAUDE.md` (blinding protocol with its known leak, six prohibitions, category scope,
seven competitor classes, language obligation, git rules), `research-protocol.md` (source
ladder, typed absence, confidence grades, source class, failure sampling), `industry-registry.md`
(empty by design), four schemas designed backward from the merge, and four append-only logs.
Key rule: a merged row inherits the **weakest** grade among its inputs — makes uneven depth
structurally visible instead of merely discouraged.

**02 · 2026-08-10 · Four protocol amendments**
`row_grade` demoted to advisory — per-cell grades govern, because a grade that reads UNKNOWN
everywhere stops being a signal. `competitor_class` struck. `source_language` made mandatory on
every fetch attempt so language bias carries a number. Materiality resolved by removing the
threshold: rank everything, cut nothing, and *done* = every category enumerated, never *enough
found*.

**03 · 2026-08-10 · Pass 01 — denominators**
Fetched what could be fetched. G2's full taxonomy at Rung 1 (**2,235 categories, 38 branches**),
its governance rules at Rung 2 on `research.g2.com` while `www.g2.com` blocked. Shopify **161**
categories and HubSpot **60** from sitemaps. Gartner returned 403 on all seven paths including
`robots.txt`.
Caught the fetch tool inventing three numbers — it reported the Shopify sitemap at 216/246/226
URLs where byte-exact capture shows **161** in all three. Every count since is `curl` plus
deterministic parsing.

**04 · 2026-08-10 · Pass 01 output**
`outputs/source-taxonomies.md`. Two findings promoted from method to evidence: G2 **deletes**
discontinued products and their reviews by policy, so it is structurally incapable of showing
failure; and G2 removes listings to comply with OFAC sanctions, so a Russian vendor's absence is
evidence about sanctions policy, not about the vendor.
Honest verdict on the pass: 2,235 categories classified by **name**, because every definition
sat behind a 403. A directory listing, not a study.

**05 · 2026-08-10 · Three corrections**
Amendment 2 reversed — G2 runs nine service-provider branches, so "taxonomies only classify
software" was false; classes 3–4 return as a supply-side-only column. Scope widened from
"customer" to **identified external recipient** (patient, citizen, donor, candidate…), employees
excluded, with in-app *messaging* IN and on-site *personalisation* OUT. **Stop at Rung 3** made a
hard rule after pass 01 logged a blocker and kept working past it.

**06 · 2026-08-10 · Pass 02 — Gartner, human transport**
Seven market pages supplied. Established the discriminator that governs everything since:
analyst **Markets** publish mandatory features plus a Magic Quadrant or Market Guide; Peer
Insights **Categories** publish neither — and both live at the same URL.
First non-winners evidence in the study: **15 `(Legacy)` products**, ratings intact beside the
marker. Gartner's FAQ also excludes Russian, Turkish and Georgian reviews from publication by
policy — three of our six required languages.

**07 · 2026-08-10 · Incident I-0001 — 13 captures destroyed**
A reorganisation with a shell quoting bug ended in `rm -rf`; most files were never moved and
were deleted. Eight Gartner pages survived in git. Lost: the Gartner Marketing branch list, one
market page, all eleven G2 category pages.
Cause was not the bug — it was processing pasted content before committing it. New rule: pastes
are committed **on arrival**, before being read, moved or parsed, as their own commit. Never
`rm -rf` under `sources/`.

**08 · 2026-08-10 · Recovery**
Extracted content preserved as `UNVERIFIED-EXTRACTION`, below SINGLE-SOURCE, barred from
anchoring anything. G2 pages re-supplied, committed untouched, re-verified against the restored
files — **every count and criteria block matched exactly**, so that extraction returned to
PRIMARY.
Measured then: a G2 category page renders ~**25 of its declared listings**; Gartner prints
*122 of 122*. That asymmetry decides which source can carry a company list.

**09 · 2026-08-10 · Gartner Marketing branch recovered**
**82 categories**, fully enumerated, with the study's first `(Retired)` markets — Ad Tech
Platforms, Advanced Analytics Service Providers for Marketing, Online Marketplace Optimization
Tools. Markets that failed at category level; nothing else in our source set produces that
signal.

**10 · 2026-08-10 · Classification test replaces name-reading**
Scope cut to supplied pages only. `R1–R4` shorthand replaced by four plain questions asked of
each category's **published admission test**: does it require holding a list of identifiable
people, choosing who gets what, deciding when to send, and **actually sending on a channel the
person receives**. IN = the fourth, plus either of the first two.
It immediately caught what names hide: G2 and Gartner give **opposite verdicts on
personalization**; both rule **CDP out** independently in near-identical language; and overlap
turns out to be per-pair — Gartner's markets overlap, G2's Email Marketing and Marketing
Automation exclude each other by rule.

**11 · 2026-08-10 · Menu made choosable**
Every classification given its source's own formal description, quoted with the date the source
stamps on it — G2 definition ages span October 2024 to July 2026. Corrected a mislabel that had
presented my own deleted file as a gap in what was supplied.

**12 · 2026-08-10 · Three remaining markets added, document finalised**
Voice of the Customer Platforms **OUT** — all three requirements are collection, analysis and
*internal* action. Direct Mail Automation **IN**. Conversational Marketing left **BOUNDARY** on
purpose: its definition never says who starts the conversation.
Proofread fixed section numbering, stale totals, and moved `(Legacy)` counts and Gartner's
`Popular` flag into the menu where they inform a choice. New pattern: Gartner's three
requirement-free categories are also its three smallest (11, 15, 22) against 45–122 for every
governed Market.

---

## Where it stands

`outputs/classification-menu.md` — **19 rows, 8 IN.** Gartner 6 IN (352 products, 6 pastes);
G2 4 IN (1,810 listings, ~75 pastes). One BOUNDARY (Conversational Marketing). One OUT that
could flip (Account Data Management, on whether *"facilitate communication"* means outbound).

**Awaiting:** your ticks, and one page — G2 Mobile Marketing Software, the only G2 counterpart
to Gartner's Mobile Marketing Platforms.

**Open structural gaps, not tasks:** demand-side evidence exists for none of competitor classes
2–7. No funding data from any source. Russian, Turkish and Georgian are excluded from Gartner by
policy and censored on G2 by sanctions compliance. No vendor row anywhere is yet
`corroborated: yes` — every source so far is self-declared.
