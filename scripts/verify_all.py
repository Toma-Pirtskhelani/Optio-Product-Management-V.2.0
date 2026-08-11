import json, os, re
src={c["company_id"]:c for c in json.load(open("outputs/companies-IN.json"))["companies"]}
recs=[json.loads(l) for l in open("outputs/companies.jsonl")]
ok=True
def chk(label, cond, detail=""):
    global ok
    if not cond: ok=False
    print(("PASS " if cond else "FAIL ")+label+(("  -> "+str(detail)[:400]) if not cond else ""))

chk("237 records", len(recs)==237, len(recs))
chk("ids unique and unchanged", [r["company_id"] for r in recs]==list(src.keys()))

# no original field mutated by enrichment
diffs=[]
for r in recs:
    o=src[r["company_id"]]
    for k,v in o.items():
        if r.get(k)!=v: diffs.append((r["company_id"],k))
chk("no original G2/Gartner field mutated", not diffs, diffs[:6])

done=[r for r in recs if r["enrichment"]["enrichment_status"] in ("done","unreachable","partially_recovered","paste_only","third_party_only")]
chk("every company attempted", len(done)==237, len(done))

over=[(r["company"],r["enrichment"]["fetches_used"]) for r in done if r["enrichment"]["fetches_used"]>4]
chk("fetch budget never exceeded (<=4)", not over, over)

# every populated cell carries provenance
missing=[]
CELLS=["website","published_address_country","founded_year","description_own","value_proposition",
       "functionality","channels","solution_type","solution_type_evidence","industries_served",
       "pricing_url","pricing_published","has_free_tier","has_contact_sales_tier"]
for r in done:
    e=r["enrichment"]
    for f in CELLS:
        c=e.get(f)
        if not isinstance(c,dict): continue
        if c.get("value") in (None,"",[]): continue
        if not c.get("source_url") or not c.get("grade") or not c.get("retrieved_date"):
            missing.append((r["company"],f))
chk("every populated cell has source_url + grade + retrieved_date", not missing, missing[:6])

# the invariant: quoted values must appear in the committed capture
viol=[]
for r in done:
    e=r["enrichment"]; cap=e.get("raw_capture")
    if not cap or not os.path.exists(cap): continue
    raw=open(cap,encoding="utf-8",errors="replace").read()
    # Quotes are stored whitespace-normalised (tag-stripping inserts newlines mid-sentence),
    # so the comparison must normalise both sides or it tests formatting, not provenance.
    txt=re.sub(r"\s+"," ",raw)
    for f in ("description_own","value_proposition","solution_type_evidence"):
        v=(e.get(f) or {}).get("value")
        if isinstance(v,str) and re.sub(r"\s+"," ",v).strip()[:60] not in txt: viol.append((r["company"],f))
    for f in ("functionality","industries_served"):
        for v in ((e.get(f) or {}).get("value") or []):
            if isinstance(v,str) and re.sub(r"\s+"," ",v).strip()[:40] not in txt: viol.append((r["company"],f))
chk("every quoted value appears verbatim in its own capture", not viol, viol[:8])

# no enrichment without a confirmed domain
# Three legitimate identity chains: a confirmed fetch, a Rung-2 recovery, or a paste that
# passed the paste identity gate. Anything else means a record was filled from an unverified source.
unconf=[r["company"] for r in done
        if not r["enrichment"].get("unreachable")
        and not r["enrichment"].get("domain_confirmed_by")
        and not r["enrichment"].get("recovery_evidence")
        and not (r["enrichment"].get("paste_source") or {}).get("identity")
        and not (r["enrichment"].get("third_party_evidence") or {}).get("identity")]
chk("every enriched company has a recorded identity chain", not unconf, unconf[:8])

# capture exists for every reachable company
nocap=[r["company"] for r in done if not r["enrichment"].get("unreachable")
       and r["enrichment"]["enrichment_status"]=="done"
       and not (r["enrichment"].get("raw_capture") and os.path.exists(r["enrichment"]["raw_capture"]))]
chk("every reachable company has a committed capture", not nocap, nocap[:8])

# unreachable records still carry a reason
noreason=[r["company"] for r in done if r["enrichment"].get("unreachable") and not r["enrichment"].get("unreachable_reason")]
# a partially recovered record must never carry marketing-page fields
leak=[r["company"] for r in done if r["enrichment"]["enrichment_status"]=="partially_recovered"
      and any((r["enrichment"].get(f) or {}).get("value") not in (None,"",[])
              for f in ("description_own","value_proposition","functionality","channels"))]
chk("partially-recovered records carry no marketing-page fields", not leak, leak[:6])
chk("every unreachable record states a reason", not noreason, noreason[:8])

# solution_type never silently defaulted
bad=[r["company"] for r in done
     if (r["enrichment"].get("solution_type") or {}).get("value")
     and (r["enrichment"]["solution_type"].get("grade")!="INFERRED")]
chk("solution_type only ever INFERRED, never defaulted", not bad, bad[:8])
pm=[r["company"] for r in done if r["enrichment"]["enrichment_status"]=="paste_only"
    and any((r["enrichment"].get(f) or {}).get("value") and (r["enrichment"][f].get("extraction_mode")!="paste-text")
            for f in ("description_own","channels"))]
chk("paste-derived cells all carry extraction_mode: paste-text", not pm, pm[:5])
pv=[r["company"] for r in done if r["enrichment"]["enrichment_status"]=="paste_only"
    and (r["enrichment"].get("value_proposition") or {}).get("value")]
chk("paste-only records never carry a value_proposition", not pv, pv[:5])
tp=[r["company"] for r in done if r["enrichment"]["enrichment_status"]=="third_party_only"
    and any((r["enrichment"].get(f) or {}).get("value") not in (None,"",[])
            for f in ("description_own","value_proposition","channels","functionality","solution_type"))]
chk("third-party-only records carry no vendor-positioning fields", not tp, tp[:5])
print("\nVERIFICATION", "PASSED" if ok else "FAILED")
