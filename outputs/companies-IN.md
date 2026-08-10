# outputs/companies-IN.md — companion to `companies-IN.json`

**237 unique companies**, deduplicated from **454 product rows** across the **10 IN classifications**.
Full data, with descriptions and provenance, is in [`companies-IN.json`](companies-IN.json).

---

## Read this before using the list

**The two halves of this file have completely different coverage, and merging them in your head would be the one mistake that matters.**

| | Categories | Rows | Coverage |
|---|---|---|---|
| **Gartner** | 6 | **352 of 352** | **COMPLETE.** Every category enumerates fully (*"Products 1–N of N"*) and every parsed count reconciles exactly with the declared total. A company absent from the Gartner portion is `ABSENT-ENUMERATED` — genuinely not listed. |
| **G2** | 4 | **102 of 1,810** | **5.6% — VISIBLE PAGE ONLY.** G2 renders ~25 listings per page. A company absent from the G2 portion is `ABSENT-IN-VISIBLE-PAGE` and that is **not** evidence of absence. |

Every company record carries `coverage` per category, so the distinction survives into any downstream use.

---

## What is in it

- **27 companies appear in both sources.** These are the only rows with two independent listings — though per the protocol this is still not corroboration, because Gartner and G2 are both `SELF-DECLARED` and their errors correlate.
- **192 Gartner-only**, **18 G2-only**. The G2-only figure is inflated by the 5.6% sample: many G2-only names would appear on both if the full G2 lists were held.
- **7 companies carry a Gartner `(Legacy)` product** — managed decline with ratings intact: Microsoft, Oracle, Precisely, SAP, SAS, SpiceSend, Upland.
- **3 companies hold a paid `Sponsored` placement on G2**, flagged per product: Emma, Mailgun, Netmera.
- **230 of 237 have a description** quoted from the source.

## Deduplication

Merging is conservative and every rule is recorded in `meta.merge_rules`. Only **7 merges** were applied, each because a source had put a product name in the vendor field (`Adobe Marketo Engage` → Adobe, `HubSpot Marketing Hub` → HubSpot, `Intuit Mailchimp` → Intuit). **No fuzzy matching.** Similar names stay separate.

Gartner's parenthetical vendor form turned out to encode two different things, so it is split rather than assumed:

| Reading | Cases |
|---|---|
| **Acquisition** — parenthetical names an acquired brand | CleverTap (Leanplum), Constant Contact (SharpSpring), Upland (Localytics), Tech Mahindra (Comviva), Capillary Technologies (SessionM), HCLTech (HCLSoftware), Soprano (Whispir), Mastercard (Dynamic Yield) |
| **Abbreviation** — parenthetical is just the owner's initials | Amazon Web Services (AWS), Hewlett Packard Enterprise (HPE), Inspired Thinking Group (ITG) |

The abbreviation test is computed, not eyeballed: the parenthetical is compared against the owner's initials and against the owner string itself.

---

## The 27 companies listed by both sources

| Company | Categories | Products | Max reviews | Legacy |
|---|---|---|---|---|
| Salesforce | 7 | 9 | 4629 |  |
| Braze | 6 | 6 | 1688 |  |
| Dotdigital | 6 | 6 | 1235 |  |
| Adobe | 5 | 10 | 3149 |  |
| Brevo | 5 | 5 | 2621 |  |
| Klaviyo | 5 | 5 | 1360 |  |
| Customer.io | 5 | 5 | 894 |  |
| Iterable | 5 | 5 | 825 |  |
| MoEngage | 5 | 5 | 525 |  |
| Netmera | 5 | 5 | 49 |  |
| ActiveCampaign | 4 | 4 | 14779 |  |
| Intuit | 4 | 4 | 12984 |  |
| Attentive | 4 | 4 | 1483 |  |
| Insider One | 4 | 4 | 1415 |  |
| Zoho | 4 | 7 | 1041 |  |
| WebEngage | 4 | 4 | 768 |  |
| HubSpot | 3 | 3 | 14909 |  |
| Constant Contact | 3 | 4 | 7426 |  |
| Omnisend | 3 | 3 | 1258 |  |
| Epsilon | 3 | 3 | 146 |  |
| Pipedrive | 2 | 2 | 3105 |  |
| MailerLite | 2 | 2 | 1113 |  |
| Bloomreach | 2 | 2 | 775 |  |
| Salesmsg | 2 | 2 | 414 |  |
| Sender | 2 | 2 | 265 |  |
| EVAM | 2 | 2 | 227 |  |
| Sinch | 2 | 3 | 62 |  |

---

## Limits that travel with this data

Ratings and review counts measure **review-solicitation effort** at least as much as customer volume — Gartner's FAQ confirms vendors solicit reviews and that nominal gifts are permitted. Gartner reviews **never expire**, so counts are cumulative and reflect history rather than current position. No funding, revenue or investor data exists in either source and none is inferred. Both sources are `SELF-DECLARED`, so **no company here is `corroborated: yes`**. Gartner will not publish reviews in Russian, Turkish or Georgian, and G2 removes listings under OFAC sanctions — so absence of a vendor from a sanctioned or non-supported-language market is evidence about source policy, not about the market.
