# Blocked and unresolved domains — handoff to a later human-transport pass

Companies this pass could not reach at Rungs 1–2. **No paste was requested during the pass**
and **no user-agent was spoofed** to get past a refusal.

**10 of 237 attempted (4%).**

| Company | Cause | Best HTTP | Candidates tried |
|---|---|---|---|
| AT Internet | served a page that did not identify the company (parked, for-sale, or a different owner) | 200 | atinternet.com, atinternet.io, www.atinternet.io, atinternet.ai, www.atinternet. |
| Beaconsmind | served a page that did not identify the company (parked, for-sale, or a different owner) | 200 | beaconsmind.com, beaconsmind.io, www.beaconsmind.io, beaconsmind.ai, www.beacons |
| Datorama | served a page that did not identify the company (parked, for-sale, or a different owner) | 200 | datorama.com, datorama.io, www.datorama.io, datorama.ai, www.datorama.ai, datora |
| FollowAnalytics | served a page that did not identify the company (parked, for-sale, or a different owner) | 200 | followanalytics.com, followanalytics.io, www.followanalytics.io, followanalytics |
| Fresh Relevance | blocked (403/401/429) | 403 | freshrelevance.com, freshrelevance.io, www.freshrelevance.io, freshrelevance.ai, |
| Longtail UX | served a page that did not identify the company (parked, for-sale, or a different owner) | 200 | longtailux.com, www.longtailux.com, longtailux.io, www.longtailux.io, longtailux |
| PAR | served a page that did not identify the company (parked, for-sale, or a different owner) | 200 | par.com, par.io, www.par.io, par.ai, www.par.ai, par.co, www.par.co |
| Spectrm | served a page that did not identify the company (parked, for-sale, or a different owner) | 200 | spectrm.com, www.spectrm.com, spectrm.io, spectrm.ai, www.spectrm.ai, spectrm.co |
| Striker Soft Solutions | served a page that did not identify the company (parked, for-sale, or a different owner) | 200 | strikersoftsolutions.com, www.strikersoftsolutions.com, strikersoftsolutions.io, |
| Wigzo | served a page that did not identify the company (parked, for-sale, or a different owner) | 200 | wigzo.com, wigzo.io, www.wigzo.io, wigzo.ai, www.wigzo.ai, wigzo.co, www.wigzo.c |

## Partially recovered — domain confirmed, marketing site still blocked

**9 companies** were reached only through a documentation, developer or support
subdomain after their marketing site refused automated access. That confirms the company is
live and the domain is correct. It establishes nothing about positioning, channels, pricing
or deployment, so those fields remain `UNKNOWN` — filling them from a docs page would mix two
different kinds of evidence under one field name.

| Company | Reached via |
|---|---|
| Adobe | https://experienceleague.adobe.com/en/docs |
| AfterShip | https://support.aftership.com/en |
| Constant Contact | https://knowledgebase.constantcontact.com/ |
| Freshworks | https://developers.freshworks.com/ |
| Mastercard | https://developer.mastercard.com/ |
| MessageGears | https://docs.messagegears.com/ |
| PostcardMania | https://help.postcardmania.com/ |
| PostGrid | https://docs.postgrid.com/ |
| Swrve | https://docs.swrve.com/ |

## Cause breakdown

- **served a page that did not identify the company (parked, for-sale, or a different owner)** — 9
- **blocked (403/401/429)** — 1

Each remains a full record in `companies.jsonl` with `unreachable: true` and its reason.
None was dropped; none was filled from memory.

**Name-derived domain guessing has a structural limit.** Where a listing name is not the web
brand — Zeta for Zeta Global, Capillary Technologies for capillarytech.com — no candidate ladder
reaches it. Those need the vendor URL from a source that publishes it.
