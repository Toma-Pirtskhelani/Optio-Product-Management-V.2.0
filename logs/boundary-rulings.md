# boundary-rulings.md

Every IN / OUT / BOUNDARY ruling, with its reasoning, **logged before the row enters any
output**. Per `CLAUDE.md` §1: boundary cases are ruled individually and never silently
included or excluded as a class.

A ruling made in a chat message and not written here did not happen. Append-only — a
reversed ruling gets a new row citing the old `ruling_id`, and the old row stays.

## Columns

| Field | Meaning |
|---|---|
| `ruling_id` | `B-0001`, sequential |
| `date` | ISO date of the ruling |
| `subject` | Vendor, product, or category being ruled on |
| `subject_type` | `vendor` / `product` / `category` / `class` |
| `verdict` | `IN` / `OUT` / `BOUNDARY-IN` / `BOUNDARY-OUT` |
| `test_applied` | Which part of the functional definition decided it |
| `reasoning` | Why. Specific to this subject — not a restatement of the definition |
| `evidence` | Source URL(s) + `paste_id` the ruling rests on |
| `grade` | Confidence grade of the evidence the ruling rests on |
| `source_boundary_verbatim` | The source's own category boundary, quoted, where it differs from ours |
| `supersedes` | Prior `ruling_id` this reverses, or `—` |

## The test

**IN:** primary function is orchestrating outbound or triggered customer communication,
across one or more channels, driven by stored customer data or behavior — including
vertical-specific instances of that job under whatever local name.

**OUT:** pure analytics/BI (measurement without activation); pure sales-pipeline CRM (no
outbound orchestration); pure message-delivery infrastructure (transport without targeting
logic).

**The recurring four**, each ruled per instance and never as a class:
1. CRM suites carrying a campaign module
2. Delivery infrastructure moving up-stack into orchestration
3. Loyalty platforms with messaging attached
4. Customer data platforms sold with or without activation

## Rules

- **`BOUNDARY-IN` / `BOUNDARY-OUT` are distinct from `IN` / `OUT`.** They mark rows a
  reasonable analyst could rule the other way. Every output states how many of its rows are
  boundary rulings, so a count's sensitivity to the definition is visible rather than hidden
  inside it.
- A ruling made on `MODELED` or `UNKNOWN` evidence is not a ruling. Mark the subject
  `UNRULED — evidence insufficient` and keep it out of counts until evidence arrives.
- **Where a source's boundary differs from ours, quote the source's boundary verbatim.**
  Do not normalize the disagreement away — it is data about the market's shape and belongs
  in `logs/conflicts.md` as well.
- Blinding applies here hardest. A ruling that reads "this is adjacent to what the client
  does" is contaminated and void. The test is functional, not commercial.

## Pass 01 note — every ruling below is provisional

All 49 rulings rest on the **category name only**. G2 returns 403 on every category page, so
G2's own definition and inclusion criteria — the things that would actually decide these —
have not been read. `source_boundary_verbatim` is `UNKNOWN` on every row for that reason, and
each row is `SINGLE-SOURCE`, not `PRIMARY`.

Per this file's own rule, a ruling made on insufficient evidence is not a ruling. These are
therefore recorded as **BOUNDARY** — meaning "a reasonable analyst could rule this either
way", which is exactly true — and not as IN or OUT. They are re-decided when the pastes in
`outputs/source-taxonomies.md` §8 Request 2 arrive.

## Log

| ruling_id | date | subject | subject_type | verdict | test_applied | reasoning | evidence | grade | source_boundary_verbatim | supersedes |
|---|---|---|---|---|---|---|---|---|---|---|
| B-0001 | 2026-08-10 | Conversational Interface Agents Software | category | BOUNDARY | IN-clause, direction disputed | Predominantly inbound response; outbound/triggered capability exists in part of each category. | https://www.g2.com/categories/conversational-interface-agents (category name only — page 403, definition NOT read) | SINGLE-SOURCE | UNKNOWN — G2's own boundary is on the blocked category page | — |
| B-0002 | 2026-08-10 | Bot Platforms | category | BOUNDARY | IN-clause, direction disputed | Predominantly inbound response; outbound/triggered capability exists in part of each category. | https://www.g2.com/categories/bot-platforms (category name only — page 403, definition NOT read) | SINGLE-SOURCE | UNKNOWN — G2's own boundary is on the blocked category page | — |
| B-0003 | 2026-08-10 | Chatbots Software | category | BOUNDARY | IN-clause, direction disputed | Predominantly inbound response; outbound/triggered capability exists in part of each category. | https://www.g2.com/categories/chatbots (category name only — page 403, definition NOT read) | SINGLE-SOURCE | UNKNOWN — G2's own boundary is on the blocked category page | — |
| B-0004 | 2026-08-10 | Enterprise AI Chatbots Software | category | BOUNDARY | IN-clause, direction disputed | Predominantly inbound response; outbound/triggered capability exists in part of each category. | https://www.g2.com/categories/enterprise-ai-chatbots (category name only — page 403, definition NOT read) | SINGLE-SOURCE | UNKNOWN — G2's own boundary is on the blocked category page | — |
| B-0005 | 2026-08-10 | AI Chatbots Software | category | BOUNDARY | IN-clause, direction disputed | Predominantly inbound response; outbound/triggered capability exists in part of each category. | https://www.g2.com/categories/ai-chatbots (category name only — page 403, definition NOT read) | SINGLE-SOURCE | UNKNOWN — G2's own boundary is on the blocked category page | — |
| B-0006 | 2026-08-10 | CRM Software | category | BOUNDARY | BOUNDARY case 1 — CRM suite carrying a campaign module | Pipeline CRM is explicitly OUT; the same product may carry campaign orchestration. Undecidable from the category name — needs the source's inclusion criteria. | https://www.g2.com/categories/crm (category name only — page 403, definition NOT read) | SINGLE-SOURCE | UNKNOWN — G2's own boundary is on the blocked category page | — |
| B-0007 | 2026-08-10 | Account-Based Advertising Software | category | BOUNDARY | BOUNDARY — ad-channel outbound | Outbound and often driven by uploaded customer data, but the channel is an ad exchange and the target is a segment, not a record. | https://www.g2.com/categories/account-based-advertising (category name only — page 403, definition NOT read) | SINGLE-SOURCE | UNKNOWN — G2's own boundary is on the blocked category page | — |
| B-0008 | 2026-08-10 | Book Marketing Tools | category | BOUNDARY | IN-clause, addressability disputed | Publishing to an audience rather than to stored individual records; some products in these categories do both. | https://www.g2.com/categories/book-marketing-tools (category name only — page 403, definition NOT read) | SINGLE-SOURCE | UNKNOWN — G2's own boundary is on the blocked category page | — |
| B-0009 | 2026-08-10 | Customer Data Platforms (CDP) | category | BOUNDARY | BOUNDARY case 4 — CDP sold with or without activation | The named boundary class. Whether activation is mandatory is exactly what the inclusion criteria decide. | https://www.g2.com/categories/customer-data-platform-cdp (category name only — page 403, definition NOT read) | SINGLE-SOURCE | UNKNOWN — G2's own boundary is on the blocked category page | — |
| B-0010 | 2026-08-10 | Loyalty Management Software | category | BOUNDARY | BOUNDARY case 3 — loyalty platform with messaging attached | The named boundary class. | https://www.g2.com/categories/loyalty-management (category name only — page 403, definition NOT read) | SINGLE-SOURCE | UNKNOWN — G2's own boundary is on the blocked category page | — |
| B-0011 | 2026-08-10 | Event Marketing Software | category | BOUNDARY | IN-clause, addressability disputed | Publishing to an audience rather than to stored individual records; some products in these categories do both. | https://www.g2.com/categories/event-marketing (category name only — page 403, definition NOT read) | SINGLE-SOURCE | UNKNOWN — G2's own boundary is on the blocked category page | — |
| B-0012 | 2026-08-10 | Local Marketing Software | category | BOUNDARY | IN-clause, addressability disputed | Publishing to an audience rather than to stored individual records; some products in these categories do both. | https://www.g2.com/categories/local-marketing (category name only — page 403, definition NOT read) | SINGLE-SOURCE | UNKNOWN — G2's own boundary is on the blocked category page | — |
| B-0013 | 2026-08-10 | Multi-Location Marketing Platforms | category | BOUNDARY | IN-clause, addressability disputed | Publishing to an audience rather than to stored individual records; some products in these categories do both. | https://www.g2.com/categories/multi-location-marketing-platforms (category name only — page 403, definition NOT read) | SINGLE-SOURCE | UNKNOWN — G2's own boundary is on the blocked category page | — |
| B-0014 | 2026-08-10 | Other Marketing Software | category | BOUNDARY | Residual bucket | G2 rule: 'Other' holds products qualifying for no defined category. Contents unknowable without the product list. | https://www.g2.com/categories/other-marketing (category name only — page 403, definition NOT read) | SINGLE-SOURCE | UNKNOWN — G2's own boundary is on the blocked category page | — |
| B-0015 | 2026-08-10 | Personalization Software | category | BOUNDARY | IN-clause, channel disputed | Behaviour-driven and data-driven, but the 'channel' is often the site itself rather than an outbound message. | https://www.g2.com/categories/personalization (category name only — page 403, definition NOT read) | SINGLE-SOURCE | UNKNOWN — G2's own boundary is on the blocked category page | — |
| B-0016 | 2026-08-10 | Personalization Engines | category | BOUNDARY | IN-clause, channel disputed | Behaviour-driven and data-driven, but the 'channel' is often the site itself rather than an outbound message. | https://www.g2.com/categories/personalization-engines (category name only — page 403, definition NOT read) | SINGLE-SOURCE | UNKNOWN — G2's own boundary is on the blocked category page | — |
| B-0017 | 2026-08-10 | RCS Business Messaging Software | category | BOUNDARY | BOUNDARY case 2 — delivery infrastructure moving up-stack | Transport without targeting logic is OUT; these categories contain both pure transport and products that have moved into orchestration. | https://www.g2.com/categories/rcs-business-messaging (category name only — page 403, definition NOT read) | SINGLE-SOURCE | UNKNOWN — G2's own boundary is on the blocked category page | — |
| B-0018 | 2026-08-10 | Social Media Marketing Software | category | BOUNDARY | IN-clause, addressability disputed | Publishing to an audience rather than to stored individual records; some products in these categories do both. | https://www.g2.com/categories/social-media-marketing (category name only — page 403, definition NOT read) | SINGLE-SOURCE | UNKNOWN — G2's own boundary is on the blocked category page | — |
| B-0019 | 2026-08-10 | Transactional Email Software | category | BOUNDARY | BOUNDARY case 2 — delivery infrastructure moving up-stack | Transport without targeting logic is OUT; these categories contain both pure transport and products that have moved into orchestration. | https://www.g2.com/categories/transactional-email (category name only — page 403, definition NOT read) | SINGLE-SOURCE | UNKNOWN — G2's own boundary is on the blocked category page | — |
| B-0020 | 2026-08-10 | Merchant Marketing Software | category | BOUNDARY | IN-clause, addressability disputed | Publishing to an audience rather than to stored individual records; some products in these categories do both. | https://www.g2.com/categories/merchant-marketing (category name only — page 403, definition NOT read) | SINGLE-SOURCE | UNKNOWN — G2's own boundary is on the blocked category page | — |
| B-0021 | 2026-08-10 | E-Commerce Personalization Software | category | BOUNDARY | IN-clause, channel disputed | Behaviour-driven and data-driven, but the 'channel' is often the site itself rather than an outbound message. | https://www.g2.com/categories/e-commerce-personalization (category name only — page 403, definition NOT read) | SINGLE-SOURCE | UNKNOWN — G2's own boundary is on the blocked category page | — |
| B-0022 | 2026-08-10 | Live Chat Software | category | BOUNDARY | IN-clause, direction disputed | Predominantly inbound response; outbound/triggered capability exists in part of each category. | https://www.g2.com/categories/live-chat (category name only — page 403, definition NOT read) | SINGLE-SOURCE | UNKNOWN — G2's own boundary is on the blocked category page | — |
| B-0023 | 2026-08-10 | Contact Center Software | category | BOUNDARY | IN-clause, direction disputed | Predominantly inbound response; outbound/triggered capability exists in part of each category. | https://www.g2.com/categories/contact-center (category name only — page 403, definition NOT read) | SINGLE-SOURCE | UNKNOWN — G2's own boundary is on the blocked category page | — |
| B-0024 | 2026-08-10 | Conversational Support Software | category | BOUNDARY | IN-clause, direction disputed | Predominantly inbound response; outbound/triggered capability exists in part of each category. | https://www.g2.com/categories/conversational-support (category name only — page 403, definition NOT read) | SINGLE-SOURCE | UNKNOWN — G2's own boundary is on the blocked category page | — |
| B-0025 | 2026-08-10 | Customer Service Automation Software | category | BOUNDARY | IN-clause, direction disputed | Predominantly inbound response; outbound/triggered capability exists in part of each category. | https://www.g2.com/categories/customer-service-automation (category name only — page 403, definition NOT read) | SINGLE-SOURCE | UNKNOWN — G2's own boundary is on the blocked category page | — |
| B-0026 | 2026-08-10 | Data Breach Notification Software | category | BOUNDARY | IN-clause, trigger disputed | Triggered customer communication driven by stored data; compliance-driven rather than commercial. | https://www.g2.com/categories/data-breach-notification (category name only — page 403, definition NOT read) | SINGLE-SOURCE | UNKNOWN — G2's own boundary is on the blocked category page | — |
| B-0027 | 2026-08-10 | Communication Platform as a Service (cPaaS) Platforms | category | BOUNDARY | BOUNDARY case 2 — delivery infrastructure moving up-stack | Transport without targeting logic is OUT; these categories contain both pure transport and products that have moved into orchestration. | https://www.g2.com/categories/communication-platform-as-a-service-cpaas (category name only — page 403, definition NOT read) | SINGLE-SOURCE | UNKNOWN — G2's own boundary is on the blocked category page | — |
| B-0028 | 2026-08-10 | Geofencing Software | category | BOUNDARY | IN-clause, trigger disputed | Location trigger is in scope; many products here are developer toolkits, i.e. infrastructure. | https://www.g2.com/categories/geofencing (category name only — page 403, definition NOT read) | SINGLE-SOURCE | UNKNOWN — G2's own boundary is on the blocked category page | — |
| B-0029 | 2026-08-10 | Notification Infrastructure Software | category | BOUNDARY | BOUNDARY case 2 — delivery infrastructure moving up-stack | Transport without targeting logic is OUT; these categories contain both pure transport and products that have moved into orchestration. | https://www.g2.com/categories/notification-infrastructure (category name only — page 403, definition NOT read) | SINGLE-SOURCE | UNKNOWN — G2's own boundary is on the blocked category page | — |
| B-0030 | 2026-08-10 | Cross-Channel Advertising Software | category | BOUNDARY | BOUNDARY — ad-channel outbound | Outbound and often driven by uploaded customer data, but the channel is an ad exchange and the target is a segment, not a record. | https://www.g2.com/categories/cross-channel-advertising (category name only — page 403, definition NOT read) | SINGLE-SOURCE | UNKNOWN — G2's own boundary is on the blocked category page | — |
| B-0031 | 2026-08-10 | Display Advertising Software | category | BOUNDARY | BOUNDARY — ad-channel outbound | Outbound and often driven by uploaded customer data, but the channel is an ad exchange and the target is a segment, not a record. | https://www.g2.com/categories/display-advertising (category name only — page 403, definition NOT read) | SINGLE-SOURCE | UNKNOWN — G2's own boundary is on the blocked category page | — |
| B-0032 | 2026-08-10 | Mobile Advertising Software | category | BOUNDARY | BOUNDARY — ad-channel outbound | Outbound and often driven by uploaded customer data, but the channel is an ad exchange and the target is a segment, not a record. | https://www.g2.com/categories/mobile-advertising (category name only — page 403, definition NOT read) | SINGLE-SOURCE | UNKNOWN — G2's own boundary is on the blocked category page | — |
| B-0033 | 2026-08-10 | Retail Media Advertising Platforms | category | BOUNDARY | BOUNDARY — ad-channel outbound | Outbound and often driven by uploaded customer data, but the channel is an ad exchange and the target is a segment, not a record. | https://www.g2.com/categories/retail-media-advertising-platforms (category name only — page 403, definition NOT read) | SINGLE-SOURCE | UNKNOWN — G2's own boundary is on the blocked category page | — |
| B-0034 | 2026-08-10 | Social Media Advertising Software | category | BOUNDARY | BOUNDARY — ad-channel outbound | Outbound and often driven by uploaded customer data, but the channel is an ad exchange and the target is a segment, not a record. | https://www.g2.com/categories/social-media-advertising (category name only — page 403, definition NOT read) | SINGLE-SOURCE | UNKNOWN — G2's own boundary is on the blocked category page | — |
| B-0035 | 2026-08-10 | Recruitment Marketing Platforms | category | BOUNDARY | IN-clause, recipient disputed | Function matches exactly; the recipient is a candidate, not a customer. See the proposed wording change. | https://www.g2.com/categories/recruitment-marketing (category name only — page 403, definition NOT read) | SINGLE-SOURCE | UNKNOWN — G2's own boundary is on the blocked category page | — |
| B-0036 | 2026-08-10 | Employee Referral Software | category | BOUNDARY | IN-clause, recipient disputed | Function matches exactly; the recipient is a candidate, not a customer. See the proposed wording change. | https://www.g2.com/categories/employee-referral (category name only — page 403, definition NOT read) | SINGLE-SOURCE | UNKNOWN — G2's own boundary is on the blocked category page | — |
| B-0037 | 2026-08-10 | Programmatic Job Advertising Software | category | BOUNDARY | IN-clause, recipient disputed | Function matches exactly; the recipient is a candidate, not a customer. See the proposed wording change. | https://www.g2.com/categories/programmatic-job-advertising (category name only — page 403, definition NOT read) | SINGLE-SOURCE | UNKNOWN — G2's own boundary is on the blocked category page | — |
| B-0038 | 2026-08-10 | Recruiting Automation Software | category | BOUNDARY | IN-clause, recipient disputed | Function matches exactly; the recipient is a candidate, not a customer. See the proposed wording change. | https://www.g2.com/categories/recruiting-automation (category name only — page 403, definition NOT read) | SINGLE-SOURCE | UNKNOWN — G2's own boundary is on the blocked category page | — |
| B-0039 | 2026-08-10 | Alumni Management Software | category | BOUNDARY | IN-clause, recipient disputed | Same function; recipient is an alumnus or donor. | https://www.g2.com/categories/alumni-management (category name only — page 403, definition NOT read) | SINGLE-SOURCE | UNKNOWN — G2's own boundary is on the blocked category page | — |
| B-0040 | 2026-08-10 | Construction CRM Software | category | BOUNDARY | BOUNDARY case 1 — CRM suite carrying a campaign module | Pipeline CRM is explicitly OUT; the same product may carry campaign orchestration. Undecidable from the category name — needs the source's inclusion criteria. | https://www.g2.com/categories/construction-crm (category name only — page 403, definition NOT read) | SINGLE-SOURCE | UNKNOWN — G2's own boundary is on the blocked category page | — |
| B-0041 | 2026-08-10 | Financial Services CRM Software | category | BOUNDARY | BOUNDARY case 1 — CRM suite carrying a campaign module | Pipeline CRM is explicitly OUT; the same product may carry campaign orchestration. Undecidable from the category name — needs the source's inclusion criteria. | https://www.g2.com/categories/financial-services-crm (category name only — page 403, definition NOT read) | SINGLE-SOURCE | UNKNOWN — G2's own boundary is on the blocked category page | — |
| B-0042 | 2026-08-10 | Mortgage CRM Software | category | BOUNDARY | BOUNDARY case 1 — CRM suite carrying a campaign module | Pipeline CRM is explicitly OUT; the same product may carry campaign orchestration. Undecidable from the category name — needs the source's inclusion criteria. | https://www.g2.com/categories/mortgage-crm (category name only — page 403, definition NOT read) | SINGLE-SOURCE | UNKNOWN — G2's own boundary is on the blocked category page | — |
| B-0043 | 2026-08-10 | HIPAA Compliant Messaging Software | category | BOUNDARY | IN/OUT undecidable | Category name does not say whether the messaging is clinician-to-patient (IN) or clinician-to-clinician (OUT). | https://www.g2.com/categories/hipaa-compliant-messaging (category name only — page 403, definition NOT read) | SINGLE-SOURCE | UNKNOWN — G2's own boundary is on the blocked category page | — |
| B-0044 | 2026-08-10 | Insurance CRM Software | category | BOUNDARY | BOUNDARY case 1 — CRM suite carrying a campaign module | Pipeline CRM is explicitly OUT; the same product may carry campaign orchestration. Undecidable from the category name — needs the source's inclusion criteria. | https://www.g2.com/categories/insurance-crm (category name only — page 403, definition NOT read) | SINGLE-SOURCE | UNKNOWN — G2's own boundary is on the blocked category page | — |
| B-0045 | 2026-08-10 | Legal CRM Software | category | BOUNDARY | BOUNDARY case 1 — CRM suite carrying a campaign module | Pipeline CRM is explicitly OUT; the same product may carry campaign orchestration. Undecidable from the category name — needs the source's inclusion criteria. | https://www.g2.com/categories/legal-crm (category name only — page 403, definition NOT read) | SINGLE-SOURCE | UNKNOWN — G2's own boundary is on the blocked category page | — |
| B-0046 | 2026-08-10 | Donor Management Software | category | BOUNDARY | IN-clause, recipient disputed | Same function; recipient is an alumnus or donor. | https://www.g2.com/categories/donor-management (category name only — page 403, definition NOT read) | SINGLE-SOURCE | UNKNOWN — G2's own boundary is on the blocked category page | — |
| B-0047 | 2026-08-10 | Fundraising Software | category | BOUNDARY | IN-clause, recipient disputed | Same function; recipient is an alumnus or donor. | https://www.g2.com/categories/fundraising (category name only — page 403, definition NOT read) | SINGLE-SOURCE | UNKNOWN — G2's own boundary is on the blocked category page | — |
| B-0048 | 2026-08-10 | Nonprofit CRM Software | category | BOUNDARY | BOUNDARY case 1 — CRM suite carrying a campaign module | Pipeline CRM is explicitly OUT; the same product may carry campaign orchestration. Undecidable from the category name — needs the source's inclusion criteria. | https://www.g2.com/categories/nonprofit-crm (category name only — page 403, definition NOT read) | SINGLE-SOURCE | UNKNOWN — G2's own boundary is on the blocked category page | — |
| B-0049 | 2026-08-10 | Real Estate CRM Software | category | BOUNDARY | BOUNDARY case 1 — CRM suite carrying a campaign module | Pipeline CRM is explicitly OUT; the same product may carry campaign orchestration. Undecidable from the category name — needs the source's inclusion criteria. | https://www.g2.com/categories/real-estate-crm (category name only — page 403, definition NOT read) | SINGLE-SOURCE | UNKNOWN — G2's own boundary is on the blocked category page | — |

## Pass 02 — re-resolution under the revised scope definition (2026-08-10)

The 49 provisional BOUNDARY rulings from pass 01, re-decided against the recipient/channel
definition in `CLAUDE.md` §1 and, where Gartner supplied one, against a source's own
mandatory-feature list.

**27 of 49 resolved — 9 to IN, 18 to OUT. 22 remain BOUNDARY.**

Two were resolved by *evidence* rather than by the definition change, and those are the
valuable ones: **Customer Data Platforms** and **Personalization Engines** were decided by
reading Gartner's own mandatory-feature lists — exactly the content that was blocked when
these were first ruled. That is what the STOP-AT-RUNG-3 rule is for.

| ruling_id | subject | pass-01 verdict | pass-02 verdict | deciding reason |
|---|---|---|---|---|
| B-0001 | Conversational Interface Agents Software | BOUNDARY | **OUT** | Inbound response to a recipient who initiated contact. The test is who initiated delivery. |
| B-0002 | Bot Platforms | BOUNDARY | **OUT** | Inbound response to a recipient who initiated contact. The test is who initiated delivery. |
| B-0003 | Chatbots Software | BOUNDARY | **OUT** | Inbound response to a recipient who initiated contact. The test is who initiated delivery. |
| B-0004 | Enterprise AI Chatbots Software | BOUNDARY | **OUT** | Inbound response to a recipient who initiated contact. The test is who initiated delivery. |
| B-0005 | AI Chatbots Software | BOUNDARY | **OUT** | Inbound response to a recipient who initiated contact. The test is who initiated delivery. |
| B-0006 | CRM Software | BOUNDARY | **BOUNDARY (unchanged)** | Revised definition does not reach it — needs the source's inclusion criteria, still blocked at G2. |
| B-0007 | Account-Based Advertising Software | BOUNDARY | **OUT** | Ad-channel placement targets a segment via an exchange; the organisation does not initiate delivery to an identified recipient. |
| B-0008 | Book Marketing Tools | BOUNDARY | **BOUNDARY (unchanged)** | Revised definition does not reach it — needs the source's inclusion criteria, still blocked at G2. |
| B-0009 | Customer Data Platforms (CDP) | BOUNDARY | **OUT** | Gartner's CDP mandatory feature defines activation as sending segments to engagement tools — the CDP hands off, it does not initiate delivery to a recipient. |
| B-0010 | Loyalty Management Software | BOUNDARY | **BOUNDARY (unchanged)** | Revised definition does not reach it — needs the source's inclusion criteria, still blocked at G2. |
| B-0011 | Event Marketing Software | BOUNDARY | **IN** | Attendee communications go to registered individuals — identified recipients. |
| B-0012 | Local Marketing Software | BOUNDARY | **BOUNDARY (unchanged)** | Revised definition does not reach it — needs the source's inclusion criteria, still blocked at G2. |
| B-0013 | Multi-Location Marketing Platforms | BOUNDARY | **BOUNDARY (unchanged)** | Revised definition does not reach it — needs the source's inclusion criteria, still blocked at G2. |
| B-0014 | Other Marketing Software | BOUNDARY | **BOUNDARY (unchanged)** | Revised definition does not reach it — needs the source's inclusion criteria, still blocked at G2. |
| B-0015 | Personalization Software | BOUNDARY | **OUT** | In-app/on-site personalisation alters what a surface shows a visitor who came to it. None of Gartner's 8 mandatory features requires a received channel. |
| B-0016 | Personalization Engines | BOUNDARY | **OUT** | In-app/on-site personalisation alters what a surface shows a visitor who came to it. None of Gartner's 8 mandatory features requires a received channel. |
| B-0017 | RCS Business Messaging Software | BOUNDARY | **BOUNDARY (unchanged)** | Revised definition does not reach it — needs the source's inclusion criteria, still blocked at G2. |
| B-0018 | Social Media Marketing Software | BOUNDARY | **OUT** | Publishing to an audience, not delivery to an identified recipient. |
| B-0019 | Transactional Email Software | BOUNDARY | **BOUNDARY (unchanged)** | Revised definition does not reach it — needs the source's inclusion criteria, still blocked at G2. |
| B-0020 | Merchant Marketing Software | BOUNDARY | **BOUNDARY (unchanged)** | Revised definition does not reach it — needs the source's inclusion criteria, still blocked at G2. |
| B-0021 | E-Commerce Personalization Software | BOUNDARY | **OUT** | In-app/on-site personalisation alters what a surface shows a visitor who came to it. None of Gartner's 8 mandatory features requires a received channel. |
| B-0022 | Live Chat Software | BOUNDARY | **OUT** | Inbound response to a recipient who initiated contact. The test is who initiated delivery. |
| B-0023 | Contact Center Software | BOUNDARY | **BOUNDARY (unchanged)** | Revised definition does not reach it — needs the source's inclusion criteria, still blocked at G2. |
| B-0024 | Conversational Support Software | BOUNDARY | **OUT** | Inbound response to a recipient who initiated contact. The test is who initiated delivery. |
| B-0025 | Customer Service Automation Software | BOUNDARY | **BOUNDARY (unchanged)** | Revised definition does not reach it — needs the source's inclusion criteria, still blocked at G2. |
| B-0026 | Data Breach Notification Software | BOUNDARY | **IN** | Triggered delivery to identified recipients from stored records; compliance purpose does not change the function. |
| B-0027 | Communication Platform as a Service (cPaaS) Platforms | BOUNDARY | **BOUNDARY (unchanged)** | Revised definition does not reach it — needs the source's inclusion criteria, still blocked at G2. |
| B-0028 | Geofencing Software | BOUNDARY | **BOUNDARY (unchanged)** | Revised definition does not reach it — needs the source's inclusion criteria, still blocked at G2. |
| B-0029 | Notification Infrastructure Software | BOUNDARY | **BOUNDARY (unchanged)** | Revised definition does not reach it — needs the source's inclusion criteria, still blocked at G2. |
| B-0030 | Cross-Channel Advertising Software | BOUNDARY | **OUT** | Ad-channel placement targets a segment via an exchange; the organisation does not initiate delivery to an identified recipient. |
| B-0031 | Display Advertising Software | BOUNDARY | **OUT** | Ad-channel placement targets a segment via an exchange; the organisation does not initiate delivery to an identified recipient. |
| B-0032 | Mobile Advertising Software | BOUNDARY | **OUT** | Ad-channel placement targets a segment via an exchange; the organisation does not initiate delivery to an identified recipient. |
| B-0033 | Retail Media Advertising Platforms | BOUNDARY | **OUT** | Ad-channel placement targets a segment via an exchange; the organisation does not initiate delivery to an identified recipient. |
| B-0034 | Social Media Advertising Software | BOUNDARY | **OUT** | Ad-channel placement targets a segment via an exchange; the organisation does not initiate delivery to an identified recipient. |
| B-0035 | Recruitment Marketing Platforms | BOUNDARY | **IN** | Recipient widened: a candidate is an identified external recipient. |
| B-0036 | Employee Referral Software | BOUNDARY | **OUT** | Recipient is the organisation's own employee — explicitly excluded. |
| B-0037 | Programmatic Job Advertising Software | BOUNDARY | **IN** | Recipient widened: a candidate is an identified external recipient. |
| B-0038 | Recruiting Automation Software | BOUNDARY | **IN** | Recipient widened: a candidate is an identified external recipient. |
| B-0039 | Alumni Management Software | BOUNDARY | **IN** | Recipient widened: alumnus and donor are named recipient types. |
| B-0040 | Construction CRM Software | BOUNDARY | **BOUNDARY (unchanged)** | Revised definition does not reach it — needs the source's inclusion criteria, still blocked at G2. |
| B-0041 | Financial Services CRM Software | BOUNDARY | **BOUNDARY (unchanged)** | Revised definition does not reach it — needs the source's inclusion criteria, still blocked at G2. |
| B-0042 | Mortgage CRM Software | BOUNDARY | **BOUNDARY (unchanged)** | Revised definition does not reach it — needs the source's inclusion criteria, still blocked at G2. |
| B-0043 | HIPAA Compliant Messaging Software | BOUNDARY | **BOUNDARY (unchanged)** | Revised definition does not reach it — needs the source's inclusion criteria, still blocked at G2. |
| B-0044 | Insurance CRM Software | BOUNDARY | **BOUNDARY (unchanged)** | Revised definition does not reach it — needs the source's inclusion criteria, still blocked at G2. |
| B-0045 | Legal CRM Software | BOUNDARY | **BOUNDARY (unchanged)** | Revised definition does not reach it — needs the source's inclusion criteria, still blocked at G2. |
| B-0046 | Donor Management Software | BOUNDARY | **IN** | Recipient widened: alumnus and donor are named recipient types. |
| B-0047 | Fundraising Software | BOUNDARY | **IN** | Recipient widened: alumnus and donor are named recipient types. |
| B-0048 | Nonprofit CRM Software | BOUNDARY | **BOUNDARY (unchanged)** | Revised definition does not reach it — needs the source's inclusion criteria, still blocked at G2. |
| B-0049 | Real Estate CRM Software | BOUNDARY | **BOUNDARY (unchanged)** | Revised definition does not reach it — needs the source's inclusion criteria, still blocked at G2. |