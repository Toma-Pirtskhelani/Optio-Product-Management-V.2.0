# outputs/source-taxonomies.md

**Pass 01 — what does each source think it is cataloguing?**
Answered before any vendor is counted, because the sources do not agree, and merging
"Marketing Automation" in one with a similarly-named object in another without establishing
that produces a table that looks rigorous and means nothing.

Captured 2026-08-10. Raw captures in `sources/raw/`, indexed in `sources/raw/CAPTURES.md`.
Every attempt, including every failure, in `logs/fetch-log.md`.

---

## 0. Read this before the tables

**Competitor classes 2–7 gap statement** (`CLAUDE.md` §4). In-house builds, agencies,
services firms, systems integrators, bundled modules, assembled substitutes and the status
quo are unmeasured by any source currently in this study. Their size is `UNKNOWN`, not zero.
Everything below describes **contest among listed software vendors only.**
*But see §6 — the evidence partly contradicts the premise of that amendment, and you should
decide what to do about it.*

**No cutting, no recommending** (`CLAUDE.md` §2.1). Every category the screen surfaced is
listed with its scope call. Nothing is filtered for interest. No category is recommended.

**Grades are read per cell** (`research-protocol.md` §4). A `PRIMARY` count inside a row with
an `UNKNOWN` cell is still `PRIMARY`.

**The headline, stated first because it changes what you can do with this document:**
the two sources that are supposed to carry the study are the two whose per-category detail is
blocked. We have complete *taxonomies* for G2, Shopify and HubSpot, and **nothing at all** for
Gartner. We have **no product counts from any source.** The ranked table you asked for is
therefore a ranked-by-nothing table, and §7 says so rather than substituting a proxy that
would look like a measurement.

---

## 1. Coverage: what was actually obtained

| Source | Complete category index? | Count | Rung | Per-category detail (definition, inclusion criteria, product count) |
|---|---|---|---|---|
| **Gartner Peer Insights** | **NO — nothing at all** | `UNKNOWN` | 1, 2 both 403 | **Blocked.** Needs Rung 3 |
| **G2** | **YES** | **2,235** categories in 38 branches | 1 (`/categories`) | **Blocked** (403 on every category page). Needs Rung 3 |
| **Shopify App Store** | **YES** | **161** categories | 2 (sitemap) | Pages reachable, but **Shopify publishes no per-category app count** |
| **HubSpot ecosystem** | **YES** | **60** categories | 2 (sitemap) | Pages are JS-rendered shells — identical bytes for different categories. Needs Rung 3 |

**Gartner returned 403 to all seven paths attempted, including `robots.txt` itself.** We
cannot read its crawl policy, let alone its markets. Gartner is the source the brief ranks
first and the one designated as this study's only failure-detection mechanism — the
`(Legacy)` / `(Retired)` / `(Transitioning to X)` markers exist nowhere else in our source
set. **Everything that depends on Gartner is currently `NOT-CHECKED`, and no amount of
cleverness with the other three substitutes for it.**

**What the Gartner gap means for anything built on top of this document:**
1. **No failure detection.** G2 deletes dead products by policy (§3), Shopify and HubSpot
   simply drop listings. Without Gartner markers this study has **no mechanism whatsoever**
   for identifying failed products or dissolved categories. Any pass built on this document
   today would be a winners-only output — **rejected and rerun** under
   `research-protocol.md` §6.
2. **No denominator, so no coverage claim.** For G2, Shopify and HubSpot we can say
   `ABSENT-ENUMERATED` when something is missing. For Gartner we cannot say anything: we do
   not know how many markets exist, so every Gartner absence is `NOT-CHECKED`, permanently,
   until a human opens the page.
3. **No enterprise correction.** Gartner is the one source weighted toward banking,
   insurance and telecom. Without it, this document is G2 plus two e-commerce/SMB app stores
   — precisely the structural blind spot `CLAUDE.md` §7.2 warns about, with nothing pushing
   back on it.

### Block rate by language

`en` 29 attempts / 13 blocked (45%) · `tr` 1 / 0 · `es` 1 / 0 · `ru`, `zh`, `pt`, `ka` **zero
attempts**.

Reported at `n=2` so its inadequacy is visible rather than absent. The two non-English
attempts were *locale variants of an Anglophone platform*, not domestic sources, so they do
not test what the measurement exists to test. Note the direction: in this pass **all**
blocking fell on English-language enterprise sources. Do not generalize from `n=2`.

---

## 2. A method finding that changes how you should read every number below

The agent's own page-fetching tool (`WebFetch`) converts a page to markdown and answers a
prompt against it **using a small model**. It is not a verbatim transport.

It reported the Shopify English category sitemap as containing **216** URLs. A byte-exact
`curl` of the same URL, seconds later, contains **161**. It also reported the Turkish sitemap
at 246 and the Spanish at 226 — a difference that would have been logged as a genuine
cross-locale taxonomy conflict and reasoned about. All three sitemaps contain exactly 161.

**The tool invented three numbers and one finding.** Under this protocol an invented number
is the specific thing that must never happen, and it nearly happened at the first opportunity.

**Consequence, applied throughout:** every count in this document was produced by `curl` plus
deterministic parsing, and every raw capture in `sources/raw/` is byte-exact. `WebFetch`
output is treated as a **Rung-4 secondary source about a Rung-1 page** — usable for "does this
page exist and roughly what is on it", never for a number. `logs/conflicts.md` records the
discrepancy as `C-0001`.

---

## 3. G2 — the taxonomy's own rules

Source: `https://research.g2.com/methodology/categorization`, Rung 2, PRIMARY, `en`.
Reachable while `www.g2.com` category pages return 403 — the alternate-subdomain pattern the
protocol predicts, now a known working path.

| Rule | G2's own wording (verbatim) | Why it matters to counting |
|---|---|---|
| Classification basis | "Products on G2 are categorized into at least one category based on the functionality of the software or service, i.e., the product's features, and **not based on what it is used for or who uses it.**" | Function, not industry served. G2 is answering a different question from a vertical taxonomy |
| Category creation | "When evaluating a new category, G2 evaluates the number of products in the space (**10 at minimum**) in order to ensure that the space is established to some degree." | A G2 category implies ≥10 products existed at creation. It does **not** imply 10 today |
| Inclusion criteria | "the feature requirements are a list of features that a product must have to be included in the category… **A product needs to meet all the feature requirements** to be added into that category." | Bar height is per-category and published — but only on the category page, which is blocked |
| Multi-category placement | "We categorize products in **all relevant categories** that they meet the requirements for, even if that category does not represent the product's primary or core use case." | **Counts double-count aggressively by design.** Summing products across G2 categories is meaningless |
| Removal from a category | "we do **not** remove products from categories if they still meet the feature requirements" — vendor requests to leave because "they will not be able to compete with bigger vendors" are explicitly "not an appropriate rationale" | Category membership is sticky. Inflation over time is structural |
| Parent categories | "Parent categories… **do not actually contain any G2 product profiles.** Product profiles cannot be categorized within a parent category; products are placed only within child categories." | **The unit of count is the leaf.** A branch total is not a product count |
| Vertical vs horizontal | "The vast majority of the time, products are categorized in either horizontal categories or vertical categories, **but not both.**" | A vendor serving a vertical from a horizontal product is invisible in the vertical category |
| "Other" categories | "Products that do not qualify for any defined categories on G2 will be listed in a relevant 'Other' software category." | Residual buckets. Their contents are unknowable from the name |
| Add-ons | Third-party add-ons "are listed as separate products"; same-vendor add-ons are not, their functionality instead being "represented by the core product's inclusion in the relevant categories" | Product counts are partly an artefact of who wrote the add-on |
| Services | "A service provider is any business offering where there is **majority of human intervention**"; each gets one profile "categorized in as many services categories as the company qualifies for" | G2 catalogues services as well as software — see §6 |
| Change log | "7/9/25 - Made updates throughout, including adding details on individual software products and removing product suites section." | The taxonomy rules are dated and moving |

### Two G2 rules that are findings in their own right

**1. G2 destroys the failure evidence by policy.**

> "A product's G2 profile will be **removed from the site** upon confirmation from the vendor
> that a product is no longer being sold or that a sunset date has been set… **All reviews for
> invalidated products are removed from G2 along with the product.**"

A dead product does not become a `(Legacy)` marker on G2. It disappears, and its review
history disappears with it. **G2 is structurally incapable of showing failure** — the survivor
set is all that is ever visible, and the erasure is retroactive. This is not a gap in our
sampling that better sampling could close; it is the source's design. It also means
capture-to-capture comparison is the *only* way G2 can ever yield a failure signal, which
requires two dated captures we do not yet have. Prohibition 4 cannot be satisfied from G2.

**2. G2 removes vendors to comply with U.S. sanctions.**

> "G2 may **decline, suspend, or remove listings** as necessary to comply with applicable U.S.
> sanctions laws, including regulations administered by the Office of Foreign Assets Control
> (**OFAC**)."

This study is required to cover Russian-language sources specifically as a bias control
(`CLAUDE.md` §6). G2 states a policy that removes sanctioned-jurisdiction vendors from the
catalogue. **A Russian vendor's absence from G2 is therefore not evidence about that vendor or
its market — it is evidence about U.S. sanctions policy.** Any count of vendors in any market
touched by sanctions is censored at the source, in a direction we can name but not size. The
language obligation cannot be met by reading G2 harder in Russian; it requires domestic
Russian-language sources that G2's policy does not govern.

---

## 4. Shopify App Store — the taxonomy's own rules

Source: `https://apps.shopify.com/sitemap.xml` and per-locale category sitemaps. Rung 2,
PRIMARY, `en`/`tr`/`es`.

| Rule | Status | Evidence |
|---|---|---|
| Taxonomy shape | 3 levels, 7 top-level categories, **161 category URLs total** | `sitemap_categories_en.xml`, PRIMARY |
| Organizing principle | **By merchant workflow, not by software category** — "Marketing and conversion", "Orders and shipping", "Store design" | Category slugs, PRIMARY |
| Localization | Taxonomy is **not localized at slug level**: 23 locales, identical 161 English slugs with `?locale=` appended. `tr` = 161, `es` = 161, `en` = 161 | Three sitemaps, PRIMARY |
| Whether displayed names are translated | **UNKNOWN** — requires a localized category page | not captured |
| Per-category app count | **Not published.** The category page is a curated landing page; no "1–24 of N" anywhere | PRIMARY (page captured, count absent) |
| Store-wide app total | "over 16,000 apps" seen via a model-mediated read only — **not verified by byte-exact capture**, so `SINGLE-SOURCE`, and per §2 treat any tool-reported number with suspicion | Rung 4 |
| Listing requirements | **UNKNOWN** — not located in this pass | — |
| Quality marker | "Built for Shopify" apps "meet our highest standards for performance, design, and integration" — criteria not captured | Rung 4 |

**The consequence for this study is severe and worth being blunt about:** a marketplace with
no published per-category count cannot be ranked, and cannot corroborate anyone else's count.
Shopify's usable contribution to a taxonomy pass is the **shape** of the taxonomy — which is
genuinely informative, because a workflow-shaped taxonomy tells you the buyer is a merchant
choosing a task, not a buyer choosing a software category.

### Shopify categories in scope

| raw_name (from slug) | Path | Scope call | Deciding clause |
|---|---|---|---|
| Email marketing | marketing-and-conversion › marketing › email-marketing | **IN** | IN-clause |
| SMS marketing | marketing-and-conversion › marketing › sms-marketing | **IN** | IN-clause |
| Web push | marketing-and-conversion › marketing › web-push | **IN** | IN-clause |
| Abandoned cart | marketing-and-conversion › marketing › abandoned-cart | **IN** | IN-clause — behaviour-triggered by definition |
| Marketing other | marketing-and-conversion › marketing › marketing-other | **BOUNDARY** | Residual bucket; contents unknowable from the name |
| Loyalty and rewards | marketing-and-conversion › customer-loyalty › loyalty-and-rewards | **BOUNDARY** | Boundary case 3 — loyalty with messaging attached |
| Pop-ups | store-design › notifications › pop-ups | **BOUNDARY** | On-site, not outbound; behaviour-triggered |
| Forms | store-design › notifications › forms | **BOUNDARY** | Collection, not orchestration — but feeds it |
| Banners | store-design › notifications › banners | **OUT** | On-site display, no stored-data targeting |
| Stock alerts | marketing-and-conversion › upsell-and-bundles › stock-alerts | **IN** | Triggered outbound driven by stored interest |
| Chat | store-management › support › chat | **BOUNDARY** | Predominantly inbound |
| Social proof | marketing-and-conversion › social-trust › social-proof | **OUT** | On-site display |
| Product reviews | marketing-and-conversion › social-trust › product-reviews | **OUT** | Feedback collection |
| Discounts / Promotions | marketing-and-conversion › promotions › * | **BOUNDARY** | Offer mechanics; delivery may or may not be in the product |
| Gift cards | marketing-and-conversion › gifts › gift-cards | **OUT** | Payment instrument |
| Donations | marketing-and-conversion › customer-loyalty › donations | **OUT** | Payment collection |
| Wishlists | marketing-and-conversion › customer-loyalty › wishlists | **BOUNDARY** | Stored behaviour; triggering varies |

**Note the taxonomy disagreement, which is data and not noise.** Shopify files **pop-ups,
forms and banners under "Store design"** — a design concern — while G2 files the equivalent
functions under Marketing. Shopify files **loyalty under "Marketing and conversion"**; G2
files Loyalty Management under Demand Generation. Neither is wrong. They are answering
different questions, and any merged count across them is an artefact of that difference.
Logged as `C-0002`.

---

## 5. HubSpot ecosystem — the taxonomy's own rules

Source: `https://ecosystem.hubspot.com/marketplace-en-apps-categories-1.xml`, discovered via
`robots.txt`. Rung 2, PRIMARY, `en`.

| Rule | Status | Evidence |
|---|---|---|
| Taxonomy shape | **Flat. 60 categories, no hierarchy** | sitemap, PRIMARY |
| Organizing principle | **By software category** (`marketing-automation`, `crm`, `erp`, `sms`) — closer to G2's basis than to Shopify's | slugs, PRIMARY |
| Localization | 17 locales; category slugs identical across them | sitemap index, PRIMARY |
| Per-category app count | **Not published.** But the sitemap exposes pagination depth per category (`/page/1`…`/page/N`), which is a **relative size proxy, not a count** | PRIMARY for the depth; the count itself `UNKNOWN` |
| Category pages | **JS-rendered.** Every category URL returns an identical 53,230-byte shell | PRIMARY (two categories fetched, byte-identical) |
| Listing requirements | **UNKNOWN** — not located in this pass | — |

### HubSpot categories in scope, with the only size-like signal any source gave us

`pages` = number of listing pages the sitemap exposes. **This is a proxy for relative size and
is not a product count.** It is `PRIMARY` as a page count and `UNKNOWN` as a product count,
and it must never be presented as the latter.

| raw_name (slug) | pages | Scope call | Deciding clause |
|---|---|---|---|
| `marketing-automation` | 3 | **IN** | IN-clause |
| `sms` | 2 | **IN** | IN-clause |
| `direct-mail-automation` | 1 | **IN** | IN-clause |
| `messaging-network` | 1 | **IN** | IN-clause |
| `email` | 1 | **BOUNDARY** | Ambiguous between marketing send and mail client |
| `crm` | 4 | **BOUNDARY** | Boundary case 1 — CRM suite with campaign module |
| `live-chat` | 2 | **BOUNDARY** | Predominantly inbound |
| `abm` | 2 | **IN** | IN-clause |
| `advertising` | 1 | **BOUNDARY** | Ad-channel outbound |
| `social-media-management` | 1 | **BOUNDARY** | Publishing to an audience, not to records |
| `event-management` | 1 | **BOUNDARY** | Triggered attendee comms are part of the job |
| `lead-scoring-routing` | 3 | **OUT** | Scoring and routing; no outbound orchestration |
| `marketing-analytics` | 3 | **OUT** | OUT-clause 1 — measurement without activation |
| `sales-engagement` | 1 | **IN** | IN-clause |
| `surveys` | 1 | **OUT** | Collection, not orchestration |
| `ecommerce` | 2 | **OUT** | Different job |
| `experience-management` | 1 | **BOUNDARY** | Name does not resolve the function |

**A category-cluster warning, per `CLAUDE.md` §7.3.** HubSpot's `crm` at 4 pages and G2's
`CRM` category are not the same object and their sizes are not comparable: HubSpot lists apps
that *integrate with* HubSpot, so its taxonomy measures **an ecosystem around one vendor**,
not a market. A vendor absent from HubSpot has told you it does not integrate with HubSpot —
nothing more.

---

## 6. G2 catalogues services — which contradicts amendment 2, and you should decide what to do

Amendment 2 struck `competitor_class` on the stated premise that **"taxonomies only classify
software."** The evidence says that premise is wrong for G2, and I am not going to quietly
apply an amendment whose reasoning the first pass falsified.

G2 operates **9 service-provider branches** alongside its software branches, governed by a
published rule: *"A service provider is any business offering where there is majority of human
intervention or involvement in completing projects."* Within the screen, **31 categories are
service-provider categories**, including:

- **Marketing Automation Consulting Providers** (`marketing-automation-consulting`)
- **Email Marketing Services Providers** (`email-marketing-services`)
- **Mobile Marketing Companies** (`mobile-marketing-companies`)
- **Outbound Marketing Services** (`outbound-marketing`), with Advertising Agencies beneath it
- **Contact Center Outsourcing Service Providers**, **Contact Center Consulting Providers**
- **Managed Live Chat Providers**
- 4 VAR categories — **Infor CRM Resellers**, **Sage CRM Resellers**, Unified Communication VARs

That is **competitor class 3 (agencies and services firms) and class 4 (systems integrators)
appearing directly in a vendor taxonomy** — the thing the amendment says taxonomies cannot do.

**What the amendment got right, and it is the more important half:** these listings are
`SELF-DECLARED`, so they enumerate *agencies that chose to list on G2*, which is a far smaller
and differently-shaped population than *buyers who solved this by hiring an agency*. G2 cannot
tell you how often the agency route wins. It can tell you the route exists and name firms
selling it.

**So the honest position is narrower than either the amendment or its opposite:** classes 3
and 4 are **partially enumerable, at self-declared-supply level only**. Class 2 (in-house),
5 (bundled modules), 6 (assembled substitutes) and 7 (status quo) remain fully unmeasured.

**This is your call, not mine.** Option A: keep the amendment as written and drop these 31
categories, accepting that a visible, named part of the competitive set is excluded by a rule
whose premise does not hold. Option B: reinstate a *supply-side-only* services column for
classes 3–4, explicitly marked as self-declared supply and not demand. I recommend B, and I
have left the 31 categories in the tables marked `SERVICES` so that either decision is one
edit away. I have not applied B.

---

## 7. The ranked table — and why it is not ranked

You asked to close with a single ranked table of every IN and BOUNDARY category, ranked by
product count within each source.

**No source in this pass gave us a product count.**

- **G2** publishes counts on category pages. Every category page returns 403.
- **Gartner** publishes counts. Every Gartner URL returns 403.
- **Shopify** does not publish per-category counts at all.
- **HubSpot** does not publish counts; the page-depth proxy is not a count and will not be
  presented as one.

So the table below is **complete and unranked**. Producing a ranking from page-depth proxies,
or from alphabetical order, or from branch size, would produce a column that looks like a
measurement and is not one — and a reader would rank off it anyway. Per `CLAUDE.md` §2.1 the
map is handed over complete; the ordering is `UNKNOWN` and stays `UNKNOWN` until §8 is
answered.

**Counts, when they arrive, are still not comparable** — across categories with different bar
heights (G2's feature-requirement lists differ per category and are themselves blocked),
across sources with different construction rules (§3 vs §4 vs §5), or across G2 branches given
that G2 places a product in every category it qualifies for.

**Screen recall is `UNKNOWN` and this is the biggest hole in the table.** All 2,235 G2
categories were screened, but by **name only** — 65 substrings covering channels, functions
and verticals. A category whose name does not signal the function (a vertical suite with an
embedded campaign module) is invisible to a name screen. Catching those requires category
*definitions*, which are exactly what is blocked. The full 2,235-row enumeration is committed
at `sources/derived/g2-taxonomy-full.csv` so the screen can be re-run and audited against a
different keyword set.

**Screen result: 2,235 categories screened → 219 candidates → 29 IN, 49 BOUNDARY, 31 SERVICES,
110 OUT.**

### 7.1 Complete classification — G2

#### IN — 29 categories

| raw_name (verbatim) | G2 branch | slug | scope call | deciding clause |
|---|---|---|---|---|
| AI Marketing Agents Software | Artificial Intelligence Software | `ai-marketing-agents` | IN | IN-clause |
| Conversational Commerce Platforms | Commerce Software | `conversational-commerce-platforms` | IN | IN-clause |
| Appointment Reminder Software | Customer Service Software | `appointment-reminder` | IN | IN-clause |
| Customer Communications Management Software | Customer Service Software | `customer-communications-management` | IN | IN-clause |
| Proactive Customer Retention Software | Customer Service Software | `proactive-customer-retention` | IN | IN-clause |
| Proactive Notification Software | Customer Service Software | `proactive-notification` | IN | IN-clause |
| Account-Based Direct Mail Software | Marketing Software | `account-based-direct-mail` | IN | IN-clause |
| Account-Based Marketing Software | Marketing Software | `account-based-marketing` | IN | IN-clause |
| Conversational Marketing Software | Marketing Software | `conversational-marketing` | IN | IN-clause |
| Direct Mail Automation Software | Marketing Software | `direct-mail-automation` | IN | IN-clause |
| Email Marketing Software | Marketing Software | `email-marketing` | IN | IN-clause |
| Location-Based Marketing Software | Marketing Software | `location-based-marketing` | IN | IN-clause |
| Marketing Automation Software | Marketing Software | `marketing-automation` | IN | IN-clause |
| Mobile Marketing Software | Marketing Software | `mobile-marketing` | IN | IN-clause |
| Push Notification Software | Marketing Software | `push-notification` | IN | IN-clause |
| SMS Marketing Software | Marketing Software | `sms-marketing` | IN | IN-clause |
| WhatsApp Marketing Software | Marketing Software | `whatsapp-marketing` | IN | IN-clause |
| Emergency Notification Software | Office Management Software | `emergency-notification` | IN | IN-clause |
| Sales Engagement Software | Sales Tools | `sales-engagement` | IN | IN-clause |
| Through-Channel Marketing Software | Sales Tools | `through-channel-marketing` | IN | IN-clause |
| AI Patient Engagement & Operations Software | Vertical Industry Software | `ai-patient-engagement-operations` | IN | IN-clause + vertical instance |
| Automotive Marketing Software | Vertical Industry Software | `automotive-marketing` | IN | IN-clause + vertical instance |
| Citizen Engagement Software | Vertical Industry Software | `citizen-engagement` | IN | IN-clause + vertical instance |
| Classroom Messaging Software | Vertical Industry Software | `classroom-messaging` | IN | IN-clause + vertical instance |
| Guest Messaging Software | Vertical Industry Software | `guest-messaging` | IN | IN-clause + vertical instance |
| Patient Engagement Software | Vertical Industry Software | `patient-engagement` | IN | IN-clause + vertical instance |
| Political Campaign Software | Vertical Industry Software | `political-campaign` | IN | IN-clause + vertical instance |
| Real Estate Marketing Software | Vertical Industry Software | `real-estate-marketing` | IN | IN-clause + vertical instance |
| Restaurant Marketing Tools Software | Vertical Industry Software | `restaurant-marketing-tools` | IN | IN-clause + vertical instance |

#### BOUNDARY — 49 categories

| raw_name (verbatim) | G2 branch | slug | scope call | deciding clause |
|---|---|---|---|---|
| AI Chatbots Software | Artificial Intelligence Software | `ai-chatbots` | BOUNDARY | IN-clause, direction disputed |
| Bot Platforms | Artificial Intelligence Software | `bot-platforms` | BOUNDARY | IN-clause, direction disputed |
| Chatbots Software | Artificial Intelligence Software | `chatbots` | BOUNDARY | IN-clause, direction disputed |
| Conversational Interface Agents Software | Artificial Intelligence Software | `conversational-interface-agents` | BOUNDARY | IN-clause, direction disputed |
| Enterprise AI Chatbots Software | Artificial Intelligence Software | `enterprise-ai-chatbots` | BOUNDARY | IN-clause, direction disputed |
| Merchant Marketing Software | B2B Marketplaces | `merchant-marketing` | BOUNDARY | IN-clause, addressability disputed |
| E-Commerce Personalization Software | Commerce Software | `e-commerce-personalization` | BOUNDARY | IN-clause, channel disputed |
| Contact Center Software | Customer Service Software | `contact-center` | BOUNDARY | IN-clause, direction disputed |
| Conversational Support Software | Customer Service Software | `conversational-support` | BOUNDARY | IN-clause, direction disputed |
| Customer Service Automation Software | Customer Service Software | `customer-service-automation` | BOUNDARY | IN-clause, direction disputed |
| Live Chat Software | Customer Service Software | `live-chat` | BOUNDARY | IN-clause, direction disputed |
| Data Breach Notification Software | Data Privacy Software | `data-breach-notification` | BOUNDARY | IN-clause, trigger disputed |
| Communication Platform as a Service (cPaaS) Platforms | Development Software | `communication-platform-as-a-service-cpaas` | BOUNDARY | BOUNDARY case 2 — delivery infrastructure moving up-stack |
| Geofencing Software | Development Software | `geofencing` | BOUNDARY | IN-clause, trigger disputed |
| Notification Infrastructure Software | Development Software | `notification-infrastructure` | BOUNDARY | BOUNDARY case 2 — delivery infrastructure moving up-stack |
| Cross-Channel Advertising Software | Digital Advertising Tech | `cross-channel-advertising` | BOUNDARY | BOUNDARY — ad-channel outbound |
| Display Advertising Software | Digital Advertising Tech | `display-advertising` | BOUNDARY | BOUNDARY — ad-channel outbound |
| Mobile Advertising Software | Digital Advertising Tech | `mobile-advertising` | BOUNDARY | BOUNDARY — ad-channel outbound |
| Retail Media Advertising Platforms | Digital Advertising Tech | `retail-media-advertising-platforms` | BOUNDARY | BOUNDARY — ad-channel outbound |
| Social Media Advertising Software | Digital Advertising Tech | `social-media-advertising` | BOUNDARY | BOUNDARY — ad-channel outbound |
| Employee Referral Software | HR Software | `employee-referral` | BOUNDARY | IN-clause, recipient disputed |
| Programmatic Job Advertising Software | HR Software | `programmatic-job-advertising` | BOUNDARY | IN-clause, recipient disputed |
| Recruiting Automation Software | HR Software | `recruiting-automation` | BOUNDARY | IN-clause, recipient disputed |
| Recruitment Marketing Platforms | HR Software | `recruitment-marketing` | BOUNDARY | IN-clause, recipient disputed |
| Account-Based Advertising Software | Marketing Software | `account-based-advertising` | BOUNDARY | BOUNDARY — ad-channel outbound |
| Book Marketing Tools | Marketing Software | `book-marketing-tools` | BOUNDARY | IN-clause, addressability disputed |
| Customer Data Platforms (CDP) | Marketing Software | `customer-data-platform-cdp` | BOUNDARY | BOUNDARY case 4 — CDP sold with or without activation |
| Event Marketing Software | Marketing Software | `event-marketing` | BOUNDARY | IN-clause, addressability disputed |
| Local Marketing Software | Marketing Software | `local-marketing` | BOUNDARY | IN-clause, addressability disputed |
| Loyalty Management Software | Marketing Software | `loyalty-management` | BOUNDARY | BOUNDARY case 3 — loyalty platform with messaging attached |
| Multi-Location Marketing Platforms | Marketing Software | `multi-location-marketing-platforms` | BOUNDARY | IN-clause, addressability disputed |
| Other Marketing Software | Marketing Software | `other-marketing` | BOUNDARY | Residual bucket |
| Personalization Engines | Marketing Software | `personalization-engines` | BOUNDARY | IN-clause, channel disputed |
| Personalization Software | Marketing Software | `personalization` | BOUNDARY | IN-clause, channel disputed |
| RCS Business Messaging Software | Marketing Software | `rcs-business-messaging` | BOUNDARY | BOUNDARY case 2 — delivery infrastructure moving up-stack |
| Social Media Marketing Software | Marketing Software | `social-media-marketing` | BOUNDARY | IN-clause, addressability disputed |
| Transactional Email Software | Marketing Software | `transactional-email` | BOUNDARY | BOUNDARY case 2 — delivery infrastructure moving up-stack |
| CRM Software | Sales Tools | `crm` | BOUNDARY | BOUNDARY case 1 — CRM suite carrying a campaign module |
| Alumni Management Software | Vertical Industry Software | `alumni-management` | BOUNDARY | IN-clause, recipient disputed |
| Construction CRM Software | Vertical Industry Software | `construction-crm` | BOUNDARY | BOUNDARY case 1 — CRM suite carrying a campaign module |
| Donor Management Software | Vertical Industry Software | `donor-management` | BOUNDARY | IN-clause, recipient disputed |
| Financial Services CRM Software | Vertical Industry Software | `financial-services-crm` | BOUNDARY | BOUNDARY case 1 — CRM suite carrying a campaign module |
| Fundraising Software | Vertical Industry Software | `fundraising` | BOUNDARY | IN-clause, recipient disputed |
| HIPAA Compliant Messaging Software | Vertical Industry Software | `hipaa-compliant-messaging` | BOUNDARY | IN/OUT undecidable |
| Insurance CRM Software | Vertical Industry Software | `insurance-crm` | BOUNDARY | BOUNDARY case 1 — CRM suite carrying a campaign module |
| Legal CRM Software | Vertical Industry Software | `legal-crm` | BOUNDARY | BOUNDARY case 1 — CRM suite carrying a campaign module |
| Mortgage CRM Software | Vertical Industry Software | `mortgage-crm` | BOUNDARY | BOUNDARY case 1 — CRM suite carrying a campaign module |
| Nonprofit CRM Software | Vertical Industry Software | `nonprofit-crm` | BOUNDARY | BOUNDARY case 1 — CRM suite carrying a campaign module |
| Real Estate CRM Software | Vertical Industry Software | `real-estate-crm` | BOUNDARY | BOUNDARY case 1 — CRM suite carrying a campaign module |

#### SERVICES — 31 categories

| raw_name (verbatim) | G2 branch | slug | scope call | deciding clause |
|---|---|---|---|---|
| Contact Center Consulting Providers | Business Services Providers | `contact-center-consulting` | SERVICES | n/a — not software |
| DataRobot Consulting Services | Ecosystem Service Providers | `datarobot-consulting-services` | SERVICES | n/a — not software |
| Advertising Agencies | Marketing Services Providers | `advertising-agencies` | SERVICES | n/a — not software |
| Affiliate Marketing Companies | Marketing Services Providers | `affiliate-marketing-agencies` | SERVICES | n/a — not software |
| Amazon Marketing Services Providers | Marketing Services Providers | `amazon-marketing-services` | SERVICES | n/a — not software |
| Content Marketing Agencies | Marketing Services Providers | `content-marketing-agencies` | SERVICES | n/a — not software |
| Digital Marketing Services | Marketing Services Providers | `digital-marketing` | SERVICES | n/a — not software |
| Email Marketing Services Providers | Marketing Services Providers | `email-marketing-services` | SERVICES | n/a — not software |
| Experiential Marketing Agencies | Marketing Services Providers | `experiential-marketing-agencies` | SERVICES | n/a — not software |
| Inbound Marketing Services | Marketing Services Providers | `inbound-marketing` | SERVICES | n/a — not software |
| Marketing Analytics Service Providers | Marketing Services Providers | `marketing-analytics-services` | SERVICES | n/a — not software |
| Marketing Automation Consulting Providers | Marketing Services Providers | `marketing-automation-consulting` | SERVICES | n/a — not software |
| Marketing Strategy Agencies | Marketing Services Providers | `marketing-strategy` | SERVICES | n/a — not software |
| Mobile Marketing Companies | Marketing Services Providers | `mobile-marketing-companies` | SERVICES | n/a — not software |
| Other Marketing Services Providers | Marketing Services Providers | `other-marketing-services` | SERVICES | n/a — not software |
| Outbound Marketing Services | Marketing Services Providers | `outbound-marketing` | SERVICES | n/a — not software |
| Reputation Management Services Providers | Marketing Services Providers | `reputation-management-services` | SERVICES | n/a — not software |
| Search Engine Marketing (SEM) Agencies | Marketing Services Providers | `search-engine-marketing-sem` | SERVICES | n/a — not software |
| Social Media Marketing (SMM) Companies | Marketing Services Providers | `social-media-marketing-smm-companies` | SERVICES | n/a — not software |
| Traditional Advertising Agencies | Marketing Services Providers | `traditional-advertising` | SERVICES | n/a — not software |
| Managed Live Chat Providers | Other Services Providers | `managed-live-chat` | SERVICES | n/a — not software |
| Account-Based Marketing Agencies | Professional Services Providers | `account-based-marketing-agencies` | SERVICES | n/a — not software |
| Robotic Process Automation (RPA) Consultancy Services | Professional Services Providers | `robotic-process-automation-rpa-consultancy-services` | SERVICES | n/a — not software |
| Shopify Marketing Experts | Professional Services Providers | `shopify-marketing-experts` | SERVICES | n/a — not software |
| Email Security Services Providers | Security and Privacy Services Providers | `email-security-services` | SERVICES | n/a — not software |
| Recruitment Marketing Agencies | Staffing Services Providers | `recruitment-marketing-agencies` | SERVICES | n/a — not software |
| Marketing Localization Providers | Translation Services Providers | `marketing-localization` | SERVICES | n/a — not software |
| Cisco Unified Communications Resellers | Value-Added Resellers (VARs) | `cisco-unified-communications-resellers` | SERVICES | n/a — not software |
| Infor CRM Resellers | Value-Added Resellers (VARs) | `infor-crm-resellers` | SERVICES | n/a — not software |
| Sage CRM Resellers | Value-Added Resellers (VARs) | `sage-crm-resellers` | SERVICES | n/a — not software |
| Unified Communication VARs Providers | Value-Added Resellers (VARs) | `unified-communication-vars` | SERVICES | n/a — not software |

#### Deciding-clause reasons (BOUNDARY only)

- **IN-clause, direction disputed** — Predominantly inbound response; outbound/triggered capability exists in part of each category.
- **BOUNDARY case 1 — CRM suite carrying a campaign module** — Pipeline CRM is explicitly OUT; the same product may carry campaign orchestration. Undecidable from the category name — needs the source's inclusion criteria.
- **BOUNDARY — ad-channel outbound** — Outbound and often driven by uploaded customer data, but the channel is an ad exchange and the target is a segment, not a record.
- **IN-clause, addressability disputed** — Publishing to an audience rather than to stored individual records; some products in these categories do both.
- **BOUNDARY case 4 — CDP sold with or without activation** — The named boundary class. Whether activation is mandatory is exactly what the inclusion criteria decide.
- **BOUNDARY case 3 — loyalty platform with messaging attached** — The named boundary class.
- **Residual bucket** — G2 rule: 'Other' holds products qualifying for no defined category. Contents unknowable without the product list.
- **IN-clause, channel disputed** — Behaviour-driven and data-driven, but the 'channel' is often the site itself rather than an outbound message.
- **BOUNDARY case 2 — delivery infrastructure moving up-stack** — Transport without targeting logic is OUT; these categories contain both pure transport and products that have moved into orchestration.
- **IN-clause, trigger disputed** — Triggered customer communication driven by stored data; compliance-driven rather than commercial.
- **IN-clause, recipient disputed** — Function matches exactly; the recipient is a candidate, not a customer. See the proposed wording change.
- **IN/OUT undecidable** — Category name does not say whether the messaging is clinician-to-patient (IN) or clinician-to-clinician (OUT).

### 7.2 Complete classification — Shopify and HubSpot

See §4 and §5. Shopify: 5 IN, 7 BOUNDARY of 161 categories. HubSpot: 6 IN, 8 BOUNDARY of 60.

### 7.3 Cross-source spine

| | G2 | Gartner | Shopify | HubSpot |
|---|---|---|---|---|
| Categories enumerated | 2,235 | **NOT-CHECKED** | 161 | 60 |
| In-scope IN | 29 | **NOT-CHECKED** | 5 | 6 |
| In-scope BOUNDARY | 49 | **NOT-CHECKED** | 7 | 8 |
| Organizing principle | product function | **UNKNOWN** | merchant workflow | software category, HubSpot-adjacent |
| Hierarchy | 3+ levels, products only in leaves | **UNKNOWN** | 3 levels | flat |
| Multi-category placement | all qualifying categories | **UNKNOWN** | UNKNOWN | UNKNOWN |
| Minimum to create a category | 10 products | **UNKNOWN** | UNKNOWN | UNKNOWN |
| Inclusion criteria published? | yes, per category — **blocked** | yes, per market — **blocked** | UNKNOWN | UNKNOWN |
| Product counts published? | yes — **blocked** | yes — **blocked** | **no** | **no** |
| Decline markers | **none — dead products are deleted** | `(Legacy)` `(Retired)` `(Transitioning to X)` — **blocked** | none | none |
| Failure detectable? | **no, by policy** | would be, if reachable | only by two-capture diff | only by two-capture diff |

**Every column that decides anything is blocked or absent.** That is the state of the
evidence, and it is why §8 exists.

---

## 8. What I need from you — batched Rung 3 requests

Ordered by what each unblocks. Requests 1–2 are the difference between a study and a
directory listing.

### Request 1 — Gartner Peer Insights: the markets index (**highest value**)
- **URL:** `https://www.gartner.com/reviews/markets`
- **Copy:** the whole page — **every market name**, including any `(Legacy)`, `(Retired)` or
  `(Transitioning to X)` suffix, exactly as printed.
- **Pagination:** likely. If it says "1–20 of N" or has page numbers, **please page through to
  the end** — a partial index gives us no denominator, which is the entire point of the request.
- **Decides:** whether this study has a Gartner denominator at all, and whether it has any
  failure-detection mechanism. Without it, §7.3's Gartner column stays `NOT-CHECKED` forever
  and every pass built on this is winners-only.

### Request 2 — G2 category pages: definition + inclusion criteria + product count
For each URL: copy **the category definition paragraph(s)**, **the entire "To qualify for
inclusion in the … category, a product must:" bullet list**, and **the product count line**
(e.g. "Products 1–20 of 122") — verbatim, including the numbers.

1. `https://www.g2.com/categories/marketing-automation`
2. `https://www.g2.com/categories/email-marketing`
3. `https://www.g2.com/categories/sms-marketing`
4. `https://www.g2.com/categories/push-notification`
5. `https://www.g2.com/categories/mobile-marketing`
6. `https://www.g2.com/categories/customer-communications-management`
7. `https://www.g2.com/categories/customer-data-platform-cdp`
8. `https://www.g2.com/categories/loyalty-management`
9. `https://www.g2.com/categories/proactive-notification`
10. `https://www.g2.com/categories/patient-engagement`
11. `https://www.g2.com/categories/citizen-engagement`
12. `https://www.g2.com/categories/political-campaign`

- **Pagination:** the definition and criteria are on page 1 — **no need to page through the
  product list.** I need the *declared total*, not the products.
- **Decides:** bar height per category (§3 says a product must meet **all** feature
  requirements, so the bullet count is the entry cost), the first real counts in the study,
  and — for 7 and 8 — whether the CDP and loyalty boundary cases resolve IN or OUT on G2's
  own criteria rather than on my reading of a name.
- **Why these twelve:** 1–6 are the functional core; 7–8 are two of the four named boundary
  classes; 9 tests whether a service-desk-framed category carries the same criteria as a
  marketing-framed one; 10–12 are vertical instances in healthcare, public sector and
  politics — the branch most likely to contain a large market invisible to the other sources.
  **This is a sample I chose, and it is logged as such in `logs/paste-log.md`.** If you have
  appetite for more, the next twelve are yours to pick from the 78 IN/BOUNDARY rows above —
  and it would be better for the study if *you* picked them, because then the sampling frame
  is not mine alone.

### Request 3 — Gartner: one market page, to learn the shape
- **URL:** `https://www.gartner.com/reviews/market/marketing-automation-platforms`
  (if it 404s, any market page reachable from Request 1's index)
- **Copy:** the **market definition**, any **mandatory/core capabilities list**, the
  **declared vendor count**, and any decline marker.
- **Decides:** the column layout for `schemas/gartner.md` against a real page instead of an
  assumed one.

### Request 4 — listing requirements for the two marketplaces (low value, cheap)
- `https://apps.shopify.com/` → whatever page states **app listing / review requirements**
- `https://ecosystem.hubspot.com/` → the **app certification / listing requirements** page
- **Copy:** the requirements list verbatim.
- **Decides:** bar height for both marketplaces, currently `UNKNOWN`, which is what makes
  their counts non-comparable to anything.

**If you cannot supply one of these, say so and I will mark it `UNKNOWN` and state what it
would have decided.** I will not fill it with a search summary.

---

## 9. Registry and logs

- `industry-registry.md` — entries appended for every IN and BOUNDARY category, with source
  aliases. Entries are `PROVISIONAL` where the scope call rests on a category **name** rather
  than a fetched definition, which is currently **all of them**.
- `logs/fetch-log.md` — 31 attempts, all outcomes, block rate by language.
- `logs/paste-log.md` — the four requests above, pre-registered before the pastes arrive, so
  the sampling frame is recorded independently of what comes back.
- `logs/conflicts.md` — `C-0001` tool-vs-source count discrepancy; `C-0002` Shopify/G2
  taxonomy placement disagreement.
- `logs/boundary-rulings.md` — 49 BOUNDARY rulings.
- `sources/derived/g2-taxonomy-full.csv` — all 2,235 G2 categories, so the screen is auditable
  and re-runnable.
