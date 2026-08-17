# Finding the ahead-of-the-curve vendors — method, verification, and what today's evidence supports

Written 2026-08-17 in response to a request for the five most innovative companies in the store,
ranked on technological solutions, value propositions, pipeline, product capability and UX.

**Conclusion first: that ranking cannot be produced from the current evidence base, and the
attempt would produce a confident list that is wrong.** This file shows why with numbers, sets
out the method that would answer the question, and defines how the answer would be falsified
rather than confirmed. It ends with the one part of the ranking today's evidence *does* support
— which is the bottom, not the top.

---

## 1 · What we hold, against what was asked

| Asked for | In the store | Usable? |
|---|---|---|
| Value propositions | `value_proposition`, `description_own` — 186 / 208 of 237 | Marketing copy, verbatim. Usable **as copy**, not as capability |
| Technological solutions | `functionality` — 146 companies, 855 items | **Section headings scraped by position.** Braze's entire entry is its trademarked slogan |
| Product capabilities | same field | same defect |
| Pipeline / roadmap | nothing | **No** |
| UX | nothing — no screenshots, no usability data, no trial access | **No** |

Two of the five inputs are absent outright. One is a heading scraper's output
(`LEARNINGS.md` #18). That leaves marketing copy, and the strongest thing that can be built from
marketing copy is a measurement of marketing copy.

---

## 2 · Proof that the obvious method fails

The obvious method is to score AI/agentic language across `value_proposition`,
`description_own` and `functionality`. Ran it over all 216 companies carrying text. **104 of 216
(48%) mention AI at all**, so the metric discriminates at least. Then check where it puts
companies whose position we can independently characterise:

| Company | Rank of 216 | AI terms | Independent marker |
|---|---:|---:|---|
| Salesforce | **2** | 7 | the largest incumbent in the set |
| Oracle | **11** | 5 | Gartner **Legacy** marker on Datalogix |
| Precisely | **17** | 4 | Gartner **Legacy** marker on Portrait Dialogue |
| SAP | 66 | 1 | Gartner **Legacy** marker on SAP Marketing Cloud |
| Braze | **99** | 1 | named by the requester as ahead of the curve |
| Zeta | **108** | 0 | named by the requester as ahead of the curve |

**The metric ranks the two exemplars 99th and 108th, below three companies a third party has
marked Legacy.** It is not a weak proxy for innovation; it is inversely related to it here. What
it actually measures is **how recently a vendor rewrote its homepage** — and the vendors with
the largest marketing budgets rewrite most often.

A second, independent demonstration from the pilot in §5: **Klaviyo** scores in the top 20 on AI
language, and its published API changelog's most recent entry is **2025-06-17** — fourteen months
stale. Claim density and shipping cadence disagree, and only one of them is a behaviour.

**Do not rank on stated capability. Every vendor in this category claims agentic AI in 2026;
the claim carries no information.**

---

## 3 · The method: rank on what a company shipped, not what it says

The organising principle is the repo's own source-class rule. `SELF-DECLARED` evidence is what a
vendor asserts; `REVEALED-BEHAVIOR` is what it had to actually do. **Innovation claims are worth
grading only at the second.** Signals, strongest first:

| # | Signal | Class | Why it is hard to fake | Obtainable |
|---|---|---|---|---|
| 1 | **Shipping cadence** — dated release notes / changelog: entries per quarter, recency of the latest | REVEALED | Each entry is a dated commitment to a shipped change. A dead changelog is a dead product | Yes — proven in §5 |
| 2 | **Documented API surface** — do the marketed primitives exist as endpoints? Is there an agent/LLM/streaming API, an MCP server, webhooks? | REVEALED | A documented endpoint is load-bearing; a homepage banner is not | Yes — docs sites are rarely blocked |
| 3 | **Claim-to-doc gap** — capabilities marketed on the homepage that appear nowhere in the docs | DERIVED | Isolates vapour directly. **The single most diagnostic measure available** | Yes — needs 1 and 2 |
| 4 | **Job postings naming a stack** | REVEALED | Hiring is expensive and forward-looking | Yes, unbuilt |
| 5 | **Public code** — GitHub org: SDK breadth, commit recency | REVEALED | Commits are dated and attributable | Yes, partial coverage |
| 6 | **Third-party decline markers** — Gartner `(Legacy)` | REVEALED-ish | A third party, not the vendor, saying the product is end-of-road | **Already in the store** |
| 7 | Analyst position movement over time | MODELED | lagging, and we hold no time series | No |
| 8 | Marketing language density | SELF-DECLARED | §2 shows it is inverted | Do not use |

**Grading rule.** An innovation claim reaches `CORROBORATED` only with two sources of *different*
class — e.g. docs describe an agent API (self-declared) **and** the changelog shows dated releases
against it (revealed). Two marketing pages agreeing is not corroboration; their errors correlate.

---

## 4 · Verification — designed to break the list, not confirm it

A ranking that survives only tests designed to confirm it is worthless. Six gates:

1. **Pre-registered falsifiers.** Before scoring, write down per company what would prove it *not*
   ahead: changelog silent >6 months; marketed capability absent from docs; no API for the
   flagship claim; SDKs unchanged in a year. Findings recorded whether or not they suit the
   ranking.
2. **Negative controls, already in hand.** Seven companies carry Gartner `(Legacy)` markers —
   Oracle, SAP, Microsoft, SAS, Upland, Precisely, SpiceSend. **If the method scores a
   Legacy-marked product as ahead of the curve, the method is broken and the run is void.** The
   §2 metric fails this immediately: Oracle 11th, Precisely 17th.
3. **Blind scoring.** Strip vendor names and brand words from changelogs and docs before scoring.
   Brand halo is the main contaminant in innovation judgments, and Salesforce at rank 2 is what
   it looks like unblinded.
4. **Rank stability.** Re-run with inputs shuffled and paraphrased. Ranks that move more than a
   band or two are noise being read as signal.
5. **Both ends reported.** `CLAUDE.md` prohibition 4 rejects winners-only output. The
   behind-the-curve five ship with the ahead-of-the-curve five, or neither ships.
6. **Identity gate first — see §6.** A ranking is only as good as knowing which company each row
   describes.

**What the method still cannot do.** It measures *shipping*, which is the best available proxy
and not the same thing as innovation. A company can ship weekly and ship nothing that matters. It
cannot see private roadmaps, unlaunched work, or anything under NDA. And it cannot assess UX at
all without product access. Stated so the output is not read as more than it is.

---

## 5 · Feasibility pilot — run 2026-08-17

Three probes, to test whether signal 1 is obtainable and whether it discriminates.

| Vendor | URL | Result |
|---|---|---|
| Braze | `braze.com/docs/help/release_notes/` | **Monthly cadence, latest 2026-07-23** — 5 dated releases across 4 months, current to within a month |
| Klaviyo | `developers.klaviyo.com/en/docs/changelog` | **Latest 2025-06-17 — 14 months stale**; prior entries 2024 |
| Customer.io | `docs.customer.io/journeys/release-notes/` | **404** — guessed URL wrong |

**Three things this settles.** The signal exists, is dated, and is machine-readable. It
discriminates — Braze and Klaviyo separate cleanly, and in the opposite direction to §2's
language metric. And **URL guessing fails**, exactly as domain guessing failed in the enrichment
pass: discovery must drive it (`/llms.txt`, `robots.txt` sitemap, docs-site search), never a
guessed path. The Klaviyo row also needs a caveat recorded with it — an *API* changelog is not
the whole product's changelog, and treating one as the other would misjudge the company.

---

## 6 · Blocker — the base is not clean

Seven records describe the **wrong company** (`logs/incidents.md` I-0002), found because the
requester's own remark about Zeta did not match the store. `Zeta` was enriched from `zeta.tech`,
a banking card-issuing firm, while its Gartner products — Selligent, Cheetah Digital, Zeta
Marketing Platform — identify **Zeta Global**, whose platform is *Athena by Zeta™*: the exact
product named in the request. Also wrong: MINT, Trueblue, CAKE, Insightly, Marigold, Levitate.

**Ranking innovation across a set containing a staffing firm, a productivity suite, an
alternative-energy company and a parked domain is not a ranking.** These must be re-enriched
against the right domains before any scoring run.

---

## 7 · What today's evidence *does* support — and it is the bottom of the list

Asymmetry worth stating plainly: **the store can evidence which companies are behind, and cannot
evidence which are ahead.** Behind has a third-party marker; ahead has only self-description.

**Behind the curve — `SINGLE-SOURCE`, Gartner, third-party-declared:**

| Company | Legacy-marked product |
|---|---|
| SAS | SAS Marketing Automation; SAS Real-Time Decision Manager |
| Upland | BlueVenn |
| Oracle | Datalogix |
| Microsoft | Dynamics CRM |
| **SAP** | **SAP Marketing Cloud** |
| Precisely | Portrait Dialogue |
| SpiceSend | SpiceSend Email Marketing Tool |

The requester's third example is **independently confirmed**: SAP is Legacy-marked by Gartner, by
a third party rather than by us. The two "ahead" examples are not confirmed by anything in the
store — which is a statement about our evidence, not about Braze and Zeta Global.

**No top five is published here.** Naming five without evidence, in a file that would be read as
research output, is the failure this repository was built to prevent.

---

## 8 · The pass that would answer it

**Scope.** All 237 companies, uniform budget — no depth tiers, same comparability control as the
enrichment pass. Order: (0) re-enrich the 7 wrong-identity records and add the product-name
cross-check as verification check 16; (1) discover the docs/changelog root per company via
`/llms.txt`, `robots.txt` sitemap, then docs-site search — **never a guessed path**; (2) capture
dated release entries for 24 months; (3) capture the API/docs surface; (4) compute the
claim-to-doc gap against `value_proposition` already stored.

**Budget.** ~3 fetches per company, ~700 total. G2 and Gartner blocks do not apply — these are
vendor docs sites, and Rung 1-B browser transport (`logs/fetch-log.md` pass 03) covers what
`WebFetch` cannot reach.

**Output.** Per company: cadence, recency, doc surface, claim-to-doc gap, each with rung, grade
and source class; every company that produced no signal listed as `UNKNOWN` rather than omitted,
so absence of evidence never reads as evidence of absence. Then top five **and** bottom five,
with the pre-registered falsifiers attached to each, and the Legacy-marked control group's scores
printed as the method's own audit.
