# Capture index — sources/raw/

Native-format captures keep their original bytes (`.html`, `.xml`) so nothing is
reformatted; the required header block for each lives here rather than inside the file,
because prepending a header to an HTML or XML capture would alter the evidence.

Every capture below was obtained by direct HTTP GET with no user-agent spoofing. Where a
source returned 403 to that request, it was **not** worked around — it was escalated to
Rung 3 (human transport). See `logs/fetch-log.md`.

---

## 2026-08-10__g2__categories-index__r1.html
```
url:            https://www.g2.com/categories
source:         g2
capture_date:   2026-08-10
rung:           1
transport:      fetch (curl, default user-agent)
paste_id:       —
source_class:   SELF-DECLARED
language:       en
visible_count:  2235 category rows / 38 branch tables
total_count:    UNKNOWN — G2 declares no total on this page
pagination:     none — the full taxonomy is present in one document
sort_order:     alphabetical within branch
filters_active: none (page offers All / Software / Services filters; capture is "All")
notes:          Nested child categories are present in the HTML but rendered collapsed
                behind "Expand/Collapse" controls. They ARE in the capture, so the
                enumeration is complete despite not being visible in a browser at once.
```

## 2026-08-10__g2__methodology-categorization__r2.html
```
url:            https://research.g2.com/methodology/categorization
source:         g2
capture_date:   2026-08-10
rung:           2  (alternate subdomain — research.g2.com is open while www.g2.com
                    category pages return 403; the exact Rung-2 pattern the protocol predicts)
transport:      fetch (curl, default user-agent)
paste_id:       —
source_class:   SELF-DECLARED
language:       en
visible_count:  n/a — prose document
total_count:    n/a
pagination:     none
sort_order:     n/a
filters_active: none
notes:          Carries a dated change log ending "7/9/25 - Made updates throughout,
                including adding details on individual software products and removing
                product suites section."
```

## 2026-08-10__shopify__sitemap-categories-en__r2.xml
```
url:            https://apps.shopify.com/sitemap_categories_en.xml
source:         shopify-app-store
capture_date:   2026-08-10
rung:           2  (sitemap — the category index page itself is a curated landing page
                    that does not enumerate the taxonomy)
transport:      fetch (curl, default user-agent)
paste_id:       —
source_class:   SELF-DECLARED
language:       en
visible_count:  161 <loc> entries
total_count:    161 — the sitemap IS the enumeration, so this is ABSENT-ENUMERATED-capable
pagination:     none
sort_order:     sitemap order (roughly by depth, then unspecified)
filters_active: none
notes:          Sitemap index at /sitemap.xml lists per-language category sitemaps for 23
                locales. lastmod on all: 2026-08-10.
```

## 2026-08-10__shopify__sitemap-categories-tr__r2.xml / __es__r2.xml
```
url:            https://apps.shopify.com/sitemap_categories_tr.xml
                https://apps.shopify.com/sitemap_categories_es.xml
source:         shopify-app-store
capture_date:   2026-08-10
rung:           2
transport:      fetch (curl, default user-agent)
paste_id:       —
source_class:   SELF-DECLARED
language:       tr / es
visible_count:  161 each
total_count:    161 each
pagination:     none
sort_order:     sitemap order
filters_active: none
notes:          Identical count to en, and identical English slugs with ?locale= appended.
                The taxonomy is not localized at the slug level. Whether the DISPLAYED
                category names are translated is NOT established by this capture and is
                UNKNOWN — it requires fetching a localized category page.
```

## 2026-08-10__hubspot__sitemap-apps-categories-en__r2.xml
```
url:            https://ecosystem.hubspot.com/marketplace-en-apps-categories-1.xml
source:         hubspot-ecosystem
capture_date:   2026-08-10
rung:           2  (sitemap, discovered via ecosystem.hubspot.com/robots.txt)
transport:      fetch (curl, default user-agent)
paste_id:       —
source_class:   SELF-DECLARED
language:       en
visible_count:  112 <loc> entries → 60 distinct categories once /page/N URLs are collapsed
total_count:    60 categories
pagination:     the sitemap itself exposes per-category pagination depth (/page/1../page/N),
                which is a usable proxy for relative category size
sort_order:     reverse alphabetical
filters_active: none
notes:          Category PAGES are JavaScript-rendered — every category URL returns an
                identical 53,230-byte shell with no app content. The sitemap is therefore
                the only non-JS route to the taxonomy, and per-category detail requires
                Rung 3.
```
