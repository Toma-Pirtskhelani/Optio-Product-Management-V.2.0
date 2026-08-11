"""Paste-mode extraction: for vendors whose site still refuses a fetch, the human-transported
plain text is the only evidence there is.

Plain text has no <meta description> and no <h1>, so the fields cannot be derived from the same
elements as the other 218 records. Every cell therefore carries extraction_mode: paste-text and
a basis saying which line of the paste it came from. It is graded PRIMARY - the source of record,
human transport - but it is NOT the same evidence type as an HTML-derived cell, and the record
says so rather than letting the two blur."""
import json, re, sys
sys.path.insert(0, "scripts"); import enrich as E
D = "2026-08-11"
plan = {x[2]: x for x in json.load(open("/tmp/paste_plan.json")) if x[3] != "ARTEFACT"}
recs = [json.loads(l) for l in open("outputs/companies.jsonl")]

CH = E.CH
def cell(v, u, basis, grade="PRIMARY"):
    return dict(value=v, source_url=u, rung=3, grade=grade, retrieved_date=D,
                extraction_mode="paste-text", basis=basis)

def lines_of(p):
    return [l.strip() for l in open(p, encoding="utf-8", errors="replace").read().split("\n") if l.strip()]

n = 0
for r in recs:
    e = r["enrichment"]
    if e["enrichment_status"] not in ("unreachable","paste_only"): continue
    x = plan.get(r["company_id"])
    if not x or not x[7]: continue                 # no paste, or paste rejected
    p, _, cid, kind, url, host, pre, ok, why = x
    if kind not in ("VENDOR_SITE", "VENDOR_PAGE_NO_URL"): continue   # third-party handled separately
    L = lines_of(p)
    body = "\n".join(L)
    src = url or f"human paste, no URL supplied (sources/raw/vendors-pasted/{cid}.txt)"
    NAV = re.compile(r"^(https?://|skip to|menu$|login$|log in$|sign in$|book demo|contact us$|search$)|logo$|cookie", re.I)
    def usable(l, lo, hi, minwords):
        return lo < len(l) < hi and not NAV.search(l) and len(l.split()) >= minwords
    # A sentence-shaped line is a defensible stand-in for a positioning statement.
    # Anything weaker is left UNKNOWN: a URL string or "Emailidea logo" in description_own
    # is worse than an empty cell, because it looks like data.
    desc = next((l for l in L[:60] if usable(l, 40, 400, 6)), None)
    if desc:
        e["description_own"] = cell(desc, src,
            "first sentence-shaped line (>=6 words) in the first 60 lines of the pasted page. Plain text carries no meta description, so this is an analogue and not the element the HTML-derived records use.")
    else:
        e["description_own"] = dict(value=None, source_url=None, rung=None, grade="UNKNOWN",
            retrieved_date=D, note="Pasted plain text contained no sentence-shaped line; plain text has no meta description to fall back on.")
    # value_proposition is NOT extracted in paste mode. A sentence-shaped filter makes
    # description_own defensible; there is no equivalent structural signal for a headline in
    # plain text, and guessing positionally returned navigation - "Partner Login",
    # "Slide 2 of 6.", "Demos and trials". An empty cell beats a cell that looks like data.
    vp = None
    e["value_proposition"] = dict(value=None, source_url=None, rung=None, grade="UNKNOWN",
        retrieved_date=D,
        note="Not extracted in paste mode: plain text carries no <h1>, and positional guessing "
             "returns navigation rather than a headline. UNKNOWN is the accurate answer.")
    hits, ev = [], {}
    for k, pat in CH.items():
        m = re.search(pat, body, re.I)
        if m: hits.append(k); ev[k] = re.sub(r"\s+", " ", body[max(0, m.start()-45):m.end()+45]).strip()
    if hits:
        c = cell(hits, src, "controlled vocabulary matched across the whole pasted page. The page is the vendor's own, but this is a wider match window than the HTML path uses, which biases toward more channels.")
        c["evidence"] = ev
        e["channels"] = c
    e["enrichment_status"] = "paste_only"
    e["unreachable"] = False
    e["paste_source"] = dict(file=f"sources/raw/vendors-pasted/{cid}.txt", url=url, rung=3,
        classification=kind, identity=why, preamble_lines_discarded=pre,
        note="Site refuses automated fetching. Human-transported text is the only evidence. Fields are paste-derived and not interchangeable with HTML-derived fields.")
    n += 1
    print(f"  {r['company'][:26]:28s} desc={'y' if desc else 'n'} vp={'y' if vp else 'n'} channels={len(hits)}")
with open("outputs/companies.jsonl", "w") as f:
    for r in recs: f.write(json.dumps(r, ensure_ascii=False) + "\n")
print(f"\npaste-mode records: {n}")
