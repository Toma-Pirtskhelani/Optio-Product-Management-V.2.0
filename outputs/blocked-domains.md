# Blocked domains — handoff to a later human-transport pass

Companies this pass could not reach at Rungs 1–2. **No paste was requested during the pass** —
pausing on each of 237 companies is not a workflow — so they accumulate here instead.

**No user-agent spoofing was used to get past any of these.** Where a site refuses a
non-browser request, that refusal is recorded as the finding it is.

**9 of 70 companies attempted so far (13%).**

| Company | Cause | Best HTTP | Candidates tried |
|---|---|---|---|
| Adobe | HTTP 301 | 301 | adobe.com, www.adobe.com, adobe.io, adobe.ai, www.adobe.ai, adobe.co, www.adobe.co |
| Cisco Systems | HTTP 200 | 200 | ciscosystems.com, www.ciscosystems.com, ciscosystems.io, www.ciscosystems.io, ciscosystems |
| Constant Contact | blocked (403/401/429) | 403 | constantcontact.com, www.constantcontact.com, constantcontact.io, www.constantcontact.io,  |
| MessageGears | blocked (403/401/429) | 403 | messagegears.com, www.messagegears.com, messagegears.io, www.messagegears.io, messagegears |
| Mindmatrix | HTTP 503 | 503 | mindmatrix.com, www.mindmatrix.com, mindmatrix.io, www.mindmatrix.io, mindmatrix.ai, www.m |
| NewZapp | blocked (403/401/429) | 403 | newzapp.com, www.newzapp.com, newzapp.io, www.newzapp.io, newzapp.ai, www.newzapp.ai, newz |
| Pegasystems | HTTP 200 | 200 | pegasystems.com, pegasystems.io, pegasystems.ai, pegasystems.co |
| SAP | blocked (403/401/429) | 403 | sap.com, www.sap.com, sap.io, www.sap.io, sap.ai, www.sap.ai, sap.co, www.sap.co |
| Wigzo | HTTP 200 | 200 | wigzo.com, wigzo.io, www.wigzo.io, wigzo.ai, www.wigzo.ai, wigzo.co, www.wigzo.co |

## Cause breakdown

- **blocked (403/401/429)** — 4
- **HTTP 200** — 3
- **HTTP 301** — 1
- **HTTP 503** — 1

Each remains a full record in `companies.jsonl` with `unreachable: true` and its reason.
None was dropped, and none was filled from memory.
