"""Fetch the fixed 4-page budget per company and write a digest for judgement.
Page 3/4 selection is deterministic and identical for every company."""
import json, re, sys, os, html, subprocess
sys.path.insert(0, "scripts")
from fetch_vendor import get, text, signals

def links(h, base):
    out = []
    for m in re.finditer(r'href=["\']([^"\'#]+)["\']', h, re.I):
        u = m.group(1)
        if u.startswith("/"): u = base.rstrip("/") + u
        if u.startswith("http"): out.append(u)
    return out

PROD = re.compile(r"/(products?|platform|features?|solutions?)(/overview)?/?$", re.I)
PROD_LOOSE = re.compile(r"(product|platform|feature)", re.I)
PRICE = re.compile(r"/(pricing|plans|price)/?$", re.I)
TRUST = re.compile(r"/(trust|security|compliance)/?$", re.I)

def pick(cands, rx, domain):
    root = domain.split(".")[-2]
    hits = [u for u in cands if rx.search(u) and root in u and "cdn." not in u]
    hits.sort(key=len)
    return hits[0] if hits else None

def run(cid, domain):
    base = f"https://{domain}"
    used, log, pages = 0, [], {}
    requests = []
    def fetch(label, url):
        """One budget slot. May issue more than one HTTP request for the SAME logical page
        (www variant, HTTP/1.1 retry); those are recorded but do not consume extra budget."""
        nonlocal used
        if used >= 4 or not url: return None
        used += 1
        attempts = [url]
        if "://www." not in url: attempts.append(url.replace("://", "://www.", 1))
        body = None; code = 0; final = url
        for i, u in enumerate(attempts):
            for h1 in (False, True):
                try: code, final, body = get(u, http1=h1)
                except Exception: code, final, body = 0, u, ""
                requests.append(dict(slot=used, url=u, http1=h1, http=code, bytes=len(body or "")))
                if code == 200 and len(body or "") > 400: break
            if code == 200 and len(body or "") > 400: break
        ok = code == 200 and len(body or "") > 400
        log.append(dict(n=used, label=label, url=url, final_url=final, http=code,
                        bytes=len(body or ""), ok=ok))
        if ok: pages[label] = dict(url=final, html=body)
        return body if ok else None

    llms = fetch("llms.txt", f"{base}/llms.txt")
    home = fetch("homepage", base)
    cands = []
    if llms: cands += re.findall(r"\((https?://[^)]+)\)", llms)
    if home: cands += links(home, base)
    cands = list(dict.fromkeys(cands))
    prod = pick(cands, PROD, domain) or pick(cands, PROD_LOOSE, domain)
    fetch("product", prod)
    p4 = pick(cands, PRICE, domain) or pick(cands, TRUST, domain)
    fetch("pricing_or_trust", p4)

    out = dict(company_id=cid, domain=domain, fetches_used=used, fetch_log=log,
               http_requests=requests,
               unreachable=not any(p["label"] in ("homepage",) and p["ok"] for p in log), pages={})
    dump = []
    for label, p in pages.items():
        t = text(p["html"])
        out["pages"][label] = dict(url=p["url"], signals=signals(p["html"], t), chars=len(t))
        dump.append(f"===== {label} :: {p['url']}\n{t[:14000]}")
    os.makedirs("sources/raw/vendors", exist_ok=True)
    open(f"sources/raw/vendors/{cid}.txt", "w").write("\n\n".join(dump))
    return out

if __name__ == "__main__":
    targets = json.load(open(sys.argv[1]))
    res = [run(cid, dom) for cid, dom in targets]
    json.dump(res, open(sys.argv[2], "w"), ensure_ascii=False, indent=1)
    for r in res:
        got = [l["label"] for l in r["fetch_log"] if l["ok"]]
        print(f"{r['company_id']:16s} fetches={r['fetches_used']} ok={got}")
