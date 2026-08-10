# outputs/classification-menu.md

**Purpose: you tick the classifications worth diving into. This document exists to make that
choice on evidence, and to make it cheap.**

Scope: **only the categories whose pages were supplied**, plus a small number of close
neighbours flagged as candidates. Max 10 per source. Nothing is enumerated beyond that.

---

## 1. The test — four questions, asked of the source's own published requirements

The failure of the earlier approach was reading category *names*. This reads each category's
**published admission test** — Gartner's `Mandatory Features:` list, G2's *"To qualify for
inclusion… a product must:"* list — and asks four yes/no questions of it.

| | Question | What counts as "yes" |
|---|---|---|
| **Q1** | **Does it require holding a list of identifiable people?** | Stored contacts, profiles, subscriber lists, unified customer records |
| **Q2** | **Does it require choosing who gets what?** | Segmentation, audience building, targeting, scoring |
| **Q3** | **Does it require deciding when to send?** | Triggers, journeys, drip sequences, scheduling, real-time reaction |
| **Q4** | **Does it require actually sending on a channel the person receives?** | Email, SMS, push, in-app message, messaging app, voice, physical mail |

### The verdict rule

> **IN** if **Q4 = yes** **and** (**Q1** or **Q2** = yes).
> Otherwise **OUT**.

**Q4 is load-bearing.** It is the difference between a system that *sends to a person* and one
that *hands data to a system that sends*. That single distinction separates a marketing hub
from a CDP, and an activation tool from an analytics tool, without anyone arguing about names.

### Three rules that make it valid rather than just tidy

1. **Only mandatory requirements count.** If a capability appears in marketing prose but not
   in the published requirement list, it scores **no**. A category is defined by what it
   *forces* every member to do.
2. **Every "yes" cites the deciding line, verbatim.** No verdict is a judgement call you
   cannot audit. Scroll to §4 and check any row against its quote.
3. **Same test, both sources.** Because both publish requirement lists in the same shape, the
   test runs identically on Gartner and G2 — so when they disagree, the disagreement is real
   and not an artefact of how I read them. **It found exactly that: see §3.**

**Known limit, stated:** a category with no published requirement list cannot be scored this
way. That applies to Gartner Peer Insights *Categories* (as opposed to analyst *Markets*) and
to G2 *parent* categories. Those rows say so rather than being guessed.

---

## 2. THE MENU — tick what you want

`Companies` = cost to produce the full vendor list for that row.
**Gartner enumerates fully in one page ("Products 1–122 of 122"). G2 shows ~25 of its declared
listings, so a G2 vendor list costs ~1 paste per 25.** This is why the two columns differ so
sharply, and it should drive your picks.

### Gartner Peer Insights

| ☐ | Category | Type | Q1 | Q2 | Q3 | **Q4** | Verdict | Bar | Products | Decline marker | Companies |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ☐ | **Multichannel Marketing Hubs** | Market | ✅ | ✅ | ✅ | **✅** | **IN** | 6 | **122** | — | **1 paste** |
| ☐ | **Email Marketing** | Market | ✅ | ✅ | ❌ | **✅** | **IN** | 4 | **100** | **(Transitioning to Email Marketing Platforms)** | **1 paste** |
| ☐ | **B2B Marketing Automation Platforms** | Market | ✅ | ✅ | ✅ | **✅** | **IN** | 5 | **59** | — | **1 paste** |
| ☐ | **Mobile Marketing Platforms** | Market | ✅ | ~ | ~ | **✅** | **IN** | 3 | **45** | — | **1 paste** |
| ☐ | **Location Based Marketing Software** | *Category* | — | — | — | **✅ (definition only)** | **IN — weak basis** | **none published** | **15** | — | **1 paste** |
| ☐ | Customer Data Platforms | Market | ✅ | ✅ | ~ | **❌** | **OUT** | 4 | 71 | — | 1 paste |
| ☐ | Personalization Engines | Market | ✅ | ✅ | ✅ | **❌** | **OUT** | 8 | 64 | — | 1 paste |
| ☐ | Voice of the Customer Platforms | Market | ? | ? | ? | **?** | **NOT SCORED** | ? | ? | ? | needs page |
| ☐ | *Conversational Marketing Solutions* | candidate | ? | ? | ? | ? | **NOT SCORED** | ? | ? | ? | needs page |
| ☐ | *Direct Mail Automation Software* | candidate | ? | ? | ? | ? | **NOT SCORED** | ? | ? | ? | needs page |

### G2

| ☐ | Category | Type | Q1 | Q2 | Q3 | **Q4** | Verdict | Bar | Listings | Companies |
|---|---|---|---|---|---|---|---|---|---|---|
| ☐ | **Marketing Automation** | leaf | ✅ | ✅ | ✅ | **✅** | **IN** | 10 | **511** | ~21 pastes |
| ☐ | **SMS Marketing** | leaf | ~ | ❌ | ❌ | **✅** | **IN** | 4 | **531** | ~22 pastes |
| ☐ | **Email Marketing** | leaf | ✅ | ✅ | ❌ | **✅** | **IN** | 7 | **527** | ~22 pastes |
| ☐ | **Personalization** | leaf | ✅ | ✅ | ❌ | **✅** | **IN** | 3 | **241** | ~10 pastes |
| ☐ | Marketing Analytics | leaf | ✅ | ✅ | ❌ | **❌** | **OUT** | 5 | 556 | ~23 pastes |
| ☐ | Digital Analytics | leaf | ❌ | ✅ | ❌ | **❌** | **OUT** | 4 | 287 | ~12 pastes |
| ☐ | Customer Data Platform (CDP) | leaf | ✅ | ✅ | ❌ | **❌** | **OUT** | 5 | 296 | ~12 pastes |
| ☐ | Marketing Account Intelligence | leaf | ✅ | ✅ | ❌ | **❌** | **OUT** | 3 | 123 | ~5 pastes |
| ☐ | Account Data Management | leaf | ✅ | ✅ | ❌ | **❌ ambiguous** | **OUT — borderline** | 4 | 77 | ~4 pastes |
| ☐ | *Mobile Marketing Software* | candidate leaf | ? | ? | ? | ? | **NOT SCORED** | ? | ? | needs page |

**Not classifiers — G2 parent categories.** Account-Based Marketing, Lead Generation,
Conversion Rate Optimization Tools each show **no listing count and no inclusion criteria**,
matching G2's published rule that *"Parent categories… do not actually contain any G2 product
profiles."* They are navigation, not populations. Confirmed on all three (n=3).

---

## 3. What the test found that a name-based read would have missed

**1. Personalization: G2 says IN, Gartner says OUT — on the same concept.**
G2 mandates *"Deliver personalized **emails, messaging**, websites, content, promotions, or
product recommendations"* → Q4 yes. Gartner's 8 mandatory features for Personalization Engines
require segmentation, GenAI, ML, testing, real-time alteration, profile management — **and no
send on any received channel** → Q4 no. Same word, two different objects. **Merging them on the
name would have silently combined 241 listings with 64 products that do different jobs.**

**2. CDP: both sources say OUT, independently, in near-identical language.**
Gartner: activation is *"the ability to send segments… **to engagement tools and platforms**."*
G2: *"**Connect with other systems** to allow marketers to execute campaigns."*
Two taxonomies, written separately, both draw the line at handing off rather than sending. That
is the strongest single corroboration in this study so far — and it settles a boundary case
named in the original brief.

**3. Email Marketing and Marketing Automation are explicitly disjoint on G2.**
Email Marketing requires *"not be categorized as marketing automation"*; Marketing Automation
requires *"not be categorized in the email marketing software category."* So **527 + 511 does
not double-count** — unusual for G2, whose general rule places a product in every category it
qualifies for. Dedup logic must treat this pair as exclusive and other pairs as overlapping.

**4. Gartner says its own markets overlap.** *"MMHs overlap with customer data platforms (CDPs)
and personalization engines."* So 122 + 71 + 64 **does** double-count. Opposite of the G2 pair
above — which is why overlap has to be read per source, per pair, from published rules.

**5. Bar height does not predict size.** Mobile Marketing Platforms has the lowest bar in the
sample — 3 requirements, each literally prefixed *"Basic"* — and only 45 products. Multichannel
Marketing Hubs has bar 6 and 122. Whatever drives participation here, it is not ease of entry.

---

## 4. Evidence — the deciding line for every Q4 verdict

| Category | Source | Q4 | Deciding requirement, verbatim |
|---|---|---|---|
| Multichannel Marketing Hubs | Gartner | ✅ | "Multichannel execution and measurement: Enables deployment and measurement of personalized messages across digital channels, such as email, mobile messaging and advertising." |
| Email Marketing | Gartner | ✅ | "Ability to send out email messages to many contacts in one step" |
| B2B Marketing Automation Platforms | Gartner | ✅ | "Deploy and manage coordinated customer engagement programs across multiple channels, including native email and landing page execution." |
| Mobile Marketing Platforms | Gartner | ✅ | "Basic mobile channel campaign management and support (for channels such as SMS/MMS, push notifications and/or in-app messages)" |
| Location Based Marketing Software | Gartner | ✅ | *No mandatory list exists.* Definition only: "allowing businesses to send personalized messages, offers, or ads when users are near a specific location" |
| Customer Data Platforms | Gartner | ❌ | "Activation: The ability to send segments, with instructions for activating them, **to engagement tools and platforms**" — recipient is a system, not a person |
| Personalization Engines | Gartner | ❌ | None of the 8 mandatory features names a received channel |
| Marketing Automation | G2 | ✅ | "Contact targets across multiple channels after specific actions, triggers, or periods of time"; "Automate two or more of the following workflows: email, social media, SMS, and digital ads" |
| SMS Marketing | G2 | ✅ | "Reach mobile users via SMS messaging" |
| Email Marketing | G2 | ✅ | "Enable the creation and sending of emails via HTML or a WYSIWYG editor" |
| Personalization | G2 | ✅ | "Deliver personalized emails, messaging, websites, content, promotions, or product recommendations for individual users or audience segments" |
| Customer Data Platform (CDP) | G2 | ❌ | "Connect with other systems to allow marketers to execute campaigns" — connects, does not send |
| Marketing Analytics | G2 | ❌ | Requirements are collect / monitor / analyze / integrate / visualize. No send |
| Digital Analytics | G2 | ❌ | Requirements are measure / track / report / segment traffic. No send |
| Marketing Account Intelligence | G2 | ❌ | Requirements are collect account data / score leads / integrate. No send |
| Account Data Management | G2 | ❌ | "Facilitate sales and marketing communication relating to accounts within the system" — **"facilitate" is not "send"**; flagged borderline, would flip if the page's fuller text mandates outbound |

**Q1–Q3 quotes** are in `sources/derived/g2-gartner-scoring.md` alongside the full requirement
lists. Every raw capture is in `sources/raw/{g2,gartner}/`.

---

## 5. What happens after you tick

1. For each ticked row, produce the vendor list — Gartner rows in 1 paste each, G2 rows
   paginated at ~25 per paste.
2. Rows carry: vendor, product, rating, review count, **`(Legacy)` marker**, and provenance.
3. Cross-source dedup respects the overlap rules in §3 — Gartner's three markets overlap;
   G2's Email Marketing and Marketing Automation do not.
4. `NOT SCORED` rows need their page before they can be ticked meaningfully.

**Suggested minimum if you want breadth cheaply:** the five Gartner **IN** rows cost **5 pastes
and yield 341 fully-enumerated products**, with decline markers included. The equivalent from
G2 costs ~75 pastes. I am not recommending which categories matter — that judgement needs deal
size and cost to serve, which are withheld by design.
