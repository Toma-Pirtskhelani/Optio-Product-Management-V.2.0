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

**13 · 2026-08-10 · Company export for all 10 IN classifications**
Deterministic parsers over the raw captures, reconciled against each source's declared total —
all six Gartner categories match exactly (**352 of 352**), so absence there is `ABSENT-ENUMERATED`.
G2 yields **102 of 1,810 (5.6%)**, visible page only; that half is `ABSENT-IN-VISIBLE-PAGE` and
carries the flag per row.
Deduplicated to **237 unique companies** with 7 conservative merges, no fuzzy matching. **27 are
listed by both sources** — still not corroboration, since both are self-declared. 7 carry a
Gartner `(Legacy)` product; G2 sponsored placements are flagged.
Gartner's parenthetical vendor form turned out to encode two different things, now split by a
computed test: **acquisitions** (CleverTap–Leanplum, Constant Contact–SharpSpring,
Upland–Localytics, Mastercard–Dynamic Yield, Capillary–SessionM, Tech Mahindra–Comviva,
Soprano–Whispir, HCLTech–HCLSoftware) versus mere **abbreviations** (AWS, HPE, ITG).
Output: `outputs/companies-IN.json` + `outputs/companies-IN.md`.

**14 · 2026-08-10 · Proofread caught a coverage error in my own favour**
G2's published figure was **102 of 1,810 (5.6%)** — but that counted *rendered blocks*, not
products. A G2 category page lists each product **twice**: a main listing with `By <vendor>`
lines, then a summary rendering without vendors. True coverage is **65 of 1,810 (3.6%)**, about
16 distinct products per page. The error overstated G2 coverage by 57% and risked splitting a
product from its parent company wherever only the vendor-less rendering was captured.
Blocks now collapse to distinct products, preferring the one that names the vendor. Paste-cost
estimates in the menu corrected upward (~75 → ~111 for the four G2 IN rows). Gartner unaffected
and still exact at 352 of 352.
Also fixed: legacy stated as 8 products where it is **9 listings across 8 distinct products**
(`SAP Marketing Cloud (Legacy)` sits in two categories), and 4 product names truncated by the
source page itself are now flagged `name_truncated_in_source` rather than silently carrying an
ellipsis. 18-check audit now passes clean.

**15 · 2026-08-10 · Storage migrated to JSONL before enrichment**
`companies-IN.json` was 824 KB — unreadable in one context, and enrichment would have made it
worse. Canonical store is now **`outputs/companies.jsonl`**, one complete company per line:
retrievable by `grep` without parsing, and **a changed field is a one-line git diff instead of
a whole-file rewrite**, which is what keeps the audit trail alive.
Migration verified lossless by a 10-check comparison — 237 in, 237 out, no key path dropped, no
original value altered. `outputs/companies-index.md` is the generated context anchor at
**16.1 KB**, well under the 60 KB target. Enrichment fields are scaffolded empty so every record
has one shape from line 1; `status` seeded free from the Gartner `(Legacy)` markers already held.
`outputs/enrichment-method.md` records the four-fetch budget, the Rungs-1-2-only failure rule
that deliberately suspends stop-at-Rung-3 for this pass, the `solution_type` no-default rule, and
the five parked fields with the reason and future source for each.

**16 · 2026-08-10 · Enrichment checkpoint — first 10 companies, then stop**
Fixed four-fetch budget per company, applied identically: `/llms.txt`, homepage, product page,
one discretionary. Mean **3.4 fetches**, 45 HTTP requests total, page text committed to
`sources/raw/vendors/` so every quoted field is checkable. **9 of 10 had an `llms.txt`** and it
earned its slot — it named the product and pricing pages directly.
**1 unreachable:** Adobe terminates the stream on both `adobe.com` and `business.adobe.com`;
recorded, not retried, not filled from memory.
Fill rates split sharply: description, value proposition, website **90%**, functionality and
channels **80%** — but `solution_type` **10%**, `named_clients` **10%**, `founded_year` **20%**,
`business_model` **30%**, `status` **0%**. Vendors do not publish deployment models on the pages
a marketing visitor sees, which is a finding about disclosure rather than a failure of the pass.
Caveat that governs the 25%-at-60 rule: these 10 are the **broadest** companies in the set, so
these rates are an optimistic ceiling, not a sample mean.

**17 · 2026-08-11 · All 237 companies enriched**
Twelve batches under a fixed four-fetch budget, 1,344 HTTP requests, mean 3.4 fetches per
reachable company. **192 enriched, 45 unreachable (19%).** Verification passes on all eleven
checks: no original field mutated, budget never exceeded, every populated cell carries
provenance, every quoted value present in its own capture, no company enriched from an
unconfirmed domain.
Fill rates split sharply by position, so they are reported split: **head (1–60) vs tail
(61–237)** — website 85/80, description 83/75, value proposition 83/68, functionality 68/51,
channels 65/49. The first ten were the broadest companies in the set and their 90% was a
ceiling, exactly as flagged at the checkpoint.
**`solution_type` finished at 13 of 237 (5%), every one `INFERRED`, none defaulted.** Vendors do
not publish deployment models on public marketing pages. That is a finding about disclosure.
Two defects caught by verification rather than by luck: a relaxed identity rule filed
`constant.com` (a cloud provider) under Constant Contact, and four domain-parking pages passed
identity by carrying the company name in their title. Both fixed, the bad record purged with its
capture, and every earlier resolution re-audited.

---

## Where it stands

All 10 IN classifications accepted and exported. Canonical store is **`outputs/companies.jsonl`**
(237 companies, one per line) with `outputs/companies-index.md` (16 KB) as the context anchor.
**All 237 enriched from vendor sites: 192 reachable, 45 unreachable and listed in
`outputs/blocked-domains.md` for a later human-transport pass.**

**The binding constraint is G2 coverage: 65 of 1,810 listings (3.6%).** The Gartner half is
complete at 352 of 352. Closing the G2 half needs ~111 paginated pastes; nothing else in the
pipeline is blocked.

**Also open:** G2 Mobile Marketing Software (the only G2 counterpart to Gartner's Mobile
Marketing Platforms), Conversational Marketing Solutions still BOUNDARY, and Account Data
Management an OUT that could flip.

**Open structural gaps, not tasks:** demand-side evidence exists for none of competitor classes
2–7. No funding data from any source. Russian, Turkish and Georgian are excluded from Gartner by
policy and censored on G2 by sanctions compliance. No vendor row anywhere is yet
`corroborated: yes` — every source so far is self-declared.
