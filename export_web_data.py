"""Export a compact data file for the blog post's interactive figures.

Reads results.json (plus mtld and zipf_mean from results_lexical.json)
and writes figures/data.json with only the fields the charts need, plus
a display label per document. The blog copies this file to its own tree
and renders it with Chart.js.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent

LABELS = {
    "clawpatch": "clawpatch.ai", "crabbox": "crabbox.sh", "fs-safe": "fs-safe.io",
    "gitcrawl": "gitcrawl.sh", "gogcli": "gogcli.sh", "goplaces": "goplaces.sh",
    "imsg": "imsg.sh", "mcporter": "mcporter.sh", "spogo": "spogo.sh",
    "wacli": "wacli.sh",
    "sqlite-testing": "SQLite docs", "joel-rewrite": "Spolsky 2000",
    "antirez-terminology": "antirez 2018", "makers-schedule-2009": "Graham 2009",
    "jvns-brag-documents-2019": "Evans 2019", "ripgrep-2016": "ripgrep 2016",
    "redis-2016": "redis 2016", "requests-2017": "requests 2017",
    "this-post": "this post",
}

KEYS = ["em_dash_per_1k", "triads_per_1k", "labeled_bullet_pct_of_bullets",
        "first_person_per_1k", "frag_pct", "ttr_280", "words"]

docs = json.loads((ROOT / "results.json").read_text())["docs"]
lexical = {d["doc"]: d for d in
           json.loads((ROOT / "results_lexical.json").read_text())["docs"]}
flow_data = json.loads((ROOT / "results_flow.json").read_text())
flow = {d["doc"]: d for d in flow_data["docs"]}
out = []
for d in docs:
    label = LABELS.get(d["doc"], "@" + d["doc"] if d["group"] == "tweets" else d["doc"])
    row = {"doc": d["doc"], "group": d["group"], "label": label}
    row.update({k: d[k] for k in KEYS})
    lex = lexical[d["doc"]]
    row["mtld"] = lex["mtld"]
    row["zipf_mean"] = lex["zipf_mean"]
    row["flow"] = flow[d["doc"]]["flow"]
    out.append(row)

# Raw per-sentence run sequences for the two documents the flow section
# uses as its worked example, truncated to what the chart shows.
flow_examples = [
    {"doc": doc, "label": LABELS[doc], "group": group,
     "spines": flow[doc]["spines"][:60]}
    for doc, group in (("antirez-terminology", "human"), ("crabbox", "ai"))
]

(ROOT / "figures" / "data.json").write_text(json.dumps({
    "docs": out,
    "flow_examples": flow_examples,
    "flow_edges": flow_data["edges"],
}, indent=1))
print(f"wrote {len(out)} docs to figures/data.json")
