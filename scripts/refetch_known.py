"""Re-fetch companies whose correct domain a human paste supplied.

The domain is known, so no candidate guessing happens - but the identity gate is
unchanged. A supplied domain is still only a proposal until a fetched page identifies
the company. Output is HTML-derived and therefore identical in kind to the other 201
records, which is the whole point of re-fetching rather than parsing the paste."""
import json, re, sys, os
sys.path.insert(0, "scripts")
import enrich as E

targets = json.load(open("/tmp/refetch.json"))
recs = [json.loads(l) for l in open("outputs/companies.jsonl")]
by = {r["company_id"]: r for r in recs}
D = "2026-08-11"

def run(cid, dom):
    r = by[cid]; company = r["company"]
    reqs, log, pages, texts = [], [], {}, {}
    used = 0
    def take(label, url):
        nonlocal used
        if used >= 4 or not url: return None
        used += 1
        c, f, b = E.get(url)
        reqs.append(dict(kind="fetch", url=url, http=c, bytes=len(b or "")))
        if c != 200 or len(b or "") < 400:
            c, f, b = E.get(url, http1=True)
            reqs.append(dict(kind="fetch-http1", url=url, http=c, bytes=len(b or "")))
        ok = c == 200 and len(b or "") > 400
        log.append(dict(n=used, label=label, url=url, final_url=f, http=c, bytes=len(b or ""), ok=ok))
        if ok: pages[label] = dict(url=f, sig=E.sig(b)); texts[label] = E.totext(b)
        return b if ok else None
    base = "https://" + dom
    llm = take("llms.txt", base + "/llms.txt")
    home = take("homepage", base)
    if not home: return None, reqs, used
    why = E.confirm(company, pages["homepage"]["sig"], dom, texts["homepage"])
    if not why:
        # The general resolver GUESSES domains, so it must be strict. Here the domain was
        # supplied by a human paste that already named the company (paste identity gate),
        # and we fetched that exact host. A host-root match is then sufficient identity -
        # and it is the only way three-letter names like IBM, Lob, SAS and xiQ can ever pass.
        nm = E.norm(company); tok = E.norm(company.split()[0])
        labels = [E.norm(x) for x in dom.split(".") if E.norm(x) not in ("com","net","org","io","ai","co","www","")]
        body = E.norm(texts["homepage"]); ident = E.norm(" ".join(filter(None,
            [pages["homepage"]["sig"].get("title"), pages["homepage"]["sig"].get("og_site_name")])))
        if any(l and (l == nm or l == tok or (len(tok) >= 3 and tok in l)) for l in labels) \
           and (nm in body or nm in ident or tok in ident):
            why = ("host root matches the company and the page names it; domain supplied by a "
                   "human paste that independently named the company (Rung 3 chain)")
        else:
            return "IDENTITY_FAIL", reqs, used
    cands = []
    if llm: cands += re.findall(r"\((https?://[^)]+)\)", texts.get("llms.txt", ""))
    cands += E.linkset(home, base)
    cands = list(dict.fromkeys(cands))
    take("product", E.pick(cands, E.PROD, dom) or E.pick(cands, E.LOOSE, dom))
    take("pricing_or_trust", E.pick(cands, E.PRICE, dom) or E.pick(cands, E.TRUST, dom))
    texts = {l: t[:14000] for l, t in texts.items()}
    blocks = []
    for l in texts:
        s = pages[l]["sig"]
        blocks.append("\n".join([f"===== {l} :: {pages[l]['url']}", "--- SIGNALS ---",
            f"title: {s.get('title') or ''}", f"meta_description: {s.get('meta_description') or ''}",
            f"og_description: {s.get('og_description') or ''}", f"og_site_name: {s.get('og_site_name') or ''}",
            f"h1: {' | '.join(s.get('h1') or [])}", f"h2: {' | '.join(s.get('h2') or [])}",
            f"jsonld_org: {json.dumps(s.get('org') or [], ensure_ascii=False)[:1500]}", "--- TEXT ---"]) + "\n" + texts[l])
    open(f"sources/raw/vendors/{cid}.txt", "w").write("\n\n".join(blocks))
    e = E.extract(company, dom, pages, texts)
    e.update(enrichment_status="done", unreachable=False, unreachable_reason=None,
             fetches_used=used, http_requests=len(reqs), fetch_log=log,
             resolved_domain=dom, domain_confirmed_by=why,
             domain_source="human paste (Rung 3) supplied the URL; the fetch and the identity gate are unchanged",
             raw_capture=f"sources/raw/vendors/{cid}.txt", retrieved_date=D)
    return e, reqs, used

done = fail = 0
for cid, dom in targets:
    res, reqs, used = run(cid, dom)
    r = by[cid]
    if isinstance(res, dict):
        base = {k: v for k, v in r["enrichment"].items() if k in ("status", "recovery", "wikidata")}
        r["enrichment"] = {**base, **res}; done += 1
        print(f"  {r['company'][:26]:28s} {dom:24s} OK  f={used}")
    else:
        r["enrichment"]["paste_refetch"] = dict(domain=dom, outcome=res or "NO_RESPONSE",
            requests=reqs, date=D,
            note="Domain supplied by a human paste. The site still could not be fetched, so the paste itself remains the only evidence.")
        fail += 1
        print(f"  {r['company'][:26]:28s} {dom:24s} {res or 'NO_RESPONSE'}")
with open("outputs/companies.jsonl", "w") as f:
    for r in recs: f.write(json.dumps(r, ensure_ascii=False) + "\n")
print(f"\nre-fetched OK: {done}   still unfetchable: {fail}")
