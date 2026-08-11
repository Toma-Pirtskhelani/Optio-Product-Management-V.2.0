# Unreachable companies — paste worksheet

**36 companies** this pass could not reach at Rungs 1–2. Everything else in the study is
complete; these are the whole remaining gap.

---

## How to give me the info (fastest first)

**Option 1 — paste page text (best).** For a company, open its site, select all, copy, and save
as `sources/raw/vendors-pasted/<company_id>.txt`. Homepage alone is useful; homepage + product
page is ideal. I extract with the *same deterministic rules* used for the other 201, so the
records stay comparable rather than becoming a hand-made exception.

**Option 2 — just give me the URL.** If a company's real domain is not in the *Tried* column
below, tell me the correct one and I will fetch it myself. **For several of these the only
thing missing is the right address.**

**Option 3 — skip it.** `UNKNOWN` with a recorded reason is a legitimate result. Do not invent
anything; a gap is honest, a guess is a defect.

> Paste the page as it is. Do not summarise, tidy or translate it — the raw text is the
> evidence, and I quote from it verbatim.

---

## Why each one failed

| Cause | Count | What it means |
|---|---|---|
| Served a page that did not identify the company | 26 | A parked/for-sale domain, or a different owner. Often the company's real web brand differs from its listing name (*Zeta* → Zeta Global) |
| Blocked 403/401/429 | 8 | The domain is right and the site refused a non-browser request. **A browser will open these fine** |
| No DNS / no response | 1 | Nothing answered on any candidate |
| HTTP 503 | 1 | Server error at the time of the attempt |

---

## The 36

`Cats` = how many of our IN categories list it. `Products` are the exact names Gartner or G2
carry, which is the reliable way to identify the right company — the listing name alone is
what misled the resolver in the first place.

### 1. SAP

- `company_id`: **`sap`**  → save as `sources/raw/vendors-pasted/sap.txt`
- **Cause:** blocked 403 — domain is right, browser will work
- **Tried:** `sap.com, sap.io, sap.ai, sap.co`
- **Listed as:** SAP Engagement Cloud, SAP Marketing Cloud (Legacy)
- **In categories:** Multichannel Marketing Hubs, Email Marketing (Transitioning to Email Marketing Platforms), B2B Marketing Automation Plat  (4 cats · gartner)

### 2. Wigzo

- `company_id`: **`wigzo`**  → save as `sources/raw/vendors-pasted/wigzo.txt`
- **Cause:** wrong owner / parked — real domain unknown
- **Tried:** `wigzo.com, wigzo.io, wigzo.ai, wigzo.co`
- **Listed as:** Wigzo
- **In categories:** Email Marketing (Transitioning to Email Marketing Platforms), B2B Marketing Automation Platforms, Mobile Marketing Platf  (3 cats · gartner)

### 3. Zeta

- `company_id`: **`zeta`**  → save as `sources/raw/vendors-pasted/zeta.txt`
- **Cause:** blocked 403 — domain is right, browser will work
- **Tried:** `zeta.com, zeta.io, zeta.ai, zeta.co`
- **Listed as:** Selligent, Cheetah Digital, Zeta Marketing Platform
- **In categories:** Multichannel Marketing Hubs, Email Marketing (Transitioning to Email Marketing Platforms), Mobile Marketing Platforms  (3 cats · gartner)

### 4. Capillary Technologies

- `company_id`: **`capillary-technologies`**  → save as `sources/raw/vendors-pasted/capillary-technologies.txt`
- **Cause:** wrong owner / parked — real domain unknown
- **Tried:** `capillarytechnologies.com, capillarytechnologies.io, capillarytechnologies.ai, capillarytechnologies.co, capil`
- **Listed as:** Capillary Engage+, SessionM Plaform
- **In categories:** Multichannel Marketing Hubs, Mobile Marketing Platforms  (2 cats · gartner)

### 5. Cisco Systems

- `company_id`: **`cisco-systems`**  → save as `sources/raw/vendors-pasted/cisco-systems.txt`
- **Cause:** wrong owner / parked — real domain unknown
- **Tried:** `ciscosystems.com, ciscosystems.io, ciscosystems.ai, ciscosystems.co, cisco-systems.com, cisco-systems.io`
- **Listed as:** Webex Campaign, Cisco Spaces
- **In categories:** Mobile Marketing Platforms, Location Based Marketing Software  (2 cats · gartner)

### 6. inConcert

- `company_id`: **`inconcert`**  → save as `sources/raw/vendors-pasted/inconcert.txt`
- **Cause:** blocked 403 — domain is right, browser will work
- **Tried:** `inconcert.com, inconcert.io, inconcert.ai, inconcert.co`
- **Listed as:** Infunnel
- **In categories:** Multichannel Marketing Hubs, B2B Marketing Automation Platforms  (2 cats · gartner)

### 7. Mindmatrix

- `company_id`: **`mindmatrix`**  → save as `sources/raw/vendors-pasted/mindmatrix.txt`
- **Cause:** HTTP 503
- **Tried:** `mindmatrix.com, mindmatrix.io, mindmatrix.ai, mindmatrix.co`
- **Listed as:** Mindmatrix Bridge, MSP Advantage Program
- **In categories:** Multichannel Marketing Hubs, B2B Marketing Automation Platforms  (2 cats · gartner)

### 8. NewZapp

- `company_id`: **`newzapp`**  → save as `sources/raw/vendors-pasted/newzapp.txt`
- **Cause:** blocked 403 — domain is right, browser will work
- **Tried:** `newzapp.com, newzapp.io, newzapp.ai, newzapp.co`
- **Listed as:** NewZapp
- **In categories:** Multichannel Marketing Hubs, Email Marketing (Transitioning to Email Marketing Platforms)  (2 cats · gartner)

### 9. Webmaxy

- `company_id`: **`webmaxy`**  → save as `sources/raw/vendors-pasted/webmaxy.txt`
- **Cause:** wrong owner / parked — real domain unknown
- **Tried:** `webmaxy.com, webmaxy.io, webmaxy.ai, webmaxy.co`
- **Listed as:** WebMaxy eGrowth
- **In categories:** Multichannel Marketing Hubs, Email Marketing (Transitioning to Email Marketing Platforms)  (2 cats · gartner)

### 10. Amazing Mail

- `company_id`: **`amazing-mail`**  → save as `sources/raw/vendors-pasted/amazing-mail.txt`
- **Cause:** wrong owner / parked — real domain unknown
- **Tried:** `amazingmail.com, amazingmail.io, amazingmail.ai, amazingmail.co, amazing-mail.com, amazing-mail.io, amazing-ma`
- **Listed as:** Amazing Mail
- **In categories:** Direct Mail Automation Software  (1 cats · gartner)

### 11. AT Internet

- `company_id`: **`at-internet`**  → save as `sources/raw/vendors-pasted/at-internet.txt`
- **Cause:** wrong owner / parked — real domain unknown
- **Tried:** `atinternet.com, atinternet.io, atinternet.ai, atinternet.co, at-internet.com, at-internet.io, at-internet.ai, `
- **Listed as:** AT Internet Analytics Suite
- **In categories:** Multichannel Marketing Hubs  (1 cats · gartner)

### 12. Beaconsmind

- `company_id`: **`beaconsmind`**  → save as `sources/raw/vendors-pasted/beaconsmind.txt`
- **Cause:** wrong owner / parked — real domain unknown
- **Tried:** `beaconsmind.com, beaconsmind.io, beaconsmind.ai, beaconsmind.co`
- **Listed as:** Beaconsmind
- **In categories:** Location Based Marketing Software  (1 cats · gartner)

### 13. BrandOps

- `company_id`: **`brandops`**  → save as `sources/raw/vendors-pasted/brandops.txt`
- **Cause:** wrong owner / parked — real domain unknown
- **Tried:** `brandops.com, brandops.io, brandops.ai, brandops.co`
- **Listed as:** BrandOps
- **In categories:** Multichannel Marketing Hubs  (1 cats · gartner)

### 14. BSI Software

- `company_id`: **`bsi-software`**  → save as `sources/raw/vendors-pasted/bsi-software.txt`
- **Cause:** wrong owner / parked — real domain unknown
- **Tried:** `bsisoftware.com, bsisoftware.io, bsisoftware.ai, bsisoftware.co, bsi-software.com, bsi-software.io, bsi-softwa`
- **Listed as:** BSI Customer Suite
- **In categories:** B2B Marketing Automation Platforms  (1 cats · gartner)

### 15. ClickDimensions

- `company_id`: **`clickdimensions`**  → save as `sources/raw/vendors-pasted/clickdimensions.txt`
- **Cause:** blocked 403 — domain is right, browser will work
- **Tried:** `clickdimensions.com, clickdimensions.io, clickdimensions.ai, clickdimensions.co`
- **Listed as:** ClickDimensions marketing automation platform
- **In categories:** B2B Marketing Automation Platforms  (1 cats · gartner)

### 16. Datorama

- `company_id`: **`datorama`**  → save as `sources/raw/vendors-pasted/datorama.txt`
- **Cause:** wrong owner / parked — real domain unknown
- **Tried:** `datorama.com, datorama.io, datorama.ai, datorama.co`
- **Listed as:** Datorama
- **In categories:** Multichannel Marketing Hubs  (1 cats · gartner)

### 17. Ecomail

- `company_id`: **`ecomail`**  → save as `sources/raw/vendors-pasted/ecomail.txt`
- **Cause:** wrong owner / parked — real domain unknown
- **Tried:** `ecomail.com, ecomail.io, ecomail.ai, ecomail.co`
- **Listed as:** Ecomail
- **In categories:** Email Marketing (Transitioning to Email Marketing Platforms)  (1 cats · gartner)

### 18. Emailidea

- `company_id`: **`emailidea`**  → save as `sources/raw/vendors-pasted/emailidea.txt`
- **Cause:** wrong owner / parked — real domain unknown
- **Tried:** `emailidea.com, emailidea.io, emailidea.ai, emailidea.co`
- **Listed as:** Emailidea
- **In categories:** Email Marketing (Transitioning to Email Marketing Platforms)  (1 cats · gartner)

### 19. FollowAnalytics

- `company_id`: **`followanalytics`**  → save as `sources/raw/vendors-pasted/followanalytics.txt`
- **Cause:** wrong owner / parked — real domain unknown
- **Tried:** `followanalytics.com, followanalytics.io, followanalytics.ai, followanalytics.co`
- **Listed as:** FollowAnalytics Mobile Marketing Automation Platform
- **In categories:** Mobile Marketing Platforms  (1 cats · gartner)

### 20. Free Stand Sampling Solutions

- `company_id`: **`free-stand-sampling-solutions`**  → save as `sources/raw/vendors-pasted/free-stand-sampling-solutions.txt`
- **Cause:** wrong owner / parked — real domain unknown
- **Tried:** `freestandsamplingsolutions.com, freestandsamplingsolutions.io, freestandsamplingsolutions.ai, freestandsamplin`
- **Listed as:** FreeStand Platform
- **In categories:** Multichannel Marketing Hubs  (1 cats · gartner)

### 21. Fresh Relevance

- `company_id`: **`fresh-relevance`**  → save as `sources/raw/vendors-pasted/fresh-relevance.txt`
- **Cause:** blocked 403 — domain is right, browser will work
- **Tried:** `freshrelevance.com, freshrelevance.io, freshrelevance.ai, freshrelevance.co, fresh-relevance.com, fresh-releva`
- **Listed as:** Fresh Relevance
- **In categories:** Email Marketing (Transitioning to Email Marketing Platforms)  (1 cats · gartner)

### 22. Hewlett Packard Enterprise

- `company_id`: **`hewlett-packard-enterprise`**  → save as `sources/raw/vendors-pasted/hewlett-packard-enterprise.txt`
- **Cause:** no response
- **Tried:** `hewlettpackardenterprise.com, hewlettpackardenterprise.io, hewlettpackardenterprise.ai, hewlettpackardenterpri`
- **Listed as:** Juniper Mist User Engagement
- **In categories:** Location Based Marketing Software  (1 cats · gartner)

### 23. IBM

- `company_id`: **`ibm`**  → save as `sources/raw/vendors-pasted/ibm.txt`
- **Cause:** wrong owner / parked — real domain unknown
- **Tried:** `ibm.com, ibm.io, ibm.ai, ibm.co`
- **Listed as:** IBM Watson Customer Experience Analytics
- **In categories:** Multichannel Marketing Hubs  (1 cats · gartner)

### 24. Intense Technologies

- `company_id`: **`intense-technologies`**  → save as `sources/raw/vendors-pasted/intense-technologies.txt`
- **Cause:** wrong owner / parked — real domain unknown
- **Tried:** `intensetechnologies.com, intensetechnologies.io, intensetechnologies.ai, intensetechnologies.co, intense-techn`
- **Listed as:** UniServe Reach
- **In categories:** Multichannel Marketing Hubs  (1 cats · gartner)

### 25. Lob

- `company_id`: **`lob`**  → save as `sources/raw/vendors-pasted/lob.txt`
- **Cause:** wrong owner / parked — real domain unknown
- **Tried:** `lob.com, lob.io, lob.ai, lob.co`
- **Listed as:** Lob
- **In categories:** Direct Mail Automation Software  (1 cats · gartner)

### 26. Longtail UX

- `company_id`: **`longtail-ux`**  → save as `sources/raw/vendors-pasted/longtail-ux.txt`
- **Cause:** wrong owner / parked — real domain unknown
- **Tried:** `longtailux.com, longtailux.io, longtailux.ai, longtailux.co, longtail-ux.com, longtail-ux.io, longtail-ux.ai, `
- **Listed as:** Longtail UX
- **In categories:** Multichannel Marketing Hubs  (1 cats · gartner)

### 27. PAR

- `company_id`: **`par`**  → save as `sources/raw/vendors-pasted/par.txt`
- **Cause:** wrong owner / parked — real domain unknown
- **Tried:** `par.com, par.io, par.ai, par.co`
- **Listed as:** PAR Engagement
- **In categories:** Mobile Marketing Platforms  (1 cats · gartner)

### 28. Reachdesk

- `company_id`: **`reachdesk`**  → save as `sources/raw/vendors-pasted/reachdesk.txt`
- **Cause:** wrong owner / parked — real domain unknown
- **Tried:** `reachdesk.com, reachdesk.io, reachdesk.ai, reachdesk.co`
- **Listed as:** Reachdesk
- **In categories:** Direct Mail Automation Software  (1 cats · gartner)

### 29. SAS

- `company_id`: **`sas`**  → save as `sources/raw/vendors-pasted/sas.txt`
- **Cause:** blocked 403 — domain is right, browser will work
- **Tried:** `sas.com, sas.io, sas.ai, sas.co`
- **Listed as:** SAS Marketing Automation (Legacy), SAS Customer Intelligence 360, SAS Real-Time Decision Manager (Legacy)
- **In categories:** Multichannel Marketing Hubs  (1 cats · gartner)

### 30. Spectrm

- `company_id`: **`spectrm`**  → save as `sources/raw/vendors-pasted/spectrm.txt`
- **Cause:** wrong owner / parked — real domain unknown
- **Tried:** `spectrm.com, spectrm.io, spectrm.ai, spectrm.co`
- **Listed as:** Spectrm
- **In categories:** Mobile Marketing Platforms  (1 cats · gartner)

### 31. Striker Soft Solutions

- `company_id`: **`striker-soft-solutions`**  → save as `sources/raw/vendors-pasted/striker-soft-solutions.txt`
- **Cause:** wrong owner / parked — real domain unknown
- **Tried:** `strikersoftsolutions.com, strikersoftsolutions.io, strikersoftsolutions.ai, strikersoftsolutions.co, striker-s`
- **Listed as:** Office24by7
- **In categories:** B2B Marketing Automation Platforms  (1 cats · gartner)

### 32. SwiftERM Hyper-Personalisation

- `company_id`: **`swifterm-hyper-personalisation`**  → save as `sources/raw/vendors-pasted/swifterm-hyper-personalisation.txt`
- **Cause:** wrong owner / parked — real domain unknown
- **Tried:** `swiftermhyperpersonalisation.com, swiftermhyperpersonalisation.io, swiftermhyperpersonalisation.ai, swiftermhy`
- **Listed as:** SwiftERM
- **In categories:** Email Marketing (Transitioning to Email Marketing Platforms)  (1 cats · gartner)

### 33. Treasure AI

- `company_id`: **`treasure-ai`**  → save as `sources/raw/vendors-pasted/treasure-ai.txt`
- **Cause:** wrong owner / parked — real domain unknown
- **Tried:** `treasureai.com, treasureai.io, treasureai.ai, treasureai.co, treasure-ai.com, treasure-ai.io, treasure-ai.ai, `
- **Listed as:** Treasure Engagement AI Suite
- **In categories:** Multichannel Marketing Hubs  (1 cats · gartner)

### 34. Veloxy IO

- `company_id`: **`veloxy-io`**  → save as `sources/raw/vendors-pasted/veloxy-io.txt`
- **Cause:** wrong owner / parked — real domain unknown
- **Tried:** `veloxyio.com, veloxyio.io, veloxyio.ai, veloxyio.co, veloxy-io.com, veloxy-io.io, veloxy-io.ai, veloxy-io.co, `
- **Listed as:** Veloxy
- **In categories:** Email Marketing (Transitioning to Email Marketing Platforms)  (1 cats · gartner)

### 35. WILY

- `company_id`: **`wily`**  → save as `sources/raw/vendors-pasted/wily.txt`
- **Cause:** wrong owner / parked — real domain unknown
- **Tried:** `wily.com, wily.io, wily.ai, wily.co`
- **Listed as:** SPRY
- **In categories:** Multichannel Marketing Hubs  (1 cats · gartner)

### 36. xiQ

- `company_id`: **`xiq`**  → save as `sources/raw/vendors-pasted/xiq.txt`
- **Cause:** blocked 403 — domain is right, browser will work
- **Tried:** `xiq.com, xiq.io, xiq.ai, xiq.co`
- **Listed as:** xiQ Workbench
- **In categories:** B2B Marketing Automation Platforms  (1 cats · gartner)

---

## What I extract from a paste

The same fields as every other record, by the same rules: website, description (meta
description), value proposition (first `h1`), functionality (product-page headings), channels,
industries served, pricing (published? free tier? contact-sales tier?), deployment model,
founded year, published address country.

**A paste is graded `PRIMARY` — it is the source of record and only the transport is human.**
Two things get recorded alongside it, per the standing protocol: that the page was
human-transported, and that **you chose which pages to send**, which is a sampling decision and
is logged as one.

