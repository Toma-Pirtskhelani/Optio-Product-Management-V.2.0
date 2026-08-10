"""Regenerate outputs/companies-index.md from companies.jsonl. A view, never a source."""
import json, os, datetime
recs=[json.loads(l) for l in open("outputs/companies.jsonl")]
def v(r,k):
    c=r["enrichment"].get(k) or {}
    x=c.get("value")
    return x if x not in (None,"",[]) else None
rows=[]
for r in recs:
    e=r["enrichment"]
    rows.append(dict(
        company=r["company"], cid=r["company_id"],
        hq=v(r,"hq_country") or "—", founded=v(r,"founded_year") or "—",
        status=v(r,"status") or "—",
        deploy=", ".join(v(r,"solution_type") or []) or "—",
        ch=len(v(r,"channels") or []), ind=len(v(r,"industries_served") or []),
        cats=r["category_count"], src="B" if r["in_both_sources"] else ("G" if r["sources"]==["gartner"] else "2"),
        st=e["enrichment_status"][0].upper(), fu=e["fetches_used"]))
rows.sort(key=lambda x:(-x["cats"], x["company"].lower()))
done=sum(1 for r in recs if r["enrichment"]["enrichment_status"]=="done")
L=[ "# Companies index",
    "",
    f"**{len(recs)} companies.** A generated **view** over `companies.jsonl` — never edit it, regenerate it.",
    f"Enriched so far: **{done} of {len(recs)}**. Regenerated {datetime.date.today().isoformat()}.",
    "",
    "Pull a full record by id:",
    "",
    "```bash",
    "grep '\"company_id\": \"braze\"' outputs/companies.jsonl | jq .",
    "jq -c 'select(.category_count>=5) | {company, channels:.enrichment.channels.value}' outputs/companies.jsonl",
    "```",
    "",
    "`Src` — **B** both sources · **G** Gartner only · **2** G2 only.  ",
    "`St` — enrichment state: **N** not started · **D** done · **U** unreachable.  ",
    "`Ch` / `Ind` — count of channels / industries served.  ",
    "A dash means `UNKNOWN`: not found within the fixed four-fetch budget, which is a finding, not a gap in effort.",
    "",
    "| Company | HQ | Founded | Status | Deployment | Ch | Ind | Cats | Src | St | F |",
    "|---|---|---|---|---|---|---|---|---|---|---|"]
for r in rows:
    L.append(f"| {r['company']} | {r['hq']} | {r['founded']} | {r['status']} | {r['deploy']} | "
             f"{r['ch'] or '—'} | {r['ind'] or '—'} | {r['cats']} | {r['src']} | {r['st']} | {r['fu']} |")
open("outputs/companies-index.md","w").write("\n".join(L)+"\n")
print("index KB:", round(os.path.getsize("outputs/companies-index.md")/1024,1), "| rows:", len(rows))
