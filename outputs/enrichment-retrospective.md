# Enrichment pass — retrospective and next-phase plan

Written after all 237 companies were processed. Part 1 records what happened, part 2 judges
how well the method spent its effort, part 3 is the plan that follows from part 2.

---

## 1. What happened

| Step | Outcome |
|---|---|
| Store migrated to JSONL | 237 records, verified lossless on 10 checks |
| Checkpoint: 10 companies hand-filled | Schema approved; hand-filling then abandoned |
| Extractor built, first 10 re-run | All 237 produced by one deterministic method |
| Gate at 70 | 4 fields under the 25% floor; 4 decisions taken |
| Batches 4–12 | All 237 attempted, 12 commits |
| Verification | **11 checks, all green** |

**Two defects were caught by verification rather than by luck**, and both would have been
invisible in the output:

1. **A relaxed identity rule filed the wrong company.** `constant.com` resolved for Constant
   Contact and is an unrelated cloud-infrastructure provider. Four domain-parking pages passed
   identity the same way, carrying the company name in their title. Fixed; the bad record and
   its capture were purged; every earlier resolution re-audited.
2. **Extraction read more text than was committed.** A quoted value could cite evidence absent
   from the repository. Truncation now happens before extraction.

A third defect cost a batch: the driver wrote results only after the whole loop, so one page
serving non-UTF-8 bytes discarded twenty companies of work. It now persists per company.

---

## 2. Was the effort well spent?

**1,344 HTTP requests → 192 enriched companies.**

### Where the requests went

| | Requests | Share |
|---|---|---|
| **Guessing domains from company names** | **458** | **34%** |
| Fetching content pages | 886 | 66% |

**Every one of the 458 domain-guessing requests belongs to a company we failed to reach.**
The 45 unreachable consumed 458 requests and produced nothing. That is the single largest
inefficiency in the pass, and it is structural: a candidate ladder built from a listing name
cannot reach a vendor whose web brand differs from it — *Zeta* for Zeta Global,
*Capillary Technologies* for capillarytech.com.

### Yield per fetch slot

| Slot | Successful fetches | What it produced |
|---|---|---|
| 1 · `/llms.txt` | 99 | Page map; directly improved slots 3–4. **Cheap and worth keeping** |
| 2 · homepage | 192 | `description_own` 77%, `value_proposition` 72% — **the highest-yield fetch by far** |
| 3 · product | 146 | `functionality` 56%, `channels` 53% |
| 4 · pricing/trust | 109 | 81 pricing rows, **13 `solution_type` rows** |

**Slot 4 is the weak one.** 109 fetches produced pricing for 81 companies — acceptable — but
`solution_type` for 13. As a *deployment-model* probe it failed; as a *pricing* probe it worked.

### What the fixed budget bought

It worked exactly as intended and is the reason the numbers mean anything: `UNKNOWN` here means
*not published on four pages of the vendor's own site*, uniformly, for every company. Verified —
the budget was never exceeded once in 237 records. Without it, the head-versus-tail gradient
(value proposition 83% vs 68%) would have been indistinguishable from uneven effort.

### How I would do it differently

1. **Do not guess domains.** 34% of all traffic went to guessing, with a 19% failure rate.
   Get the URL from a source that publishes it, then let the identity gate validate the fetch.
2. **Never try alternates only at the top level.** For the 16 vendors that returned 403 to
   `www`, we never tried `docs.`, `developers.`, `sitemap.xml` or `/llms.txt` — the exact
   Rung-2 pattern that rescued G2 earlier in this study. That was an oversight, not a limit.
3. **Split slot 4.** Pricing and deployment are different questions; one page cannot answer both.
4. **Keep everything else.** Fixed budget, identity confirmation, deterministic extraction,
   extract-only-what-is-committed, per-cell grading. These are what made the pass auditable.

---

## 3. Two feasibility tests that shaped the plan

Both were run before planning, and both changed it.

**Wikidata — usable, but only as a candidate generator.** Coverage of this population is
patchy and disambiguation is dangerous: *Klaviyo*, *HubSpot*, *Twilio* and *Optimove* resolve
correctly, while *Braze*, *Netmera* and *Xtremepush* have no entity at all, and **"Bloomreach"
returns an open-source CMS** — the `constant.com` failure mode again, in a new source.

> **Therefore Wikidata is never trusted directly.** It proposes a domain; our existing identity
> gate disposes. A proposed domain is fetched and must still identify the company before any
> value is recorded. This cannot corrupt the data, because nothing bypasses the gate.

**DNS/MX liveness — rejected.** The intuition was that a dead company has no mail record. It is
false: `datorama.com` and `followanalytics.com` both resolve with live MX records years after
being absorbed. It would have produced a confident "alive" signal for companies that no longer
exist. **Not used.**

---

## 4. Plan for the next phase

Ordered by evidential value per unit of effort. **Nothing here modifies an existing
vendor-sourced cell.**

### Phase A — Wikidata as a domain oracle *(attacks the 45 unreachable)*
Query Wikidata for each unreachable company, take `P856 official website` as a **candidate
domain only**, and re-run the standard enrichment against it. The identity gate is unchanged, so
a wrong Wikidata match fails exactly as a wrong guess does today.

### Phase B — Rung-2 alternates for blocked vendors *(attacks the 16 × 403)*
For every vendor blocked at `www`, try `/llms.txt`, `/sitemap.xml`, and `docs.` / `developers.` /
`help.` subdomains before declaring it unreachable. This is the protocol's own Rung-2 rule,
which this pass never applied at vendor level.

### Phase C — corroboration, the study's largest structural hole
**No row anywhere in this study is `corroborated: yes`**, because every source so far is
`SELF-DECLARED`. Where a Wikidata entity is confirmed by domain match against a vendor site we
already fetched, `founded_year` and country gain a **second, differently-biased source**.
Wikidata is third-party curated: its error modes are not the vendor's error modes. That is the
first genuine corroboration available to this study, and it is free.

### Phase D — new companies from an unblocked source
The company set is capped by what we hold: Gartner is complete at 352, but **G2 gave only 65 of
1,810 listings (3.6%)**. The Shopify App Store is open at Rungs 1–2, and its
`email-marketing`, `sms-marketing`, `web-push` and `abandoned-cart` categories are IN under our
own test. It adds a differently-shaped population — SMB and e-commerce — which is exactly the
segment our analyst-weighted sources under-represent.

**Discipline for Phase D, unchanged from the main study:** vendors enter as their own rows with
`source: shopify`, their own coverage type, and are never merged into the Gartner/G2 counts.
A marketplace is cheap supplementary signal, not an equal partner.

### Explicitly not attempted
- **G2 pagination** — 1,745 unseen listings needing ~111 human-transported pastes. The single
  largest known gap, and not automatable. It stays recorded rather than quietly closed.
- **`web.archive.org`** — blocked at tool level.
- **User-agent spoofing** to defeat the 16 × 403. The line held all pass and holds here.
