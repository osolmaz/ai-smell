"""Render blog figures for the AI de-smeller post.

Figure 1: six-panel horizontal bar chart, one panel per table metric,
eighteen documents in a fixed order, AI pages in orange and human
baselines in blue.
Figure 2: scatter of exactly-three-list rate vs labeled-bullet share, the
two metrics that each classify the whole corpus alone, with the detector
thresholds drawn as dashed reference lines.

Figure 4: scatter of mean Zipf word frequency vs MTLD lexical diversity
(from results_lexical.json), the two word-choice metrics, in the same
style as figure 2, with the tweet samples drawn faintly and the post as
a green diamond.

Figure 3: three vertically stacked scatter panels of the in-the-wild
tweet samples (from results.json) over different metric pairs, with the
ground-truth pages and baselines drawn faintly for reference in every
panel and the detector thresholds marked where they exist. Every panel
also carries the blog post itself as a green diamond. The first panel
repeats figure 2's axes and limits exactly.

Solid light background baked in so the figures read on the blog's light
and dark themes alike.
"""
import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = Path(__file__).resolve().parent / "figures"
OUT.mkdir(parents=True, exist_ok=True)

BG = "#fdfdfd"
PANEL = "#ffffff"
AI_COLOR = "#d97706"
HUMAN_COLOR = "#3b82f6"
TEXT = "#1f2933"
MUTED = "#6b7280"
BORDER = "#d1d5db"

# doc, group, em_dash/1k, triads/1k, labeled-bullet %, first-person/1k,
# fragment %, type-token ratio (first 280 words)
ROWS = [
    ("clawpatch.ai", "ai", 61.3, 9.4, 95.0, 0.0, 3.6, 0.589),
    ("fs-safe.io", "ai", 44.0, 7.3, 91.7, 0.0, 6.5, 0.636),
    ("goplaces.sh", "ai", 20.1, 8.6, 57.1, 0.0, 35.8, 0.636),
    ("spogo.sh", "ai", 19.8, 9.9, 84.6, 0.0, 31.4, 0.589),
    ("mcporter.sh", "ai", 18.8, 6.3, 76.5, 2.1, 25.0, 0.632),
    ("crabbox.sh", "ai", 7.1, 9.1, 53.3, 0.0, 9.2, 0.639),
    ("imsg.sh", "ai", 5.9, 8.9, 94.1, 0.0, 41.9, 0.693),
    ("gitcrawl.sh", "ai", 3.5, 14.0, 55.6, 0.0, 26.1, 0.611),
    ("wacli.sh", "ai", 2.3, 15.9, 85.0, 0.0, 27.5, 0.596),
    ("gogcli.sh", "ai", 0.0, 12.2, 100.0, 0.0, 30.9, 0.614),
    ("ripgrep 2016", "human", 4.7, 0.0, 7.7, 2.4, 3.9, 0.575),
    ("SQLite docs", "human", 1.3, 0.4, 2.9, 3.8, 2.0, 0.532),
    ("redis 2016", "human", 0.0, 1.1, 11.1, 3.2, 2.6, 0.539),
    ("requests 2017", "human", 0.0, 0.0, 0.0, 0.0, 17.4, 0.668),
    ("Spolsky 2000", "human", 0.0, 2.0, 0.0, 8.7, 11.5, 0.586),
    ("Graham 2009", "human", 0.0, 0.0, 0.0, 37.7, 1.4, 0.529),
    ("Evans 2019", "human", 0.0, 0.6, 0.0, 34.3, 1.4, 0.607),
    ("antirez 2018", "human", 0.0, 0.0, 0.0, 50.9, 2.3, 0.539),
]

METRICS = {
    "Em dashes / 1k words": [r[2] for r in ROWS],
    "Exactly-three lists / 1k words": [r[3] for r in ROWS],
    "Labeled bullets (% of bullets)": [r[4] for r in ROWS],
    "First person / 1k words": [r[5] for r in ROWS],
    "Fragment sentences (% of sentences)": [r[6] for r in ROWS],
    "Type-token ratio (first 280 words)": [r[7] for r in ROWS],
}

plt.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["Helvetica Neue", "Helvetica", "Arial", "DejaVu Sans"],
    "text.color": TEXT,
    "axes.edgecolor": BORDER,
    "axes.labelcolor": TEXT,
    "xtick.color": MUTED,
    "ytick.color": TEXT,
    "svg.fonttype": "path",
})


def style_axis(ax):
    ax.set_facecolor(PANEL)
    for spine in ax.spines.values():
        spine.set_color(BORDER)
        spine.set_linewidth(0.8)
    ax.tick_params(length=0)


def fig1():
    fig, axes = plt.subplots(3, 2, figsize=(9.6, 14.8))
    fig.patch.set_facecolor(BG)
    labels = [r[0] for r in ROWS]
    colors = [AI_COLOR if r[1] == "ai" else HUMAN_COLOR for r in ROWS]
    ypos = list(range(len(ROWS)))[::-1]

    for ax, (title, values) in zip(axes.flat, METRICS.items()):
        style_axis(ax)
        ax.barh(ypos, values, height=0.62, color=colors)
        ax.set_yticks(ypos, labels, fontsize=8)
        ax.set_title(title, fontsize=10.5, pad=8, color=TEXT, loc="left", fontweight="bold")
        xmax = max(values) / 0.86
        ax.set_xlim(0, xmax)
        ax.set_xticks([])
        for y, v in zip(ypos, values):
            ax.text(v + xmax * 0.013, y, f"{v:g}", va="center", fontsize=7.5, color=MUTED)

    handles = [
        plt.Rectangle((0, 0), 1, 1, color=AI_COLOR, label="AI-flavored pages"),
        plt.Rectangle((0, 0), 1, 1, color=HUMAN_COLOR, label="Human baselines (pre-LLM)"),
    ]
    fig.legend(handles=handles, loc="lower center", ncol=2, frameon=False,
               fontsize=9, bbox_to_anchor=(0.5, 0.004))
    fig.suptitle("Six metrics across ten AI pages and eight human texts",
                 fontsize=13, fontweight="bold", color=TEXT, x=0.055, ha="left", y=0.992)
    fig.tight_layout(rect=(0, 0.022, 1, 0.968), h_pad=2.2, w_pad=2.4)
    fig.savefig(OUT / "metrics.svg", facecolor=BG)
    fig.savefig(OUT / "metrics.png", facecolor=BG, dpi=200)
    plt.close(fig)


def fig2():
    fig, ax = plt.subplots(figsize=(8.0, 5.6))
    fig.patch.set_facecolor(BG)
    style_axis(ax)

    ax.axvline(3, color=MUTED, linestyle="--", linewidth=1)
    ax.axhline(30, color=MUTED, linestyle="--", linewidth=1)
    ax.text(3.15, 20.5, "triad threshold (3 / 1k)", fontsize=8, color=MUTED, rotation=90)
    ax.text(16.9, 31.8, "labeled-bullet threshold (30%)", fontsize=8, color=MUTED, ha="right")

    offsets = {
        "clawpatch.ai": (0.25, 1.5), "fs-safe.io": (-0.25, 1.8), "goplaces.sh": (-0.28, -1.2),
        "spogo.sh": (0.25, -3.4), "mcporter.sh": (-0.25, 1.8), "crabbox.sh": (0.25, -3.6),
        "imsg.sh": (-0.28, -1.2), "gitcrawl.sh": (0.25, -3.4), "wacli.sh": (0.25, 1.2),
        "gogcli.sh": (0.25, 0.4),
        "ripgrep 2016": (0.25, 1.2), "SQLite docs": (0.25, 1.0), "redis 2016": (0.25, 1.2),
        "Spolsky 2000": (0.15, 1.6), "Evans 2019": (0.2, -3.6),
    }
    for label, group, _, x, y, *_ in ROWS:
        color = AI_COLOR if group == "ai" else HUMAN_COLOR
        ax.scatter(x, y, s=64, color=color, zorder=3, edgecolors="white", linewidths=0.8)
        if label in offsets:
            dx, dy = offsets[label]
            ha = "right" if dx < 0 else "left"
            ax.text(x + dx, y + dy, label, fontsize=8, color=TEXT, ha=ha)
    ax.text(0.15, -5.8, "requests 2017, Graham 2009,\nantirez 2018 at (0, 0)",
            fontsize=8, color=MUTED, ha="left", va="top")

    ax.set_xlim(-0.7, 17.2)
    ax.set_ylim(-11, 106)
    ax.set_xlabel("Exactly-three lists per 1,000 words", fontsize=10)
    ax.set_ylabel("Labeled bullets, % of all bullets", fontsize=10)
    ax.set_title("Either structural metric alone separates the groups",
                 fontsize=13, fontweight="bold", loc="left", pad=10)
    ax.tick_params(labelsize=8.5)

    handles = [
        plt.Line2D([], [], marker="o", linestyle="", color=AI_COLOR, label="AI-flavored pages"),
        plt.Line2D([], [], marker="o", linestyle="", color=HUMAN_COLOR, label="Human baselines (pre-LLM)"),
    ]
    ax.legend(handles=handles, loc="lower right", frameon=False, fontsize=9)
    fig.tight_layout()
    fig.savefig(OUT / "detector.svg", facecolor=BG)
    fig.savefig(OUT / "detector.png", facecolor=BG, dpi=200)
    plt.close(fig)


def fig3():
    docs = json.loads((Path(__file__).resolve().parent / "results.json").read_text())["docs"]
    tw = [r for r in docs if r["group"] == "tweets"]
    self_doc = next(r for r in docs if r["group"] == "self")
    TW_COLOR = "#475569"
    SELF_COLOR = "#16a34a"

    # (title, json x key, json y key, ROWS x idx, ROWS y idx,
    #  x label, y label, x threshold, y threshold)
    panels = [
        ("The detector's two metrics, with its thresholds",
         "triads_per_1k", "labeled_bullet_pct_of_bullets", 3, 4,
         "Exactly-three lists / 1k words", "Labeled bullets, % of bullets", 3, 30),
        ("Em dashes against exactly-three lists",
         "em_dash_per_1k", "triads_per_1k", 2, 3,
         "Em dashes / 1k words", "Exactly-three lists / 1k words", 4.7, 3),
        ("Em dashes against fragment sentences",
         "em_dash_per_1k", "frag_pct", 2, 6,
         "Em dashes / 1k words", "Fragment sentences, % of sentences", 4.7, 17.4),
    ]

    from adjustText import adjust_text

    fig, axes = plt.subplots(3, 1, figsize=(11.0, 22.5))
    fig.patch.set_facecolor(BG)

    for i, (ax, (title, xk, yk, xi, yi, xl, yl, xt, yt)) in enumerate(zip(axes.flat, panels)):
        style_axis(ax)
        if xt is not None:
            ax.axvline(xt, color=MUTED, linestyle="--", linewidth=1)
        if yt is not None:
            ax.axhline(yt, color=MUTED, linestyle="--", linewidth=1)
        for row in ROWS:
            color = AI_COLOR if row[1] == "ai" else HUMAN_COLOR
            ax.scatter(row[xi], row[yi], s=44, color=color, alpha=0.3, zorder=2, linewidths=0)
        xs = [r[xk] for r in tw]
        ys = [r[yk] for r in tw]
        ax.scatter(xs, ys, s=40, color=TW_COLOR, zorder=3, edgecolors="white", linewidths=0.7)
        sx, sy = self_doc[xk], self_doc[yk]
        ax.scatter(sx, sy, s=64, color=SELF_COLOR, zorder=4, marker="D",
                   edgecolors="white", linewidths=0.8)
        import numpy as np
        np.random.seed(0)
        texts = [ax.text(r[xk], r[yk], "@" + r["doc"], fontsize=7, color=TEXT)
                 for r in tw]
        texts.append(ax.text(sx, sy, "this post", fontsize=7.5, color=SELF_COLOR,
                             fontweight="bold"))
        adjust_text(texts, x=xs + [sx] + [row[xi] for row in ROWS],
                    y=ys + [sy] + [row[yi] for row in ROWS], ax=ax,
                    expand=(1.3, 1.7), force_text=(0.4, 0.7), time_lim=5,
                    arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.4, alpha=0.6))
        ax.set_title(title, fontsize=10.5, pad=8, loc="left", fontweight="bold")
        ax.set_xlabel(xl, fontsize=9)
        ax.set_ylabel(yl, fontsize=9)
        ax.tick_params(labelsize=8)

    # match panel 1 to figure 2's limits so the two charts superimpose
    ax0 = axes.flat[0]
    ax0.set_xlim(-0.7, 17.2)
    ax0.set_ylim(-11, 106)
    ax0.text(3.15, 55, "triad threshold (3 / 1k)", fontsize=8, color=MUTED, rotation=90)
    ax0.text(16.9, 32.5, "labeled-bullet threshold (30%)", fontsize=8, color=MUTED, ha="right")

    # label the reference lines in the second and third panels: the
    # detector's triad threshold, and the human-baseline maximum on the
    # axes that carry no threshold (ripgrep 2016 for dashes, the
    # Requests README for fragments)
    axes.flat[1].text(58, 3.25, "triad threshold (3 / 1k)", fontsize=8, color=MUTED, ha="right")
    axes.flat[1].text(5.4, 15.8, "densest human baseline\n(ripgrep, 4.7 / 1k)",
                      fontsize=8, color=MUTED, rotation=90, va="top")
    axes.flat[2].text(5.4, 33.5, "densest human baseline\n(ripgrep, 4.7 / 1k)",
                      fontsize=8, color=MUTED, rotation=90, va="top")
    axes.flat[2].text(58, 19.0, "most fragmented human baseline (Requests, 17.4%)",
                      fontsize=8, color=MUTED, ha="right")

    handles = [
        plt.Line2D([], [], marker="o", linestyle="", color=TW_COLOR,
                   label="Tweet samples (no ground truth)"),
        plt.Line2D([], [], marker="o", linestyle="", color=AI_COLOR, alpha=0.3,
                   label="AI pages (reference)"),
        plt.Line2D([], [], marker="o", linestyle="", color=HUMAN_COLOR, alpha=0.3,
                   label="Human baselines (reference)"),
        plt.Line2D([], [], marker="D", linestyle="", color=SELF_COLOR,
                   label="This post"),
    ]
    fig.legend(handles=handles, loc="lower center", ncol=2, frameon=False,
               fontsize=9, bbox_to_anchor=(0.5, 0.002))
    fig.suptitle("42 accounts' long-form tweets against the ground-truth corpus",
                 fontsize=13, fontweight="bold", color=TEXT, x=0.055, ha="left", y=0.99)
    fig.tight_layout(rect=(0, 0.035, 1, 0.972), h_pad=2.8)
    fig.savefig(OUT / "tweets.svg", facecolor=BG)
    fig.savefig(OUT / "tweets.png", facecolor=BG, dpi=200)
    plt.close(fig)


def fig4():
    root = Path(__file__).resolve().parent
    lex = json.loads((root / "results_lexical.json").read_text())["docs"]
    labels = json.loads((root / "figures" / "data.json").read_text())["docs"]
    label_of = {d["doc"]: d["label"] for d in labels}
    TW_COLOR = "#475569"
    SELF_COLOR = "#16a34a"

    fig, ax = plt.subplots(figsize=(8.0, 5.6))
    fig.patch.set_facecolor(BG)
    style_axis(ax)

    # neither line separates alone (ripgrep crosses the frequency line,
    # Requests crosses the diversity line); the pair does: every AI page
    # sits in the top-left quadrant and no human text enters it
    ax.axvline(5.35, color=MUTED, linestyle="--", linewidth=1)
    ax.axhline(100, color=MUTED, linestyle="--", linewidth=1)
    ax.text(5.36, 45, "word-frequency threshold (Zipf 5.35)", fontsize=8,
            color=MUTED, rotation=90, va="bottom")
    ax.text(4.62, 92, "diversity threshold (MTLD 100)", fontsize=8,
            color=MUTED, ha="left")

    from adjustText import adjust_text
    texts = []
    for d in lex:
        x, y = d["zipf_mean"], d["mtld"]
        if d["group"] == "tweets":
            ax.scatter(x, y, s=26, color=TW_COLOR, alpha=0.35, zorder=2, linewidths=0)
            continue
        if d["group"] == "self":
            ax.scatter(x, y, s=72, color=SELF_COLOR, zorder=4, marker="D",
                       edgecolors="white", linewidths=0.8)
            texts.append(ax.text(x, y, "this post", fontsize=8, color=SELF_COLOR,
                                 fontweight="bold"))
            continue
        color = AI_COLOR if d["group"] == "ai" else HUMAN_COLOR
        ax.scatter(x, y, s=64, color=color, zorder=3, edgecolors="white", linewidths=0.8)
        texts.append(ax.text(x, y, label_of.get(d["doc"], d["doc"]),
                             fontsize=8, color=TEXT))
    adjust_text(texts, ax=ax, expand=(1.25, 1.5), force_text=(0.3, 0.6), time_lim=3,
                arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.4, alpha=0.6))

    ax.set_xlabel("Mean Zipf word frequency (higher = commoner words)", fontsize=10)
    ax.set_ylabel("MTLD lexical diversity", fontsize=10)
    ax.set_title("AI pages use rarer words and rotate them more",
                 fontsize=13, fontweight="bold", loc="left", pad=10)
    ax.tick_params(labelsize=8.5)

    handles = [
        plt.Line2D([], [], marker="o", linestyle="", color=AI_COLOR, label="AI-flavored pages"),
        plt.Line2D([], [], marker="o", linestyle="", color=HUMAN_COLOR, label="Human baselines (pre-LLM)"),
        plt.Line2D([], [], marker="o", linestyle="", color=TW_COLOR, alpha=0.35,
                   label="Tweet samples (no ground truth)"),
        plt.Line2D([], [], marker="D", linestyle="", color=SELF_COLOR, label="This post"),
    ]
    ax.legend(handles=handles, loc="upper right", frameon=False, fontsize=8.5)
    fig.tight_layout()
    fig.savefig(OUT / "lexical.svg", facecolor=BG)
    fig.savefig(OUT / "lexical.png", facecolor=BG, dpi=200)
    plt.close(fig)


def fig5():
    """Two-panel raw sequence view for the flow section: the longest
    unbroken run per sentence, in document order, human vs AI."""
    root = Path(__file__).resolve().parent
    flow = {d["doc"]: d for d in
            json.loads((root / "results_flow.json").read_text())["docs"]}

    picks = [
        ("antirez-terminology", HUMAN_COLOR, "antirez blog post (human, 2018)"),
        ("crabbox", AI_COLOR, "crabbox.sh landing page (AI)"),
    ]
    fig, axes = plt.subplots(2, 1, figsize=(9.6, 5.4))
    fig.patch.set_facecolor(BG)
    for ax, (doc, color, title) in zip(axes, picks):
        style_axis(ax)
        sp = flow[doc]["spines"][:60]
        ax.bar(range(len(sp)), sp, color=color, width=0.8)
        ax.axhline(10, color=MUTED, linestyle="--", linewidth=1)
        ax.set_ylim(0, 42)
        ax.set_ylabel("longest run\n(words)", fontsize=8.5)
        ax.set_title(f"{title}   flow = {flow[doc]['flow']:.2f}",
                     fontsize=10, loc="left", color=TEXT)
    axes[0].text(59, 11, "10 words", fontsize=8, color=MUTED, ha="right", va="bottom")
    axes[1].set_xlabel("sentence number (first 60 sentences)", fontsize=9)
    fig.suptitle("The longest unbroken run of words in each sentence, in order",
                 fontsize=12.5, fontweight="bold", color=TEXT, x=0.06, ha="left")
    fig.tight_layout(rect=(0, 0, 1, 0.95))
    fig.savefig(OUT / "flow-seq.svg", facecolor=BG)
    fig.savefig(OUT / "flow-seq.png", facecolor=BG, dpi=200)
    plt.close(fig)


def fig6():
    """Flow score ranking for the ground-truth corpus plus this post."""
    root = Path(__file__).resolve().parent
    data = json.loads((root / "results_flow.json").read_text())
    labels = json.loads((root / "figures" / "data.json").read_text())["docs"]
    label_of = {d["doc"]: d["label"] for d in labels}
    SELF_COLOR = "#16a34a"

    rows = sorted((d["flow"], d["group"], d["doc"]) for d in data["docs"]
                  if d["group"] in ("ai", "human", "self"))
    colors = {"ai": AI_COLOR, "human": HUMAN_COLOR, "self": SELF_COLOR}

    fig, ax = plt.subplots(figsize=(8.6, 5.8))
    fig.patch.set_facecolor(BG)
    style_axis(ax)
    ys = range(len(rows))
    ax.barh(list(ys), [r[0] for r in rows], height=0.62,
            color=[colors[r[1]] for r in rows])
    ax.set_yticks(list(ys), [label_of.get(r[2], r[2]) for r in rows], fontsize=8)
    thr = data["edges"]["threshold"]
    ax.axvline(thr, color=MUTED, linestyle="--", linewidth=1)
    ax.text(thr, len(rows) - 0.4, f"  midpoint threshold ({thr:.2f})",
            fontsize=8, color=MUTED, va="top")
    ax.set_xlabel("flow score (mean corpus percentile of sentence runs)",
                  fontsize=9.5)
    ax.set_title("Every AI page flows less than every human text",
                 fontsize=13, fontweight="bold", loc="left", pad=10, color=TEXT)
    handles = [
        plt.Rectangle((0, 0), 1, 1, color=AI_COLOR, label="AI-flavored pages"),
        plt.Rectangle((0, 0), 1, 1, color=HUMAN_COLOR, label="Human baselines (pre-LLM)"),
        plt.Rectangle((0, 0), 1, 1, color=SELF_COLOR, label="This post"),
    ]
    ax.legend(handles=handles, loc="lower right", frameon=False, fontsize=8.5)
    fig.tight_layout()
    fig.savefig(OUT / "flow-scores.svg", facecolor=BG)
    fig.savefig(OUT / "flow-scores.png", facecolor=BG, dpi=200)
    plt.close(fig)


def fig7():
    """Flow scores for the 42 tweet samples plus this post, against the
    threshold and group edges learned from the ground-truth corpus."""
    root = Path(__file__).resolve().parent
    data = json.loads((root / "results_flow.json").read_text())
    SELF_COLOR = "#16a34a"
    TW_COLOR = "#64748b"

    rows = sorted((d["flow"], d["group"], d["doc"]) for d in data["docs"]
                  if d["group"] in ("tweets", "self"))
    edges = data["edges"]

    fig, ax = plt.subplots(figsize=(8.6, 10.6))
    fig.patch.set_facecolor(BG)
    style_axis(ax)
    ys = range(len(rows))
    ax.barh(list(ys), [r[0] for r in rows], height=0.62,
            color=[SELF_COLOR if r[1] == "self" else TW_COLOR for r in rows])
    ax.set_yticks(list(ys),
                  ["this post" if r[1] == "self" else "@" + r[2] for r in rows],
                  fontsize=7.5)
    for y, r in zip(ys, rows):
        if r[1] == "self":
            ax.get_yticklabels()[y].set_color(SELF_COLOR)
            ax.get_yticklabels()[y].set_fontweight("bold")
    ax.axvline(edges["threshold"], color=MUTED, linestyle="--", linewidth=1)
    ax.text(edges["threshold"], len(rows) - 0.2,
            f"  midpoint threshold ({edges['threshold']:.2f})",
            fontsize=8, color=MUTED, va="top")
    ax.axvline(edges["ai"], color=AI_COLOR, linestyle=":", linewidth=1)
    ax.text(edges["ai"], -0.6, "highest AI page ", fontsize=7.5,
            color=AI_COLOR, ha="right", va="top")
    ax.axvline(edges["human"], color=HUMAN_COLOR, linestyle=":", linewidth=1)
    ax.text(edges["human"], -0.6, " lowest human baseline", fontsize=7.5,
            color=HUMAN_COLOR, va="top")
    ax.set_xlabel("flow score (mean corpus percentile of sentence runs)",
                  fontsize=9.5)
    ax.set_title("The tweet samples on the flow metric",
                 fontsize=13, fontweight="bold", loc="left", pad=10, color=TEXT)
    fig.tight_layout()
    fig.savefig(OUT / "flow-tweets.svg", facecolor=BG)
    fig.savefig(OUT / "flow-tweets.png", facecolor=BG, dpi=200)
    plt.close(fig)


fig1()
fig2()
fig3()
fig4()
fig5()
fig6()
fig7()
print("written to", OUT)
