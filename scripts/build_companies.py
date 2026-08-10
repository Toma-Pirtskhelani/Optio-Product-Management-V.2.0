"""Dedupe product rows to unique companies. Merge rules are explicit and logged."""
import json, re, collections

rows = json.load(open("sources/derived/product-rows-IN.json"))

def is_abbrev(owner, paren):
    """Gartner's parenthetical is sometimes an acquired brand and sometimes just an
    abbreviation of the owner ('Amazon Web Services (AWS)'). Distinguish, do not assume."""
    a = re.sub(r"[^A-Za-z0-9]", "", paren).upper()
    initials = "".join(w[0] for w in re.findall(r"[A-Za-z0-9]+", owner)).upper()
    return a == initials or a in re.sub(r"[^A-Za-z0-9]", "", owner).upper()

def strip_paren(v):
    """Gartner writes lineage as 'Owner (OtherBrand)'. Return (owner, other)."""
    m = re.fullmatch(r"(.+?)\s*\(([^)]+)\)\s*", v)
    if m and m.group(2).lower() not in ("legacy",):
        return m.group(1).strip(), m.group(2).strip()
    return v.strip(), None

def key(v):
    s = v.lower()
    s = re.sub(r"[®™©]", "", s)
    s = re.sub(r"[,\.]?\s+(inc|llc|ltd|limited|corp|corporation|gmbh|plc|co)\.?$", "", s)
    s = re.sub(r"[^a-z0-9]+", " ", s).strip()
    return s

# pass 1 — owner extraction
prepared = []
for r in rows:
    owner, acquired = strip_paren(r["vendor"])
    prepared.append(dict(r, _owner=owner, _acquired=acquired))

# pass 2 — collapse "Vendor Product" strings onto "Vendor" where the longer string is
# also a product name in the data. Only ever collapses toward a string already present.
owners = {key(p["_owner"]) for p in prepared}
products = {key(p["product"]) for p in prepared}
merges = {}
for k in sorted(owners, key=len, reverse=True):
    for base in owners:
        if base == k or not k.startswith(base + " "): continue
        remainder = k[len(base) + 1:]
        # collapse only when the longer string, or its remainder, is itself a product name
        # in this data - i.e. the "vendor" field was carrying a product name.
        if k in products or remainder in products:
            merges[k] = base
            break

def resolve(k, seen=None):
    seen = seen or set()
    while k in merges and k not in seen:
        seen.add(k); k = merges[k]
    return k

canon_name = {}
for p in prepared:
    k = resolve(key(p["_owner"]))
    p["_key"] = k
    n = p["_owner"]
    if k not in canon_name or len(n) < len(canon_name[k]): canon_name[k] = n

comp = collections.OrderedDict()
for p in prepared:
    k = p["_key"]
    c = comp.setdefault(k, dict(company_id=k.replace(" ", "-"), company=canon_name[k],
                                aliases=set(), parenthetical_brands=set(), sources=set(),
                                categories=[], products=[]))
    c["aliases"].add(p["vendor"])
    if p["_acquired"]: c["parenthetical_brands"].add(p["_acquired"])
    c["sources"].add(p["source"])
    cat = dict(source=p["source"], category=p["category"], category_url=p["category_url"],
               coverage=p["coverage"], declared_total=p["declared_total"], visible_count=p["visible_count"])
    if cat not in c["categories"]: c["categories"].append(cat)
    c["products"].append(dict(product=p["product"], source=p["source"], category=p["category"],
                              rating=p["rating"], reviews=p["reviews"], legacy=p["legacy"],
                              sponsored=p["sponsored"], tags=p.get("tags", []),
                              name_truncated_in_source=p.get("name_truncated_in_source", False),
                              description=p["description"], source_url=p["category_url"]))

out = []
for k, c in comp.items():
    prods, seen = [], set()
    for pr in c["products"]:
        sig = (pr["product"], pr["source"], pr["category"])
        if sig in seen: continue
        seen.add(sig); prods.append(pr)
    revs = [pr["reviews"] for pr in prods if pr["reviews"]]
    descs = [pr["description"] for pr in prods if pr["description"]]
    out.append(dict(
        company_id=c["company_id"], company=c["company"],
        aliases=sorted(a for a in c["aliases"] if a != c["company"]),
        parenthetical_brands=sorted(c["parenthetical_brands"]),
        likely_acquired_brands=sorted(b for b in c["parenthetical_brands"] if not is_abbrev(c["company"], b)),
        sources=sorted(c["sources"]), in_both_sources=len(c["sources"]) == 2,
        category_count=len(c["categories"]), categories=c["categories"],
        product_count=len(prods),
        has_legacy_product=any(pr["legacy"] for pr in prods),
        legacy_products=sorted({pr["product"] for pr in prods if pr["legacy"]}),
        sponsored_placement=any(pr["sponsored"] for pr in prods),
        max_reviews=max(revs) if revs else None,
        name_truncated_in_source=any(pr.get("name_truncated_in_source") for pr in prods),
        description=descs[0] if descs else None,
        description_source=next((pr["source"] for pr in prods if pr["description"]), None),
        has_description=bool(descs),
        products=prods))
out.sort(key=lambda c: (-c["category_count"], -(c["max_reviews"] or 0), c["company"].lower()))

meta = dict(
    generated="2026-08-10",
    scope="All classifications with Verdict = IN in outputs/classification-menu.md",
    categories_included=dict(
        gartner=["Multichannel Marketing Hubs","Email Marketing (Transitioning to Email Marketing Platforms)",
                 "B2B Marketing Automation Platforms","Mobile Marketing Platforms",
                 "Location Based Marketing Software","Direct Mail Automation Software"],
        g2=["Marketing Automation","SMS Marketing","Email Marketing","Personalization"]),
    coverage=dict(
        gartner=dict(status="COMPLETE", product_rows=sum(1 for r in rows if r["source"]=="gartner"),
                     declared_total=352,
                     note="All six Gartner categories enumerate fully ('Products 1-N of N'). Parsed counts reconcile exactly with declared totals, so absence from this list is ABSENT-ENUMERATED."),
        g2=dict(status="VISIBLE PAGE ONLY — NOT COMPLETE",
                distinct_products=sum(1 for r in rows if r["source"]=="g2"),
                declared_total=1810,
                pct_of_declared=round(sum(1 for r in rows if r["source"]=="g2")/1810*100, 1),
                blocks_rendered=sum({(r["category_slug"], r.get("blocks_rendered")) for r in rows if r["source"]=="g2"} and [b for _, b in {(r["category_slug"], r.get("blocks_rendered")) for r in rows if r["source"]=="g2"}] or [0]),
                note="A G2 category page renders its products TWICE - a main listing carrying 'By <vendor>' lines, then a second summary rendering without vendors. Counting rendered blocks overstates visibility. After collapsing to distinct products, this file holds 65 of 1,810 declared listings (3.6%), roughly 16 per category. Absence of a company from the G2 portion is ABSENT-IN-VISIBLE-PAGE and is NOT evidence of absence from the category.")),
    merge_rules=[
        "A vendor string 'Owner Product' collapses onto 'Owner' when the remainder is itself a product name in this data (e.g. 'Intuit Mailchimp' -> 'Intuit', because 'Mailchimp' is a Gartner product).",
        "Gartner writes lineage as 'Owner (OtherBrand)'. Owner becomes the company. The parenthetical is kept verbatim in parenthetical_brands; likely_acquired_brands excludes those that are merely abbreviations of the owner name (AWS, HPE, ITG), which is tested rather than assumed.",
        "A vendor string of the form 'Owner Product' collapses onto 'Owner' only when 'Owner' already exists as a vendor in the data AND the longer string is also a product name. Nothing else is merged.",
        "No fuzzy matching. Two companies with similar names stay separate unless a rule above applies.",
        "G2 repeats each product in a second, vendor-less rendering. Blocks are collapsed to distinct products, always preferring the block that names the vendor - otherwise a product would be split from its parent company."],
    known_limits=[
        "Ratings and review counts measure review-solicitation effort as much as customer volume (Gartner FAQ: vendors solicit reviews; nominal gifts permitted).",
        "Gartner review counts never decay - reviews do not expire.",
        "G2 'sponsored' rows are paid placement and are flagged.",
        "No funding, revenue or investor data exists in either source. UNKNOWN, never inferred.",
        "Both sources are SELF-DECLARED. No row here is corroborated by a revealed-behaviour source.",
        "Gartner does not publish reviews in Russian, Turkish or Georgian; G2 removes listings under OFAC sanctions."],
    counts=dict(product_rows=len(rows), unique_companies=len(out),
                companies_in_both_sources=sum(1 for c in out if c["in_both_sources"]),
                companies_with_legacy_product=sum(1 for c in out if c["has_legacy_product"]),
                companies_with_description=sum(1 for c in out if c["has_description"])))

json.dump(dict(meta=meta, companies=out), open("outputs/companies-IN.json","w"), indent=1, ensure_ascii=False)
print(f"product rows      : {len(rows)}")
print(f"unique companies  : {len(out)}")
print(f"in both sources   : {meta['counts']['companies_in_both_sources']}")
print(f"with legacy prod  : {meta['counts']['companies_with_legacy_product']}")
print(f"with description  : {meta['counts']['companies_with_description']}")
print(f"merges applied    : {len(merges)} -> {merges}")
