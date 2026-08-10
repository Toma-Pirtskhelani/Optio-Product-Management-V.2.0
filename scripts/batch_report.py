import json,sys
lo,hi=int(sys.argv[1]),int(sys.argv[2])
recs=[json.loads(l) for l in open('outputs/companies.jsonl')]
sl=[r for r in recs[lo:hi] if r['enrichment']['enrichment_status'] in ('done','unreachable')]
cum=[r for r in recs if r['enrichment']['enrichment_status'] in ('done','unreachable')]
F=["website","hq_country","founded_year","description_own","value_proposition","functionality",
   "channels","solution_type","industries_served","vertical_focus","pricing_url","pricing_published",
   "pricing_detail","has_free_tier","has_contact_sales_tier"]
def filled(v):
    # False is a real answer for the boolean fields (no free tier), not an empty cell.
    return v is not None and v != "" and v != []
def rate(rs,f): return sum(1 for r in rs if filled((r['enrichment'].get(f) or {}).get('value')))
un=[r['company'] for r in sl if r['enrichment']['unreachable']]
print(f"BATCH {lo}-{hi-1}: done={len(sl)} unreachable={len(un)} mean_fetches={sum(r['enrichment']['fetches_used'] for r in sl)/max(1,len(sl)):.1f}")
if un: print("  unreachable:", ", ".join(un))
print(f"  {'field':24s} {'batch':>7s} {'cumulative':>12s}")
for f in F:
    b=rate(sl,f); c=rate(cum,f)
    flag=" <25%" if c/len(cum)<0.25 else ""
    print(f"  {f:24s} {b:3d}/{len(sl):<3d} {c:5d}/{len(cum):<4d} {c/len(cum)*100:5.0f}%{flag}")
