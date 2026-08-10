"""Fetch up to 4 pages of a vendor's own site and dump a deterministic digest.
No model reads the page. Extraction is regex/HTML only; judgement happens afterwards
against the saved text, so every quote can be checked against sources/raw/vendors/."""
import json, re, subprocess, sys, html, os

UA = "Mozilla/5.0 (compatible; research-study/1.0)"
def get(url, timeout=20, http1=False):
    cmd = ["curl","-sS","-L","--max-time",str(timeout),"-A",UA]
    if http1: cmd.append("--http1.1")
    r = subprocess.run(cmd + [
                        "-w","\n__HTTP__%{http_code}__URL__%{url_effective}","-o","-",url],
                       capture_output=True, text=True)
    body = r.stdout or ""
    m = re.search(r"\n__HTTP__(\d+)__URL__(.*)$", body, re.S)
    code, final = (m.group(1), m.group(2).strip()) if m else ("000", url)
    if m: body = body[:m.start()]
    return int(code), final, body

def text(h):
    h = re.sub(r"<(script|style|noscript|svg)[^>]*>.*?</\1>", " ", h, flags=re.S|re.I)
    t = html.unescape(re.sub(r"<[^>]+>", "\n", h))
    return re.sub(r"\n{2,}", "\n", re.sub(r"[ \t]+", " ", t)).strip()

def signals(h, t):
    s = {}
    def one(pat, flags=re.I|re.S):
        m = re.search(pat, h, flags); return html.unescape(m.group(1)).strip() if m else None
    s["title"] = one(r"<title[^>]*>(.*?)</title>")
    s["meta_description"] = one(r'<meta[^>]+name=["\']description["\'][^>]+content=["\'](.*?)["\']') \
        or one(r'<meta[^>]+content=["\'](.*?)["\'][^>]+name=["\']description["\']')
    s["og_description"] = one(r'<meta[^>]+property=["\']og:description["\'][^>]+content=["\'](.*?)["\']')
    s["og_site_name"] = one(r'<meta[^>]+property=["\']og:site_name["\'][^>]+content=["\'](.*?)["\']')
    s["h1"] = [html.unescape(re.sub(r"<[^>]+>","",x)).strip() for x in re.findall(r"<h1[^>]*>(.*?)</h1>", h, re.S|re.I)][:4]
    s["h2"] = [html.unescape(re.sub(r"<[^>]+>","",x)).strip() for x in re.findall(r"<h2[^>]*>(.*?)</h2>", h, re.S|re.I)][:25]
    ld = []
    for blk in re.findall(r'<script[^>]+application/ld\+json[^>]*>(.*?)</script>', h, re.S|re.I):
        try: ld.append(json.loads(blk.strip()))
        except Exception: pass
    def walk(o, out):
        if isinstance(o, dict):
            if o.get("@type") in ("Organization","Corporation","SoftwareApplication") or "foundingDate" in o:
                out.append({k: o.get(k) for k in ("@type","name","foundingDate","url","address","legalName") if k in o})
            for v in o.values(): walk(v, out)
        elif isinstance(o, list):
            for v in o: walk(v, out)
    org = []; walk(ld, org); s["jsonld_org"] = org[:4]
    return s

def probe(company_id, urls):
    used, log, pages = 0, [], {}
    for label, url in urls:
        if used >= 4: break
        used += 1
        try: code, final, body = get(url)
        except Exception as ex: code, final, body = 0, url, ""
        ok = code == 200 and len(body) > 500
        log.append(dict(n=used, label=label, url=url, final_url=final, http=code, bytes=len(body), ok=ok))
        if ok: pages[label] = dict(url=final, html=body)
    return used, log, pages

if __name__ == "__main__":
    cid, domain = sys.argv[1], sys.argv[2]
    base = f"https://{domain}"
    plan = [("llms.txt", f"{base}/llms.txt"), ("homepage", base)]
    used, log, pages = probe(cid, plan)
    out = dict(company_id=cid, domain=domain, fetch_log=log, fetches_used=used, pages={})
    dump = []
    for label, p in pages.items():
        t = text(p["html"])
        out["pages"][label] = dict(url=p["url"], signals=signals(p["html"], t), chars=len(t))
        dump.append(f"===== {label} :: {p['url']}\n{t[:14000]}")
    os.makedirs("sources/raw/vendors", exist_ok=True)
    open(f"sources/raw/vendors/{cid}.txt","w").write("\n\n".join(dump))
    print(json.dumps(out, ensure_ascii=False, indent=1)[:4000])
