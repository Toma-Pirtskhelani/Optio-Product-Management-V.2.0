# sources/raw/ — verbatim captures

**The most valuable directory in this repository.** Everything else is derived from it and
can be rebuilt; this cannot. It is committed in full, always, and `.gitignore` explicitly
refuses to cover it.

## The rule

Content goes here **unedited**. No summarizing, no reformatting, no cleaning, no trimming of
"irrelevant" navigation, no fixing of encoding. A capture that has been tidied is a capture
that has been sampled a second time, by whoever tidied it.

**If a parsed row and the raw file ever disagree, the raw file wins.**

## Naming

```
<YYYY-MM-DD>__<source>__<slug>__<rung>[__<paste_id>].md
```

Examples of the shape (not of real captures):
`2026-08-11__g2__category-<slug>__r1.md`
`2026-08-11__gartner__market-<slug>__r3__P-0004.md`

- `source` — `g2` / `gartner` / `<marketplace_id>`
- `rung` — `r1`–`r4`, which ladder rung produced it
- `paste_id` — present only for human-transported content

Two captures of the same URL on different dates are **two files**. Never overwrite. The
two-capture comparison is this study's only mechanism for detecting that something
disappeared (`research-protocol.md` §6), and overwriting destroys it.

## Header block — required at the top of every capture file

```
---
url:            <exact URL>
source:         <g2 | gartner | marketplace_id>
capture_date:   <YYYY-MM-DD>
rung:           <1 | 2 | 3 | 4>
transport:      <fetch | paste>
paste_id:       <P-NNNN | —>
source_class:   <SELF-DECLARED | REVEALED-BEHAVIOR>
language:       <ISO code>
visible_count:  <n | n/a>
total_count:    <n | UNKNOWN>
pagination:     <none | page X of Y | unknown>
sort_order:     <as displayed | UNKNOWN>
filters_active: <verbatim | none | UNKNOWN>
notes:          <truncation, sponsored markers, anything not as requested>
---
```

Below the header: the content, verbatim.

## What must never end up here

- Secrets or credentials — nothing in this study needs one.
- Large binaries. Text captures only; if a page's evidence is an image, describe what is
  visible in `notes` and keep the text.
- **Anything naming the client's product or customers.** Per `CLAUDE.md` §2, report it
  immediately and stop using the file.
