"""Resolve -> fetch (4-page budget) -> extract deterministically -> write JSONL.
No model reads a page. Every value comes from a defined element of committed page text."""
import json, re, os, sys, html, subprocess, datetime

D = datetime.date.today().isoformat()
UA = "Mozilla/5.0 (compatible; research-study/1.0)"

# ---------- transport ----------
def get(url, timeout=20, http1=False):
    cmd = ["curl","-sS","-L","--max-time",str(timeout),"-A",UA]
    if http1: cmd.append("--http1.1")
    r = subprocess.run(cmd+["-w","\n__H__%{http_code}__U__%{url_effective}","-o","-",url],
                       capture_output=True, text=True)
    b = r.stdout or ""
    m = re.search(r"\n__H__(\d+)__U__(.*)$", b, re.S)
    code, final = (int(m.group(1)), m.group(2).strip()) if m else (0, url)
    if m: b = b[:m.start()]
    return code, final, b

def totext(h):
    h = re.sub(r"<(script|style|noscript|svg)[^>]*>.*?</\1>", " ", h, flags=re.S|re.I)
    t = html.unescape(re.sub(r"<[^>]+>", "\n", h))
    return re.sub(r"\n{2,}", "\n", re.sub(r"[ \t]+", " ", t)).strip()

def sig(h):
    def one(p):
        m = re.search(p, h, re.I|re.S)
        return html.unescape(m.group(1)).strip() if m else None
    s = dict(
      title=one(r"<title[^>]*>(.*?)</title>"),
      meta_description=one(r'<meta[^>]+name=["\']description["\'][^>]+content=["\'](.*?)["\']')
                       or one(r'<meta[^>]+content=["\'](.*?)["\'][^>]+name=["\']description["\']'),
      og_description=one(r'<meta[^>]+property=["\']og:description["\'][^>]+content=["\'](.*?)["\']'),
      og_site_name=one(r'<meta[^>]+property=["\']og:site_name["\'][^>]+content=["\'](.*?)["\']'))
    def tags(t, n):
        return [re.sub(r"\s+"," ",html.unescape(re.sub(r"<[^>]+>","",x))).strip()
                for x in re.findall(rf"<{t}[^>]*>(.*?)</{t}>", h, re.S|re.I)][:n]
    s["h1"], s["h2"] = tags("h1",4), tags("h2",30)
    org=[]
    for blk in re.findall(r'<script[^>]+application/ld\+json[^>]*>(.*?)</script>', h, re.S|re.I):
        try: j=json.loads(blk.strip())
        except Exception: continue
        def walk(o):
            if isinstance(o,dict):
                if o.get("@type") in ("Organization","Corporation") or "foundingDate" in o: org.append(o)
                for v in o.values(): walk(v)
            elif isinstance(o,list):
                for v in o: walk(v)
        walk(j)
    s["org"]=org[:5]
    return s

# ---------- domain resolution ----------
def norm(x): return re.sub(r"[^a-z0-9]","",(x or "").lower())
def candidates(company):
    c = company.lower()
    c = re.sub(r"\s*\([^)]*\)","",c)
    c = c.replace("&"," and ")
    base = re.sub(r"[^a-z0-9. ]"," ",c).strip()
    if re.search(r"\.(io|com|ai|co|net|org)$", base):     # name already carries a TLD
        return [base.replace(" ","")]
    joined = base.replace(" ","")
    hyph   = re.sub(r"\s+","-",base)
    out=[]
    for host in dict.fromkeys([joined, hyph]):
        for tld in (".com",".io",".ai",".co"):
            out.append(host+tld)
    return out[:6]

def confirm(company, s, domain):
    """Accept a domain only if the served page identifies the company."""
    hay = norm(" ".join(filter(None,[s.get("title"), s.get("og_site_name"),
          " ".join(o.get("name","") for o in s.get("org",[]) if isinstance(o.get("name"),str))])))
    n = norm(company)
    if len(n) >= 4 and n in hay: return "name in title/og:site_name/JSON-LD"
    first = norm(company.split()[0])
    if len(first) >= 5 and first in hay and first in norm(domain): return "first token in page identity and domain"
    return None

def resolve(company, http_requests):
    for dom in candidates(company):
        code, final, body = get("https://"+dom)
        http_requests.append(dict(kind="resolve", url="https://"+dom, http=code, bytes=len(body or "")))
        if code != 200 or len(body or "") < 400:
            code, final, body = get("https://www."+dom)
            http_requests.append(dict(kind="resolve", url="https://www."+dom, http=code, bytes=len(body or "")))
        if code == 200 and len(body or "") > 400:
            s = sig(body)
            why = confirm(company, s, dom)
            if why: return dom, final, body, s, why
    return None, None, None, None, None

# ---------- page selection ----------
PROD  = re.compile(r"/(products?|platform|features?|solutions?)(/overview)?/?$", re.I)
LOOSE = re.compile(r"(product|platform|feature)", re.I)
PRICE = re.compile(r"/(pricing|plans|price)/?$", re.I)
TRUST = re.compile(r"/(trust|security|compliance)/?$", re.I)
def linkset(h, base):
    out=[]
    for m in re.finditer(r'href=["\']([^"\'#]+)["\']', h, re.I):
        u=m.group(1)
        if u.startswith("/"): u=base.rstrip("/")+u
        if u.startswith("http"): out.append(u)
    return list(dict.fromkeys(out))
def pick(c, rx, dom):
    root=dom.split(".")[0]
    h=[u for u in c if rx.search(u) and root in u and "cdn." not in u]
    h.sort(key=len); return h[0] if h else None

# ---------- extraction ----------
CH = {"email":r"\bemails?\b","sms":r"\bSMS\b|\btext messag","push":r"push notification|\bpush\b",
 "web-push":r"web[- ]push|browser push","in-app":r"in-?app messag","whatsapp":r"\bWhatsApp\b",
 "viber":r"\bViber\b","rcs":r"\bRCS\b","voice":r"\bvoice\b|\bIVR\b","direct-mail":r"direct mail",
 "ads":r"\bad(vertis|s)\b","chat":r"live chat|\bchatbot"}
DEP = [("on-premise",r"on-?prem(ise|ises)?\b"),("self-hosted",r"self[- ]host"),
 ("private-cloud",r"private cloud|in your own (AWS|Azure|GCP|cloud)"),
 ("saas-single-tenant",r"single[- ]tenant|dedicated instance"),
 ("managed-service",r"managed service"),("api-platform",r"API[- ]first|developer platform")]

def cell(v,u,g="PRIMARY",**kw): return dict(value=v, source_url=u, rung=1, grade=g, retrieved_date=D, **kw)
def unk(note=None):
    d=dict(value=None, source_url=None, rung=None, grade="UNKNOWN", retrieved_date=D)
    if note: d["note"]=note
    return d
def unkl(note=None):
    d=dict(value=[], source_url=None, rung=None, grade="UNKNOWN", retrieved_date=D)
    if note: d["note"]=note
    return d

def extract(company, dom, pages, texts):
    home = pages.get("homepage"); prod = pages.get("product"); pay = pages.get("pricing_or_trust")
    e = {}
    e["website"] = cell(home["url"], home["url"]) if home else unk()
    # identity / firmographics from JSON-LD only
    country = founded = None; csrc = fsrc = None
    for lbl,p in pages.items():
        for o in p["sig"]["org"]:
            a=o.get("address")
            if isinstance(a,list): a=a[0] if a else None
            if isinstance(a,dict) and a.get("addressCountry") and not country:
                c=a["addressCountry"]; country = c if isinstance(c,str) else c.get("name"); csrc=p["url"]
            if o.get("foundingDate") and not founded:
                m=re.search(r"\d{4}",str(o["foundingDate"]))
                if m: founded=int(m.group(0)); fsrc=p["url"]
    e["hq_country"] = cell(country, csrc, basis="JSON-LD PostalAddress as published on the site. This is the address in the markup, not a verified headquarters.") if country else unk("No addressCountry in JSON-LD on the pages fetched.")
    e["founded_year"] = cell(founded, fsrc) if founded else unk("No foundingDate in JSON-LD on the pages fetched.")
    # positioning, verbatim from defined elements
    md = home["sig"]["meta_description"] or home["sig"]["og_description"] if home else None
    e["description_own"] = cell(md, home["url"], basis="meta description, verbatim") if md else unk()
    h1 = next((x for x in (home["sig"]["h1"] if home else []) if len(x)>8), None)
    e["value_proposition"] = cell(h1, home["url"], basis="first <h1>, verbatim") if h1 else unk()
    h2 = [x for x in (prod["sig"]["h2"] if prod else []) if 8 < len(x) < 120][:8]
    e["functionality"] = cell(h2, prod["url"], basis="product-page section headings, verbatim. These are headings, not a vetted capability list.") if h2 else unk()
    # channels - matched only in positioning text, never sitewide nav
    llm_summary = " ".join(re.findall(r"^>\s*(.+)$", texts.get("llms.txt",""), re.M))[:1200]
    pos = " ".join(filter(None,[md, h1, " ".join(h2), llm_summary,
          prod["sig"]["meta_description"] if prod else None,
          texts.get("product","")]))
    hits, ev = [], {}
    for k,p in CH.items():
        m=re.search(p,pos,re.I)
        if m:
            hits.append(k); ev[k]=re.sub(r"\s+"," ",pos[max(0,m.start()-45):m.end()+45]).strip()
    e["channels"] = cell(hits, (prod or home)["url"], evidence=ev,
        basis="controlled vocabulary matched in the vendor's positioning text (meta description, h1, llms.txt summary) and the product page body. The homepage body is excluded because its navigation produces false positives.") if hits else unkl("No channel named in the vendor's positioning text within budget.")
    # deployment
    # Deployment claims are only credible in a sentence on a product/pricing/trust page.
    # Sitewide nav and link lists produce false positives at grade INFERRED, which is worse
    # than an empty column.
    scope = "\n".join(texts.get(k,"") for k in ("product","pricing_or_trust"))
    dep, depev = [], None
    for k,p in DEP:
        for m in re.finditer(p, scope, re.I):
            s=max(0,scope.rfind("\n",0,m.start())); en=scope.find("\n",m.end())
            line=re.sub(r"\s+"," ",scope[s:en if en>0 else len(scope)]).strip()
            if len(line) >= 40 and re.search(r"\b(we|you|your|is|are|can|deploy|host|hosted|instance|tenant|cloud|run|available)\b", line, re.I):
                dep.append(k)
                if not depev: depev=line[:300]
                break
    if dep:
        e["solution_type"] = cell(dep, (pay or prod or home)["url"], "INFERRED")
        e["solution_type_evidence"] = cell(depev, (pay or prod or home)["url"], "INFERRED")
    else:
        e["solution_type"] = unkl("No deployment or tenancy statement found on the pages fetched. Not defaulted to SaaS.")
        e["solution_type_evidence"] = unk()
    # industries - only an explicit block
    inds=[]; isrc=None
    llm = texts.get("llms.txt","")
    m = re.search(r"^#+\s*(Industries|Verticals)\s*$(.*?)(^#|\Z)", llm, re.M|re.S)
    if m:
        inds=[x.strip() for x in re.findall(r"\[([^\]]+)\]\(", m.group(2))][:20]; isrc=pages["llms.txt"]["url"]
    if not inds and prod:
        blk=re.search(r"\n(Industries|By industry|Industries we serve)\n(.{0,600})", texts.get("product",""), re.I|re.S)
        if blk: inds=[x.strip(" -•") for x in blk.group(2).split("\n") if 2<len(x.strip())<40][:12]; isrc=prod["url"]
    e["industries_served"] = cell(inds, isrc) if inds else unkl("No explicit industries block on the pages fetched.")
    n=len(inds)
    e["vertical_focus"] = dict(value=("vertical" if 0<n<=2 else "mixed" if n<=5 else "horizontal") if n else None,
        source_url=isrc, rung=None, grade="COMPUTED" if n else "UNKNOWN", retrieved_date=D,
        note=f"Computed from {n} stated industries; never researched.")
    e["named_clients"] = unkl("Not collected: no reliably-delimited client block exists across vendors.")
    # pricing
    if pay and PRICE.search(pay["url"]):
        pt = re.findall(r"[$€£]\s?\d[\d,]*(?:\.\d+)?", texts.get("pricing_or_trust",""))
        free = bool(re.search(r"free plan|start free|free tier|free forever", texts.get("pricing_or_trust",""), re.I))
        cs   = bool(re.search(r"contact (us|sales)|talk to sales|custom pricing", texts.get("pricing_or_trust",""), re.I))
        e["pricing_url"] = cell(pay["url"], pay["url"])
        e["pricing_published"] = cell("yes" if pt else "no", pay["url"],
            basis="'yes' means numeric prices appear on the page; 'no' means the page exists and shows none.")
        e["pricing_detail"] = cell(list(dict.fromkeys(pt))[:12], pay["url"],
            basis="numeric price tokens as they appear on the pricing page") if pt else unk("Pricing page fetched; no numeric prices served.")
        e["has_free_tier"] = cell(free, pay["url"])
        e["has_contact_sales_tier"] = cell(cs, pay["url"])
    else:
        for k in ("pricing_url","pricing_published","pricing_detail","has_free_tier","has_contact_sales_tier"):
            e[k]=unk("No pricing page reached within the 4-fetch budget.")
    e["business_model"] = unk("Replaced by has_free_tier / has_contact_sales_tier; recorded only where a vendor states terms explicitly.")
    return e

# ---------- driver ----------
def run_one(rec):
    company = rec["company"]; http_requests=[]; log=[]; pages={}; texts={}
    dom, final, body, s, why = resolve(company, http_requests)
    if not dom:
        return dict(enrichment_status="unreachable", unreachable=True, fetches_used=0,
                    http_requests=len(http_requests), resolve_attempts=http_requests,
                    unreachable_reason="No candidate domain served a page identifying this company.",
                    fetch_log=[], raw_capture=None, retrieved_date=D)
    used=0
    def take(label,url,code=None,fin=None,b=None,sg=None):
        nonlocal used
        if used>=4 or not url: return None
        used+=1
        if b is None:
            c,f,bb = get(url); http_requests.append(dict(kind="fetch",url=url,http=c,bytes=len(bb or "")))
            if c!=200 or len(bb or "")<400:
                c,f,bb = get(url,http1=True); http_requests.append(dict(kind="fetch-http1",url=url,http=c,bytes=len(bb or "")))
        else: c,f,bb = code,fin,b
        ok = c==200 and len(bb or "")>400
        log.append(dict(n=used,label=label,url=url,final_url=f,http=c,bytes=len(bb or ""),ok=ok))
        if ok:
            pages[label]=dict(url=f,sig=sg or sig(bb)); texts[label]=totext(bb)
        return bb if ok else None
    base=f"https://{dom}"
    llm = take("llms.txt", base+"/llms.txt")
    take("homepage", base, 200, final, body, s)
    cands=[]
    if llm: cands+=re.findall(r"\((https?://[^)]+)\)", texts.get("llms.txt",""))
    if "homepage" in pages: cands+=linkset(body, base)
    cands=list(dict.fromkeys(cands))
    take("product", pick(cands,PROD,dom) or pick(cands,LOOSE,dom))
    take("pricing_or_trust", pick(cands,PRICE,dom) or pick(cands,TRUST,dom))
    # Invariant: extraction reads exactly the text that gets committed, so every quoted
    # value is checkable against sources/raw/vendors/. Truncate FIRST, then extract.
    texts = {l: t[:14000] for l,t in texts.items()}
    os.makedirs("sources/raw/vendors",exist_ok=True)
    blocks=[]
    for l in texts:
        s=pages[l]["sig"]
        head=["===== %s :: %s" % (l, pages[l]["url"]), "--- SIGNALS ---",
              "title: %s" % (s.get("title") or ""),
              "meta_description: %s" % (s.get("meta_description") or ""),
              "og_description: %s" % (s.get("og_description") or ""),
              "og_site_name: %s" % (s.get("og_site_name") or ""),
              "h1: %s" % " | ".join(s.get("h1") or []),
              "h2: %s" % " | ".join(s.get("h2") or []),
              "jsonld_org: %s" % json.dumps(s.get("org") or [], ensure_ascii=False)[:1500],
              "--- TEXT ---"]
        blocks.append("\n".join(head)+"\n"+texts[l])
    open(f"sources/raw/vendors/{rec['company_id']}.txt","w").write("\n\n".join(blocks))
    e = extract(company, dom, pages, texts)
    e.update(enrichment_status="done", unreachable=False, unreachable_reason=None,
             fetches_used=used, http_requests=len(http_requests), fetch_log=log,
             resolved_domain=dom, domain_confirmed_by=why,
             raw_capture=f"sources/raw/vendors/{rec['company_id']}.txt", retrieved_date=D)
    return e

if __name__ == "__main__":
    lo, hi = int(sys.argv[1]), int(sys.argv[2])
    recs=[json.loads(l) for l in open("outputs/companies.jsonl")]
    for i,r in enumerate(recs):
        if not (lo <= i < hi): continue
        e = run_one(r)
        base = {k:v for k,v in r["enrichment"].items() if k=="status"}
        r["enrichment"] = {**base, **e}
        print(f"  [{i:3d}] {r['company'][:28]:30s} {'UNREACHABLE' if e['unreachable'] else 'ok'} "
              f"f={e['fetches_used']} http={e['http_requests']}")
    with open("outputs/companies.jsonl","w") as f:
        for r in recs: f.write(json.dumps(r,ensure_ascii=False)+"\n")
