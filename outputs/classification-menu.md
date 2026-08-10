# Classification menu — choose what to dive into

**What this is.** Every software classification whose source page you supplied, judged against
one consistent test, with the source's own description quoted so you can choose on substance
rather than on my summary. Tick the rows you want; §7 says what happens next.

**Coverage.** 10 Gartner Peer Insights markets and categories; 9 G2 leaf categories. Only what
was supplied — nothing beyond it is enumerated or guessed.

**At a glance:** **8 of 19 rows are IN** — 6 on Gartner (**352 products**, 6 pastes) and
4 on G2 (**1,810 listings**, ~75 pastes). One row is BOUNDARY and one OUT verdict could flip.

---

## 1. How every row was judged

Category *names* mislead. "Personalization" denotes two different objects on the two sources,
and reading names is what produced the earlier unusable list. So each category is judged on its
**published admission test** — Gartner's `Mandatory Features:` list, G2's *"To qualify for
inclusion… a product must:"* list. Four yes/no questions are put to that list:

| | Question | A "yes" looks like |
|---|---|---|
| **Q1** | Does it require **holding a list of identifiable people**? | stored contacts, subscriber lists, unified customer profiles |
| **Q2** | Does it require **choosing who gets what**? | segmentation, audience building, targeting, lead scoring |
| **Q3** | Does it require **deciding when to send**? | triggers, journeys, drip sequences, real-time reaction |
| **Q4** | Does it require **actually sending on a channel the person receives**? | email, SMS, push, in-app message, messaging app, voice, physical mail |

> ## **IN** = **Q4 yes**, and **Q1 or Q2** yes.

**Q4 carries the decision.** It separates a system that *sends to a person* from one that
*hands data to a system that sends*. That single line divides a marketing hub from a CDP, and
an activation tool from an analytics tool, with no argument about names.

**What makes this auditable rather than merely tidy:**

1. **Only mandatory requirements count.** A capability described in marketing prose but absent
   from the requirement list scores **no**. A category is defined by what it *forces* every
   member to do.
2. **Every Q4 verdict quotes the line that decided it**, verbatim, in §3 and §4.
3. **The same test runs on both sources**, so a disagreement between them is a real difference
   between the taxonomies rather than an artefact of how I read them. It found exactly that —
   see §5.

**The limit, stated plainly.** A category that publishes no requirement list cannot be scored
this way. That covers Gartner **Peer Insights Categories** (as distinct from analyst
**Markets**) and G2 **parent** categories. Those rows are judged on the definition alone and
say so, or are left unscored.

---

## 2. THE MENU

**`Cost` should drive your picks.** Gartner enumerates completely in one page — *"Products
1–122 of 122"* — so a full vendor list is **one paste**. G2 renders only about 25 of its
declared listings per page, so a G2 vendor list costs roughly **one paste per 25**.

**`(Legacy)`** counts products Gartner has marked as being in managed decline while their
ratings stay live. G2 publishes no equivalent: it **deletes** discontinued products and their
reviews, so its columns are structurally blank, not zero.

**`Popular`** is Gartner's own flag for *"categories with the most reviews in the past 12
months"* — a current-activity signal, not a size one.

### Gartner Peer Insights

| ☐ | # | Category | Type | Verdict | Bar | Products | (Legacy) | Popular | Cost |
|---|---|---|---|---|---|---|---|---|---|
| ☐ | 1 | Multichannel Marketing Hubs | Market | **IN** | 6 | **122** | **5** | ● | 1 paste |
| ☐ | 2 | Email Marketing *(Transitioning)* | Market | **IN** | 4 | **100** | 1 | ● | 1 paste |
| ☐ | 3 | B2B Marketing Automation Platforms | Market | **IN** | 5 | **59** | 3 | ● | 1 paste |
| ☐ | 4 | Mobile Marketing Platforms | Market | **IN** | 3 | **45** | 0 | | 1 paste |
| ☐ | 5 | Location Based Marketing Software | *Category* | **IN** *weak basis* | none | **15** | 0 | | 1 paste |
| ☐ | 6 | Direct Mail Automation Software | *Category* | **IN** *weak basis* | none | **11** | 0 | | 1 paste |
| ☐ | 7 | Conversational Marketing Solutions | *Category* | **BOUNDARY** | none | **22** | 1 | | 1 paste |
| ☐ | 8 | Customer Data Platforms | Market | OUT | 4 | 71 | 1 | ● | 1 paste |
| ☐ | 9 | Personalization Engines | Market | OUT | 8 | 64 | 5 | ● | 1 paste |
| ☐ | 10 | Voice of the Customer Platforms | Market | OUT | 3 (+10 sub) | 59 | 2 | ● | 1 paste |

### G2

| ☐ | # | Category | Verdict | Bar | Listings | Definition age | Cost |
|---|---|---|---|---|---|---|---|
| ☐ | 1 | Marketing Automation | **IN** | **10** | **511** | Jul 2025 | ~21 pastes |
| ☐ | 2 | SMS Marketing | **IN** *Q1 implied* | 4 | **531** | Jul 2026 | ~22 pastes |
| ☐ | 3 | Email Marketing | **IN** | 7 | **527** | Apr 2026 | ~22 pastes |
| ☐ | 4 | Personalization | **IN** | 3 | **241** | Jul 2026 | ~10 pastes |
| ☐ | 5 | Customer Data Platform (CDP) | OUT | 5 | 296 | Oct 2024 | ~12 pastes |
| ☐ | 6 | Marketing Analytics | OUT | 5 | 556 | Apr 2026 | ~23 pastes |
| ☐ | 7 | Digital Analytics | OUT | 4 | 287 | Oct 2024 | ~12 pastes |
| ☐ | 8 | Marketing Account Intelligence | OUT | 3 | 123 | Oct 2024 | ~5 pastes |
| ☐ | 9 | Account Data Management | **OUT — could flip** | 4 | 77 | Oct 2024 | ~4 pastes |

**Three G2 entries are not classifications at all.** Account-Based Marketing, Lead Generation
and Conversion Rate Optimization Tools each show **no listing count and no inclusion criteria**,
matching G2's published rule that *"Parent categories… do not actually contain any G2 product
profiles."* They are navigation. Confirmed on all three.

---

## 3. Gartner — what each classification is, in Gartner's words

### 1. Multichannel Marketing Hubs

*Gartner **Market** · Magic Quadrant + Critical Capabilities · **Popular** · bar **6** · **122 products** · **5 (Legacy)***

**What the source says it is** — requirements updated October 2025

> Gartner defines multichannel marketing hubs (MMHs) as software applications, primarily delivered as SaaS, that orchestrate personalized campaigns and event-driven customer journeys across marketing channels. These applications leverage customer data, predictive models and real-time insights to optimize the timing, channel and content of interactions.

**Q1** ✅ · **Q2** ✅ · **Q3** ✅ · **Q4 ✅** → **IN**

**Why Q4 lands there:** "Multichannel execution and measurement: Enables deployment and measurement of personalized messages across digital channels, such as email, mobile messaging and advertising."

Largest and most contested row here. Gartner states this market **overlaps** CDPs and Personalization Engines, so its 122 may not be added to their counts.

Its 5 legacy products — BlueVenn, Portrait Dialogue, SAP Marketing Cloud, SAS Marketing Automation, SAS Real-Time Decision Manager — are the densest concentration of managed decline in the set.

### 2. Email Marketing *(Transitioning to Email Marketing Platforms)*

*Gartner **Market** · Market Guide · **Popular** · bar **4** · **100 products** · **1 (Legacy)***

**What the source says it is** — requirements updated December 2025

> Gartner defines email marketing as the use of the email channel to deliver and optimize marketing messages — such as brand newsletters or contextually relevant, real-time and personalized communications — in support of engagement across the customer journey. Email service providers often bolster their technology platforms with supplementary managed services to improve the value and scalability of the email channel.

**Q1** ✅ · **Q2** ✅ · **Q3** ❌ · **Q4 ✅** → **IN**

**Why Q4 lands there:** "Ability to send out email messages to many contacts in one step"

**The category is mid-rename.** Counts taken before and after the transition are not comparable, and the new name will not match the old one in any merge.

### 3. B2B Marketing Automation Platforms

*Gartner **Market** · Magic Quadrant + Critical Capabilities · **Popular** · bar **5** · **59 products** · **3 (Legacy)***

**What the source says it is** — requirements updated September 2025

> Gartner defines B2B marketing automation platforms (B2B MAPs) as software applications that support demand generation processes at scale. B2B MAPs help marketers capture and qualify leads and accounts, orchestrate marketing-driven engagement across the full customer journey, and use analytics to optimize and measure performance.

**Q1** ✅ · **Q2** ✅ · **Q3** ✅ · **Q4 ✅** → **IN**

**Why Q4 lands there:** "Deploy and manage coordinated customer engagement programs across multiple channels, including native email and landing page execution."

The only row scoped explicitly to **B2B**. Gartner splits B2B from the rest of marketing automation; G2 does not, which is why no G2 row corresponds to it.

### 4. Mobile Marketing Platforms

*Gartner **Market** · Market Guide only · bar **3** · **45 products** · **0 (Legacy)***

**What the source says it is** — requirements updated February 2026

> Gartner defines mobile marketing platforms (MMPs) as software solutions that help organizations create, activate, execute, analyze and optimize mobile marketing campaigns and experiences. The platforms target audiences on their mobile device through multiple channels or message types such as SMS/text, push notifications, messaging apps, in-app messages and mobile apps.

**Q1** ✅ · **Q2** ~ · **Q3** ~ · **Q4 ✅** → **IN**

**Why Q4 lands there:** "Basic mobile channel campaign management and support (for channels such as SMS/MMS, push notifications and/or in-app messages)"

**Lowest bar of any Gartner market here** — all three requirements are literally prefixed *"Basic"* — yet only 45 products. Ease of entry is not what limits this market. It is also the only IN market with **no Magic Quadrant**, only a Market Guide.

### 5. Location Based Marketing Software

*Gartner **Peer Insights Category** — *not* an analyst market · **no published requirements** · **15 products** · **0 (Legacy)***

**What the source says it is** — no dated requirement list exists

> Location-based marketing software uses geolocation technology to deliver targeted content and promotions to users based on their physical location. This software can identify where users are through their mobile devices, IP addresses, or other connected devices, allowing businesses to send personalized messages, offers, or ads when users are near a specific location, such as a store or event.

**Q1** — · **Q2** — · **Q3** — · **Q4 ✅ *from the definition, not a requirement*** → **IN — weak basis**

**Why Q4 lands there:** No requirement list exists. Definition only: *"allowing businesses to send personalized messages, offers, or ads when users are near a specific location."*

**Judged on prose, not on requirements**, because Gartner publishes none for Peer Insights Categories. Its 15 products are not comparable to any Market above — there is no entry test at all.

### 6. Direct Mail Automation Software

*Gartner **Peer Insights Category** — *not* an analyst market · **no published requirements** · **11 products** · **0 (Legacy)***

**What the source says it is** — no dated requirement list exists

> Direct mail automation software automates the process of creating, managing, and sending physical mail campaigns. It can include letters, brochures, catalogs, postcards, gifts, and such. It enables marketers to segment target audiences, personalize mail pieces, automate the sending process, and track delivery and response rates.

**Q1** ✅ *def.* · **Q2** ✅ *def.* · **Q3** ~ *def.* · **Q4 ✅ *def.*** → **IN — weak basis**

**Why Q4 lands there:** No requirement list exists. Definition only: *"automates the process of creating, managing, and sending physical mail campaigns… enables marketers to segment target audiences, personalize mail pieces, automate the sending process."*

**Physical mail is a received channel**, so this passes the test on its definition. Smallest row in the study at 11 products — and, like every Peer Insights Category here, it has no entry test.

### 7. Conversational Marketing Solutions

*Gartner **Peer Insights Category** — *not* an analyst market · **no published requirements** · **22 products** · **1 (Legacy)***

**What the source says it is** — no dated requirement list exists

> Conversational marketing is a customer-centric approach that leverages real-time, personalized interactions between companies and customers and mimics human dialogue for the vendor at scale. These technologies employ AI chatbots and automation to design session-based, cross-channel exchanges in the form of natural language dialogue, using a blend of text and audio.

**Q1** — · **Q2** — · **Q3** — · **Q4 **undecidable**** → **BOUNDARY**

**Why Q4 lands there:** **The definition never says who starts the conversation.** *"Session-based, cross-channel exchanges in the form of natural language dialogue"* describes a two-way session, which could be customer-initiated (out of scope) or company-initiated (in scope). With no requirement list, there is nothing to settle it.

**Not scored either way, deliberately.** Resolving it needs the product list — if most members are outbound campaign tools it is IN; if most are website chat widgets it is OUT. One paste answers it.

### 8. Customer Data Platforms

*Gartner **Market** · Magic Quadrant + Critical Capabilities · **Popular** · bar **4** · **71 products** · **1 (Legacy)***

**What the source says it is** — requirements updated January 2026

> Customer data platforms (CDPs) are software applications that support customer experience use cases by unifying a company’s customer data from marketing, sales, service, commerce and other sources. CDPs unify customer data to facilitate its output to coordinate profiles between cross-functional systems, create segments and/or audience targets, optimize offers and/or decisions, and inform analysis while distributing insights that create triggers for other experiences.

**Q1** ✅ · **Q2** ✅ · **Q3** ~ · **Q4 ❌** → **OUT**

**Why Q4 lands there:** "Activation: The ability to send segments, with instructions for activating them, **to engagement tools and platforms**." The thing receiving the send is a system, not a person.

A named boundary case from the original brief, now **settled on the source’s own wording** rather than on judgement.

### 9. Personalization Engines

*Gartner **Market** · Magic Quadrant + Critical Capabilities · **Popular** · bar **8** · **64 products** · **5 (Legacy)***

**What the source says it is** — requirements updated February 2026

> Personalization engines use knowledge about customers to create and deliver an optimum experience for them and measure the impact on customer experience. These engines apply AI, advanced analytics and business rules to create meaningful experiences across channels that facilitate customer engagement and drive revenue.

**Q1** ✅ · **Q2** ✅ · **Q3** ✅ · **Q4 ❌** → **OUT**

**Why Q4 lands there:** **Not one of the 8 requirements names a channel the person receives.** They require segmentation, embedded generative AI, automated machine learning, extensive testing (A/B, multivariate, multiarmed bandit), real-time alteration of interactions, CX profile management, behaviour tracking and performance reporting.

**Hardest bar in the study.** Gartner's definition also admits **employees** as valid recipients, which is wider than our scope.

**Opposite verdict to G2's Personalization** (row 4 below), which does mandate delivering emails and messaging. Same word, two different objects.

### 10. Voice of the Customer Platforms

*Gartner **Market** · Magic Quadrant + Critical Capabilities · **Popular** · bar **3 top-level requirements, 10 sub-requirements** · **59 products** · **2 (Legacy)***

**What the source says it is** — requirements updated July 2026 — the freshest in the set

> Gartner defines a voice of the customer (VoC) platform as one that integrates feedback collection, analysis and action into a single interconnected platform that helps understand and improve the customer experience. Sources of feedback extend beyond direct surveying to include other, more indirect and inferred sources. VoC platforms enable leaders responsible for functions such as customer service, marketing, or sales to better manage the customer experience (CX) through a deep understanding of customer needs, motivations, goals and behaviors.

**Q1** ✅ · **Q2** ❌ · **Q3** ❌ · **Q4 ❌** → **OUT**

**Why Q4 lands there:** "Action — The ability to automatically or manually act upon generated insights through the use of AI-based recommendations and automation, as well as **traditional alerts, workflows and case assignments**." Every action named is internal: an alert to staff, a workflow, a case. Nothing is sent to the customer.

This is a **feedback-in** system, the mirror image of what we are scoping. Its three requirements are collection, analysis, and internal action.

Bar height is reported honestly as **3 requirements with 10 sub-points** — counting the sub-points would make it look like the hardest category here, which would be wrong.
---

## 4. G2 — what each classification is, in G2's words

### 1. Marketing Automation

*G2 **leaf** · bar **10** · **511 listings** · ~21 pastes*

**What the source says it is** — definition updated 10 July 2025

> Marketing automation software helps businesses streamline and scale their marketing efforts by automating campaigns, workflows, or tasks across multiple channels. These platforms serve as a centralized marketing database to enable teams to create segmented, personalized, and timely marketing experiences for customers or prospects based on customer interaction data. These marketing automation tools should ideally support omnichannel marketing engagement across email, SMS, WhatsApp, social media, direct mail, digital advertising, and more.

**Q1** ✅ · **Q2** ✅ · **Q3** ✅ · **Q4 ✅** → **IN**

**Why Q4 lands there:** "Contact targets across multiple channels after specific actions, triggers, or periods of time", and "Automate two or more of the following workflows: email, social media, SMS, and digital ads."

**The highest bar of any category in this document.** Ten mandatory requirements.

Explicitly **excludes** anything categorised in Email Marketing — see row 3.

### 2. SMS Marketing

*G2 **leaf** · bar **4** · **531 listings** · ~22 pastes*

**What the source says it is** — definition updated 14 July 2026

> SMS marketing software, also known as text message marketing, helps companies plan and execute mobile-focused marketing campaigns by sending targeted, permission-based SMS and MMS messages to customers and prospects. These tools support personalized outreach, bulk messaging, and two-way messaging to drive customer engagement and loyalty.

**Q1** ~ *implied, not stated* · **Q2** ❌ · **Q3** ❌ · **Q4 ✅** → **IN**

**Why Q4 lands there:** "Reach mobile users via SMS messaging."

**The weakest IN in the document, and flagged rather than smoothed.** It passes Q4 outright, but Q1 is only *implied* by the requirement to provide *"an opt-in opportunity for new subscribers"* — a subscriber list is entailed, never stated. The other three requirements are tracking and analytics.

### 3. Email Marketing

*G2 **leaf** · bar **7** · **527 listings** · ~22 pastes*

**What the source says it is** — definition updated 9 April 2026

> Email marketing software allows businesses to build and manage email lists, segment audiences, design and send customized campaigns, and monitor subscriber engagement, helping marketing teams, growth teams, and small business owners engage prospects, nurture leads, and retain customers through personalized communication.

**Q1** ✅ · **Q2** ✅ · **Q3** ❌ · **Q4 ✅** → **IN**

**Why Q4 lands there:** "Enable the creation and sending of emails via HTML or a WYSIWYG editor."

Explicitly **excludes** anything categorised in Marketing Automation, so **527 + 511 does not double-count** — unusual for G2, whose general rule places a product in every category it qualifies for.

### 4. Personalization

*G2 **leaf** · bar **3** · **241 listings** · ~10 pastes*

**What the source says it is** — definition updated 14 July 2026

> Personalization software uses customer data to create tailored web experiences, messages, content, promotions, and product recommendations. The personalized experiences are created based on user activity and preferences that drive engagement across websites, emails, mobile applications, and other digital channels. These platforms leverage customer behavior, engagement history, and user profiling to adapt digital experiences to each customer or audience segment. Organizations often use personalization software to deliver more relevant content that captures their customers' attention and ultimately drives conversion rates.

**Q1** ✅ · **Q2** ✅ · **Q3** ❌ · **Q4 ✅** → **IN**

**Why Q4 lands there:** "Deliver personalized **emails, messaging**, websites, content, promotions, or product recommendations for individual users or audience segments."

**Opposite verdict to Gartner's Personalization Engines** (Gartner row 9). G2 mandates delivering emails and messaging; Gartner mandates no send at all. Choosing this row and the Gartner one is choosing two different populations, not two views of one.

### 5. Customer Data Platform (CDP)

*G2 **leaf** · bar **5** · **296 listings** · ~12 pastes*

**What the source says it is** — definition updated 3 October 2024 — **the stalest in the set**

> Customer data platforms (CDPs) are used to consolidate and integrate customer data into one single database. These tools offer marketing teams relevant insights needed to run campaigns. A CDP can grab information from online and offline sources such as websites, mobile apps, and email platforms to offer a complete view of the customer. After retrieving this data, a CDP can then help organizations predict the optimal next move with a particular customer. This allows businesses to learn what needs to be done to retain specific customers. A CDP can also be used by customer service teams to cater their support to each individual. Marketing automation software, data warehouse software, and other platforms that store data can typically integrate with a CDP.

**Q1** ✅ · **Q2** ✅ · **Q3** ❌ · **Q4 ❌** → **OUT**

**Why Q4 lands there:** "**Connect with other systems** to allow marketers to execute campaigns." It connects; it does not send.

**Matches Gartner's verdict, reached independently, in near-identical language.** This is the strongest corroboration in the study — two taxonomies written separately drawing the same line in the same place.

### 6. Marketing Analytics

*G2 **leaf** · bar **5** · **556 listings** · ~23 pastes*

**What the source says it is** — definition updated 23 April 2026

> Marketing analytics software encompasses tools and processes that enable an organization to manage, evaluate, and control its marketing efforts by measuring marketing performance. These solutions simplify and optimize a business’s marketing strategies and activities. With the use of marketing analytics software, businesses can improve their return-on-investment (ROI) by identifying effective marketing methods and adjusting campaigns to maximize conversions and sales.

**Q1** ✅ · **Q2** ✅ · **Q3** ❌ · **Q4 ❌** → **OUT**

**Why Q4 lands there:** The five requirements are collect, monitor, analyze, integrate, visualize. **None sends anything.**

**The largest listing count in the document at 556** — and out of scope. A reminder that size and relevance are unrelated.

### 7. Digital Analytics

*G2 **leaf** · bar **4** · **287 listings** · ~12 pastes*

**What the source says it is** — definition updated 3 October 2024

> Digital analytics software, also referred to as web analytics software, measures website engagement by tracking web traffic and visitors. Marketers, web developers, and analysts use digital analytics tools to report on the effectiveness of web experiences and to determine how visitors are interacting with their sites. By monitoring events such as page views, clicks, and conversions, businesses can distill web traffic data into meaningful insights. Digital analytics software gives organizations insights into customer behavior when encountering their brand’s website and allows reporting on online conversion, demographic, and content-interaction metrics.

**Q1** ❌ · **Q2** ✅ · **Q3** ❌ · **Q4 ❌** → **OUT**

**Why Q4 lands there:** The four requirements are measure traffic, track events, report over time, segment traffic. **None sends anything**, and the subject is a *visitor*, not an identified person.

### 8. Marketing Account Intelligence

*G2 **leaf** · bar **3** · **123 listings** · ~5 pastes*

**What the source says it is** — definition updated 3 October 2024

> Marketing account intelligence software compiles insightful prospect data to help marketers develop a list of accounts that fit a user’s ideal customer profile. Marketing account intelligence systems are implemented to combat the inefficiencies of the traditional “spray and pray" marketing approach. By deploying this software, marketing organizations can maximize efforts on accounts that have a high likelihood of converting to customers while minimizing time and money spent on prospects with a low probability of converting. These tools also assist sales teams by providing incisive information such as a prospect’s role within the company hierarchy or a prospect’s company segment.

**Q1** ✅ · **Q2** ✅ · **Q3** ❌ · **Q4 ❌** → **OUT**

**Why Q4 lands there:** The three requirements are collect account data, score or rank leads, integrate with a data-profile product. **None sends anything.**

### 9. Account Data Management

*G2 **leaf** · bar **4** · **77 listings** · ~4 pastes*

**What the source says it is** — definition updated 3 October 2024

> Account Data Management software manages prospect data throughout the account-based marketing (ABM) process so that both sales and marketing teams have continuous awareness of target accounts. In order to maximize an ABM strategy, salespeople need to know where in the pipeline a prospect is and the probability that a prospect will become a customer. Account Data Management systems serve to document and communicate all relevant account information between the sales and marketing teams. This software is deployed in marketing and sales departments to maximize the efficiency of marketing efforts and facilitate communication between the two organizations.

**Q1** ✅ · **Q2** ✅ · **Q3** ❌ · **Q4 ❌ *ambiguous*** → **OUT — borderline**

**Why Q4 lands there:** "**Facilitate** sales and marketing communication relating to accounts within the system." I read *facilitate* as enabling communication between the sales and marketing teams, not sending to a customer — the definition supports that, describing software that "document[s] and communicate[s] all relevant account information **between the sales and marketing teams**."

**The one verdict in this document that could reasonably flip.** Read *facilitate communication* as outbound and this becomes IN, bringing 77 listings with it. I am flagging it rather than deciding quietly.
---

## 5. Five things the test caught that reading names would not

**1. "Personalization" is two different objects.** G2 requires delivering *"emails,
messaging"* → **IN**, 241 listings. Gartner's eight requirements never mention a send →
**OUT**, 64 products. Merging them on the name would have fused two unrelated populations.

**2. Both sources rule CDP out independently, in near-identical language.** Gartner: send
segments *"to engagement tools and platforms."* G2: *"Connect with other systems to allow
marketers to execute campaigns."* Two taxonomies, written separately, draw the same line at
handing off rather than sending. That settles a boundary case named in the original brief, on
evidence rather than judgement.

**3. Overlap has to be read per pair, never per source.** Gartner states MMH **overlaps** CDPs
and Personalization Engines — so 122 + 71 + 64 double-counts. G2's Email Marketing and
Marketing Automation each carry a rule **excluding** the other — so 527 + 511 does not. No
single dedup assumption survives both.

**4. Entry difficulty does not predict size.** Mobile Marketing Platforms has the lowest bar of
any Gartner market — 3 requirements, each literally prefixed *"Basic"* — and holds 45 products.
Multichannel Marketing Hubs has 6 and holds 122. On G2, the 10-requirement Marketing Automation
holds 511 while the 3-requirement Personalization holds 241.

**5. Gartner's ungoverned categories are its smallest.** All three rows with **no published
requirements** — Direct Mail Automation (11), Location Based Marketing (15), Conversational
Marketing (22) — are the three smallest in the Gartner set. Every governed **Market** holds
45–122. Worth knowing before choosing one, though n=3 and it is a pattern, not a law.

**Also worth carrying:** G2 definition ages span nearly two years, from October 2024 to July
2026. Four of the five stalest are OUT rows. A definition from 2024 sitting beside a listing
count from today is not describing one moment.

---

## 6. The one remaining gap

**G2 Mobile Marketing Software** has not been supplied. It is the only G2 counterpart to
Gartner's Mobile Marketing Platforms, so without it that market cannot be cross-checked against
the other taxonomy — the one place in this document where a Gartner IN row has no possible G2
comparison. One page closes it. Everything else you asked for is here.

---

## 7. What happens once you tick

1. **Vendor list per ticked row.** Gartner rows come back complete in one paste each; G2 rows
   arrive ~25 at a time, so a G2 pick is a standing commitment rather than a single action.
2. **Each vendor row carries** product, vendor, rating, review count, the **`(Legacy)`
   marker**, and provenance back to the raw capture.
3. **Cross-source dedup applies the per-pair overlap rules in §5** — Gartner's three markets
   overlap, G2's two are mutually exclusive.
4. **Ticking a BOUNDARY row is also a decision:** for Conversational Marketing Solutions the
   product list is what resolves the verdict.

**For calibration, not as a recommendation.** The six Gartner **IN** rows cost **6 pastes** and
return **352 fully-enumerated products** with decline markers attached. The four G2 **IN** rows
cost roughly **75 pastes** for **1,810 listings**. Which of these actually matter depends on
deal size and cost to serve — withheld by design, and therefore your judgement, not mine.
