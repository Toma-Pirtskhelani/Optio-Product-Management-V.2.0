# schemas/app-marketplaces.md — platform marketplace taxonomy pass

**Governs:** `passes/app-marketplaces/<pass_id>.md`
**Merges into:** `schemas/merged-table.md` Table A (categories) and Table B
(vendors), on `normalized_name`.

This source differs from the other three in one structural way that must be
carried into every output: **a marketplace category is a map of one platform's
ecosystem, not of a market.** Presence measures a vendor's decision to integrate
with that platform and pay its terms. Absence measures nothing about the vendor.

Because of that, this pass is **per-platform**. Never pool marketplaces into a
single vendor list; every row names its platform, and the platform is part of the
row's meaning.

Column availability is an assumption until the first fetch.

---

## 1. Spine

Every row carries the spine from `schemas/merged-table.md` § 1, plus `platform`
on every row without exception.

## 2. Platform scoping

Before capture, record in the pass header, each at R1 with a URL:

| Field | Why it matters |
|---|---|
| `platform` | Marketplace name. |
| `platform_selection_rationale` | **Which platforms and why.** Choosing marketplaces from memory is P1. Selection must come from an evidenced statement about where Optio's buyers actually work — or be declared an explicit, labelled assumption. |
| `listing_requirements` | Verbatim: review process, technical certification, partner tier. |
| `listing_cost` | Fees, revenue share, partner-tier cost, with grade. This is the pay-to-play gate. |
| `ranking_basis` | What the platform states drives placement/ranking, quoted. |
| `regional_storefronts` | Whether the marketplace has regional or localized variants, and their URLs. |

## 3. Table A — categories

| Column | Definition |
|---|---|
| *spine* + `platform` | § 1 |
| `category_path` | Full breadcrumb, verbatim. |
| `stated_definition` | Verbatim if published; else `UNKNOWN`. |
| `listing_count` | With grade. |
| `filter_url` | Reproducible URL for the count. |
| `locale_variants` | Localized versions of this category page, with URLs. |
| `platform_gate_note` | Any category-specific requirement (certification, security review, partner tier). |

## 4. Table B — listings

| Column | Definition |
|---|---|
| *spine* + `platform` | § 1 |
| `listing_name` | Verbatim. |
| `vendor_name` / `vendor_aliases` | Verbatim; the publisher may differ from the app name. |
| `listing_url` | Row-level. |
| `vendor_own_site` | Fetched separately at R1. |
| `install_count` / `customer_count` | With grade. Self-reported unless the platform states otherwise — mark which. |
| `review_count` / `rating` | With grade. |
| `pricing_model` / `price_points` | With grade, currency, and as-of date. **The most fetchable pricing evidence in this whole study** — most marketplaces publish it where vendor sites don't. |
| `listed_languages` | Languages the listing declares support for. |
| `listed_regions` | Regions/markets the listing declares. |
| `partner_tier` | Verbatim, if published. |
| `first_listed` / `last_updated` | With grade. A listing untouched for years is a `DORMANT` candidate. |
| `status` | `ACTIVE` / `DELISTED` / `UNKNOWN`, with grade. |

Rung discipline: a marketplace listing is R1 for *"this vendor lists here on
these terms"* and for **published pricing**, which is a genuine primary artifact.
It is R3 for vendor claims inside the description text — install counts,
customer names, and capability claims are marketing copy carried by the platform,
not verified by it, unless the platform states it verifies them. Quote the claim;
do not adopt it.

## 5. Failure sampling (P4) — mechanisms for this source

Marketplaces purge delisted apps completely, so the archive is the only route:

1. `web.archive.org` snapshots of each category page at ≥12 and ≥24 months; diff
   the listing sets.
2. For each disappeared listing, fetch the vendor's own domain at R1 and resolve:
   shut down, acquired, migrated off the platform, or delisted for policy or
   non-payment. Four different outcomes; keep them separate.
3. Where the archive holds the old listing page, save it to `evidence/raw/` —
   dead listings are the least recoverable evidence in this study and disappear
   permanently.
4. Zero candidates requires the archive-diff log attached.

Distinguish carefully: **leaving a marketplace is a strategy decision as often as
it is a death.** A vendor that grew past needing the channel and a vendor that
died both vanish from the listing. Never code one as the other without R1
resolution against the vendor's own site.

## 6. Language protocol (P5)

Regional storefronts are the strongest local-vendor detector in the whole source
set — local vendors that never appear in English catalogues frequently do list on
regional marketplace variants. For any non-anglophone market in scope, fetch the
regional storefront, run in-language category queries, and log them verbatim.
Record `listed_languages` on every row; it is the most direct evidence available
of which markets a vendor actually sells into.

## 7. Rejection

Standard checklist, `research-protocol.md` § 7, plus:

- [ ] `platform_selection_rationale` is evidenced or explicitly labelled an
      assumption.
- [ ] `listing_cost` and `ranking_basis` captured verbatim before any
      prominence claim is made about any vendor.
- [ ] Every row names its `platform`; no cross-platform pooling.
- [ ] Vendor self-reported counts marked as self-reported, not adopted.
- [ ] Archive diff run; dead listing pages saved to `evidence/raw/`.
- [ ] Absence from a marketplace nowhere treated as absence from the market.
