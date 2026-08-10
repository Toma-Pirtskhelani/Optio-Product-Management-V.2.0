# schemas/app-marketplaces.md — marketplace pass output columns

Populates the spine in `schemas/merged-table.md`. Every spine field is mandatory here.

**Weighting, stated before the columns because it governs how the columns are read:** per
`CLAUDE.md` §7.2, the review/analyst sources carry this study. **Marketplaces are cheap
supplementary signal, not equal partners.** They are e-commerce- and SMB-shaped by
construction, and they will systematically under-represent vendors selling into banking,
insurance, telecom, and other non-e-commerce enterprise verticals. A marketplace count must
never drive a conclusion about an enterprise vertical, and a marketplace's silence about a
vertical is evidence about the marketplace.

---

## 1. The marketplace roster is itself evidence — and is NOT pre-populated

**Which marketplaces this study consults is a research finding, not a starting assumption.**

Listing marketplaces from model memory is prohibition 1 applied to sources instead of
industries — a brainstormed list treated as the universe, with the same availability bias and
the same Anglophone skew, one level further upstream where it is harder to see.

So: **the roster is built by a documented pass and recorded in the table below**, one row per
marketplace, each with the source that put it there. Any marketplace named without a fetched
or pasted source is a **candidate**, not a source, and may not contribute rows.

**Selection criteria for a marketplace to enter the roster:**

| Criterion | Requirement |
|---|---|
| Host platform is identified | The commerce/ERP/CRM/POS platform whose apps it lists, per its own pages |
| Directory is public | App listings reachable without a paid account |
| Categories are published | The marketplace states its own category names |
| Listing requirements are published | Its inclusion criteria — or `UNKNOWN`, which makes its counts non-comparable |
| Discovered by evidence | Arrived via a fetched/pasted source, with URL and date logged |

**Language obligation applies to the roster itself, not only to its contents.** A roster of
only Anglophone-platform marketplaces reports an Anglophone market as the world market and
cannot detect its own error (`CLAUDE.md` §6). The roster pass must actively seek marketplaces
whose host platforms are domestic to Russian-, Turkish-, Mandarin-, Spanish-, Portuguese-, and
Georgian-language markets, and **record explicitly which of those languages it failed to
cover, and what it tried.** "None found" is only acceptable with the search path documented.

### Roster

| marketplace_id | marketplace_name_raw | host_platform | root_url | discovered_via | discovery_date | language(s) | listing_requirements_url | in_roster |
|---|---|---|---|---|---|---|---|---|
| _(empty — the roster is built by evidence, per §1)_ | | | | | | | | |

---

## 2. Marketplace-level rows

One row per marketplace. `entity_type: category` at the platform level.

| Field | Notes |
|---|---|
| `marketplace_name_raw` | Verbatim |
| `host_platform` | The platform whose apps these are — determines the whole shape of the sample |
| `listing_requirements_verbatim` | **The marketplace's own inclusion/review requirements, quoted in full.** This is its inclusion-criteria equivalent. `UNKNOWN` makes its counts non-comparable to any other marketplace |
| `review_process_verbatim` | Whether listings are human-reviewed, auto-approved, or paid-for, quoted |
| `total_apps_declared` + `_grade` | The platform's stated total |
| `category_list_raw` | **The marketplace's own category names, verbatim** — each appended to `industry-registry.md` |
| `capture_date`, `source_url`, `rung`, `source_class`, `source_language`, `paste_id`, `raw_file` | Spine |

**Low listing requirements mean a high app count means very little.** A marketplace that
auto-approves and a marketplace that human-reviews produce numbers that must never be
compared. This is `industry-registry.md` §5 applied at platform level.

---

## 3. Category rows within a marketplace

| Field | Notes |
|---|---|
| `raw_name` | **The marketplace's category name exactly as printed**, in its own language |
| `raw_name_translation` | Working translation **in a separate column** — never replacing `raw_name` |
| `normalized_name` / `registry_id` | From the registry. Append, never force-match. Marketplace categories are usually shallower than analyst categories; that granularity difference is recorded, not flattened |
| `app_count_declared` + `_grade` | As stated |
| `app_count_visible` | As captured |
| `pagination`, `sort_order`, `filters_active` | Sampling metadata. Marketplace default sorts are usually popularity- or promotion-weighted — record which |
| `scope_verdict` / `ruling_id` | Ruled explicitly. Marketplace categories mix scope freely; expect boundary rulings |
| `taxonomy_id` | `<marketplace_id>` — **its own taxonomy.** Counts never cross taxonomies |

---

## 4. App rows

One row per app **per category**.

| Field | Notes |
|---|---|
| `entity_name_raw` | App name exactly as printed, original language |
| `developer_name_raw` | Publisher as printed |
| `entity_name_canonical` | This study's key — **the same key as the vendor's G2/Gartner row where they are the same entity**, so the coverage matrix works |
| `app_url` | Exact URL |
| `entity_type` | `product` |
| `competitor_class` | Usually `1`; **class `6` (assembled substitutes) is common here** — connector apps, spreadsheet bridges, no-code glue. Classify honestly rather than defaulting to `1` |
| `install_count` / `merchant_count` + `_grade` | Where published |
| `review_count` + `_grade` | Where published |
| `rating` + `_grade` | Where published |
| `pricing_verbatim` | Full pricing block quoted, incl. currency, free tier, trial |
| `launch_date` / `last_updated` | Where published — `last_updated` is one of the few decay signals a marketplace gives |
| `languages_supported_stated` | Verbatim |
| `position_in_list`, `promoted` | **Marketplace placement is frequently paid.** `promoted: UNKNOWN` is not acceptable where the page marks ads |
| `categories_listed_raw` / `cluster_size` | Within this marketplace's taxonomy only |
| `entity_status` | `active` / `delisted` / `UNKNOWN` — `delisted` only from a two-capture comparison (§6) |
| Spine provenance + coverage | Full set |

---

## 5. Source class — and the one place marketplaces beat the analyst sources

- **Listing existence, category placement, pricing, promoted position: `SELF-DECLARED`.** The
  app is there because someone published it.
- **`install_count` / `merchant_count`: `REVEALED-BEHAVIOR`** where the platform publishes it
  from its own telemetry rather than from a developer-supplied claim. **Verify which**, per
  marketplace, from the marketplace's own documentation, and record the basis. A
  developer-entered "10,000+ merchants" is `SELF-DECLARED`; a platform-computed install count
  is `REVEALED-BEHAVIOR`.

**This matters more than anything else in this file.** A platform-computed install count is
one of the **very few `REVEALED-BEHAVIOR` signals available to this study**, and therefore one
of the few things that can push a row to `corroborated: yes` against a `SELF-DECLARED` G2 or
Gartner row (`merged-table.md` §5). Establish the basis per marketplace before using it, and
record the basis in the roster.

Where the basis is `UNKNOWN`, the count is `SELF-DECLARED` and corroborates nothing.

---

## 6. Failure sampling in a marketplace pass

Marketplaces publish **no decline markers** — they simply remove apps. The signals available,
all requiring **two dated captures of the same URL** in `sources/raw/`:

- app present in an earlier capture, absent in a later one → `entity_status: delisted`, but
  **only** after ruling out pagination (`ABSENT-IN-VISIBLE-PAGE` is not disappearance);
- `last_updated` long stale relative to the marketplace's own cohort — a decay signal, graded
  `SINGLE-SOURCE`, never called abandonment without a second signal;
- category `app_count_declared` falling materially between captures;
- listings marked deprecated/unsupported by the marketplace or the developer.

**One capture establishes nothing about disappearance.** A single capture plus a recollection
of how it used to be is model memory, which is not a source.

---

## 7. Reject conditions (in addition to `merged-table.md` §7)

1. A marketplace contributing rows without a roster entry recording how it was discovered.
2. `raw_name` translated in place instead of into `raw_name_translation`.
3. `install_count` treated as `REVEALED-BEHAVIOR` without the basis established and recorded.
4. `promoted` blank where the page visibly marks paid placement.
5. Marketplace counts compared to G2 or Gartner counts, or across marketplaces, as if they
   measured the same thing.
6. A conclusion about a non-e-commerce enterprise vertical resting on marketplace evidence.
7. A roster pass that covered no non-English-language marketplace and did not state what it
   tried.
