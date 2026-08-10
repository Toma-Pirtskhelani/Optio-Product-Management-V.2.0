# conflicts.md

**When two sources disagree, record BOTH and flag it. Never silently pick one.**

A conflict is not a data-quality problem to be cleaned. It is usually the most informative
thing on the page: two taxonomies disagreeing about a vendor tells you where the category
boundary actually is, and a vendor's domestic and English sites disagreeing tells you how it
presents itself to two different audiences.

Append-only. Governed by `research-protocol.md` §7.

## Columns

| Field | Meaning |
|---|---|
| `conflict_id` | `C-0001`, sequential. Merged rows cite this |
| `date` | ISO date recorded |
| `subject` | Vendor, product, or category the conflict is about |
| `dimension` | What they disagree on: `count` / `price` / `category-placement` / `ownership` / `status` / `product-depth` / `customer-list` / `market-definition` / other |
| `value_a` | Side A's value, verbatim |
| `source_a` | URL + `paste_id` |
| `class_a` | `SELF-DECLARED` / `REVEALED-BEHAVIOR` |
| `grade_a` | Confidence grade of side A |
| `lang_a` | ISO language code |
| `value_b` | Side B's value, verbatim |
| `source_b` | URL + `paste_id` |
| `class_b` | `SELF-DECLARED` / `REVEALED-BEHAVIOR` |
| `grade_b` | Confidence grade of side B |
| `lang_b` | ISO language code |
| `resolution` | `UNRESOLVED — both carried` (default) / `judgment: <which side, why>` / `resolved by <new source>` |
| `effect_on_grade` | Grade the merged row carries as a result |

## Rules

- **Default resolution is `UNRESOLVED — both carried`.** Resolving is the exception and
  requires a stated reason.
- **A conflict resolved by judgment never raises the merged row's grade.** If judgment
  picked a side, the row says judgment picked, and why. Judgment is not a source.
- **Domestic-language vs. English disagreement on the same vendor** — pricing, product
  depth, customer lists — is logged here, not reconciled. Per `CLAUDE.md` §6 the
  domestic-language version is primary and the English version is marketing collateral, but
  both values stay in the row.
- **Two SELF-DECLARED sources agreeing is not corroboration** (`research-protocol.md` §5) —
  and by the same logic, two SELF-DECLARED sources *disagreeing* is a strong signal, because
  their errors are supposed to correlate. Flag those explicitly in `resolution`.
- A conflict about a **category's market definition or inclusion criteria** is logged here
  *and* reflected in `industry-registry.md`, which keeps both raw names rather than merging
  them into one normalized entry.

## Log

| conflict_id | date | subject | dimension | value_a | source_a | class_a | grade_a | lang_a | value_b | source_b | class_b | grade_b | lang_b | resolution | effect_on_grade |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| C-0001 | 2026-08-10 | Shopify English category sitemap — number of categories | count | **216** URLs | `WebFetch` on https://apps.shopify.com/sitemap_categories_en.xml | SELF-DECLARED (transport artefact) | MODELED — a model-generated count, not a read one | en | **161** `<loc>` elements | `curl` + `grep -c` on the identical URL, same day | REVEALED-BEHAVIOR (byte-exact file) | PRIMARY | en | **resolved by byte-exact capture: 161.** The 216 was invented by the summarizing model inside the fetch tool. Same tool also reported tr=246 and es=226; both are 161 | No effect on any published number — caught before use. **Effect on method: every count in this study is now produced by byte-exact capture plus deterministic parsing, never by a model reading a page** |
| C-0002 | 2026-08-10 | Placement of pop-ups, forms, banners and loyalty | category-placement | Shopify files pop-ups/forms/banners under **"Store design"** and loyalty under **"Marketing and conversion"** | https://apps.shopify.com/sitemap_categories_en.xml | SELF-DECLARED | PRIMARY | en | G2 files the equivalent functions under **Marketing Software**, and Loyalty Management under **Demand Generation Software** | https://www.g2.com/categories | SELF-DECLARED | PRIMARY | en | **UNRESOLVED — both carried.** Neither is wrong: Shopify organizes by merchant workflow, G2 by product function. Note both sides are SELF-DECLARED, so their *disagreement* is the informative part | Any merged count across the two is an artefact of this difference, not a market fact |
| C-0003 | 2026-08-10 | Whether a vendor taxonomy can enumerate services firms | market-definition | Amendment 2 (2026-08-10): "taxonomies only classify software", so competitor classes 2–7 are struck | prompts/ + CLAUDE.md §4 | n/a — instruction, not a source | n/a | en | G2 operates 9 service-provider branches with a published rule and 31 in-screen categories incl. "Marketing Automation Consulting Providers", "Email Marketing Services Providers", "Contact Center Outsourcing Service Providers" | https://research.g2.com/methodology/categorization + https://www.g2.com/categories | SELF-DECLARED | PRIMARY | en | **UNRESOLVED — escalated to the user.** Classes 3–4 are partially enumerable at self-declared-supply level; classes 2, 5, 6, 7 remain fully unmeasured. See outputs/source-taxonomies.md §6 | The 31 categories are carried in the tables marked SERVICES and excluded from IN/BOUNDARY counts, so either decision is one edit away |
