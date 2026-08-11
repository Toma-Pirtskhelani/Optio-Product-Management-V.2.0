# Learnings

What this study has taught about method, stated so a later pass does not rediscover it.
Each entry is a rule, why it exists, and the specific incident that produced it.

---

## 1. A name is not an identity

**Rule.** Never accept a source, domain or record because a name matched. Require a second,
independent property to agree.

**Incidents.** `constant.com` resolved for Constant Contact and is an unrelated
cloud-infrastructure provider. `zeta.io` and `zeta.ai` were domain-parking pages carrying
"Zeta" in the title. Wikidata returns an **open-source CMS** for "Bloomreach". Three different
sources, one failure mode.

**What worked.** The join is the *domain*, never the name — and where a partial match is
unavoidable, the full company name must appear in the page body, with the proof snippet stored
on the record. This cost recall: Brevo and Thryv were rejected because Wikidata still lists
their pre-rename domains. **That is the right trade.** A false negative is a gap; a false
positive is a lie that looks like data.

## 2. Extract only from what you commit

**Rule.** Truncate first, then extract. Evidence that is not in the repository is not evidence.

**Incident.** The extractor read full page text while the capture stored the first 14,000
characters, so a quoted value could cite a sentence nobody could check. Found by a verification
assertion, not by reading output.

**Corollary.** Meta descriptions and `h1`s live in HTML attributes and never appear in body
text, so the capture must store the extracted signals too, or "verbatim" quietly becomes
unverifiable.

## 3. Fixed effort is what makes UNKNOWN mean something

**Rule.** Give every subject the same budget, record what was spent, and verify it was never
exceeded.

**Why.** With a fixed budget, `UNKNOWN` means *not published on four pages of the vendor's own
site* — a statement about the company. With variable effort it means *nobody looked hard
enough* — a statement about us, and indistinguishable from the first.

**Payoff.** It made the head-versus-tail gradient readable as a real property of the
population (value proposition 83% in the first 60 companies, 68% in the rest) rather than an
artefact of when a company was processed.

## 4. A grade that never varies is not a grade

**Rule.** Grade per cell. Use a row-level grade as a triage flag, never as a verdict.

**Incident.** Weakest-wins at row level drove every row to `UNKNOWN`, because early rows all
carried at least one unknown cell. The column stopped discriminating and would have been
ignored — worse than absent, because it occupied the space where a real signal belonged.

## 5. Boolean `false` is an answer, not an empty cell

**Incident.** The fill-rate counter treated `has_free_tier: false` as unfilled, reporting 14%
where the true coverage was 38%. It was caught **one batch before the gate that would have
killed the column on that number.**

**Rule.** Before a metric decides anything, check what it counts as missing.

## 6. Do not guess what a source will publish for you

**Incident.** 34% of all 1,344 HTTP requests were spent guessing domains from listing names,
and every one of those 458 requests belongs to a company we then failed to reach. A ladder built
from a listing name cannot find a vendor whose web brand differs from it — *Capillary
Technologies* → `capillarytech.com`. Wikidata found it in one query.

**Rule.** Get identifiers from a source that publishes them; use your own gate to validate.
Guessing is the most expensive way to be wrong.

## 7. Try the side doors before declaring a source closed

**Incident.** Sixteen vendors returned 403 at `www` and were written off. Trying `docs.`,
`developers.`, `help.`, `/llms.txt` and `/sitemap.xml` recovered **nine of them** — the same
Rung-2 pattern that had already rescued `research.g2.com` earlier in this study, simply never
applied at vendor level.

**Rule.** "Blocked" means blocked *at every path tried*. Enumerate the paths.

## 8. Recovering access is not recovering evidence

**Rule.** When a subject is reached by a different kind of page, record what that page proves
and refuse what it does not.

**Incident.** All nine recoveries came through documentation subdomains. Filling
`description_own` from `experienceleague.adobe.com` would have mixed two evidence types under
one field name and quietly broken every comparison built on it. Those records carry
`partially_recovered`, a confirmed website, and `UNKNOWN` marketing fields — **with a
verification check that enforces it.**

## 9. Agreement between sources that share a bias is an echo

**Rule.** Corroboration requires sources whose *error modes differ*, not merely sources that
are different.

**Payoff.** Gartner, G2 and vendor sites are all `SELF-DECLARED` — they reward investing in
being seen — so no row in this study was corroborated for its entire life. Wikidata is
third-party curated by people with no stake in the vendor, which is why two `founded_year`
cells could finally reach `CORROBORATED`. Two out of 237: small, and honestly earned.

## 10. Test a source before planning around it

**Rule.** Feasibility-test a new source before it enters a plan, and let the result change
the plan.

**Incidents.** Wikidata was tested and found to cover ~5% of this population and to
disambiguate badly, so it was demoted from *data source* to *candidate generator*. DNS/MX
liveness was tested and **rejected outright**: `datorama.com` and `followanalytics.com` still
resolve with live mail records years after being absorbed, so it would have asserted that dead
companies are alive.

## 11. Commit irreplaceable input before touching it

**Incident.** Thirteen human-pasted pages were destroyed by a reorganisation that ran before the
commit did. The rule "always commit pasted content" already existed; it did not say **when**.

**Rule.** Pasted content is committed on arrival, before being read, moved, renamed or parsed,
as its own commit. Never `rm -rf` a directory under `sources/`.

## 12. Persist incrementally, and name your own failures

**Incident.** A page served non-UTF-8 bytes and the strict decode killed a batch — and because
results were written only after the loop, twenty companies of work vanished, six already
fetched.

**Rule.** Persist after each unit. And record a harness error *as* a harness error: a subject
that failed because of our code must never be indistinguishable from one that refused us.

## 13. The verifier is part of the method, not a formality

Three of the defects above were caught by assertions rather than by reading output. Two of the
assertion failures turned out to be **bugs in the checker** — a whitespace-normalisation
mismatch, and a status value the verifier did not know about.

**Rule.** When a check fails, establish whether the data or the check is wrong before changing
either. Both outcomes are common.

## 14. Report what the evidence refuses to show

`solution_type` finished at **13 of 237 (5%)**, every value `INFERRED`, none defaulted. The
temptation was to loosen the inference rule until the column filled. The honest result is that
**vendors do not publish deployment models on public marketing pages** — a finding about
disclosure, not a failed field.

The same applies to the study's largest known gap: **G2 gave 65 of 1,810 listings (3.6%)**, and
that stays recorded rather than quietly closed.

---

## Costs worth budgeting next time

| | |
|---|---|
| Fetch cost, main pass | 1,344 HTTP requests → 192 enriched companies |
| Wasted on domain guessing | 458 requests (34%), all attributable to failures |
| Highest-yield fetch | Homepage — `description_own` 77%, `value_proposition` 72% |
| Lowest-yield fetch | Pricing/trust — 109 fetches → 13 `solution_type` rows |
| Recovery cost | Wikidata + Rung-2 alternates: 9 companies recovered, 45 → 36 unreachable |
