# industry-registry.md — the merge key

**This registry starts empty and is built only by evidence.** It is not pre-populated from
anyone's knowledge of the market, including the model's. Pre-populating it would be
prohibition 1 — a brainstormed list mistaken for the universe — committed at the single
point where it would contaminate every downstream table at once.

If you are reading this file looking for the list of industries this study covers, the
answer today is: **78 provisional entries, every one of them created from a category name
read off G2's index rather than from a category definition** — because G2 returns 403 on
every category page. Not one entry rests on a definition yet. See §8.

---

## 1. What this file is for

Sources name the same industry differently. G2, Gartner, and a marketplace will describe one
economic activity with three different strings, at three different levels of granularity,
under three different theories of what a category is. Merging on the string produces
nonsense. Merging on a normalized key produces a study.

So every pass records **both**:

- **`raw_name`** — the category name **exactly as its source states it**, character for
  character, in the source's own language and capitalization. Never cleaned, never
  translated in place, never singular/plural-normalized.
- **`normalized_name`** — a key drawn from this registry.

`raw_name` is evidence. `normalized_name` is a decision. Keeping them in separate columns is
what makes the decision reversible when a later pass proves it wrong.

---

## 2. The append rule

**A pass meeting a category with no registry match appends a new entry with its alias list.
It does not force a bad match.**

Forcing a near-match is the single most damaging thing that can happen in this repository,
because it is invisible afterward: two genuinely different market definitions collapse into
one row, the disagreement between the taxonomies disappears, and the resulting count looks
more solid than either source alone. A forced match manufactures corroboration.

When in doubt, **append**. Two registry entries later found to be the same thing are trivial
to merge, and the merge is recorded. One entry that was secretly two is undetectable.

---

## 3. Entry format

Every registry entry is a block in this shape. Nothing in it is optional; missing values are
written `UNKNOWN`.

```
### <normalized_name>

- registry_id:        R-0001
- normalized_name:    <the merge key — a name this study assigns, stable forever once assigned>
- status:             ACTIVE | RETIRED-BY-SOURCE | TRANSITIONING | MERGED-INTO <registry_id> | PROVISIONAL
- first_seen:         <ISO date> via <source> <url> (paste_id if human-transported)
- definition_basis:   <which source's definition this key was created from — and the fact
                       that this key is OUR construct, not that source's property>
- scope_verdict:      IN | OUT | BOUNDARY-IN | BOUNDARY-OUT | UNRULED  (ruling_id in logs/boundary-rulings.md)

- aliases:
  | raw_name (verbatim) | source | source_url | language | date_seen | paste_id | granularity | notes |
  |---|---|---|---|---|---|---|---|

- inclusion_criteria:
  | source | criteria_verbatim | source_url | date | grade |
  |---|---|---|---|---|
  <the source's OWN inclusion criteria or mandatory-feature list, quoted, per source.
   UNKNOWN where unpublished — and see §5.>

- source_boundary_notes: <where a source's stated boundary differs from this study's
                          functional definition, quoted verbatim. Never normalized away.
                          Cross-reference conflict_id.>

- decline_markers:
  | marker | applied_by | value_verbatim | date_seen | source_url | grade |
  |---|---|---|---|---|---|
  <(Retired) / (Transitioning to X) as stated by the source. See §6.>

- merge_history: <appends, splits, merges — each with date and reason. Append-only.>
```

---

## 4. Naming rules for `normalized_name`

1. **English is a working convention here, not a claim.** The key is an internal identifier;
   it does not assert that the English name is the real one. `raw_name` in the source's own
   language remains the evidence, and per `CLAUDE.md` §6 the domestic-language name is
   primary wherever a vendor or market has one.
2. **Never invent a name more general than the evidence supports.** If one source says
   *"Retail — Grocery"* and another says *"Retail"*, those are two entries with a recorded
   relationship, not one entry. Granularity differences are recorded in the `granularity`
   column, never flattened.
3. **A key is stable once assigned.** Renaming breaks every table that cites it. To change a
   name, append a new entry and mark the old `MERGED-INTO`.
4. **A key is never created from model memory** — only from a `raw_name` that appeared in a
   fetched or pasted source. If you find yourself typing an industry name you did not read
   somewhere, stop: that is prohibition 1.

---

## 5. Inclusion criteria are part of the key

Recorded per source, per category, **verbatim**. Not paraphrased — the wording is the thing.

Categories differ enormously in how hard they are to enter. A category requiring six
mandatory features and a category requiring one are not comparable, and their product counts
are not comparable either. **Raw counts across categories must never be presented as if they
were.**

Where a source does not publish inclusion criteria, record `UNKNOWN` and treat that
category's count as **non-comparable to any other, including to itself over time** — an
unpublished criterion can change silently between captures.

This is also why `CLAUDE.md` §7 makes the **category cluster** the unit of analysis: a single
vendor may occupy many categories at once, and how many depends on the taxonomy's rules
rather than on the vendor.

---

## 6. Retired categories stay

A category marked `(Retired)` by its source is **kept**, with `status: RETIRED-BY-SOURCE` and
the marker recorded verbatim.

Deleting retired categories would rebuild survivorship bias inside the merge key itself —
the exact failure this study exists to avoid, planted at the root where every table inherits
it. A retired category is a **market that failed or dissolved**, and per
`research-protocol.md` §6 that is a stronger signal than any single dead company.

`(Transitioning to X)` gets `status: TRANSITIONING`, with **both** the source and target
names recorded as aliases. The taxonomy moving is itself a finding about the market.

---

## 7. Registry hygiene

- **Append-only.** Entries are added, merged, or marked; never deleted, never silently
  edited. Every change carries a date and a reason in `merge_history`.
- **Every entry traces to a URL and a date.** An entry with no source is a mistake to be
  investigated, not tidied away.
- **`PROVISIONAL`** marks an entry created from a single ambiguous sighting. Provisional
  entries may not anchor a finding until confirmed by a second capture.
- **A registry entry is not a claim that the industry matters.** It is a claim that a source
  named it. Whether it matters is decided in the outputs, on evidence, blind to the client.

---

## 8. Registry

### Pass 01 — 78 provisional entries

Appended from the first taxonomy pass. **Every entry is `PROVISIONAL`**: it was created from
a category *name* read off G2's index, not from a category *definition*, because G2 returns
403 on every category page. Per §7, a provisional entry may not anchor a finding until
confirmed by a second capture.

`normalized_name` is currently set to G2's `raw_name` verbatim for each entry, and `alias_count`
is 1, because **no second taxonomy has yet been read at category-definition level** — there is
nothing to merge against. Alias lists become real when Gartner's markets index and the
marketplace listing requirements arrive; that is when normalization stops being a rename and
starts being a decision.

Shopify and HubSpot categories are deliberately **not** appended yet. Their names
("Email marketing", "sms") would collide with G2's on the string while denoting different
objects — a Shopify category is a merchant workflow slot, a HubSpot category is an
integration bucket. Appending them now is exactly the forced match §2 forbids.

| registry_id | normalized_name | status | alias_count | scope_verdict | first_seen |
|---|---|---|---|---|---|
| R-0001 | AI Marketing Agents Software | PROVISIONAL | 1 | IN | 2026-08-10 via g2 https://www.g2.com/categories/ai-marketing-agents |
| R-0002 | Conversational Interface Agents Software | PROVISIONAL | 1 | BOUNDARY | 2026-08-10 via g2 https://www.g2.com/categories/conversational-interface-agents |
| R-0003 | Bot Platforms | PROVISIONAL | 1 | BOUNDARY | 2026-08-10 via g2 https://www.g2.com/categories/bot-platforms |
| R-0004 | Chatbots Software | PROVISIONAL | 1 | BOUNDARY | 2026-08-10 via g2 https://www.g2.com/categories/chatbots |
| R-0005 | Enterprise AI Chatbots Software | PROVISIONAL | 1 | BOUNDARY | 2026-08-10 via g2 https://www.g2.com/categories/enterprise-ai-chatbots |
| R-0006 | AI Chatbots Software | PROVISIONAL | 1 | BOUNDARY | 2026-08-10 via g2 https://www.g2.com/categories/ai-chatbots |
| R-0007 | CRM Software | PROVISIONAL | 1 | BOUNDARY | 2026-08-10 via g2 https://www.g2.com/categories/crm |
| R-0008 | Through-Channel Marketing Software | PROVISIONAL | 1 | IN | 2026-08-10 via g2 https://www.g2.com/categories/through-channel-marketing |
| R-0009 | Sales Engagement Software | PROVISIONAL | 1 | IN | 2026-08-10 via g2 https://www.g2.com/categories/sales-engagement |
| R-0010 | Account-Based Marketing Software | PROVISIONAL | 1 | IN | 2026-08-10 via g2 https://www.g2.com/categories/account-based-marketing |
| R-0011 | Account-Based Advertising Software | PROVISIONAL | 1 | BOUNDARY | 2026-08-10 via g2 https://www.g2.com/categories/account-based-advertising |
| R-0012 | Account-Based Direct Mail Software | PROVISIONAL | 1 | IN | 2026-08-10 via g2 https://www.g2.com/categories/account-based-direct-mail |
| R-0013 | Book Marketing Tools | PROVISIONAL | 1 | BOUNDARY | 2026-08-10 via g2 https://www.g2.com/categories/book-marketing-tools |
| R-0014 | Conversational Marketing Software | PROVISIONAL | 1 | IN | 2026-08-10 via g2 https://www.g2.com/categories/conversational-marketing |
| R-0015 | Customer Data Platforms (CDP) | PROVISIONAL | 1 | BOUNDARY | 2026-08-10 via g2 https://www.g2.com/categories/customer-data-platform-cdp |
| R-0016 | Loyalty Management Software | PROVISIONAL | 1 | BOUNDARY | 2026-08-10 via g2 https://www.g2.com/categories/loyalty-management |
| R-0017 | Direct Mail Automation Software | PROVISIONAL | 1 | IN | 2026-08-10 via g2 https://www.g2.com/categories/direct-mail-automation |
| R-0018 | Email Marketing Software | PROVISIONAL | 1 | IN | 2026-08-10 via g2 https://www.g2.com/categories/email-marketing |
| R-0019 | Event Marketing Software | PROVISIONAL | 1 | BOUNDARY | 2026-08-10 via g2 https://www.g2.com/categories/event-marketing |
| R-0020 | Local Marketing Software | PROVISIONAL | 1 | BOUNDARY | 2026-08-10 via g2 https://www.g2.com/categories/local-marketing |
| R-0021 | Location-Based Marketing Software | PROVISIONAL | 1 | IN | 2026-08-10 via g2 https://www.g2.com/categories/location-based-marketing |
| R-0022 | Marketing Automation Software | PROVISIONAL | 1 | IN | 2026-08-10 via g2 https://www.g2.com/categories/marketing-automation |
| R-0023 | Mobile Marketing Software | PROVISIONAL | 1 | IN | 2026-08-10 via g2 https://www.g2.com/categories/mobile-marketing |
| R-0024 | Multi-Location Marketing Platforms | PROVISIONAL | 1 | BOUNDARY | 2026-08-10 via g2 https://www.g2.com/categories/multi-location-marketing-platforms |
| R-0025 | Other Marketing Software | PROVISIONAL | 1 | BOUNDARY | 2026-08-10 via g2 https://www.g2.com/categories/other-marketing |
| R-0026 | Personalization Software | PROVISIONAL | 1 | BOUNDARY | 2026-08-10 via g2 https://www.g2.com/categories/personalization |
| R-0027 | Personalization Engines | PROVISIONAL | 1 | BOUNDARY | 2026-08-10 via g2 https://www.g2.com/categories/personalization-engines |
| R-0028 | Push Notification Software | PROVISIONAL | 1 | IN | 2026-08-10 via g2 https://www.g2.com/categories/push-notification |
| R-0029 | RCS Business Messaging Software | PROVISIONAL | 1 | BOUNDARY | 2026-08-10 via g2 https://www.g2.com/categories/rcs-business-messaging |
| R-0030 | SMS Marketing Software | PROVISIONAL | 1 | IN | 2026-08-10 via g2 https://www.g2.com/categories/sms-marketing |
| R-0031 | Social Media Marketing Software | PROVISIONAL | 1 | BOUNDARY | 2026-08-10 via g2 https://www.g2.com/categories/social-media-marketing |
| R-0032 | Transactional Email Software | PROVISIONAL | 1 | BOUNDARY | 2026-08-10 via g2 https://www.g2.com/categories/transactional-email |
| R-0033 | WhatsApp Marketing Software | PROVISIONAL | 1 | IN | 2026-08-10 via g2 https://www.g2.com/categories/whatsapp-marketing |
| R-0034 | Merchant Marketing Software | PROVISIONAL | 1 | BOUNDARY | 2026-08-10 via g2 https://www.g2.com/categories/merchant-marketing |
| R-0035 | Conversational Commerce Platforms | PROVISIONAL | 1 | IN | 2026-08-10 via g2 https://www.g2.com/categories/conversational-commerce-platforms |
| R-0036 | E-Commerce Personalization Software | PROVISIONAL | 1 | BOUNDARY | 2026-08-10 via g2 https://www.g2.com/categories/e-commerce-personalization |
| R-0037 | Live Chat Software | PROVISIONAL | 1 | BOUNDARY | 2026-08-10 via g2 https://www.g2.com/categories/live-chat |
| R-0038 | Appointment Reminder Software | PROVISIONAL | 1 | IN | 2026-08-10 via g2 https://www.g2.com/categories/appointment-reminder |
| R-0039 | Contact Center Software | PROVISIONAL | 1 | BOUNDARY | 2026-08-10 via g2 https://www.g2.com/categories/contact-center |
| R-0040 | Conversational Support Software | PROVISIONAL | 1 | BOUNDARY | 2026-08-10 via g2 https://www.g2.com/categories/conversational-support |
| R-0041 | Customer Communications Management Software | PROVISIONAL | 1 | IN | 2026-08-10 via g2 https://www.g2.com/categories/customer-communications-management |
| R-0042 | Customer Service Automation Software | PROVISIONAL | 1 | BOUNDARY | 2026-08-10 via g2 https://www.g2.com/categories/customer-service-automation |
| R-0043 | Proactive Customer Retention Software | PROVISIONAL | 1 | IN | 2026-08-10 via g2 https://www.g2.com/categories/proactive-customer-retention |
| R-0044 | Proactive Notification Software | PROVISIONAL | 1 | IN | 2026-08-10 via g2 https://www.g2.com/categories/proactive-notification |
| R-0045 | Data Breach Notification Software | PROVISIONAL | 1 | BOUNDARY | 2026-08-10 via g2 https://www.g2.com/categories/data-breach-notification |
| R-0046 | Communication Platform as a Service (cPaaS) Platforms | PROVISIONAL | 1 | BOUNDARY | 2026-08-10 via g2 https://www.g2.com/categories/communication-platform-as-a-service-cpaas |
| R-0047 | Geofencing Software | PROVISIONAL | 1 | BOUNDARY | 2026-08-10 via g2 https://www.g2.com/categories/geofencing |
| R-0048 | Notification Infrastructure Software | PROVISIONAL | 1 | BOUNDARY | 2026-08-10 via g2 https://www.g2.com/categories/notification-infrastructure |
| R-0049 | Cross-Channel Advertising Software | PROVISIONAL | 1 | BOUNDARY | 2026-08-10 via g2 https://www.g2.com/categories/cross-channel-advertising |
| R-0050 | Display Advertising Software | PROVISIONAL | 1 | BOUNDARY | 2026-08-10 via g2 https://www.g2.com/categories/display-advertising |
| R-0051 | Mobile Advertising Software | PROVISIONAL | 1 | BOUNDARY | 2026-08-10 via g2 https://www.g2.com/categories/mobile-advertising |
| R-0052 | Retail Media Advertising Platforms | PROVISIONAL | 1 | BOUNDARY | 2026-08-10 via g2 https://www.g2.com/categories/retail-media-advertising-platforms |
| R-0053 | Social Media Advertising Software | PROVISIONAL | 1 | BOUNDARY | 2026-08-10 via g2 https://www.g2.com/categories/social-media-advertising |
| R-0054 | Recruitment Marketing Platforms | PROVISIONAL | 1 | BOUNDARY | 2026-08-10 via g2 https://www.g2.com/categories/recruitment-marketing |
| R-0055 | Employee Referral Software | PROVISIONAL | 1 | BOUNDARY | 2026-08-10 via g2 https://www.g2.com/categories/employee-referral |
| R-0056 | Programmatic Job Advertising Software | PROVISIONAL | 1 | BOUNDARY | 2026-08-10 via g2 https://www.g2.com/categories/programmatic-job-advertising |
| R-0057 | Recruiting Automation Software | PROVISIONAL | 1 | BOUNDARY | 2026-08-10 via g2 https://www.g2.com/categories/recruiting-automation |
| R-0058 | Emergency Notification Software | PROVISIONAL | 1 | IN | 2026-08-10 via g2 https://www.g2.com/categories/emergency-notification |
| R-0059 | Alumni Management Software | PROVISIONAL | 1 | BOUNDARY | 2026-08-10 via g2 https://www.g2.com/categories/alumni-management |
| R-0060 | Automotive Marketing Software | PROVISIONAL | 1 | IN | 2026-08-10 via g2 https://www.g2.com/categories/automotive-marketing |
| R-0061 | Construction CRM Software | PROVISIONAL | 1 | BOUNDARY | 2026-08-10 via g2 https://www.g2.com/categories/construction-crm |
| R-0062 | Classroom Messaging Software | PROVISIONAL | 1 | IN | 2026-08-10 via g2 https://www.g2.com/categories/classroom-messaging |
| R-0063 | Financial Services CRM Software | PROVISIONAL | 1 | BOUNDARY | 2026-08-10 via g2 https://www.g2.com/categories/financial-services-crm |
| R-0064 | Mortgage CRM Software | PROVISIONAL | 1 | BOUNDARY | 2026-08-10 via g2 https://www.g2.com/categories/mortgage-crm |
| R-0065 | AI Patient Engagement & Operations Software | PROVISIONAL | 1 | IN | 2026-08-10 via g2 https://www.g2.com/categories/ai-patient-engagement-operations |
| R-0066 | HIPAA Compliant Messaging Software | PROVISIONAL | 1 | BOUNDARY | 2026-08-10 via g2 https://www.g2.com/categories/hipaa-compliant-messaging |
| R-0067 | Patient Engagement Software | PROVISIONAL | 1 | IN | 2026-08-10 via g2 https://www.g2.com/categories/patient-engagement |
| R-0068 | Guest Messaging Software | PROVISIONAL | 1 | IN | 2026-08-10 via g2 https://www.g2.com/categories/guest-messaging |
| R-0069 | Restaurant Marketing Tools Software | PROVISIONAL | 1 | IN | 2026-08-10 via g2 https://www.g2.com/categories/restaurant-marketing-tools |
| R-0070 | Insurance CRM Software | PROVISIONAL | 1 | BOUNDARY | 2026-08-10 via g2 https://www.g2.com/categories/insurance-crm |
| R-0071 | Legal CRM Software | PROVISIONAL | 1 | BOUNDARY | 2026-08-10 via g2 https://www.g2.com/categories/legal-crm |
| R-0072 | Donor Management Software | PROVISIONAL | 1 | BOUNDARY | 2026-08-10 via g2 https://www.g2.com/categories/donor-management |
| R-0073 | Fundraising Software | PROVISIONAL | 1 | BOUNDARY | 2026-08-10 via g2 https://www.g2.com/categories/fundraising |
| R-0074 | Nonprofit CRM Software | PROVISIONAL | 1 | BOUNDARY | 2026-08-10 via g2 https://www.g2.com/categories/nonprofit-crm |
| R-0075 | Political Campaign Software | PROVISIONAL | 1 | IN | 2026-08-10 via g2 https://www.g2.com/categories/political-campaign |
| R-0076 | Citizen Engagement Software | PROVISIONAL | 1 | IN | 2026-08-10 via g2 https://www.g2.com/categories/citizen-engagement |
| R-0077 | Real Estate CRM Software | PROVISIONAL | 1 | BOUNDARY | 2026-08-10 via g2 https://www.g2.com/categories/real-estate-crm |
| R-0078 | Real Estate Marketing Software | PROVISIONAL | 1 | IN | 2026-08-10 via g2 https://www.g2.com/categories/real-estate-marketing |

### Pass 02 — 7 Gartner entries, the first backed by definitions

**These are the first registry entries in this study that rest on a source's own definition and
mandatory-feature list rather than on a category name.** They are `ACTIVE`, not `PROVISIONAL`.

`Email Marketing (Transitioning to Email Marketing Platforms)` carries **both** names as
aliases of one entry, per §6 — the source name and the target name. A count captured before the
transition is not comparable to one captured after.

`Multichannel Marketing Hubs` is registered as its **own entry with no G2 alias**, because no
equivalent name exists in G2's 2,235 categories (`C-0006`). Per §2, append rather than
force-match: inventing a G2 counterpart for it would manufacture corroboration.

| registry_id | normalized_name | status | alias_count | scope_verdict | first_seen |
|---|---|---|---|---|---|
| R-0079 | B2B Marketing Automation Platforms | ACTIVE | 1 | IN | 2026-08-10 via gartner peer-insights MARKET, bar 5, 59 products (P-0016) |
| R-0080 | Customer Data Platforms | ACTIVE | 1 | OUT | 2026-08-10 via gartner peer-insights MARKET, bar 4, 71 products (P-0017) |
| R-0081 | Email Marketing (Transitioning to Email Marketing Platforms) | TRANSITIONING | 1 | IN | 2026-08-10 via gartner peer-insights MARKET, bar 4, 100 products (P-0018) |
| R-0082 | Location Based Marketing Software | ACTIVE | 1 | IN | 2026-08-10 via gartner peer-insights CATEGORY, bar none, 15 products (P-0019) |
| R-0083 | Mobile Marketing Platforms | ACTIVE | 1 | IN | 2026-08-10 via gartner peer-insights MARKET, bar 3, 45 products (P-0020) |
| R-0084 | Multichannel Marketing Hubs | ACTIVE | 1 | IN | 2026-08-10 via gartner peer-insights MARKET, bar 6, 122 products (P-0021) |
| R-0085 | Personalization Engines | ACTIVE | 1 | OUT | 2026-08-10 via gartner peer-insights MARKET, bar 8, 64 products (P-0022) |
