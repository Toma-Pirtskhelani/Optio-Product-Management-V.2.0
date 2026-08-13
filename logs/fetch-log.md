# fetch-log.md

Every fetch attempt, **logged as it happens** — including failures, including refusals to
try. Retroactive logging is reconstruction, and reconstruction is what this study refuses to
accept from anyone else.

Append-only. Never edit a past row; add a new one and reference it.

Governed by `research-protocol.md` §1 and §9.

## Columns

| Field | Meaning |
|---|---|
| `date` | ISO date of the attempt (YYYY-MM-DD) |
| `url` | Full URL attempted |
| `source` | Source of record this belongs to (e.g. `g2`, `gartner`, marketplace name) |
| `rung` | Ladder rung attempted: `1` / `2` / `3` / `4` |
| `outcome` | `ok` / `403` / `404` / `timeout` / `blocked-by-environment` / `partial` / `skipped-by-judgment` / `paste-requested` / `paste-received` |
| `obtained` | What content was actually obtained — or the reason for skipping |
| `raw_file` | Path under `sources/raw/`, or `—` |
| `escalated_to` | Rung escalated to, and why. `—` if none needed |
| `source_language` | ISO code of the page's language (`en`, `ru`, `tr`, `zh`, `es`, `pt`, `ka`, …). **Mandatory on every row, including failures** |

## Measuring the language bias instead of suffering it

Rung 3 makes the user the throughput limit of this study, and **blocking is not
language-neutral**: non-English sources are more likely to block, to lack alternate paths, and
to be expensive to request. The language obligation (`CLAUDE.md` §6) therefore fails hardest
exactly where it matters most — and, unmeasured, it fails *looking like diligence*.

That constraint cannot be removed. It can be made visible with a number attached.

**`source_language` is recorded on every attempt, including every failure**, so the block rate
can be computed per language. Every pass reports:

> Attempts by language: `en` N (M blocked, X%) · `ru` N (M blocked, X%) · …

**If non-English sources block at several times the English rate, that is a measured bias, not
a silent one.** It is reported as a finding about the method, and any conclusion about
non-Anglophone market coverage carries the block rate beside it.

`skipped-by-judgment` rows count toward the denominator too. A source skipped because
requesting it was expensive is still a source this study did not see.

## Rules

- `skipped-by-judgment` **requires** a stated reason in `obtained` describing what the page
  would have decided and why that decision does not matter here. A skip with no reason is a
  silent omission — prohibition 6.
- A `403` or `blocked-by-environment` row **must** have a non-`—` `escalated_to`, or a
  `skipped-by-judgment` row immediately following it. A block with neither is an
  unfinished action, not a finished attempt.
- `web.archive.org` is `blocked-by-environment` at the tool level. Do not attempt it and do
  not design fallbacks around it.

## Log

### Pass 01 — source taxonomy enumeration, 2026-08-10

Two transports were used and are distinguished because they behave differently:
**`WebFetch`** (agent tool; converts the page to markdown and answers a prompt against it
using a small model — **model-mediated, not verbatim**) and **`curl`** (default user-agent,
no spoofing — **byte-exact**).

| date | url | source | rung | outcome | obtained | raw_file | escalated_to | source_language |
|---|---|---|---|---|---|---|---|---|
| 2026-08-10 | https://www.gartner.com/reviews/markets | gartner | 1 | 403 | nothing | — | Rung 2 | en |
| 2026-08-10 | https://www.gartner.com/reviews/sitemap.xml | gartner | 2 | 403 | nothing | — | Rung 2 | en |
| 2026-08-10 | https://www.gartner.com/sitemap.xml | gartner | 2 | 403 | nothing | — | Rung 2 | en |
| 2026-08-10 | https://www.gartner.com/robots.txt | gartner | 2 | 403 | nothing — robots.txt itself is blocked, so even the crawl policy is unreadable | — | Rung 2 | en |
| 2026-08-10 | https://www.gartner.com/reviews/markets/all | gartner | 2 | 403 | nothing | — | Rung 2 | en |
| 2026-08-10 | https://www.gartner.com/reviews/market/marketing-automation-platforms | gartner | 2 | 403 | nothing | — | Rung 2 | en |
| 2026-08-10 | https://gartner.com/reviews/markets (no `www`) | gartner | 2 | 403 | nothing | — | **Rung 3 — all Rung-1/2 paths exhausted; Gartner has no denominator without human transport** | en |
| 2026-08-10 | https://www.g2.com/categories (WebFetch) | g2 | 1 | partial | 19 top-level branch names; tool reported its own output truncated | — | retried via curl | en |
| 2026-08-10 | https://www.g2.com/categories (curl) | g2 | 1 | ok | **complete taxonomy: 38 branch tables, 2,235 category rows** | 2026-08-10__g2__categories-index__r1.html | — | en |
| 2026-08-10 | https://www.g2.com/categories/marketing | g2 | 1 | 403 | nothing | — | Rung 2 | en |
| 2026-08-10 | https://www.g2.com/categories/{marketing-automation, email-marketing, mobile-marketing, customer-data-platform-cdp, push-notification} (curl ×5) | g2 | 1 | 403 ×5 | nothing — identical 1,704-byte block page each time | — | **Rung 3 — category definitions and inclusion criteria are unobtainable without human transport** | en |
| 2026-08-10 | https://www.g2.com/robots.txt | g2 | 2 | ok | crawl policy; names `ClaudeBot` explicitly; declares sitemap index + `llms.txt` | — | — | en |
| 2026-08-10 | https://www.g2.com/sitemaps/sitemap_index.xml.gz | g2 | 2 | 403 | nothing | — | superseded — `/categories` already yielded the full enumeration | en |
| 2026-08-10 | https://www.g2.com/llms.txt | g2 | 2 | ok | platform self-description; no taxonomy rules | — | — | en |
| 2026-08-10 | https://documentation.g2.com/docs | g2 | 2 | ok | vendor-onboarding docs; **no** taxonomy governance | — | — | en |
| 2026-08-10 | https://research.g2.com/methodology | g2 | 2 | ok | index of 6 methodology documents | — | — | en |
| 2026-08-10 | https://research.g2.com/methodology/categorization | g2 | 2 | ok | **complete taxonomy governance rules, verbatim** | 2026-08-10__g2__methodology-categorization__r2.html | — | en |
| 2026-08-10 | https://research.g2.com/methodology/standard-definitions | g2 | 2 | ok | definitions of attributes/features; no category-governance rules | — | — | en |
| 2026-08-10 | https://apps.shopify.com/categories | shopify-app-store | 1 | ok (301 on curl) | curated landing page; does **not** enumerate the taxonomy | — | Rung 2 (sitemap) | en |
| 2026-08-10 | https://apps.shopify.com/sitemap.xml | shopify-app-store | 2 | ok | sitemap index; per-language category sitemaps for 23 locales | — | — | en |
| 2026-08-10 | https://apps.shopify.com/sitemap_categories_en.xml | shopify-app-store | 2 | ok | **161 categories — complete enumeration** | 2026-08-10__shopify__sitemap-categories-en__r2.xml | — | en |
| 2026-08-10 | https://apps.shopify.com/sitemap_categories_tr.xml | shopify-app-store | 2 | ok | 161 categories | 2026-08-10__shopify__sitemap-categories-tr__r2.xml | — | tr |
| 2026-08-10 | https://apps.shopify.com/sitemap_categories_es.xml | shopify-app-store | 2 | ok | 161 categories | 2026-08-10__shopify__sitemap-categories-es__r2.xml | — | es |
| 2026-08-10 | https://apps.shopify.com/categories/marketing-and-conversion-marketing-email-marketing | shopify-app-store | 1 | ok | category page; description present, **no app count published** | — | — | en |
| 2026-08-10 | https://apps.shopify.com/categories/marketing-and-conversion-marketing-sms-marketing | shopify-app-store | 1 | 302 | redirect, not followed | — | Rung 3 (batched) | en |
| 2026-08-10 | https://ecosystem.hubspot.com/marketplace/apps | hubspot-ecosystem | 1 | partial | landing page; no category enumeration | — | Rung 2 | en |
| 2026-08-10 | https://ecosystem.hubspot.com/marketplace/apps/marketing | hubspot-ecosystem | 1 | partial | JS-rendered shell; no content | — | Rung 2 | en |
| 2026-08-10 | https://ecosystem.hubspot.com/marketplace/apps/{marketing-automation, sms} (curl ×2) | hubspot-ecosystem | 1 | partial | **identical 53,230-byte shell for different categories** — content is client-rendered | — | **Rung 3 — per-category detail needs human transport** | en |
| 2026-08-10 | https://ecosystem.hubspot.com/robots.txt | hubspot-ecosystem | 2 | ok | declares 7 marketplace sitemaps | — | — | en |
| 2026-08-10 | https://ecosystem.hubspot.com/marketplace-apps-categories.xml | hubspot-ecosystem | 2 | ok | sitemap index; 17 languages | — | — | en |
| 2026-08-10 | https://ecosystem.hubspot.com/marketplace-en-apps-categories-1.xml | hubspot-ecosystem | 2 | ok | **60 categories — complete enumeration**, plus per-category pagination depth | 2026-08-10__hubspot__sitemap-apps-categories-en__r2.xml | — | en |

### Block rate by language — pass 01

| language | attempts | blocked (403) | block rate |
|---|---|---|---|
| `en` | 29 | 13 | 45% |
| `tr` | 1 | 0 | 0% |
| `es` | 1 | 0 | 0% |
| `ru`, `zh`, `pt`, `ka` | 0 | — | **NOT-ATTEMPTED** |

**This measurement is not yet meaningful, and saying so is the point of having it.** The two
non-English attempts were *locale variants of an Anglophone platform* (Shopify), not
domestically-owned sources. Nothing here tests the hypothesis the measurement exists to test.
Four of the six required languages have zero attempts. The number is reported anyway, at
`n=2`, so that it is visibly inadequate rather than invisibly absent.

**A finding that runs the other way and should be stated plainly:** in this pass the blocking
fell entirely on English-language enterprise sources — Gartner at 100%, G2's category pages at
100% — while every non-English attempt succeeded. The expected direction of the bias is not
the observed direction *yet*. Do not generalize from `n=2`.


### Pass 02 — Gartner Peer Insights via human transport, 2026-08-10

| date | url | source | rung | outcome | obtained | raw_file | escalated_to | source_language |
|---|---|---|---|---|---|---|---|---|
| 2026-08-10 | https://www.gartner.com/reviews/faq | gartner | **3** | paste-received | Peer Insights governance: language eligibility, write-in vendors, incentives, non-expiry, review-vs-rating denominators, category-expansion policy | `sources/raw/web pages/gartner/…/reviews/faq#rq20` | — | en |
| 2026-08-10 | https://www.gartner.com/reviews/market/multichannel-marketing-hubs | gartner | **3** | paste-received | definition, 6 mandatory features (Oct 2025), 122 of 122 products, 5 (Legacy) | `…/market/multichannel-marketing-hubs` | — | en |
| 2026-08-10 | https://www.gartner.com/reviews/market/email-marketing | gartner | **3** | paste-received | definition, 4 mandatory features (Dec 2025), 100 of 100, 1 (Legacy), category marked (Transitioning to Email Marketing Platforms) | `…/market/email-marketing` | — | en |
| 2026-08-10 | https://www.gartner.com/reviews/market/customer-data-platforms | gartner | **3** | paste-received | definition, 4 mandatory features (Jan 2026), 71 of 71, 1 (Legacy) | `…/market/customer-data-platforms` | — | en |
| 2026-08-10 | https://www.gartner.com/reviews/market/personalization-engines | gartner | **3** | paste-received | definition, 8 mandatory features (Feb 2026), 64 of 64, 5 (Legacy) | `…/market/personalization-engines` | — | en |
| 2026-08-10 | https://www.gartner.com/reviews/market/b2b-marketing-automation-platforms | gartner | **3** | paste-received | definition, 5 mandatory features (Sep 2025), 59 of 59, 3 (Legacy) | `…/market/b2b-marketing-automation-platforms` | — | en |
| 2026-08-10 | https://www.gartner.com/reviews/market/mobile-marketing-platforms | gartner | **3** | paste-received | definition, 3 mandatory features (Feb 2026), 45 of 45, 0 (Legacy) | `…/market/mobile-marketing-platforms` | — | en |
| 2026-08-10 | https://www.gartner.com/reviews/market/location-based-marketing-software | gartner | **3** | paste-received | definition, **no mandatory features**, **no analyst documents**, 15 of 15 | `…/market/location-based-marketing-software` | — | en |
| 2026-08-10 | Gartner **Marketing branch** category list | gartner | **3** | **outstanding** | nothing — every supplied page carries the *Application Development* nav list, truncated at "View More" | — | **re-requested (Request A)** | en |

**Sample type: PURPOSIVE.** The seven market pages were selected by the user, non-randomly,
using information this study does not have. No count here generalises to the branch.

**Block rate by language, pass 01 + 02 cumulative:** `en` 38 attempts / 13 blocked (34%) ·
`tr` 1 / 0 · `es` 1 / 0 · `ru`, `zh`, `pt`, `ka` **zero attempts**. Human transport reduced the
English block rate by supplying content no automated rung could reach; it changed nothing for
the four untested languages. **And per `outputs/gartner-marketing-extraction.md` §6.1, three of
those four are excluded from Gartner by published policy — so for `ru`, `tr` and `ka` the
constraint is not our access, it is that the content does not exist.**

### Pass 03 — browser-transport probe, 2026-08-13

Two probes, run through the user's own Chrome via the browser-automation MCP, to test whether a
real browser reaches what `WebFetch` and `curl` cannot. **It does.** Both pages rendered in full.

| date | url | source | rung | outcome | obtained | raw_file | escalated_to | source_language |
|---|---|---|---|---|---|---|---|---|
| 2026-08-13 | https://www.g2.com/products/insider-one/reviews (WebFetch) | g2 | 1 | 403 | nothing — no body returned | — | Rung 1-B | en |
| 2026-08-13 | https://insiderone.com/ (WebFetch) | g2 | 1 | ok | title, h1, positioning text — matches the 2026-08-11 stored record verbatim, so that record is still current | — | — | en |
| 2026-08-13 | https://www.g2.com/products/insider-one/reviews (browser) | g2 | **1-B** | ok | full product page: 4.8/5 (1,415), breadcrumb `Mobile Marketing Software`, full review bodies | — | — | en |
| 2026-08-13 | https://www.g2.com/categories/marketing-automation (browser) | g2 | **1-B** | ok | **"510 Listings"**, 16 vendor rows with `By <vendor>` attribution, ratings, review counts, `Sponsored` flag, **the category's verbatim inclusion criteria**, pagination `1…34`, and a Language filter | — | — | en |

**What this overturns.** Row 78 above recorded the inclusion criteria as *"unobtainable without
human transport."* That is now false: a browser reaches them directly. The Rung-3 paste request
for G2 category pages is superseded, not satisfied — no paste was needed.

**Rung 1-B is a new designation and is deliberately not called Rung 1.** Same origin, same page,
no intermediary summarising it — evidentially it is a direct read. But the transport differs: it
renders JavaScript in the user's authenticated-capable browser, so what it returns can depend on
session state and on client-side rendering in a way `curl` output cannot. Recording it as plain
Rung 1 would erase that difference. `research-protocol.md` needs an amendment before any pass
relies on it.

**Drift noted, not a conflict.** The store carries `declared_total: 511` for Marketing
Automation (captured 2026-08-10); the page said **510** on 2026-08-13. Same source, three days
apart — category membership moves. Any G2 recount must re-read the denominator, never reuse it.
