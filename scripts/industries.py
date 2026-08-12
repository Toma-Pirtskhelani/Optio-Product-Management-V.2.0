#!/usr/bin/env python3
"""Derive the unique industry list and per-industry analytics from outputs/companies.jsonl.

Reads ONLY `enrichment.industries_served` — vendor-self-declared industry blocks captured
at Rung 1 from the vendor's own site. Adds no industry from model memory: every canonical
label is a surface string some vendor actually published (prohibition 1).

The raw field is contaminated. It was filled by a heading-anchored block extractor
(scripts/enrich.py) that took the lines following an "Industries"/"Verticals" heading, so
it swept in navigation, CTAs, product names, client names and Material-icon ligatures at
grade PRIMARY. This script does NOT edit the store. It rules every raw string into one of
three buckets and shows all of them, so nothing is silently dropped:

  INDUSTRY  a named industry/vertical            -> counted
  SEGMENT   audience or business-model descriptor -> listed, never counted as an industry
  REJECTED  not an industry claim at all          -> listed with a reason code

Outputs: outputs/industries.md, outputs/industries.json
"""
import json, re, collections, datetime, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC  = ROOT / "outputs" / "companies.jsonl"

# ---------------------------------------------------------------- normalisation

# Compounds that name ONE industry; never split on their separator.
NO_SPLIT = {"oil & gas", "food & beverage", "food and beverage",
            "advertising and marketing", "arts & entertainment"}

# Prefixes/suffixes the vendor wraps around an industry name in a nav label.
STRIP_PATTERNS = [
    (r"^(?:worksbuddy|text)\s*[-–]?\s*(?:customer service solution\s*)?for\s+", ""),
    (r"^for\s+", ""),
    (r"\s+industry solutions$", ""),
    (r"\s+solutions$", ""),
]

SPLIT_RE = re.compile(r"\s*(?:&|,|/| and )\s*", re.I)


def norm(s):
    s = s.replace("’", "'").strip().strip("-•–—:?")
    s = re.sub(r"\s+", " ", s)
    return s.lower()


def atoms(raw):
    """Split one raw string into industry atoms, after stripping vendor wrappers."""
    s = norm(raw)
    for pat, rep in STRIP_PATTERNS:
        s = re.sub(pat, rep, s).strip()
    if not s:
        return []
    if s in NO_SPLIT:
        return [s]
    return [a.strip() for a in SPLIT_RE.split(s) if a.strip()]


# ---------------------------------------------------------------- the ruling map
# key -> list of accepted atom spellings. Display label is chosen by observed
# frequency among these spellings, so no label is invented here either.
INDUSTRY = {
    "financial-services": ["financial services", "finance", "financial"],
    "banking":            ["banking", "banks", "bank"],
    "credit-unions":      ["credit unions", "credit union"],
    "capital-markets":    ["capital markets"],
    "insurance":          ["insurance"],
    "fintech":            ["fintech"],
    "lending":            ["lending"],
    "mortgage":           ["mortgage"],
    "mutual-funds":       ["mutual funds"],
    "private-equity":     ["private equity"],
    "financial-advisors": ["financial advisors"],
    "healthcare":         ["healthcare", "health care", "health"],
    "life-sciences":      ["life sciences"],
    "pharma":             ["pharma"],
    "pharmacy":           ["pharmacy"],
    "retail":             ["retail", "retail stores"],
    "fuel-retail":        ["fuel retail"],
    "ecommerce":          ["ecommerce", "e-commerce"],
    "d2c":                ["d2c"],
    "cpg":                ["cpg", "fmcg", "consumer packaged goods", "consumer goods"],
    "food-beverage":      ["food & beverage", "food and beverage"],
    "restaurants":        ["restaurants", "restaurant"],
    "coffee-shops":       ["coffee shops"],
    "hospitality":        ["hospitality"],
    "hotels":             ["hotels"],
    "travel":             ["travel", "tourism"],
    "airlines":           ["airline"],
    "aviation":           ["aviation"],
    "aerospace":          ["aerospace"],
    "defense":            ["defense"],
    "satellite":          ["satellite"],
    "telecommunications": ["telecommunications", "telecommunication", "telecom", "telco",
                           "communications"],
    "broadband":          ["fiber", "broadband"],
    "media":              ["media", "publishing", "publishers", "news"],
    "entertainment":      ["entertainment"],
    "ticketing":          ["ticketing"],
    "gaming":             ["gaming", "social gaming", "social games"],
    "igaming":            ["igaming"],
    "prediction-markets": ["prediction markets"],
    "online-trading":     ["online trading"],
    "sports":             ["sports"],
    "education":          ["education"],
    "higher-education":   ["higher education"],
    "k12-education":      ["education (k-12)"],
    "edtech":             ["edtech"],
    "nonprofits":         ["nonprofits", "non-profit", "ngos"],
    "churches":           ["churches"],
    "government":         ["government", "public sector", "public services"],
    "energy":             ["energy"],
    "utilities":          ["utilities"],
    "oil-gas":            ["oil & gas"],
    "manufacturing":      ["manufacturing"],
    "automotive":         ["automotive", "automobile"],
    "car-dealerships":    ["car dealerships"],
    "auto-services":      ["auto services"],
    "logistics":          ["logistics"],
    "supply-chain":       ["supply chain"],
    "transportation":     ["transportation"],
    "last-mile-delivery": ["last-mile delivery"],
    "distribution":       ["distribution"],
    "real-estate":        ["real estate"],
    "proptech":           ["proptech"],
    "shopping-centres":   ["shopping centers"],
    "mixed-use":          ["mixed-use"],
    "airports":           ["airports"],
    "smart-cities":       ["smart cities"],
    "technology":         ["technology", "high tech", "hi tech", "tech"],
    "software":           ["software"],
    "it-services":        ["it services", "it"],
    "saas":               ["saas"],
    "business-services":  ["business services"],
    "legal":              ["legal"],
    "agriculture":        ["agriculture"],
    "beauty":             ["beauty", "cosmetics"],
    "wellness":           ["wellness"],
    "spas":               ["spas"],
    "salons":             ["salons"],
    "pet-services":       ["pet services"],
    "home-services":      ["home services"],
    "luxury":             ["luxury"],
    "advertising":        ["advertising and marketing"],
}

# Audience / business-model descriptors. Real claims, but not industries.
SEGMENT = {
    "enterprise": "company size", "startups": "company stage",
    "startups & scaleups": "company stage", "scaleups": "company stage",
    "small business": "company size", "smb": "company size",
    "b2b": "go-to-market", "franchises": "ownership model",
    "franchisees": "ownership model", "operators": "ownership model",
    "marketplace": "business model", "marketplaces": "business model",
    "on-demand": "business model", "digital native businesses": "business model",
    "conglomerates": "org type", "mobile apps": "product type",
    "agencies": "competitor class 3 - services firms", "consultants": "competitor class 3 - services firms",
    "mgmt. consulting": "competitor class 3 - services firms",
    "in-house marketing": "competitor class 2 - in-house build",
    "in-house operations": "competitor class 2 - in-house build",
    "operations service providers": "competitor class 3 - services firms",
    "marketers": "buyer role", "teams": "buyer role", "customer service": "buyer role",
    "cx teams": "buyer role", "technical": "buyer role", "operations": "buyer role",
    "business": "too generic", "enterprises": "company size",
}

# Reason codes for everything else, applied by rule then by explicit listing.
NAV_RE = re.compile(
    r"^(resources?|blog|blogs|company|support|about|about us|contact|contact us|solutions?"
    r"|products?|features?|pricing|plans|partners?|integration partners|customers?|clients"
    r"|case stud(?:y|ies)|customer stor(?:y|ies)|success story|testimonials|news|careers"
    r"|awards|events?|webinars?|ebooks?|books|glossary|help portal|home|home page.*|compare"
    r"|training|certification|academics|communities|video tutorials|use cases?|by use case"
    r"|by team|by organization type|channels|display|language|english|german ?/ ?deutsch"
    r"|back|new|others?|services?|service|marketing|teams|pricing"
    r"|industries|all industries|see all industries|explore industries|industry versions"
    r"|white papers? ?& ?guides|resource (?:center|library|hub|library -->)|content library"
    r"|solutions library|one pagers|books and reports|webinars and events|resources and events"
    r"|featured|what's new|toggle menu|expand menu|close resources|open resources"
    r"|log in|sign up now|download|webinar|event|customer stories|clients|plans"
    r"|security and compliance|process mining|personalization|capabilities|all capabilities"
    r"|journey designer|omnichannel engagement|email marketing|sms marketing"
    r"|mobile app marketing|email|social media|website|mobile|hipaa|apps"
    r"|state of direct mail|digital certified mail|direct mail (?:editor|api|mailing lists)"
    r"|contact us.*|ebooks? \+ guides|customer case studies|our solutions"
    r"|product features|product tours?|developer hub|explore more|view blog|view now"
    r"|switch from ga4|switch from matomo|listserv 101|maestro 101|rfp ?/ ?rfi|our story"
    r"|locations|our solutions|explore our solution suite|why smartcomm|why ipresso|why pyze"
    r"|roi calcu|turn|local|pulse: igaming.s benchmark tool|go to industry hub"
    r"|industry solutions on aws|retail leasing metrics|space optimization"
    r"|energy and hvac optimization|nurture leads|orchestrate journeys|drive engagement"
    r"|get started|learn.*|see .*|read .*|explore .*|request a demo|schedule a demo"
    r"|click for demo|see product tour|already a customer\? log in here\.|let.s talk results"
    r"|boost prof|increase engagement|convert more customers|manage customer lifecycle"
    r"|reduce churn, boost loyal|airship guarantees results"
    r"|solutions that drive business results|what we can do for you|optikpi for\.\.\."
    r"|shopping_cart|approval_delegation|auto_stories|account_balance|computer)$")

ICON_RE  = re.compile(r"^[a-z]+_[a-z_]+$")
CLIENTS  = {"vodafone fiji", "earthy orgins", "cybele", "tourism fiji",
            "enthusiast hotels", "hcltech", "netmera"}
DESCRIPTORS = {
    "trades & field work", "salons, spas, fitness", "clinics, dental, chiro",
    "law, accounting", "grooming, boarding, vets", "repair shops & detailing",
    "compliant cdp for regulated sectors", "personalization at purchase scale",
    "loyalty and lifecycle marketing", "audience monetization and retention",
    "real-time player context and activation", "learn about optikpi heritage and story",
    "learn with airship", "airship guarantees results",
}

ATOM2KEY = {sp: k for k, sps in INDUSTRY.items() for sp in sps}


def reject(s):
    """Reason this string is not an industry claim, or None."""
    if s in DESCRIPTORS:
        return "sub-label describing the row above, not an industry heading"
    if s in CLIENTS:
        return "named client or vendor, not an industry"
    if ICON_RE.match(s):
        return "Material-icon ligature scraped from markup"
    if NAV_RE.match(s):
        return "site navigation, CTA, product or content label"
    return None


def rule_raw(raw):
    """Rule one raw string -> [(atom, bucket, key_or_reason), ...].

    The WHOLE string is ruled before any splitting. Splitting first would turn
    "Energy and HVAC Optimization" — a use-case label — into the Energy industry.
    """
    n = norm(raw)
    r = reject(n)
    if r:
        return [(n, "REJECTED", r)]
    if n in ATOM2KEY:
        return [(n, "INDUSTRY", ATOM2KEY[n])]
    if n in SEGMENT:
        return [(n, "SEGMENT", SEGMENT[n])]

    out = []
    for a in atoms(raw):
        if a in ATOM2KEY:
            out.append((a, "INDUSTRY", ATOM2KEY[a]))
        elif a in SEGMENT:
            out.append((a, "SEGMENT", SEGMENT[a]))
        else:
            r = reject(a)
            out.append((a, "REJECTED", r) if r else (a, "UNRESOLVED", a))
    return out or [(n, "REJECTED", "empty after stripping vendor wrapper")]


# ---------------------------------------------------------------- load + rule
rows = [json.loads(l) for l in open(SRC)]
by_id = {r["company_id"]: r for r in rows}

disposition = {}                       # raw string -> (bucket, key/reason)
company_industries = collections.defaultdict(set)   # company_id -> {key}
company_segments = collections.defaultdict(set)
industry_surface = collections.defaultdict(collections.Counter)  # key -> Counter(atom)
raw_count = collections.Counter()
sources_for = collections.defaultdict(set)          # key -> {source_url}

declared, empty, absent = [], [], []
for r in rows:
    f = r.get("enrichment", {}).get("industries_served")
    if f is None:
        absent.append(r); continue
    if not f.get("value"):
        empty.append(r); continue
    declared.append(r)
    for raw in f["value"]:
        raw_count[raw] += 1
        for a, bucket, val in rule_raw(raw):
            disposition.setdefault(raw, []).append((a, bucket, val))
            if bucket == "INDUSTRY":
                company_industries[r["company_id"]].add(val)
                industry_surface[val][a] += 1
                if f.get("source_url"):
                    sources_for[val].add(f["source_url"])
            elif bucket == "SEGMENT":
                company_segments[r["company_id"]].add(a)

unresolved = sorted({v for d in disposition.values() for a, b, v in d if b == "UNRESOLVED"})
if unresolved:
    print("UNRESOLVED atoms — rule these before publishing:")
    for u in unresolved:
        print("   ", u)


def label(key):
    """Display label = most frequent observed spelling, title-cased as published."""
    top = industry_surface[key].most_common()
    if not top:
        return key
    best = max(top, key=lambda kv: (kv[1], -len(kv[0])))[0]
    # Recover the published casing of that spelling, with the vendor's nav wrapper
    # ("For ...", "... Industry Solutions", "WorksBuddy for ...") removed.
    for r in declared:
        for raw in r["enrichment"]["industries_served"]["value"]:
            if best not in atoms(raw):
                continue
            stripped = raw.strip()
            for pat, rep in STRIP_PATTERNS:
                stripped = re.sub(pat, rep, stripped, flags=re.I).strip()
            if norm(stripped) == best:
                return stripped.strip("-•–—:")
            for piece in re.split(r"\s*(?:&|,|/| and )\s*", stripped, flags=re.I):
                if norm(piece) == best:
                    return piece.strip().strip("-•–—:")
    return best.title()


# ---------------------------------------------------------------- analytics
def med(xs):
    xs = sorted(xs)
    if not xs: return None
    n = len(xs)
    return xs[n // 2] if n % 2 else round((xs[n // 2 - 1] + xs[n // 2]) / 2, 1)


industries = []
for key, comps in sorted(
        ((k, sorted({c for c, ks in company_industries.items() if k in ks})) for k in industry_surface),
        key=lambda kv: (-len(kv[1]), kv[0])):
    recs = [by_id[c] for c in comps]
    both = [r for r in recs if r["in_both_sources"]]
    g2   = [r for r in recs if "g2" in r["sources"]]
    ga   = [r for r in recs if "gartner" in r["sources"]]
    chans = collections.Counter()
    countries = collections.Counter()
    free = pub = priced_known = chan_known = 0
    for r in recs:
        e = r.get("enrichment", {})
        ch = (e.get("channels") or {}).get("value") or []
        if ch:
            chan_known += 1
            chans.update(ch)
        c = (e.get("published_address_country") or {}).get("value")
        if c:
            # published address strings, verbatim except the one obvious duplicate
            countries[{"United States": "US", "USA": "US"}.get(c, c)] += 1
        if (e.get("has_free_tier") or {}).get("value") is True: free += 1
        p = (e.get("pricing_published") or {}).get("value")   # "yes"/"no", not boolean
        if p in ("yes", "no"):
            priced_known += 1
            if p == "yes": pub += 1
    co = collections.Counter()
    for c in comps:
        co.update(company_industries[c] - {key})
    industries.append({
        "key": key,
        "label": label(key),
        "vendor_count": len(comps),
        "vendors": [by_id[c]["company"] for c in comps],
        "surface_forms": dict(industry_surface[key]),
        "in_both_sources": len(both),
        "g2": len(g2), "gartner": len(ga),
        "median_reviews": med([r["max_reviews"] for r in recs if r.get("max_reviews")]),
        "median_categories": med([r["category_count"] for r in recs]),
        "median_industries_declared": med([len(company_industries[c]) for c in comps]),
        "channels_declared": dict(chans.most_common()),
        "vendors_declaring_any_channel": chan_known,
        "hq_countries_published": dict(countries.most_common()),
        "pricing_published_yes": pub,
        "pricing_published_known": priced_known,
        "vendors_with_free_tier": free,
        "co_occurring": [(label(k), n) for k, n in co.most_common(3)],
        "source_urls": sorted(sources_for[key]),
        "grade": "PRIMARY", "rung": 1, "source_class": "SELF-DECLARED",
    })

segments = collections.Counter()
for c, ss in company_segments.items():
    segments.update(ss)

out = {
    "generated": str(datetime.date.today()),
    "source": "outputs/companies.jsonl :: enrichment.industries_served",
    "denominators": {
        "companies_in_store": len(rows),
        "companies_with_declared_industries": len(declared),
        "companies_with_field_UNKNOWN": len(empty),
        "companies_without_the_field": len(absent),
        "pct_of_store_declaring": round(100 * len(declared) / len(rows), 1),
    },
    "raw_strings_seen": len(raw_count),
    "industries": industries,
    "segments_not_industries": dict(segments.most_common()),
    "disposition": {raw: [{"atom": a, "bucket": b, "ruling": v} for a, b, v in d]
                    for raw, d in sorted(disposition.items())},
}
(ROOT / "outputs" / "industries.json").write_text(json.dumps(out, indent=1, ensure_ascii=False))

# ---------------------------------------------------------------- markdown
L = []
W = L.append
d = out["denominators"]
W("# Industries served — unique list and per-industry analytics\n")
W(f"Generated {out['generated']} by `scripts/industries.py` from "
  "`outputs/companies.jsonl` → `enrichment.industries_served`. Regenerate, never hand-edit.\n")
W("## What this counts, and what it does not\n")
W("Every row below counts **vendors that published an industry block on their own website "
  "and whose block the enrichment pass captured within its four-fetch budget**. That is a "
  "count of self-declaration, not of market coverage, revenue, customers or wins.\n")
W(f"| Denominator | Companies |\n|---|---:|")
W(f"| In the store | {d['companies_in_store']} |")
W(f"| Declared ≥1 industry (the base for every number here) | **{d['companies_with_declared_industries']}** "
  f"({d['pct_of_store_declaring']}% of the store) |")
W(f"| `industries_served` present but UNKNOWN — no block found in budget | {d['companies_with_field_UNKNOWN']} |")
W(f"| Field absent — paste-only, third-party-only or unreachable records | {d['companies_without_the_field']} |")
W("")
base_src = collections.Counter(
    ("both" if r["in_both_sources"] else "g2-only" if "g2" in r["sources"] else "gartner-only")
    for r in declared)
W(f"**The declaring base is Gartner-shaped** — {base_src['gartner-only']} Gartner-only, "
  f"{base_src['both']} in both sources, {base_src['g2-only']} G2-only. G2 coverage in this study "
  "is 65 of 1,810 listings (3.6%), and that limit propagates straight into every count below.\n")
W("**A vendor absent from an industry row is not evidence it does not serve that industry.** "
  f"{d['companies_with_field_UNKNOWN'] + d['companies_without_the_field']} of "
  f"{d['companies_in_store']} companies never had an industry block read at all.\n")
W("**Grade.** Every cell is `PRIMARY` / Rung 1 / `SELF-DECLARED` — read off the vendor's own "
  "page. Two self-declared sources agreeing is not corroboration, so **no industry row here "
  "is `CORROBORATED`, and none can be** without a revealed-behaviour source.\n")
W("**Standing statement.** Demand-side evidence exists for none of competitor classes 2–7. "
  "Nothing here counts buyers; it counts vendors' claims about who they sell to.\n")
W(f"**Ranking is within this source only** — the vendor-website population. It is never "
  "comparable with G2 or Gartner category counts, which have different bar heights.\n")
W("---\n")
W(f"## 1 · The unique industry list — {len(industries)} industries\n")
W("Each named once. The label is the **most frequently published spelling** of that "
  "industry among the vendors, not a name invented here.\n")
W("| # | Industry | Vendors | Also spelled as |\n|---:|---|---:|---|")
for i, it in enumerate(industries, 1):
    alts = [s for s in it["surface_forms"] if s != norm(it["label"])]
    W(f"| {i} | **{it['label']}** | {it['vendor_count']} | {', '.join(sorted(alts)) or '—'} |")
W("")
per_vendor = sorted((len(v) for v in company_industries.values()), reverse=True)
singletons = [it for it in industries if it["vendor_count"] == 1]
claims = sum(it["vendor_count"] for it in industries)
top10 = sum(it["vendor_count"] for it in industries[:10])
broadest = sorted(company_industries.items(), key=lambda kv: -len(kv[1]))[:5]
W("### Shape of the list\n")
W(f"| Measure | Value |\n|---|---:|")
W(f"| Industries named | {len(industries)} |")
W(f"| Industry claims (vendor × industry pairs) | {claims} |")
W(f"| Declaring vendors | {len(declared)} |")
W(f"| Industries per vendor — median / max | {med(per_vendor)} / {per_vendor[0]} |")
W(f"| Industries claimed by exactly one vendor | {len(singletons)} ({round(100*len(singletons)/len(industries))}%) |")
W(f"| Share of all claims held by the top 10 industries | {round(100*top10/claims)}% |")
W("")
W(f"**The list is a short head and a long tail.** {len(singletons)} of {len(industries)} "
  "industries rest on a single vendor's website — `SINGLE-SOURCE` in substance, and each one "
  "would disappear if that one vendor rewrote its nav. The top 10 hold "
  f"{round(100*top10/claims)}% of all claims.\n")
W("**Broadest claimers** (they inflate the tail): " +
  ", ".join(f"{by_id[c]['company']} ({len(ks)})" for c, ks in broadest) + ".\n")
W("---\n")
W("## 2 · Per-industry analytics\n")
W("`Both` = present in G2 **and** Gartner. `Median reviews` is the vendor's largest product "
  "review count — a measure of review-solicitation effort as much as customer volume. "
  "`Breadth` is the median number of industries those vendors each declare: low means the "
  "industry is claimed by focused vendors, high means it is claimed in passing by generalists.\n")
W("| Industry | Vendors | Both | G2 | Gartner | Median reviews | Median categories | Breadth | Most-common co-claim |")
W("|---|---:|---:|---:|---:|---:|---:|---:|---|")
for it in industries:
    co = it["co_occurring"][0][0] + f" ({it['co_occurring'][0][1]})" if it["co_occurring"] else "—"
    W(f"| **{it['label']}** | {it['vendor_count']} | {it['in_both_sources']} | {it['g2']} | "
      f"{it['gartner']} | {it['median_reviews'] if it['median_reviews'] is not None else '—'} | "
      f"{it['median_categories']} | {it['median_industries_declared']} | {co} |")
W("")
W("### Channel and commercial posture, by industry\n")
W("Each cell shows the count **over the vendors in that industry for whom the field is known** "
  "— the denominator is printed, because these fields are far from complete and a bare "
  "percentage would hide that.\n")
W("| Industry | Vendors | Channels declared by | Top channels | Publishes price | Free tier | HQ published |")
W("|---|---:|---:|---|---:|---:|---|")
for it in industries:
    top = ", ".join(f"{c} ({n})" for c, n in list(it["channels_declared"].items())[:4]) or "—"
    hq = ", ".join(f"{c} {n}" for c, n in list(it["hq_countries_published"].items())[:3]) or "—"
    W(f"| **{it['label']}** | {it['vendor_count']} | {it['vendors_declaring_any_channel']} | {top} | "
      f"{it['pricing_published_yes']}/{it['pricing_published_known']} | "
      f"{it['vendors_with_free_tier']} | {hq} |")
W("")
W("### Vendors behind each industry\n")
for it in industries:
    W(f"**{it['label']}** ({it['vendor_count']}) — {', '.join(it['vendors'])}")
    W("")
W("---\n")
W("## 3 · Segments recorded but not counted as industries\n")
W("These are real published claims, but they name an audience or a business model, not an "
  "industry. Counting them as industries would inflate the list with a different kind of thing.\n")
W("| Claim | Vendors | Why not an industry |\n|---|---:|---|")
for s, n in segments.most_common():
    W(f"| {s} | {n} | {SEGMENT.get(s, '')} |")
W("")
W("Two of these are notable: **Agencies / Consultants** and **In-house marketing** appear as "
  "*target segments of software vendors* — supply-side self-declaration, competitor classes 2 "
  "and 3 showing up as buyers rather than as rivals. Neither is evidence any buyer chose that "
  "route.\n")
W("---\n")
W("## 4 · Disposition of every raw string\n")
W(f"The field held **{len(raw_count)} distinct raw strings**. The extractor that filled it was "
  "heading-anchored — it took the lines after an `Industries`/`Verticals` heading — so it swept "
  "in navigation, CTAs, product names, client names and Material-icon ligatures **at grade "
  "PRIMARY**. Every string is shown with its ruling; none is silently dropped.\n")
W("| Raw string | Seen | Atom | Bucket | Ruling |\n|---|---:|---|---|---|")
for raw in sorted(disposition, key=lambda r: (-raw_count[r], r.lower())):
    for a, b, v in disposition[raw]:
        W(f"| `{raw}` | {raw_count[raw]} | {a} | {b} | {v} |")
W("")
(ROOT / "outputs" / "industries.md").write_text("\n".join(L))

print(f"{len(industries)} industries from {len(declared)} declaring companies "
      f"({len(raw_count)} raw strings, {len(segments)} segment claims)")
