import json,re,collections,os
recs=[json.loads(l) for l in open('outputs/companies.jsonl')]
done=[r for r in recs if r['enrichment']['enrichment_status'] in ("done","unreachable","partially_recovered","paste_only","third_party_only")]
un=[r for r in done if r['enrichment'].get('unreachable')]
rows=["# Blocked and unresolved domains — handoff to a later human-transport pass","",
 "Companies this pass could not reach at Rungs 1–2. **No paste was requested during the pass**",
 "and **no user-agent was spoofed** to get past a refusal.","",
 f"**{len(un)} of {len(done)} attempted ({len(un)/max(1,len(done))*100:.0f}%).**","",
 "| Company | Cause | Best HTTP | Candidates tried |","|---|---|---|---|"]
k=collections.Counter()
for r in sorted(un,key=lambda x:x['company'].lower()):
    a=r['enrichment'].get('resolve_attempts',[]); best=max((x['http'] for x in a),default=0)
    kind=("blocked (403/401/429)" if best in (401,403,405,429) else
          "no DNS / no response" if best==0 else
          "served a page that did not identify the company (parked, for-sale, or a different owner)" if best==200 else f"HTTP {best}")
    k[kind]+=1
    rows.append(f"| {r['company']} | {kind} | {best or '—'} | {', '.join(dict.fromkeys(re.sub('^https://','',x['url']) for x in a))[:80]} |")
rec=[r for r in recs if r['enrichment']['enrichment_status']=='partially_recovered']
rows+=["","## Partially recovered — domain confirmed, marketing site still blocked","",
 f"**{len(rec)} companies** were reached only through a documentation, developer or support",
 "subdomain after their marketing site refused automated access. That confirms the company is",
 "live and the domain is correct. It establishes nothing about positioning, channels, pricing",
 "or deployment, so those fields remain `UNKNOWN` — filling them from a docs page would mix two",
 "different kinds of evidence under one field name.","",
 "| Company | Reached via |","|---|---|"]
for r in sorted(rec,key=lambda x:x['company'].lower()):
    rows.append(f"| {r['company']} | {r['enrichment']['recovery_evidence']['url']} |")
rows+=["","## Cause breakdown",""]+[f"- **{a}** — {b}" for a,b in k.most_common()]
rows+=["","Each remains a full record in `companies.jsonl` with `unreachable: true` and its reason.",
"None was dropped; none was filled from memory.","",
"**Name-derived domain guessing has a structural limit.** Where a listing name is not the web",
"brand — Zeta for Zeta Global, Capillary Technologies for capillarytech.com — no candidate ladder",
"reaches it. Those need the vendor URL from a source that publishes it.",""]
open('outputs/blocked-domains.md','w').write("\n".join(rows))
print(f"blocked: {len(un)}/{len(done)}", dict(k))
