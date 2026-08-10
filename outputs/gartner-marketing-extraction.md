# outputs/gartner-marketing-extraction.md

**Pass 02 — extraction from the supplied Gartner Peer Insights pages.**
Captured 2026-08-10 by human transport (Rung 3). Raw pages in
`sources/raw/web pages/gartner/`.

---

## 0. This is a PURPOSIVE SAMPLE. Read this before any number below.

**The seven market pages extracted here were selected by the user, deliberately and
non-randomly, using information this study does not have.** That is purposive sampling: a
legitimate method when declared, and a silent bias when not. It is declared.

**What may be said:** *"within the supplied set, X."*
**What may never be said:** *"the market contains N categories of this kind"* — unsupportable
from a purposive sample, in either direction.

**Nothing is inferred from the selection itself.** Not what the client sells, not what it
cares about, not why these seven and not others. The blinding protocol holds (`CLAUDE.md` §2).

**Gartner's Marketing-branch denominator still does not exist.** Seven pages were supplied;
how many Marketing categories Gartner operates is `UNKNOWN`. Every Gartner absence therefore
remains `NOT-CHECKED` — never `ABSENT` — at the *branch* level. See §7.

**Done for this pass** = every supplied page fully extracted. All seven were. Not "enough
found."

**Competitor-class statement** (`CLAUDE.md` §4): demand-side evidence exists for none of
classes 2–7. Everything here is contest among listed software vendors.

---

## 1. What arrived, at a glance

| raw_name (verbatim) | Market or Category | Bar height | Features dated | Products stated | Products visible | (Legacy) products |
|---|---|---|---|---|---|---|
| Multichannel Marketing Hubs | MARKET (analyst-defined) | **6** | October 2025 | **122** | 122 (full) | 5 |
| Email Marketing (Transitioning to Email Marketing Platforms) | MARKET (analyst-defined) | **4** | December 2025 | **100** | 100 (full) | 1 |
| Customer Data Platforms | MARKET (analyst-defined) | **4** | January 2026 | **71** | 71 (full) | 1 |
| Personalization Engines | MARKET (analyst-defined) | **8** | February 2026 | **64** | 64 (full) | 5 |
| B2B Marketing Automation Platforms | MARKET (analyst-defined) | **5** | September 2025 | **59** | 59 (full) | 3 |
| Mobile Marketing Platforms | MARKET (analyst-defined) | **3** | February 2026 | **45** | 45 (full) | 0 |
| Location Based Marketing Software | CATEGORY (Peer Insights-created) | **none published** | — | **15** | 15 (full) | 0 |
**Every one of the seven enumerates fully** — "Products 1 – N of N". This is the first place
in the study where `ABSENT-ENUMERATED` is actually available: if a vendor is not in Gartner's
Multichannel Marketing Hubs list of 122, it is genuinely absent from that market, not merely
absent from a visible page. That is a materially stronger evidentiary position than anything
G2, Shopify or HubSpot has given us.

---

## 2. The single most useful thing learned: Market ≠ Category

The Peer Insights FAQ states the rule:

> "Markets and Categories are both collections of software or services of comparable products
> or service offerings. **The difference between Markets and Categories is in how they are
> defined. Markets are defined by Gartner analysts within Gartner Insights. The market
> definitions are published in Magic Quadrant and Market Guide documents.** … To that end,
> **Gartner Peer Insights creates and defines Categories** in other technology and business
> areas."

**Both live at the same URL pattern `/reviews/market/…`. The URL does not disclose which one
you are looking at.** Treating them as one object would merge analyst-governed markets with
Peer-Insights-generated buckets and average their bar heights — a defect invisible in the
output.

**Two discriminators were tested against the seven pages. One works, one does not:**

| Discriminator | Verdict |
|---|---|
| Definition opens *"Gartner defines…"* | **Fails.** True for B2B MAP, Email Marketing, MMH, Mobile Marketing Platforms — but **false** for Customer Data Platforms and Personalization Engines, which are analyst markets with Magic Quadrants |
| **Presence of a `Mandatory Features:` list AND at least one analyst document** (Magic Quadrant / Critical Capabilities / Market Guide) | **Works. 7/7.** Six markets have both; Location Based Marketing Software has neither |

**Use the second. It is the operational test for every Gartner page from here on.**

Location Based Marketing Software is the control case: no Magic Quadrant, no Critical
Capabilities, no Market Guide, **no mandatory features at all**, 15 products. Its product
count is not comparable to Multichannel Marketing Hubs' 122 in any respect — different
governance, different entry cost, different reason for existing.

---

## 3. Bar height — and the pattern that only definitions could reveal

The brief predicted this exactly: *"Some categories demand three capabilities each labelled
'basic'; others demand eight including generative AI and multiarmed-bandit testing."* Both
extremes are in the sample, verbatim.

| Market | Bar | Character of the requirements | Products |
|---|---|---|---|
| Personalization Engines | **8** | Hardest in the sample. Requires *"Embedded generative AI (GenAI) in content creation"*, *"Automated machine learning capabilities"*, and *"Extensive testing capabilities (e.g., A/B, multivariate, **multiarmed bandit**)"* | 64 |
| Multichannel Marketing Hubs | **6** | Broad and operational — consent/preference management, application governance incl. *"global frequency capping"*, journey management, analytics, data integration, multichannel execution | **122** |
| B2B Marketing Automation Platforms | **5** | Demand-generation shaped: lead scoring, drip journeys, unified profile, native email + landing page execution | 59 |
| Customer Data Platforms | **4** | Data-shaped: profile management, **activation**, ingestion, analytic reporting | 71 |
| Email Marketing *(Transitioning)* | **4** | Lowest of the markets, and plainly worded: template design, list ingest/segment, bulk send, opt-in/opt-out | **100** |
| Mobile Marketing Platforms | **3** | Every requirement literally prefixed **"Basic"** — *"Basic analytics…"*, *"Basic customer profile data management…"*, *"Basic mobile channel campaign management…"* | 45 |
| Location Based Marketing Software | **none** | No mandatory features published | 15 |

### Where bar and count point in opposite directions

**Mobile Marketing Platforms is the anomaly: the lowest bar in the sample (3, all "Basic")
producing only 45 products — while Email Marketing at bar 4 holds 100 and Multichannel
Marketing Hubs at bar 6 holds 122.**

A low bar with few products is the combination worth naming. The mechanical reading is that
entry cost does not explain participation here, so something else limits it. Candidate
explanations, **all unverified and none to be treated as findings**: the market is genuinely
smaller; it is being absorbed by the higher-bar hubs above it; or Gartner has not run the
review-solicitation effort that populates a listing. **Three of the four highest-bar markets
also carry Magic Quadrants**, which attract vendor participation, and Mobile Marketing
Platforms has only a Market Guide. Distinguishing these requires the branch denominator and a
second dated capture. Logged as an open question, not a conclusion.

The inverse pattern — **Multichannel Marketing Hubs, bar 6, 122 products, the largest count in
the sample** — says the opposite: a demanding, analyst-governed definition with the heaviest
participation. Whatever is happening in this branch, it is not that low barriers drive counts.

**Counts across these rows are not comparable**, and the table above is the proof rather than
the exception: 3 "Basic" requirements and 8 including multiarmed-bandit testing are not the
same admission test, so 45 and 64 are not the same kind of number.

---

## 4. Failure evidence — the first non-winners data in this study

Gartner marks decline explicitly. **15 `(Legacy)` product instances appear across the seven
pages**, and they are concentrated in exactly the markets with the highest bars.

| Market | `(Legacy)` products |
|---|---|
| Multichannel Marketing Hubs | `BlueVenn (Legacy)`, `Portrait Dialogue (Legacy)`, `SAP Marketing Cloud (Legacy)`, `SAS Marketing Automation (Legacy)`, `SAS Real-Time Decision Manager (Legacy)` |
| Personalization Engines | `Experience Orchestrator (XO) (Legacy)`, `IBM Interact (Legacy)`, `IBM Watson Personalization (Legacy)`, `Oracle Maxymiser (Legacy)`, `Reflektion Customer Engagement Platform (Legacy)` |
| B2B Marketing Automation Platforms | `Datalogix (Legacy)`, `Dynamics CRM (Legacy)`, `SAP Marketing Cloud (Legacy)` |
| Customer Data Platforms | `BlueVenn (Legacy)` |
| Email Marketing *(Transitioning)* | `SpiceSend Email Marketing Tool (Legacy)` |
| Mobile Marketing Platforms | none |
| Location Based Marketing Software | none |

**What makes these valuable is that the ratings survive the marker.** `SAS Real-Time Decision
Manager (Legacy)` still carries its rating and review history while its own analyst source
labels it managed decline. A reader ranking by rating alone would not see it. This is the
exact row type the protocol calls the highest-value single observation in the study, and it
exists only because Gartner publishes decline — G2 **deletes** dead products and their reviews
by policy, so no amount of G2 reading produces this.

**Named incumbents are visibly declining in this branch:** SAP, SAS, IBM and Oracle appear
between them nine times in the legacy list. Stated as an observation within the supplied
sample, not as a market conclusion.

### A category in motion

**`Email Marketing (Transitioning to Email Marketing Platforms)`** — the taxonomy itself is
moving, marked on the category name, carried through into its own artefacts:
*"Features of Email Marketing (Transitioning to Email Marketing Platforms) — Updated December
2025"* and *"Market Guide for Email Marketing (Transitioning to Email Marketing Platforms)"*.

Both names are registered as aliases of one registry entry, per `industry-registry.md` §6. The
practical consequence: **a count captured before the transition and one captured after are not
comparable**, and any trend drawn across that boundary is an artefact of the rename.

**No `(Retired)` category appears in the Marketing branch in this sample.** Forty-two
`(Retired)` markers were captured — but all in the Application Development nav list that every
page carries incidentally (`Application Composition Platform (Retired)`, `Multiexperience
Development Platforms (Retired)`, `R&D Outsourcing Providers (Retired)`, and others). Whether
the Marketing branch contains retired categories is **`NOT-CHECKED`, not `ABSENT`** — the
branch list was never supplied.

---

## 5. Scope calls under the revised definition

Applying the recipient/channel definition adopted in `CLAUDE.md` §1.

| Gartner market | Scope call | Deciding clause |
|---|---|---|
| **Multichannel Marketing Hubs** | **IN** | "orchestrate personalized campaigns and event-driven customer journeys across marketing channels… owned media channels such as email and app push" — organisation-initiated delivery to identified recipients, mandatory feature 6 requires multichannel execution |
| **Email Marketing (Transitioning)** | **IN** | "use of the email channel to deliver and optimize marketing messages"; mandatory features require list ingest, segmentation and bulk send |
| **B2B Marketing Automation Platforms** | **IN** | Mandatory feature 5 requires "coordinated customer engagement programs across multiple channels, including native email and landing page execution" |
| **Mobile Marketing Platforms** | **IN** | "target audiences on their mobile device through… SMS/text, push notifications, messaging apps, in-app messages" — **in-app messaging is a received channel and is IN** under the tightening |
| **Location Based Marketing Software** | **IN** | "send personalized messages, offers, or ads when users are near a specific location" — behaviour-triggered delivery to an identified recipient |
| **Customer Data Platforms** | **OUT** | **Resolved by the source's own mandatory features.** Activation is defined as *"the ability to **send segments, with instructions for activating them, to engagement tools and platforms**"* — the CDP hands segments to systems that deliver; it does not itself initiate delivery to a recipient. Boundary case 4 resolves **OUT** on Gartner's criteria |
| **Personalization Engines** | **OUT** | **Resolved by the in-app tightening.** "create and deliver an optimum experience… across channels" is altering what a surface shows a visitor who came to it. **None of the 8 mandatory features requires a received channel.** OUT unless a given product also orchestrates one |

**Where Gartner's boundary differs from ours — logged, not normalised:**

1. **Personalization Engines includes employees as recipients.** Verbatim: *"A recipient can
   be a prospect, customer (known or anonymous) **or employee (engaging with a customer or
   prospect)**."* Our definition explicitly excludes the organisation's own employees.
   Gartner's boundary is wider than ours on the recipient axis. `C-0004`.
2. **Gartner states the overlap itself.** Verbatim: *"Although MMHs overlap with customer data
   platforms (CDPs) and personalization engines, their primary focus is enabling marketing
   users to manage large-scale consumer interactions."* Gartner is telling us its own three
   markets are not disjoint — so **summing 122 + 71 + 64 counts the same vendors repeatedly**,
   and the source says so in its own words. `C-0005`.

---

## 6. Peer Insights governance — what the FAQ changes

Extracted from `sources/raw/web pages/gartner/…/reviews/faq`. Each of these alters how a
Gartner number should be read.

### 6.1 A published language exclusion that hits three of our six required languages

> "At this time, reviews must be written entirely in **English, Spanish, German, French,
> Italian, Dutch, Portuguese, Simplified Chinese, Traditional Chinese or Japanese.** Any review
> submitted in a language not supported by our site, or a mix of languages, will not be
> eligible for current or future publication."

**Russian, Turkish and Georgian reviews are ineligible for publication on Gartner Peer
Insights, by policy.** Three of the six languages `CLAUDE.md` §6 requires are structurally
excluded at the source.

This is not an undercount we can correct by reading Gartner more carefully in those languages —
**the content does not exist to be read.** A vendor whose entire customer base would review it
in Russian or Turkish can appear in a Gartner listing but can accumulate **zero** publishable
reviews. Its rating and review count are therefore not weak evidence about that vendor; they
are **evidence about Gartner's language policy**. Combined with G2's OFAC removal policy
(`outputs/source-taxonomies.md` §3), **both analyst-grade sources censor the same regions in
different ways, for different stated reasons.** The language obligation cannot be met from
either. It requires domestic-language sources neither company governs.

Note that Spanish and Portuguese **are** supported — so of our six, coverage is: `es` ✅,
`pt` ✅, `zh` ✅, `ru` ❌, `tr` ❌, `ka` ❌.

### 6.2 Vendor coverage is not gated by vendor participation — a partial revealed-behavior path

> "**Does Gartner limit the vendors covered in a market/category? No.** Reviewers may select
> from a drop-down list of vendors in a market/category or they may select 'Other' and **write
> in a vendor not included in the drop-down list.** Reviews with write-in vendors will only be
> approved after confirming the vendor belongs in the market/category."

This is the **only entry path in our entire source set where a vendor appears because a buyer
acted, rather than because the vendor invested in appearing.** A write-in is a trace left by a
reviewer's behaviour.

It is not a clean `REVEALED-BEHAVIOR` source — Gartner gates approval, and vendors solicit
reviews heavily — but it is the first thing we have found that is not purely
`SELF-DECLARED`. **Whether a given listing arrived by write-in is not visible on the page**, so
this cannot be operationalised per row yet; recorded as a lead for the vendor pass.

Corroborating this: the supplied pages list products with **"Be the first to write a review"** —
Aislelabs, Business Monster enterprise, Foursquare Audience, Foursquare Proximity, Juniper
Mist User Engagement, Qujam, SAP Engagement Cloud in Location Based Marketing alone. **Listing
does not require reviews.** So a Gartner product count is a count of *listed* products, and
the review count is a separate, much smaller population.

### 6.3 Review counts are a solicitation metric, not a customer-base metric

- > "Gartner collects Peer Insights reviews from individuals through direct outreach. **Many
  > technology vendors also encourage their customers to review their solutions.**"
- > "Gartner **sometimes offers gifts of nominal value** to individuals for submitting reviews…
  > and **does not prohibit vendors from doing the same.** Nominal gifts are defined as valued
  > at **$25 USD or less.**"

**Review count measures review-acquisition effort at least as much as customer volume.** It
stays `SELF-DECLARED` and never corroborates anything on its own.

- > "**Do Peer Insights reviews ever expire? No.**"

**Counts are cumulative and never decay.** A count reflects history, not current position, and
two vendors with equal counts may be ten years apart in when they earned them.

- > "the Total Reviews also reflects the number available under all active filters, whereas the
  > average rating and number of ratings **remains constant when filters are applied**."

**Review count and rating count are different denominators on the same page.** Never mix them.

### 6.4 Taxonomy coverage follows Gartner's own readership

> "We will continue to roll out new markets/categories in a controlled fashion, **prioritizing
> those markets/categories with high readership in our expert insights.**"

Gartner states, in its own words, that its taxonomy expands where **its enterprise clients
read**. The enterprise-Western skew flagged in `CLAUDE.md` §7.2 is not an artefact we inferred —
it is published policy. A market absent from Peer Insights may be absent because Gartner's
clients have not asked about it, which is a fact about Gartner's client base, not about the market.

### 6.5 Reviewer eligibility narrows the population further

Reviewers must be *"an IT professional or otherwise involved in technology purchasing"*, with a
corporate email matching their stated company, and must not work for a systems integrator or
consultant in that market. **Consultants and SIs are excluded from reviewing** — which is
precisely competitor class 4. Gartner cannot see the services route even where it exists.

---

## 7. Cross-reference against G2

Each supplied Gartner market matched against the G2 taxonomy captured in pass 01
(`sources/derived/g2-taxonomy-full.csv`, 2,235 categories).

| Gartner market | G2 equivalent | Names agree? | Definitions agree? |
|---|---|---|---|
| Multichannel Marketing Hubs | **no equivalent name in G2** — nearest is `Marketing Automation Software` | **No** | **UNKNOWN — G2 definition blocked (403)** |
| Email Marketing (Transitioning to Email Marketing Platforms) | `Email Marketing Software` | Yes, modulo suffix | **UNKNOWN — blocked** |
| B2B Marketing Automation Platforms | `Marketing Automation Software` | **No** — G2 does not split B2B/B2C at this level | **UNKNOWN — blocked** |
| Customer Data Platforms | `Customer Data Platforms (CDP)` | Yes | **UNKNOWN — blocked** |
| Personalization Engines | `Personalization Engines` **and** `Personalization Software` — **G2 has two** | Partially | **UNKNOWN — blocked** |
| Mobile Marketing Platforms | `Mobile Marketing Software` | Near | **UNKNOWN — blocked** |
| Location Based Marketing Software | `Location-Based Marketing Software` | Yes | **UNKNOWN — blocked** |

**The most informative disagreement is a name that does not exist.** Gartner's largest market
in the sample — **Multichannel Marketing Hubs, 122 products, bar 6, its own Magic Quadrant** —
**has no counterpart name anywhere in G2's 2,235 categories.** G2 has no "hub" concept at this
level; the same vendors are presumably distributed across `Marketing Automation Software`,
`Email Marketing Software`, `Mobile Marketing Software` and others.

**This is the central taxonomy finding of the pass.** The two sources do not disagree about
where a boundary sits — they disagree about **whether the object exists at all**. Any merged
count across them is an artefact of that disagreement, and per `industry-registry.md` §2 the
two are registered as **separate entries**, not force-matched. `C-0006`.

The mirror case: **G2 splits personalization into two categories where Gartner has one.** A
vendor could be counted twice on one side and once on the other, with no vendor changing.

**All seven definition comparisons return `UNKNOWN`, because every G2 category page returns
403.** Name-level matching is all that is currently possible, and per the STOP-AT-RUNG-3 rule
this pass does not pretend otherwise.

---

## 8. Full extraction, per supplied market

Verbatim. The wording is the evidence.

Common to all seven rows: `source: gartner-peer-insights` · `rung: 3 (human transport)` ·
`source_class: SELF-DECLARED` (§6.2 notes the partial write-in exception) ·
`source_language: en` · `capture_date: 2026-08-10` · `grade: PRIMARY` ·
`presence: ABSENT-ENUMERATED available` · `sample: PURPOSIVE`

#### Multichannel Marketing Hubs

- **Type:** MARKET (analyst-defined) — backed by: Critical Capabilities for Multichannel Marketing Hubs; Magic Quadrant for Multichannel Marketing Hubs
- **Products stated:** 122 · **visible:** 122 · **`ABSENT-ENUMERATED` is available for this market** (PRIMARY)
- **Bar height:** 6, updated October 2025
- **Definition, verbatim:**

  > Gartner defines multichannel marketing hubs (MMHs) as software applications, primarily delivered as SaaS, that orchestrate personalized campaigns and event-driven customer journeys across marketing channels. These applications leverage customer data, predictive models and real-time insights to optimize the timing, channel and content of interactions. MMHs apply advanced analytics, AI and prescriptive intelligence to help marketing and technical teams manage the end-to-end life cycle of customer journeys. Although MMHs overlap with customer data platforms (CDPs) and personalization engines, their primary focus is enabling marketing users to manage large-scale consumer interactions, particularly in owned media channels such as email and app push. Multichannel marketing hubs empower marketers to deliver personalized media and orchestrate customer journeys, thus driving revenue, engagement and loyalty. These SaaS applications unify customer data, predictive insights and real-time decision making to optimize interactions across digital channels. MMHs enable multidisciplinary teams to manage campaigns and event-driven journeys via advanced analytics, artificial intelligence/machine learning (AI/ML) and prescriptive intelligence.

- **Mandatory features, verbatim and complete:**
  1. Consent and preference management: Provides native or integrated tools for managing customer preferences, opt-ins, permissions and compliance audits. This feature ensures adherence to global corporate policies or regional regulations while fostering customer trust.
  1. Application management: Delivers tools for user and permission management, regulatory compliance (e.g., Service Organization Control [SOC] 2), and governance. This feature includes critical functions, such as global frequency capping and messaging policy enforcement, that ensure secure and scalable operations.
  1. Campaign and journey management: Provides user-friendly tools for campaign and journey design, testing, versioning and reporting. This feature orchestrates workflows to help marketers manage the life cycle of campaigns and journeys, from planning to archiving.
  1. Analytics and reporting: Offers capabilities such as segmentation, predictive modeling and customer journey analytics. These tools enhance targeting, personalization and overall program optimization. MMHs bundle features for reports and dashboards to help users understand and communicate campaign, channel and journey performance.
  1. Data integration and management: Enables users to integrate customer data or other data objects (audiences, product catalogs, etc.). Specific functions may include APIs and packaged integrations, profile management, data transformation, advanced data (aka zero-copy) access to cloud data warehouses, and support for entities, such as product catalogs, that enable seamless data activation and personalized offers.
  1. Multichannel execution and measurement: Enables deployment and measurement of personalized messages across digital channels, such as email, mobile messaging and advertising. This feature includes integrated tools for performance tracking and reporting to optimize engagement.
- **`(Legacy)` products (5):** `BlueVenn (Legacy)`, `Portrait Dialogue (Legacy)`, `SAP Marketing Cloud (Legacy)`, `SAS Marketing Automation (Legacy)`, `SAS Real-Time Decision Manager (Legacy)`


#### Email Marketing (Transitioning to Email Marketing Platforms)

- **Type:** MARKET (analyst-defined) — backed by: Market Guide for Email Marketing (Transitioning to Email Marketing Platforms)
- **Products stated:** 100 · **visible:** 100 · **`ABSENT-ENUMERATED` is available for this market** (PRIMARY)
- **Bar height:** 4, updated December 2025
- **Definition, verbatim:**

  > Gartner defines email marketing as the use of the email channel to deliver and optimize marketing messages — such as brand newsletters or contextually relevant, real-time and personalized communications — in support of engagement across the customer journey. Email service providers often bolster their technology platforms with supplementary managed services to improve the value and scalability of the email channel. Email marketing helps marketers deliver information to their audiences after obtaining an email address. This can take the form of product or service updates, new promotions, transaction updates and more. As a relatively inexpensive method for communicating at scale with contacts, email provides value for different use cases across the full customer-engagement life span. Email is the most effective channel for several marketing objectives, including demand generation, conversion to sales, and customer loyalty and advocacy.

- **Mandatory features, verbatim and complete:**
  1. Ability to develop and adjust email template designs
  1. Ability to ingest, store and segment lists of contacts that can be contacted via an email message
  1. Ability to send out email messages to many contacts in one step
  1. Opt-in and opt-out management
- **`(Legacy)` products (1):** `SpiceSend Email Marketing Tool (Legacy)`


#### Customer Data Platforms

- **Type:** MARKET (analyst-defined) — backed by: Critical Capabilities for Customer Data Platforms; Magic Quadrant for Customer Data Platforms
- **Products stated:** 71 · **visible:** 71 · **`ABSENT-ENUMERATED` is available for this market** (PRIMARY)
- **Bar height:** 4, updated January 2026
- **Definition, verbatim:**

  > Customer data platforms (CDPs) are software applications that support customer experience use cases by unifying a company’s customer data from marketing, sales, service, commerce and other sources. CDPs unify customer data to facilitate its output to coordinate profiles between cross-functional systems, create segments and/or audience targets, optimize offers and/or decisions, and inform analysis while distributing insights that create triggers for other experiences.

- **Mandatory features, verbatim and complete:**
  1. Customer data object management: The creation and management of unified customer profiles from person-level data by integrating multiple sources using deterministic or probabilistic identity resolution. It also governs and activates related objects linked to profiles, such as audiences, campaigns, scores and accounts.
  1. Activation: The ability to send segments, with instructions for activating them, to engagement tools and platforms, including those for email campaigns, mobile messaging and advertising, among others. CDPs increasingly function as centralized decision-making tools, supporting real-time personalization and next-best-action decision making.
  1. Data collection: Ingest (extract) first-party, individual-level customer data from multiple sources and formats, online and offline, in real time and without limits on storage. This includes enterprise data sources (such as cloud data warehouses and datalakes) and data sources from business functions. Data persists as long as needed for processing and is typically left unchanged in its original source. This includes both anonymous and known first-party identifiers, behaviors and attributes.
  1. Analytic reporting: Performance and propensity analysis for various levels of customer data, such as the attribute level, profile level or segment level.
- **`(Legacy)` products (1):** `BlueVenn (Legacy)`


#### Personalization Engines

- **Type:** MARKET (analyst-defined) — backed by: Critical Capabilities for Personalization Engines; Magic Quadrant for Personalization Engines
- **Products stated:** 64 · **visible:** 64 · **`ABSENT-ENUMERATED` is available for this market** (PRIMARY)
- **Bar height:** 8, updated February 2026
- **Definition, verbatim:**

  > Personalization engines use knowledge about customers to create and deliver an optimum experience for them and measure the impact on customer experience. These engines apply AI, advanced analytics and business rules to create meaningful experiences across channels that facilitate customer engagement and drive revenue. Personalization engines create a relevant, individualized interaction between two parties designed to enhance the recipient’s experience. A recipient can be a prospect, customer (known or anonymous) or employee (engaging with a customer or prospect). In commercial settings, the engines apply advanced analytics to interpret customer data — whether known or anonymous, behavioral or contextual — and adjust engagement based on where the customer is in their journey and how they’re interacting. The engines adapt content, offers and interactions in real time that facilitate the customer’s journey.

- **Mandatory features, verbatim and complete:**
  1. Segmentation of individuals across known data and inferred beliefs to support personalization rules, including responding to contextual data and user feedback.
  1. Embedded generative AI (GenAI) in content creation, testing and other employee tasks
  1. Personalization performance tracking (e.g., campaign, commerce, recommendations) and reporting
  1. Ability to alter interactions in real time based on individuals’ actions, context, data or a combination of the three.
  1. Automated machine learning capabilities that improve personalization outcomes, including identifying underperforming audiences and recommending specific actions to improve outcomes
  1. Customer experience (CX) data profile creation and management capabilities
  1. Extensive testing capabilities (e.g., A/B, multivariate, multiarmed bandit), including the ability to test a wide variety of personalization elements and tactics (e.g., messaging, campaigns, recommendations).
  1. Real-time digital behavior tracking, data collection, ingestion and storage (data augmented by batch and streaming data).
- **`(Legacy)` products (5):** `Experience Orchestrator (XO) (Legacy)`, `IBM Interact (Legacy)`, `IBM Watson Personalization (Legacy)`, `Oracle Maxymiser (Legacy)`, `Reflektion Customer Engagement Platform (Legacy)`


#### B2B Marketing Automation Platforms

- **Type:** MARKET (analyst-defined) — backed by: Critical Capabilities for B2B Marketing Automation Platforms; Magic Quadrant for B2B Marketing Automation Platforms
- **Products stated:** 59 · **visible:** 59 · **`ABSENT-ENUMERATED` is available for this market** (PRIMARY)
- **Bar height:** 5, updated September 2025
- **Definition, verbatim:**

  > Gartner defines B2B marketing automation platforms (B2B MAPs) as software applications that support demand generation processes at scale. B2B MAPs help marketers capture and qualify leads and accounts, orchestrate marketing-driven engagement across the full customer journey, and use analytics to optimize and measure performance. B2B MAPs enable marketers to automate a wide range of activities intended to drive new customer acquisition, retention and growth. To support the pursuit of new commercial opportunities (from current or prospective customers), marketers use B2B MAPs to generate, prioritize, and manage leads and account buying groups across the revenue life cycle. This includes the distribution of marketing-generated and qualified leads to sales teams for further pursuit. Also, B2B MAPs are used to orchestrate and measure multichannel customer engagement campaigns and programs. B2B MAPs enable marketers to design and activate some communication channels natively — most notably, email and web landing pages — and orchestrate customer engagement through other channels via integrations with other tools/platforms.

- **Mandatory features, verbatim and complete:**
  1. Measure the performance of marketing touchpoints and communicate results using data visualization/dashboarding capabilities.
  1. Create multistep journeys for contacts (e.g., drip campaigns, customer onboarding motions) using a graphical lead workflow UI suitable for nontechnical users.
  1. Input and synchronize customer contact and account data into a unified customer profile.
  1. Score leads to evaluate quality based on profile fit and behavioral criteria using business rules and/or predictive analytics capabilities.
  1. Deploy and manage coordinated customer engagement programs across multiple channels, including native email and landing page execution.
- **`(Legacy)` products (3):** `Datalogix (Legacy)`, `Dynamics CRM (Legacy)`, `SAP Marketing Cloud (Legacy)`


#### Mobile Marketing Platforms

- **Type:** MARKET (analyst-defined) — backed by: Market Guide for Mobile Marketing Platforms
- **Products stated:** 45 · **visible:** 45 · **`ABSENT-ENUMERATED` is available for this market** (PRIMARY)
- **Bar height:** 3, updated February 2026
- **Definition, verbatim:**

  > Gartner defines mobile marketing platforms (MMPs) as software solutions that help organizations create, activate, execute, analyze and optimize mobile marketing campaigns and experiences. The platforms target audiences on their mobile device through multiple channels or message types such as SMS/text, push notifications, messaging apps, in-app messages and mobile apps. MMPs enable marketers to engage customers and prospects through a range of mobile-specific tactics — spanning mobile websites, mobile applications, smart device engagement, messaging (such as SMS and native applications), push notifications (such as on mobile apps and off websites), location-triggered interactions and mobile wallet cards. Mobile tactics are particularly suited to, for example, providing time-sensitive notifications to audiences, whether that’s in response to a live event, location-specific moment or a fulfillment update. MMPs also help measure and optimize the effectiveness of mobile strategy.

- **Mandatory features, verbatim and complete:**
  1. Basic analytics, measurement, data storage, and reporting on mobile channels and campaign performance
  1. Basic customer profile data management (anonymous and known) to enable mobile marketing channels and/or campaigns
  1. Basic mobile channel campaign management and support (for channels such as SMS/MMS, push notifications and/or in-app messages)


#### Location Based Marketing Software

- **Type:** CATEGORY (Peer Insights-created) — **no Magic Quadrant, no Critical Capabilities, no Market Guide**
- **Products stated:** 15 · **visible:** 15 · **`ABSENT-ENUMERATED` is available for this market** (PRIMARY)
- **Bar height:** no mandatory-feature list published
- **Definition, verbatim:**

  > Location-based marketing software uses geolocation technology to deliver targeted content and promotions to users based on their physical location. This software can identify where users are through their mobile devices, IP addresses, or other connected devices, allowing businesses to send personalized messages, offers, or ads when users are near a specific location, such as a store or event. The software is used by retailers, event organizers, restaurants and cafes, travel and hospitality, etc. Key features include geofencing, location tracking, analytics & reporting, location data, push notifications, and mobile apps, which help businesses optimize their marketing strategies and measure campaign effectiveness.


---

## 9. Open questions this pass could not close, and what each needs

| Question | Status | What would close it |
|---|---|---|
| How many categories does Gartner's **Marketing branch** contain? | **UNKNOWN** | The Marketing branch nav list — every supplied page carries the *Application Development* list instead |
| Are there `(Retired)` categories in Marketing? | **NOT-CHECKED** (not `ABSENT`) | Same |
| Do G2's definitions agree with Gartner's? | **UNKNOWN** ×7 | G2 category pages — 403 |
| Does the low-bar/low-count anomaly at Mobile Marketing Platforms mean absorption, small market, or low solicitation? | **UNKNOWN** | Branch denominator + a second dated capture |
| Which listings arrived by reviewer write-in rather than vendor submission? | **UNKNOWN** | Not visible per row; may not be obtainable at all |
| Bar height for Shopify and HubSpot | **UNKNOWN** | Their listing-requirements pages |

---

## 10. Next paste request

**Per the STOP-AT-RUNG-3 rule this pass stops here.** No downstream work is done against the
missing sources.

### Request A — Gartner's Marketing branch category list (**the denominator**)
- **URL:** `https://www.gartner.com/reviews/markets` → open the **Marketing** branch, or any
  Gartner Peer Insights page with the left-hand **Marketing** category list expanded
- **Copy:** every category name under Marketing, **verbatim, including every `(Legacy)`,
  `(Retired)` and `(Transitioning to X)` suffix**. If the list ends in **"View More"**, please
  click it and copy the full list — the supplied pages all truncate at "View More" on the
  Application Development branch, and that truncation is exactly what costs us the denominator.
- **Decides:** whether Gartner absences can ever be `ABSENT` rather than `NOT-CHECKED`; whether
  any Marketing category is `(Retired)` — a market that failed at category level, the strongest
  failure signal our source set can produce and one nothing else supplies.

### Request B — G2 category pages, to close the seven `UNKNOWN` definition comparisons
Same twelve URLs as `outputs/source-taxonomies.md` §8 Request 2. **The seven that pair directly
with what you have now supplied are the priority:**
`marketing-automation` · `email-marketing` · `mobile-marketing` · `customer-data-platform-cdp` ·
`personalization-engines` · `personalization` · `location-based-marketing`
- **Copy:** definition paragraphs, the complete "To qualify for inclusion…" bullet list, and the
  declared product count line. Page 1 only.
- **Decides:** all seven definition comparisons in §7, and the eight CRM-variant boundary cases
  still open in `logs/boundary-rulings.md`.

### Request C — marketplace listing requirements (cheap)
Shopify app listing/review requirements; HubSpot app certification requirements.
- **Decides:** bar height for both marketplaces, currently `UNKNOWN`, which is what makes their
  counts non-comparable to anything.
