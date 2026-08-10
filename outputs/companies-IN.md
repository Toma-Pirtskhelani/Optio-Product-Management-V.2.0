# outputs/companies-IN.md — companion to `companies-IN.json`

**237 unique companies**, deduplicated from **417 product rows** across the **10 IN classifications**.
Full data, with descriptions and provenance, is in [`companies-IN.json`](companies-IN.json).

---

## Read this first — the two halves are not comparable

**Merging them in your head is the one mistake that matters.**

| | Categories | Products held | Coverage |
|---|---|---|---|
| **Gartner** | 6 | **352 of 352** | **COMPLETE.** Every category enumerates fully (*"Products 1–N of N"*) and every parsed count reconciles exactly with the declared total. A company absent here is `ABSENT-ENUMERATED` — genuinely not listed. |
| **G2** | 4 | **65 of 1,810** | **3.6% — VISIBLE PAGE ONLY.** ~16 distinct products render per category page. A company absent here is `ABSENT-IN-VISIBLE-PAGE`, which is **not** evidence of absence. |

Every company record carries `coverage` per category, so the distinction survives into any downstream use.

> **Correction, 2026-08-10.** An earlier version of this file reported the G2 half as *102 of 1,810 (5.6%)*. That counted **rendered blocks, not products**: a G2 category page lists each product twice — a main listing carrying `By <vendor>` lines, then a second summary rendering without vendors. After collapsing to distinct products the true figure is **65 (3.6%)**. The error made G2 coverage look 57% better than it is, and would have split products from their parent company where only the vendor-less rendering was captured. Blocks are now collapsed, always preferring the block that names the vendor.

---

## What is in it

- **27 companies appear in both sources.** The only rows with two independent listings — though per the protocol this is still **not corroboration**, because Gartner and G2 are both `SELF-DECLARED` and their errors correlate.
- **192 Gartner-only**, **18 G2-only**. The G2-only figure is a floor, not a finding: at 3.6% coverage most G2 members were never rendered.
- **7 companies carry a Gartner `(Legacy)` product** — managed decline with ratings intact: Microsoft, Oracle, Precisely, SAP, SAS, SpiceSend, Upland. **9 legacy listings across 8 distinct products** — SAS holds two, and `SAP Marketing Cloud (Legacy)` is listed in two categories.
- **3 companies hold a paid `Sponsored` placement on G2**: Emma, Mailgun, Netmera.
- **230 of 237 carry a description** quoted from the source. The 7 without one are listed by the source with no description text: Bird, Postal, Reachdesk, Sendoso, Splio, WorksBuddy, adnymics.
- **0 companies have a product name truncated by the source page itself** (rendered with a trailing ellipsis), flagged `name_truncated_in_source`. The name is left exactly as the source printed it rather than guessed: Intuit — `Intuit Mailchimp All-in-One...`, Intuit — `Intuit Mailchimp Email...`, Salesforce — `Agentforce Marketing...`.

## Deduplication

Conservative, and every rule is in `meta.merge_rules`. Only **2 name merges** were needed once the G2 double-rendering was collapsed — `Intuit Mailchimp` → Intuit and `Sender.net` → Sender. **No fuzzy matching.** Similar names stay separate, because a forced match manufactures corroboration.

Gartner's parenthetical vendor form encodes two different things, so it is split by a computed test rather than assumed:

| Reading | Cases |
|---|---|
| **Acquisition** | CleverTap (Leanplum), Constant Contact (SharpSpring), Upland (Localytics), Tech Mahindra (Comviva), Capillary Technologies (SessionM), HCLTech (HCLSoftware), Soprano (Whispir), Mastercard (Dynamic Yield) |
| **Abbreviation of the owner's own name** | Amazon Web Services (AWS), Hewlett Packard Enterprise (HPE), Inspired Thinking Group (ITG) |

The test compares the parenthetical against the owner's initials and against the owner string itself.

---

## The 27 companies listed by both sources

Sorted by number of categories, then by highest review count. Review counts are **not** a size measure — see the limits below.

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

Ratings and review counts measure **review-solicitation effort** at least as much as customer volume — Gartner's FAQ confirms vendors solicit reviews and that nominal gifts of $25 or less are permitted. Gartner reviews **never expire**, so counts are cumulative and describe history rather than current position. No funding, revenue or investor data exists in either source, and none is inferred. Both sources are `SELF-DECLARED`, so **no company here is `corroborated: yes`**. Gartner does not publish reviews in Russian, Turkish or Georgian, and G2 removes listings under OFAC sanctions — so a vendor's absence from a sanctioned or unsupported-language market is evidence about source policy, not about the market.
