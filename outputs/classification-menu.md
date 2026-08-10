# outputs/classification-menu.md

**You tick the classifications worth diving into. Everything here exists to make that choice
on evidence.**

Scope: **only the categories whose pages were supplied.** Nothing beyond that is enumerated.
Every description below is quoted from the source itself — no paraphrase, so you are choosing
against what the source actually claims the category is.

---

## 1. How each row was judged

Category *names* mislead — "Personalization" means two different things on the two sources.
So each category is judged on its **published admission test**: Gartner's `Mandatory Features:`
list, G2's *"To qualify for inclusion… a product must:"* list. Four yes/no questions are asked
of that list:

| | Question | "Yes" looks like |
|---|---|---|
| **Q1** | Does it require **holding a list of identifiable people**? | stored contacts, subscriber lists, unified customer profiles |
| **Q2** | Does it require **choosing who gets what**? | segmentation, audience building, targeting, lead scoring |
| **Q3** | Does it require **deciding when to send**? | triggers, journeys, drip sequences, real-time reaction |
| **Q4** | Does it require **actually sending on a channel the person receives**? | email, SMS, push, in-app message, messaging app, voice, physical mail |

> ### **IN** = **Q4 yes**, and **Q1 or Q2** yes.

**Q4 does the real work.** It separates a system that *sends to a person* from one that *hands
data to a system that sends*. That one line splits a marketing hub from a CDP, and an
activation tool from an analytics tool, with no argument about names.

**Why this is auditable rather than just tidy:**
1. **Only mandatory requirements count.** Capability mentioned in marketing prose but absent
   from the requirement list scores **no**. A category is what it *forces* every member to do.
2. **Every Q4 verdict quotes its deciding line**, below, verbatim.
3. **Identical test on both sources**, so a disagreement between them is real, not an artefact
   of how I read them. It found exactly that — see §4.

**Limit, stated:** a category with no published requirement list cannot be scored this way.
That applies to Gartner Peer Insights *Categories* (as distinct from analyst *Markets*) and to
G2 *parent* categories. Those rows say so instead of guessing.

---

## 2. THE MENU — tick what you want

**`Cost` is the number that should drive your picks.** Gartner enumerates completely in one
page ("Products 1–122 of 122"). G2 renders only ~25 of its declared listings, so a G2 vendor
list costs about one paste per 25.

### Gartner Peer Insights

| ☐ | Category | Verdict | Bar | Products | Marker | Cost |
|---|---|---|---|---|---|---|
| ☐ | Multichannel Marketing Hubs | **IN** | 6 | **122** | — | **1 paste** |
| ☐ | Email Marketing | **IN** | 4 | **100** | *(Transitioning)* | **1 paste** |
| ☐ | B2B Marketing Automation Platforms | **IN** | 5 | **59** | — | **1 paste** |
| ☐ | Mobile Marketing Platforms | **IN** | 3 | **45** | — | **1 paste** |
| ☐ | Location Based Marketing Software | **IN** *weak basis* | none | **15** | — | **1 paste** |
| ☐ | Customer Data Platforms | OUT | 4 | 71 | — | 1 paste |
| ☐ | Personalization Engines | OUT | 8 | 64 | — | 1 paste |
| ☐ | **Voice of the Customer Platforms** | **cannot score** | ? | ? | ? | **needs re-paste — my fault, see §5** |

### G2

| ☐ | Category | Verdict | Bar | Listings | Cost |
|---|---|---|---|---|---|
| ☐ | Marketing Automation | **IN** | 10 | **511** | ~21 pastes |
| ☐ | SMS Marketing | **IN** *Q1 implied* | 4 | **531** | ~22 pastes |
| ☐ | Email Marketing | **IN** | 7 | **527** | ~22 pastes |
| ☐ | Personalization | **IN** | 3 | **241** | ~10 pastes |
| ☐ | Marketing Analytics | OUT | 5 | 556 | ~23 pastes |
| ☐ | Customer Data Platform (CDP) | OUT | 5 | 296 | ~12 pastes |
| ☐ | Digital Analytics | OUT | 4 | 287 | ~12 pastes |
| ☐ | Marketing Account Intelligence | OUT | 3 | 123 | ~5 pastes |
| ☐ | Account Data Management | **OUT — borderline, could flip** | 4 | 77 | ~4 pastes |

**Not classifiers.** G2's **Account-Based Marketing**, **Lead Generation** and **Conversion Rate
Optimization Tools** each show no listing count and no inclusion criteria — matching G2's rule
that *"Parent categories… do not actually contain any G2 product profiles."* They are
navigation, not populations. Confirmed on all three.

---

## 3. What each classification is, in its source's own words

### Multichannel Marketing Hubs

*Gartner **Market** · Magic Quadrant + Critical Capabilities · bar height **6** · **122 products** · 1 paste*

**What the source says it is** — features updated October 2025

> Gartner defines multichannel marketing hubs (MMHs) as software applications, primarily delivered as SaaS, that orchestrate personalized campaigns and event-driven customer journeys across marketing channels. These applications leverage customer data, predictive models and real-time insights to optimize the timing, channel and content of interactions.

**Q1** ✅ · **Q2** ✅ · **Q3** ✅ · **Q4 ✅** → **IN**

**Deciding line for Q4:** "Multichannel execution and measurement: Enables deployment and measurement of personalized messages across digital channels, such as email, mobile messaging and advertising."

Gartner states this market **overlaps** CDPs and Personalization Engines — so its 122 cannot be added to their counts.

### Email Marketing *(Transitioning to Email Marketing Platforms)*

*Gartner **Market** · Market Guide · bar height **4** · **100 products** · 1 paste*

**What the source says it is** — features updated December 2025

> Gartner defines email marketing as the use of the email channel to deliver and optimize marketing messages — such as brand newsletters or contextually relevant, real-time and personalized communications — in support of engagement across the customer journey. Email service providers often bolster their technology platforms with supplementary managed services to improve the value and scalability of the email channel.

**Q1** ✅ · **Q2** ✅ · **Q3** ❌ · **Q4 ✅** → **IN**

**Deciding line for Q4:** "Ability to send out email messages to many contacts in one step"

**Category is being renamed.** Counts before and after the transition are not comparable.

### B2B Marketing Automation Platforms

*Gartner **Market** · Magic Quadrant + Critical Capabilities · bar height **5** · **59 products** · 1 paste*

**What the source says it is** — features updated September 2025

> Gartner defines B2B marketing automation platforms (B2B MAPs) as software applications that support demand generation processes at scale. B2B MAPs help marketers capture and qualify leads and accounts, orchestrate marketing-driven engagement across the full customer journey, and use analytics to optimize and measure performance.

**Q1** ✅ · **Q2** ✅ · **Q3** ✅ · **Q4 ✅** → **IN**

**Deciding line for Q4:** "Deploy and manage coordinated customer engagement programs across multiple channels, including native email and landing page execution."

### Mobile Marketing Platforms

*Gartner **Market** · Market Guide only · bar height **3** · **45 products** · 1 paste*

**What the source says it is** — features updated February 2026

> Gartner defines mobile marketing platforms (MMPs) as software solutions that help organizations create, activate, execute, analyze and optimize mobile marketing campaigns and experiences. The platforms target audiences on their mobile device through multiple channels or message types such as SMS/text, push notifications, messaging apps, in-app messages and mobile apps.

**Q1** ✅ · **Q2** ~ · **Q3** ~ · **Q4 ✅** → **IN**

**Deciding line for Q4:** "Basic mobile channel campaign management and support (for channels such as SMS/MMS, push notifications and/or in-app messages)"

**Lowest bar in the sample** — all three requirements are literally prefixed *"Basic"* — yet the second-smallest count. Ease of entry is not what limits this market.

### Location Based Marketing Software

*Gartner **Peer Insights Category** (not an analyst market) · **no mandatory features published** · **15 products** · 1 paste*

**What the source says it is** — no dated feature list exists

> Location-based marketing software uses geolocation technology to deliver targeted content and promotions to users based on their physical location. This software can identify where users are through their mobile devices, IP addresses, or other connected devices, allowing businesses to send personalized messages, offers, or ads when users are near a specific location, such as a store or event.

**Q1** — · **Q2** — · **Q3** — · **Q4 ✅ *(from the definition, not a requirement)*** → **IN — weak basis**

**Deciding line for Q4:** No mandatory list exists. Definition only: *"allowing businesses to send personalized messages, offers, or ads when users are near a specific location"*

**Scored on prose, not on requirements.** Its 15 products are not comparable to any market above: no published entry test at all.

### Customer Data Platforms

*Gartner **Market** · Magic Quadrant + Critical Capabilities · bar height **4** · **71 products** · 1 paste*

**What the source says it is** — features updated January 2026

> Customer data platforms (CDPs) are software applications that support customer experience use cases by unifying a company’s customer data from marketing, sales, service, commerce and other sources. CDPs unify customer data to facilitate its output to coordinate profiles between cross-functional systems, create segments and/or audience targets, optimize offers and/or decisions, and inform analysis while distributing insights that create triggers for other experiences.

**Q1** ✅ · **Q2** ✅ · **Q3** ~ · **Q4 ❌** → **OUT**

**Deciding line for Q4:** "Activation: The ability to send segments, with instructions for activating them, **to engagement tools and platforms**" — the recipient is a system, not a person.

### Personalization Engines

*Gartner **Market** · Magic Quadrant + Critical Capabilities · bar height **8** · **64 products** · 1 paste*

**What the source says it is** — features updated February 2026

> Personalization engines use knowledge about customers to create and deliver an optimum experience for them and measure the impact on customer experience. These engines apply AI, advanced analytics and business rules to create meaningful experiences across channels that facilitate customer engagement and drive revenue.

**Q1** ✅ · **Q2** ✅ · **Q3** ✅ · **Q4 ❌** → **OUT**

**Deciding line for Q4:** **None of the 8 mandatory features names a channel the person receives.** They require segmentation, embedded GenAI, automated ML, extensive testing (A/B, multivariate, multiarmed bandit), real-time alteration, CX profile management, behaviour tracking, and performance reporting.

**Hardest bar in the sample** — and Gartner's definition includes **employees** as valid recipients, which is wider than our scope.

---

## 3b. G2

### Marketing Automation

*G2 **leaf** · bar height **10** · **511 listings** · ~21 pastes*

**What the source says it is** — definition updated July 10, 2025

> Marketing automation software helps businesses streamline and scale their marketing efforts by automating campaigns, workflows, or tasks across multiple channels. These platforms serve as a centralized marketing database to enable teams to create segmented, personalized, and timely marketing experiences for customers or prospects based on customer interaction data. These marketing automation tools should ideally support omnichannel marketing engagement across email, SMS, WhatsApp, social media, direct mail, digital advertising, and more.

**Q1** ✅ · **Q2** ✅ · **Q3** ✅ · **Q4 ✅** → **IN**

**Deciding line for Q4:** "Contact targets across multiple channels after specific actions, triggers, or periods of time"; "Automate two or more of the following workflows: email, social media, SMS, and digital ads"

**Highest bar of any category here.** Explicitly excludes products categorised in Email Marketing.

### SMS Marketing

*G2 **leaf** · bar height **4** · **531 listings** · ~22 pastes*

**What the source says it is** — definition updated July 14, 2026

> SMS marketing software, also known as text message marketing, helps companies plan and execute mobile-focused marketing campaigns by sending targeted, permission-based SMS and MMS messages to customers and prospects. These tools support personalized outreach, bulk messaging, and two-way messaging to drive customer engagement and loyalty.

**Q1** ~ *(implied by "opt-in subscribers", not stated)* · **Q2** ❌ · **Q3** ❌ · **Q4 ✅** → **IN**

**Deciding line for Q4:** "Reach mobile users via SMS messaging"

Passes on Q4 with Q1 only **implied**. The weakest IN in the set — flagged rather than smoothed.

### Email Marketing

*G2 **leaf** · bar height **7** · **527 listings** · ~22 pastes*

**What the source says it is** — definition updated April 9, 2026

> Email marketing software allows businesses to build and manage email lists, segment audiences, design and send customized campaigns, and monitor subscriber engagement, helping marketing teams, growth teams, and small business owners engage prospects, nurture leads, and retain customers through personalized communication.

**Q1** ✅ · **Q2** ✅ · **Q3** ❌ · **Q4 ✅** → **IN**

**Deciding line for Q4:** "Enable the creation and sending of emails via HTML or a WYSIWYG editor"

Explicitly excludes products categorised in Marketing Automation, so **527 + 511 does not double-count**.

### Personalization

*G2 **leaf** · bar height **3** · **241 listings** · ~10 pastes*

**What the source says it is** — definition updated July 14, 2026

> Personalization software uses customer data to create tailored web experiences, messages, content, promotions, and product recommendations. The personalized experiences are created based on user activity and preferences that drive engagement across websites, emails, mobile applications, and other digital channels. These platforms leverage customer behavior, engagement history, and user profiling to adapt digital experiences to each customer or audience segment. Organizations often use personalization software to deliver more relevant content that captures their customers' attention and ultimately drives conversion rates.

**Q1** ✅ · **Q2** ✅ · **Q3** ❌ · **Q4 ✅** → **IN**

**Deciding line for Q4:** "Deliver personalized **emails, messaging**, websites, content, promotions, or product recommendations for individual users or audience segments"

**Opposite verdict to Gartner's Personalization Engines.** G2 mandates delivering emails and messaging; Gartner does not. Same word, different object.

### Customer Data Platform (CDP)

*G2 **leaf** · bar height **5** · **296 listings** · ~12 pastes*

**What the source says it is** — definition updated October 3, 2024

> Customer data platforms (CDPs) are used to consolidate and integrate customer data into one single database. These tools offer marketing teams relevant insights needed to run campaigns. A CDP can grab information from online and offline sources such as websites, mobile apps, and email platforms to offer a complete view of the customer. After retrieving this data, a CDP can then help organizations predict the optimal next move with a particular customer. This allows businesses to learn what needs to be done to retain specific customers. A CDP can also be used by customer service teams to cater their support to each individual. Marketing automation software, data warehouse software, and other platforms that store data can typically integrate with a CDP.

**Q1** ✅ · **Q2** ✅ · **Q3** ❌ · **Q4 ❌** → **OUT**

**Deciding line for Q4:** "**Connect with other systems** to allow marketers to execute campaigns" — connects, does not send.

**Matches Gartner's independent verdict, in near-identical language.** Strongest corroboration in the study so far.

### Marketing Analytics

*G2 **leaf** · bar height **5** · **556 listings** · ~23 pastes*

**What the source says it is** — definition updated April 23, 2026

> Marketing analytics software encompasses tools and processes that enable an organization to manage, evaluate, and control its marketing efforts by measuring marketing performance. These solutions simplify and optimize a business’s marketing strategies and activities. With the use of marketing analytics software, businesses can improve their return-on-investment (ROI) by identifying effective marketing methods and adjusting campaigns to maximize conversions and sales.

**Q1** ✅ · **Q2** ✅ · **Q3** ❌ · **Q4 ❌** → **OUT**

**Deciding line for Q4:** Requirements are collect / monitor / analyze / integrate / visualize. **No send.**

### Digital Analytics

*G2 **leaf** · bar height **4** · **287 listings** · ~12 pastes*

**What the source says it is** — definition updated October 3, 2024

> Digital analytics software, also referred to as web analytics software, measures website engagement by tracking web traffic and visitors. Marketers, web developers, and analysts use digital analytics tools to report on the effectiveness of web experiences and to determine how visitors are interacting with their sites. By monitoring events such as page views, clicks, and conversions, businesses can distill web traffic data into meaningful insights. Digital analytics software gives organizations insights into customer behavior when encountering their brand’s website and allows reporting on online conversion, demographic, and content-interaction metrics.

**Q1** ❌ · **Q2** ✅ · **Q3** ❌ · **Q4 ❌** → **OUT**

**Deciding line for Q4:** Requirements are measure traffic / track events / report / segment traffic. **No send.**

### Marketing Account Intelligence

*G2 **leaf** · bar height **3** · **123 listings** · ~5 pastes*

**What the source says it is** — definition updated October 3, 2024

> Marketing account intelligence software compiles insightful prospect data to help marketers develop a list of accounts that fit a user’s ideal customer profile. Marketing account intelligence systems are implemented to combat the inefficiencies of the traditional “spray and pray" marketing approach. By deploying this software, marketing organizations can maximize efforts on accounts that have a high likelihood of converting to customers while minimizing time and money spent on prospects with a low probability of converting. These tools also assist sales teams by providing incisive information such as a prospect’s role within the company hierarchy or a prospect’s company segment.

**Q1** ✅ · **Q2** ✅ · **Q3** ❌ · **Q4 ❌** → **OUT**

**Deciding line for Q4:** Requirements are collect account data / score or rank leads / integrate. **No send.**

### Account Data Management

*G2 **leaf** · bar height **4** · **77 listings** · ~4 pastes*

**What the source says it is** — definition updated October 3, 2024

> Account Data Management software manages prospect data throughout the account-based marketing (ABM) process so that both sales and marketing teams have continuous awareness of target accounts. In order to maximize an ABM strategy, salespeople need to know where in the pipeline a prospect is and the probability that a prospect will become a customer. Account Data Management systems serve to document and communicate all relevant account information between the sales and marketing teams. This software is deployed in marketing and sales departments to maximize the efficiency of marketing efforts and facilitate communication between the two organizations.

**Q1** ✅ · **Q2** ✅ · **Q3** ❌ · **Q4 ❌ *ambiguous*** → **OUT — borderline**

**Deciding line for Q4:** "**Facilitate** sales and marketing communication relating to accounts within the system" — *facilitate* is not *send*.

**The one verdict that could flip.** If you read "facilitate communication" as outbound, this becomes IN. I read it as OUT and am flagging it rather than deciding quietly.

---

## 4. What the test caught that reading names would not

**Personalization is two different objects.** G2 requires delivering *"emails, messaging"* →
**IN**. Gartner's eight features never require a send → **OUT**. Merging them on the name would
have fused 241 listings with 64 products doing a different job.

**Both sources rule CDP out, independently, in near-identical language.** Gartner: send segments
*"to engagement tools and platforms."* G2: *"Connect with other systems to allow marketers to
execute campaigns."* Two taxonomies written separately draw the same line at handing off rather
than sending. That settles a boundary case named in the original brief.

**Overlap must be read per pair, not per source.** Gartner states MMH overlaps CDP and
Personalization Engines — 122 + 71 + 64 double-counts. G2's Email Marketing and Marketing
Automation each carry a rule excluding the other — 527 + 511 does not. Dedup logic cannot
assume either behaviour.

**Bar height does not predict size.** Lowest bar in the set (Mobile Marketing Platforms, 3
requirements all prefixed "Basic") holds 45 products; bar 6 holds 122.

**Definition age varies by three years** — Personalization and SMS Marketing updated July 2026,
CDP and Digital Analytics still on October 3, 2024. A stale definition and a fresh count on the
same page are not describing the same moment.

---

## 5. Rows that cannot be scored, and whose fault that is

- **Voice of the Customer Platforms (Gartner).** **You did paste this page. I destroyed it**
  in incident `I-0001`, along with 12 others, and it is the only one not yet re-supplied. This
  is not a gap in what you provided. Re-paste
  `https://www.gartner.com/reviews/market/voice-of-the-customer-platforms` and it scores
  immediately.
- **Conversational Marketing Solutions**, **Direct Mail Automation Software** (Gartner) and
  **Mobile Marketing Software** (G2) were **never pasted** — they were *my* suggestions of close
  neighbours from the branch list, and the previous version of this document labelled them in a
  way that implied otherwise. They are suggestions, not omissions. The first two are the closest
  unexamined neighbours to the IN rows; the third would let Gartner's Mobile Marketing Platforms
  be compared against a G2 counterpart. Say the word and I will request them; otherwise the menu
  stands as the pages you supplied.

---

## 6. What happens after you tick

1. Vendor list per ticked row — Gartner in 1 paste each, G2 paginated at ~25.
2. Each vendor row carries: product, vendor, rating, review count, **`(Legacy)` decline marker**,
   and provenance back to the raw capture.
3. Cross-source dedup applies the per-pair overlap rules in §4.

**For reference, not as a recommendation:** the five Gartner **IN** rows cost **5 pastes** and
yield **341 fully-enumerated products** with decline markers. The same breadth from G2 costs
~75 pastes. Which categories actually matter depends on deal size and cost to serve, which are
withheld by design — that judgement is yours.
