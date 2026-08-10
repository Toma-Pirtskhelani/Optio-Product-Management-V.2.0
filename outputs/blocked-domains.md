# Blocked and unresolved domains — handoff to a later human-transport pass

Companies this pass could not reach at Rungs 1–2. **No paste was requested during the pass**
and **no user-agent was spoofed** to get past a refusal.

**19 of 130 attempted (15%).**

| Company | Cause | Best HTTP | Candidates tried |
|---|---|---|---|
| Adobe | HTTP 301 | 301 | adobe.com, www.adobe.com, adobe.io, adobe.ai, www.adobe.ai, adobe.co, www.adobe. |
| Capillary Technologies | served a page that did not identify the company (parked, for-sale, or a different owner) | 200 | capillarytechnologies.com, capillarytechnologies.io, www.capillarytechnologies.i |
| Cisco Systems | served a page that did not identify the company (parked, for-sale, or a different owner) | 200 | ciscosystems.com, www.ciscosystems.com, ciscosystems.io, www.ciscosystems.io, ci |
| Constant Contact | blocked (403/401/429) | 403 | constantcontact.com, www.constantcontact.com, constantcontact.io, www.constantco |
| Datorama | served a page that did not identify the company (parked, for-sale, or a different owner) | 200 | datorama.com, datorama.io, www.datorama.io, datorama.ai, www.datorama.ai, datora |
| FollowAnalytics | served a page that did not identify the company (parked, for-sale, or a different owner) | 200 | followanalytics.com, followanalytics.io, www.followanalytics.io, followanalytics |
| Fresh Relevance | blocked (403/401/429) | 403 | freshrelevance.com, freshrelevance.io, www.freshrelevance.io, freshrelevance.ai, |
| Freshworks | blocked (403/401/429) | 403 | freshworks.com, www.freshworks.com, freshworks.io, www.freshworks.io, freshworks |
| inConcert | blocked (403/401/429) | 403 | inconcert.com, www.inconcert.com, inconcert.io, inconcert.ai, www.inconcert.ai,  |
| MessageGears | blocked (403/401/429) | 403 | messagegears.com, www.messagegears.com, messagegears.io, www.messagegears.io, me |
| Mindmatrix | HTTP 503 | 503 | mindmatrix.com, www.mindmatrix.com, mindmatrix.io, www.mindmatrix.io, mindmatrix |
| NewZapp | blocked (403/401/429) | 403 | newzapp.com, www.newzapp.com, newzapp.io, www.newzapp.io, newzapp.ai, www.newzap |
| PAR | served a page that did not identify the company (parked, for-sale, or a different owner) | 200 | par.com, par.io, www.par.io, par.ai, www.par.ai, par.co, www.par.co |
| SAP | blocked (403/401/429) | 403 | sap.com, www.sap.com, sap.io, www.sap.io, sap.ai, www.sap.ai, sap.co, www.sap.co |
| SAS | blocked (403/401/429) | 403 | sas.com, sas.io, sas.ai, www.sas.ai, sas.co, www.sas.co |
| Swrve | blocked (403/401/429) | 403 | swrve.com, www.swrve.com, swrve.io, www.swrve.io, swrve.ai, www.swrve.ai, swrve. |
| Webmaxy | served a page that did not identify the company (parked, for-sale, or a different owner) | 200 | webmaxy.com, webmaxy.io, www.webmaxy.io, webmaxy.ai, www.webmaxy.ai, webmaxy.co |
| Wigzo | served a page that did not identify the company (parked, for-sale, or a different owner) | 200 | wigzo.com, wigzo.io, www.wigzo.io, wigzo.ai, www.wigzo.ai, wigzo.co, www.wigzo.c |
| Zeta | blocked (403/401/429) | 401 | zeta.com, www.zeta.com, zeta.io, zeta.ai, zeta.co |

## Cause breakdown

- **blocked (403/401/429)** — 10
- **served a page that did not identify the company (parked, for-sale, or a different owner)** — 7
- **HTTP 301** — 1
- **HTTP 503** — 1

Each remains a full record in `companies.jsonl` with `unreachable: true` and its reason.
None was dropped; none was filled from memory.

**Name-derived domain guessing has a structural limit.** Where a listing name is not the web
brand — Zeta for Zeta Global, Capillary Technologies for capillarytech.com — no candidate ladder
reaches it. Those need the vendor URL from a source that publishes it.
