# UNVERIFIED extractions — raw captures destroyed

**Grade: `UNVERIFIED-EXTRACTION`.** Below `SINGLE-SOURCE`. These values were extracted from
pasted pages that the agent then destroyed (`logs/incidents.md` I-0001). **The raw capture
that would adjudicate them no longer exists**, so nothing here may anchor a finding until a
re-paste restores the file and this content is re-verified against it.

Kept rather than deleted so the user's effort is not wasted twice. Kept **marked** because an
extraction whose source has been destroyed is exactly what quietly becomes a fact by repetition.

---

## 1. Gartner — Marketing branch (`https://www.gartner.com/reviews/market/marketing`)

Page declared: **`82 CATEGORIES`**. Footer declared Gartner-wide: **`View all 950+ Categories`**.
Branch definition, as printed:

> "Marketing refers to the products and services that enable organizations to plan, execute,
> measure, and optimize strategies for attracting, engaging, and retaining customers across
> digital and physical channels. This category includes markets that support content creation,
> campaign management, data-driven personalization, performance analytics and brand
> strategy—empowering businesses to deliver targeted, measurable, and customer-centric
> marketing experiences."

### Decline markers seen in the Marketing branch — the first `(Retired)` markets in this study

| Marker | Category |
|---|---|
| **(Retired)** | Ad Tech Platforms |
| **(Retired)** | Advanced Analytics Service Providers for Marketing |
| **(Retired)** | Online Marketplace Optimization Tools |
| (Transitioning to Digital Asset Management Platforms) | Digital Asset Management |
| (Transitioning to Email Marketing Platforms) | Email Marketing |
| (Transitioning to Social Media Management and Listening) | Social Marketing Management |
| (Transitioning to Social Media Management and Listening) | Social Monitoring and Analytics |
| (Transitioning to Win/Loss Analysis Solutions) | Win/Loss Analysis Providers |

**Three retired markets in one branch — markets that failed or dissolved at category level.**
Nothing else in our source set produces this signal. **Two categories are transitioning to the
same target** (`Social Media Management and Listening`), i.e. a merge in progress.

### The 82, as printed
Marked `Popular` where the page marked it ("Identifies categories with the most reviews in the
past 12 months").

A/B Testing Tools · Account-Based Marketing Platforms · Ad Tech Platforms **(Retired)** ·
Ad Verification Tools · Advanced Analytics Service Providers for Marketing **(Retired)** ·
Advertising Platforms · Affiliate Marketing Platforms · AI Agents for Marketing ·
AI GTM Platforms · Audience Intelligence Platforms · B2B Customer Community Platforms ·
B2B Marketing Automation Platforms *(Popular)* · B2B Message Testing Solutions ·
B2B Multitouch Attribution Tools · Blockchain Advertising Platforms · Brand Advocacy Services ·
Brand Health Tracking Providers · Brand Strategy Agencies · Channel Integration Software ·
Consumer Video Feedback Software · Content Marketing Platforms *(Popular)* ·
Conversational Marketing Solutions · Creative as a Service (CaaS) ·
Creative Management Platform (CMP) · Customer Data Platforms *(Popular)* ·
Digital Asset Management **(Transitioning to Digital Asset Management Platforms)** ·
Digital Experience Services · Digital Signage · Direct Mail Automation Software ·
E-commerce optimization services ·
Email Marketing **(Transitioning to Email Marketing Platforms)** *(Popular)* ·
Email Optimization · Employee Advocacy Tools · Enterprise SEO Platforms ·
Event Marketing and Management Platforms *(Popular)* · Experiential Marketing Agencies ·
Global Digital Marketing Agencies · In-Game Advertising Platforms ·
Incrementality Measurement Platforms · Influencer Marketing Platforms ·
Interactive Demonstration Applications · Landing Page Software · Lead Generation Software ·
Location Based Marketing Software · Loyalty Program Vendors · Marketing Dashboards ·
Marketing Mix Modeling Solutions · Marketing Work Management Platforms ·
Media Buying and Planning Services · Mobile Marketing Platforms ·
Multichannel Marketing Hubs *(Popular)* · Online Marketplace Optimization Tools **(Retired)** ·
Online Proofing Software · Online Reputation Management Software · Over the top TV Advertising ·
Owned Media Software · Personalization Engines *(Popular)* · Photo Management Software ·
Podcast Advertising Platforms · Podcast Hosting Platforms · PPC (Pay-Per-Click) Tools ·
PR and Media Monitoring Tools · Product Sampling Software ·
Programmatic Segment-Based Advertising · Promotional Product Management Software ·
Public Relations Agencies · Shoppable Media ·
Social Marketing Management **(Transitioning to Social Media Management and Listening)** ·
Social Monitoring and Analytics **(Transitioning to Social Media Management and Listening)** ·
Sponsorship Management Platforms · Strategic Website Agencies ·
Supply-Side Platforms for Retail Media Networks ·
Sweepstakes Software (Competition Marketing Software) · Tag Management ·
User-Generated Content (UGC) Software · Video Editing Software · Virtual Try-On Solutions ·
Visitor Identification Software · Visual Intelligence · Voice of the Customer Platforms *(Popular)* ·
Voice Search Optimization Services ·
Win/Loss Analysis Providers **(Transitioning to Win/Loss Analysis Solutions)**

**Count check:** 82 declared. The listing above must be recounted against a re-paste before any
coverage claim is made from it.

---

## 2. G2 — inclusion criteria and declared counts, 9 category pages

G2 prints its admission test as *"To qualify for inclusion in the X category, a product must:"*
and its count as *"N Listings in X Available"*.

| G2 category | Listings declared | Criteria count (bar height) |
|---|---|---|
| Marketing Analytics | **556** | 5 |
| SMS Marketing | **531** | 4 |
| Email Marketing | **527** | 7 |
| Marketing Automation | **511** | 10 |
| Customer Data Platform (CDP) | **296** | 5 |
| Digital Analytics | **287** | 4 |
| Personalization | **241** | 3 |
| Marketing Account Intelligence | **123** | 3 |
| Account Data Management | **77** | 4 |
| Account-Based Marketing | **none — parent category** | none |
| Lead Generation | **none — parent category** | none |

**Two parent categories confirm G2's published rule operationally:** Account-Based Marketing and
Lead Generation show **no listing count and no inclusion criteria**, matching
*"Parent categories… do not actually contain any G2 product profiles."* This gives a clean
mechanical test for parent vs leaf: **no count + no criteria = parent = not a countable unit.**

### The two mutual-exclusion rules — the most consequential lines found

> **Email Marketing:** "Focus on email as the primary channel and **not be categorized as
> marketing automation**"

> **Marketing Automation:** "**Not be categorized in the email marketing software category** —
> products must cater to multiple channels, including email marketing"

**G2's general rule is that a product is placed in every category it qualifies for. These two
categories are explicitly disjoint anyway.** So G2 category membership is *not* uniformly
overlapping: some pairs are mutually exclusive by published rule, others are not. Any
deduplication logic that assumes uniform overlap is wrong, and 527 + 511 does **not** double-count.

### Criteria, verbatim

**Marketing Automation** (10) — automate ≥2 of email/social/SMS/digital ads · advanced email
(A/B, spam testing, scheduling, segmentation, reporting) · central marketing database ·
dynamic segmentation · **"Contact targets across multiple channels after specific actions,
triggers, or periods of time"** · forms and landing pages · lifecycle analytics incl. ROI ·
personalization from behaviour · integrate with CRM/CDP/e-commerce · not email-marketing-categorized.

**Email Marketing** (7) — create/send via HTML or WYSIWYG · templates · preview and test sends ·
**"Store, track, segment, and manage email contact lists"** · campaign reporting · opt-in/opt-out
compliant with CAN-SPAM, GDPR, CASL · email primary and not marketing automation.

**SMS Marketing** (4) — **"Reach mobile users via SMS messaging"** · opt-in for new subscribers ·
track interaction data per campaign · analytics or insights.

**Customer Data Platform (CDP)** (5) — 360-degree view · gather 1st/2nd/3rd-party data online and
offline · unify profiles across systems · **"Connect with other systems to allow marketers to
execute campaigns"** · improve targeting.

**Personalization** (3) — use customer data/behavioural signals/preferences to personalize digital
experiences · **"Deliver personalized emails, messaging, websites, content, promotions, or product
recommendations"** · audience segmentation and targeting.

**Marketing Analytics** (5) — collect campaign data across media channels · monitor campaigns and
audiences · analyze and compile · integrate with sales/marketing/analytics software · visualize via
dashboard.

**Digital Analytics** (4) — measure web traffic · track tagged events/conversions · report over time
and real time · segment traffic by demographics/device/medium/geography/cohort.

**Marketing Account Intelligence** (3) — collect target account data from external sources ·
score/rank leads · integrate with a data-profile product.

**Account Data Management** (4) — store account data more granular than contact info · integrate
with external data-finding tools · **"Facilitate sales and marketing communication relating to
accounts within the system"** · track accounts via ABM metrics.

### Other structure observed on G2 category pages
- Facets: **Segment** (Small Business / Mid Market / Enterprise), Rating, Pricing, **Language**,
  Features, **Solution Type (All-in-One / Best-of-Breed)**.
- Product rows carry rating, review count, and an **`All-in-One` / `Best-of-Breed`** tag plus
  **`AI Verified`** where applicable.
- G2 states on the page: *"We do not allow paid placements in any of our ratings, rankings, or
  reports."*

---

## 3. What must be re-pasted to lift these to PRIMARY

All 13 files in `logs/incidents.md` I-0001. The two that matter most:
`https://www.gartner.com/reviews/market/marketing` and
`https://www.g2.com/categories/marketing-automation`.
