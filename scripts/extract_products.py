"""Extract product rows from IN-verdict category captures.
Deterministic parsing only. Every count is reconciled against the source's declared total."""
import re, json

GART_IN = [("Multichannel Marketing Hubs","multichannel-marketing-hubs",122),
           ("Email Marketing (Transitioning to Email Marketing Platforms)","email-marketing",100),
           ("B2B Marketing Automation Platforms","b2b-marketing-automation-platforms",59),
           ("Mobile Marketing Platforms","mobile-marketing-platforms",45),
           ("Location Based Marketing Software","location-based-marketing-software",15),
           ("Direct Mail Automation Software","direct-mail-automation-software",11)]
G2_IN   = [("Marketing Automation","marketing-automation",511),
           ("SMS Marketing","sms-marketing",531),
           ("Email Marketing","email-marketing",527),
           ("Personalization","personalization",241)]
ENDS = ("Popular Product Comparisons","Trending Products","Top Trending Products","Compare Products")
NOISE = {"OVERVIEW","ALTERNATIVES","Show More Details","Add to Compare","Be the first to write a review.",
         "Sort by","Number of Ratings, High to Low","Show More"}

def lines(p): return [l.rstrip("\n") for l in open(p,encoding="utf-8",errors="replace")]

def parse_gartner(slug):
    L = lines(f"sources/raw/gartner/2026-08-10__gartner__market-{slug}__r3.md")
    s = next(i for i,l in enumerate(L) if re.fullmatch(r"Products \d+ - \d+ of \d+", l.strip()))
    e = next((i for i in range(s+1,len(L)) if L[i].strip() in ENDS), len(L))
    anchors = [i for i in range(s,e) if L[i].startswith("By ")]
    out = []
    # Guard: a description paragraph can contain a sentence beginning "By ".
    # A real anchor has a short vendor name and a product name that is not page furniture.
    def is_real(a):
        vendor = L[a][3:].strip()
        j = a-1
        while j > s and not L[j].strip(): j -= 1
        return len(vendor) <= 60 and L[j].strip() not in NOISE and len(L[j].strip()) <= 80
    anchors = [a for a in anchors if is_real(a)]
    for n,a in enumerate(anchors):
        vendor = L[a][3:].strip()
        j = a-1
        while j > s and not L[j].strip(): j -= 1
        product = L[j].strip()
        end = anchors[n+1]-1 if n+1 < len(anchors) else e
        rating = nrat = None; desc = []
        for k in range(a+1, end):
            t = L[k].strip()
            if not t or t in NOISE or t.startswith("Logo of "): continue
            m = re.fullmatch(r"([0-9](?:\.[0-9])?)", t)
            if m and rating is None: rating = float(m.group(1)); continue
            m = re.fullmatch(r"\((\d+) Ratings?\)", t)
            if m: nrat = int(m.group(1)); continue
            if len(t) > 80: desc.append(t)
        out.append(dict(product=product, vendor=vendor, rating=rating, reviews=nrat,
                        description=" ".join(desc).strip() or None,
                        legacy="(Legacy)" in product, sponsored=False, tags=[]))
    return out

def parse_g2(slug):
    L = lines(f"sources/raw/g2/2026-08-10__g2__category-{slug}__r3.md")
    idx = [i for i,l in enumerate(L) if l.strip() == "Product Avatar Image"]
    out = []
    for a,b in zip(idx, idx[1:]+[len(L)]):
        blk = [x.strip() for x in L[a+1:b] if x.strip()]
        if not blk: continue
        sponsored = blk[0] == "Sponsored"
        if sponsored: blk = blk[1:]
        if not blk: continue
        product = blk[0]
        vendor = blk[1][3:].strip() if len(blk) > 1 and blk[1].startswith("By ") else product
        rating = nrat = None; desc = None
        for n,t in enumerate(blk):
            m = re.fullmatch(r"([0-9](?:\.[0-9])?)/5", t)
            if m and rating is None: rating = float(m.group(1))
            m = re.fullmatch(r"\(([\d,]+)\)", t)
            if m and nrat is None: nrat = int(m.group(1).replace(",",""))
            if t in ("What do users say?","Product Description") and desc is None:
                for u in blk[n+1:n+4]:
                    if len(u) > 60: desc = re.sub(r"\s*Show More$","",u); break
        tags = [t for t in ("All-in-One","Best-of-Breed","AI Verified") if t in blk]
        out.append(dict(product=product, vendor=vendor, rating=rating, reviews=nrat,
                        description=desc, legacy=False, sponsored=sponsored, tags=tags))
    return out

rows, report = [], []
for label, slug, dec in GART_IN:
    ps = parse_gartner(slug); ok = len(ps) == dec
    report.append((f"gartner/{slug}", len(ps), dec, ok))
    for p in ps:
        rows.append(dict(p, source="gartner", category=label, category_slug=slug,
                         category_url=f"https://www.gartner.com/reviews/market/{slug}",
                         declared_total=dec, visible_count=len(ps),
                         coverage="ABSENT-ENUMERATED" if ok else "PARTIAL"))
for label, slug, dec in G2_IN:
    ps = parse_g2(slug)
    report.append((f"g2/{slug}", len(ps), dec, None))
    for p in ps:
        rows.append(dict(p, source="g2", category=label, category_slug=slug,
                         category_url=f"https://www.g2.com/categories/{slug}",
                         declared_total=dec, visible_count=len(ps),
                         coverage="ABSENT-IN-VISIBLE-PAGE"))
for name, got, dec, ok in report:
    flag = "OK" if ok else ("VISIBLE-PAGE ONLY" if ok is None else "MISMATCH")
    print(f"{name:52s} parsed {got:4d} / declared {dec:4d}  {flag}")
json.dump(rows, open("sources/derived/product-rows-IN.json","w"), indent=1, ensure_ascii=False)
print("TOTAL product rows:", len(rows))
