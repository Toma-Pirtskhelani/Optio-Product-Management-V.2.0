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

**18 · 2026-08-11 · Phases A–C: recovery, and the first corroboration in the study**
Retrospective first: the main pass spent **34% of all 1,344 requests guessing domains from
listing names**, and every one of those 458 requests belongs to a company it then failed to
reach. Two new sources were feasibility-tested before planning and both changed the plan —
**Wikidata covers only ~5% of this population and disambiguates badly** ("Bloomreach" returns an
open-source CMS), and **DNS/MX liveness was rejected outright** because `datorama.com` and
`followanalytics.com` still resolve with live mail records years after being absorbed.
**A:** Wikidata used only to *propose* a domain, never to supply values — it found
`capillarytech.com` for Capillary Technologies, the case a name-derived ladder could never reach.
**B:** Rung-2 alternates (`docs.`, `developers.`, `help.`, `/llms.txt`, `/sitemap.xml`) recovered
**9 companies**, all via documentation subdomains. Their marketing fields stay `UNKNOWN` and a
verification check enforces it: a docs page proves the company is live, not how it positions
itself. Unreachable **45 → 36**; the 403 bucket **16 → 8**.
**C:** Joined on **domain, never name**. 2 `founded_year` cells are now **CORROBORATED** — the
first non-self-declared agreement anywhere in this study — and 5 more gained a value their own
site never published. The gate rejected Brevo and Thryv, whose Wikidata entities still carry
pre-rename domains (`sendinblue.com`, `dexmedia.com`); logged as `C-0008` rather than accepted.
**Phase D (Shopify expansion) dropped by decision.**

**19 · 2026-08-11 · 36 human-transported pages close the unreachable gap to 2**
Four kinds of thing arrived under one name, and treating them alike would have been the whole
mistake: **24 vendor sites, 10 third-party pages, 2 vendor pages with no URL, 2 rejected**.
Classification took five attempts — furniture-matching called prose a page; a short-line test
called LinkedIn profiles pages, which they are; four files turned out to be **unattributed prose
followed by a real paste**, so the preamble is discarded and the URL anchors what counts.
**The identity gate now guards pastes too and earned itself at once:** PAR's paste is
Salesforce's *Pardot* page — "par" passed a naive substring test only because it sits inside
"Pardot" — and AT Internet's paste is Piano documentation that never names AT Internet.
**The pastes' real value was the address.** 19 companies were re-fetched from paste-supplied
domains, so their records are HTML-derived and comparable in kind with the rest — including
`capillarytech.com`, `inconcertcx.com`, `zeta.tech`, `in10stech.com`, `xiqinc.com`, which no
name-derived ladder reaches. Ten failed the gate on names shorter than four characters
(`IBM`, `Lob`, `SAS`, `xiQ`); the rule is now **split by provenance** — strict when a domain is
guessed, host-root sufficient when a human supplied it and the paste already named the company.
**7 paste-only records** where the site still refuses everything. `value_proposition` is *not*
extracted there: plain text has no `<h1>` and positional guessing returned "Partner Login" and
"Slide 2 of 6." A check enforces its absence. **8 third-party records** establish existence only.
Two acquisition claims were rejected because they sat in the discarded preamble; **Wigzo →
Shiprocket** and **Datorama → Salesforce** survive because the page itself says so (`C-0009`).
**Unreachable 45 → 2.** `description_own` +26, `channels` +17, `website` +19. `solution_type`
unchanged at 13 — even human transport does not make vendors publish deployment models.

**20 · 2026-08-12 · The industry list, and the extractor defect it exposed**
Derived the unique industry list and per-industry analytics from `industries_served`
(`scripts/industries.py` → `outputs/industries.md`, `outputs/industries.json`). Store untouched;
15 checks still pass. **81 industries, 358 vendor×industry claims, from 53 of 237 companies
(22.4%)** — 158 have the field `UNKNOWN`, 26 never had it. **The base is Gartner-shaped**: of the
53, 44 are Gartner-only, 7 in both, 2 G2-only — the 3.6% G2 coverage limit propagates straight
through. **39 of 81 industries rest on one vendor's site; the top 10 hold 50% of
claims.** Head: Financial Services 31, Retail 25, Healthcare 21, Ecommerce 18, Travel 17.
**The field is contaminated and the grade could not show it.** Of 369 distinct raw strings,
**182 are not industry claims** — nav, CTAs, product names, client names, a language switcher,
six Material-icon ligatures — all carrying `PRIMARY / rung 1`, correctly, because the *fetch*
was primary. SAS's whole list is a nav bar. Every string is published with its ruling and reason
in §4 rather than dropped. `vertical_focus`, computed from the raw list length, is contaminated
the same way and should not be used. `LEARNINGS.md` 18–19.

**21 · 2026-08-17 · An innovation ranking was requested; the base could not carry one**
Asked for the 5 most innovative vendors. **Not published, and the reason is measurable.** Scoring
AI/agentic language across 216 companies ranks **Salesforce 2nd, Oracle 11th and Precisely 17th
— the latter two carrying Gartner `(Legacy)` markers — while the two vendors named as ahead of
the curve rank 99th and 108th.** The metric measures how recently a homepage was rewritten.
Pilot on the right signal — dated release notes — separates Braze (monthly, latest 2026-07-23)
from Klaviyo's API changelog (latest 2025-06-17, 14 months stale), in the opposite direction.
**A user remark exposed 7 wrong-company records** (`I-0002`): `Zeta` was enriched from
`zeta.tech`, a card-issuing bank-tech firm, while its own Gartner products — Selligent, Cheetah
Digital — identify **Zeta Global** (*Athena by Zeta™*). Also MINT, Trueblue, CAKE, Insightly,
Marigold, Levitate. All 7 passed the identity gate, because the gate tests that a name matches,
and all 7 passed 15 checks, because those assert a chain is *recorded*, not *true*.
Method, verification design and the costed pass: `outputs/innovation-method.md`.

---

## Where it stands

All 10 IN classifications accepted and exported. Canonical store is **`outputs/companies.jsonl`**
(237 companies, one per line) with `outputs/companies-index.md` (16 KB) as the context anchor.
**All 237 processed: 211 enriched, 9 partially recovered, 7 paste-only, 8 third-party-only,
2 unreachable.** 220 have a confirmed website. 2 cells are `CORROBORATED`. 15 verification
checks pass, including four that police the boundaries between evidence types.

**The binding constraint is G2 coverage: 65 of 1,810 listings (3.6%).** The Gartner half is
complete at 352 of 352. Closing the G2 half needs ~111 paginated pastes; nothing else in the
pipeline is blocked.

**Blocking any vendor-level ranking:** 7 records describe the wrong company (`I-0002`) and are
not yet re-enriched. `outputs/industries.md` inherits them and must be recomputed after the fix,
not before. The sweep detects only wrong companies in an obviously *different* business — a wrong
company in the same business would pass every check we have.

**Also open:** G2 Mobile Marketing Software (the only G2 counterpart to Gartner's Mobile
Marketing Platforms), Conversational Marketing Solutions still BOUNDARY, and Account Data
Management an OUT that could flip.

**Open structural gaps, not tasks:** demand-side evidence exists for none of competitor classes
2–7. No funding data from any source. Russian, Turkish and Georgian are excluded from Gartner by
policy and censored on G2 by sanctions compliance. No vendor row anywhere is yet
`corroborated: yes` — every source so far is self-declared.
