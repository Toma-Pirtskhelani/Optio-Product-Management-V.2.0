"""Phase A+B recovery for unreachable companies.

Domain comes from Wikidata (a proposal) or from a candidate that returned 403 during the
main pass (proof the domain exists). Either way the identity gate is unchanged: nothing is
recorded unless a fetched page identifies the company.

Rung-2 alternates are tried before giving up - the pattern that rescued research.g2.com
earlier in this study and was never applied at vendor level."""
import json, re, sys, os
sys.path.insert(0, "scripts")
import enrich as E

wd = json.load(open("/tmp/wd_out.json"))
recs = [json.loads(l) for l in open("outputs/companies.jsonl")]

def known_domain(r):
    """Wikidata proposal first; else a candidate that 403'd, which proves it exists."""
    w = wd.get(r["company"]) or {}
    if w.get("host"): return w["host"], f"wikidata {w['qid']}"
    for a in r["enrichment"].get("resolve_attempts", []):
        if a["http"] in (401, 403, 405, 429):
            return re.sub(r"^https?://(www\.)?", "", a["url"]).rstrip("/"), "403 during main pass (domain exists)"
    return None, None

ALT = ["https://{d}/llms.txt", "https://{d}/sitemap.xml", "https://docs.{d}",
       "https://developers.{d}", "https://help.{d}", "https://www.{d}"]

changed = 0
for i, r in enumerate(recs):
    e = r["enrichment"]
    if not e.get("unreachable"): continue
    dom, why = known_domain(r)
    if not dom: continue
    reqs = []
    # 1) the domain itself, through the normal gate
    code, final, body = E.get("https://" + dom)
    reqs.append(dict(kind="recover", url="https://"+dom, http=code, bytes=len(body or "")))
    hit = None
    if code == 200 and len(body or "") > 400:
        s = E.sig(body)
        if E.confirm(r["company"], s, dom, E.totext(body)): hit = ("https://"+dom, body, s)
    # 2) Rung-2 alternates
    if not hit:
        for pat in ALT:
            u = pat.format(d=dom)
            c2, f2, b2 = E.get(u)
            reqs.append(dict(kind="rung2", url=u, http=c2, bytes=len(b2 or "")))
            if c2 == 200 and len(b2 or "") > 400:
                s2 = E.sig(b2)
                if E.confirm(r["company"], s2, dom, E.totext(b2)):
                    hit = (f2 or u, b2, s2); break
    e.setdefault("recovery", {})
    e["recovery"] = dict(attempted=True, domain=dom, domain_source=why,
                         requests=reqs, recovered=bool(hit),
                         date="2026-08-11")
    print(f"  {r['company'][:26]:28s} {dom:26s} {'RECOVERED via '+hit[0] if hit else 'still unreachable'}")
    if hit:
        r["_recover_url"] = hit[0]; changed += 1
with open("outputs/companies.jsonl","w") as f:
    for r in recs: f.write(json.dumps({k:v for k,v in r.items() if k!="_recover_url"}, ensure_ascii=False)+"\n")
json.dump([r["company_id"] for r in recs if r.get("_recover_url")], open("/tmp/recovered.json","w"))
print(f"\nrecovered: {changed}")
