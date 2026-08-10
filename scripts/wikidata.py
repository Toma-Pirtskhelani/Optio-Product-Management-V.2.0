"""Wikidata is a CANDIDATE GENERATOR ONLY.

It proposes an official-website domain and firmographics. Nothing it says is recorded
until the existing identity gate confirms a fetch of that domain. Its coverage of this
population is patchy and its search disambiguates badly ("Bloomreach" -> an open-source
CMS), so it is never trusted directly."""
import json, re, subprocess, urllib.parse, sys

UA = "Mozilla/5.0 (compatible; research-study/1.0)"
def api(url):
    r = subprocess.run(["curl","-sS","--max-time","20","-A",UA,url], capture_output=True)
    try: return json.loads((r.stdout or b"").decode("utf-8","replace"))
    except Exception: return None

SOFTWARE_HINTS = re.compile(r"software|platform|company|technolog|marketing|saas|corporation|enterprise|business|firm|cloud|app", re.I)

def lookup(name):
    q = urllib.parse.quote(name)
    d = api(f"https://www.wikidata.org/w/api.php?action=wbsearchentities&search={q}&language=en&format=json&limit=5")
    if not d: return None
    for hit in d.get("search", []):
        desc = hit.get("description","") or ""
        # cheap pre-filter: an entity described as a commune, surname or article is not our company
        if not SOFTWARE_HINTS.search(desc): continue
        ent = api(f"https://www.wikidata.org/wiki/Special:EntityData/{hit['id']}.json")
        if not ent: continue
        e = list(ent["entities"].values())[0]; c = e.get("claims", {})
        def first(p):
            try: return c[p][0]["mainsnak"]["datavalue"]["value"]
            except Exception: return None
        site = first("P856")
        host = re.sub(r"^www\.","",urllib.parse.urlparse(site).netloc) if isinstance(site,str) else None
        inc = first("P571"); inc = re.search(r"(\d{4})", inc["time"]).group(1) if isinstance(inc,dict) and inc.get("time") else None
        return dict(qid=hit["id"], label=hit.get("label"), description=desc,
                    website=site, host=host, inception=int(inc) if inc else None,
                    owned_by=(first("P127") or {}).get("id") if isinstance(first("P127"),dict) else None,
                    dissolved=bool(first("P576")))
    return None

if __name__ == "__main__":
    names = json.load(open(sys.argv[1]))
    out = {}
    for n in names:
        r = lookup(n)
        out[n] = r
        print(f"  {n[:30]:32s} {'-> '+str(r['qid'])+' '+(r['host'] or 'no-website') if r else 'no usable entity'}")
    json.dump(out, open(sys.argv[2],"w"), ensure_ascii=False, indent=1)
