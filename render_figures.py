"""Render blog figures for the AI de-smeller post.

Figure 1: six-panel horizontal bar chart, one panel per table metric,
eighteen documents in a fixed order, AI pages in orange and human
baselines in blue.
Figure 2: scatter of exactly-three-list rate vs labeled-bullet share, the
two metrics that each classify the whole corpus alone, with the detector
thresholds drawn as dashed reference lines.

Figure 3: scatter of the in-the-wild tweet samples (from results.json)
on the dash and triad axes, with the detector's triad threshold and the
AI-page dash line for reference.

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

    fig, ax = plt.subplots(figsize=(8.0, 5.6))
    fig.patch.set_facecolor(BG)
    style_axis(ax)

    ax.axvline(10, color=MUTED, linestyle="--", linewidth=1)
    ax.axhline(3, color=MUTED, linestyle="--", linewidth=1)
    ax.text(10.4, 5.7, "AI-page dash territory (10 / 1k)", fontsize=8, color=MUTED,
            rotation=90, va="top")
    ax.text(35.3, 3.12, "triad threshold (3 / 1k)", fontsize=8, color=MUTED, ha="right")

    labels = {
        "TraffAlex": (0.5, 0.1), "elder_plinius": (0.5, 0.1), "quasa0": (0.5, -0.28),
        "justinskycak": (0.5, 0.1), "kwindla": (-0.5, 0.12), "davepl1968": (0.5, -0.15),
        "TheValueist": (0.5, 0.05), "TheAhmadOsman": (0.5, 0.05), "vllm_project": (0.5, 0.05),
        "ClementDelangue": (0.5, -0.22), "analogalok": (0.3, -0.3), "onusoz": (0.5, 0.05),
        "bryan_johnson": (0.5, 0.05),
    }
    for r in tw:
        x, y = r["em_dash_per_1k"], r["triads_per_1k"]
        ax.scatter(x, y, s=52, color="#64748b", zorder=3, edgecolors="white", linewidths=0.8)
        if r["doc"] in labels:
            dx, dy = labels[r["doc"]]
            ha = "right" if dx < 0 else "left"
            ax.text(x + dx, y + dy, "@" + r["doc"], fontsize=8, color=TEXT, ha=ha)

    ax.set_xlim(-1.2, 36.5)
    ax.set_ylim(-0.35, 5.9)
    ax.set_xlabel("Dashes (em, double hyphen, spaced hyphen) per 1,000 words", fontsize=10)
    ax.set_ylabel("Exactly-three lists per 1,000 words", fontsize=10)
    ax.set_title("42 accounts' long-form tweets, no ground truth",
                 fontsize=13, fontweight="bold", loc="left", pad=10)
    ax.tick_params(labelsize=8.5)

    fig.tight_layout()
    fig.savefig(OUT / "tweets.svg", facecolor=BG)
    fig.savefig(OUT / "tweets.png", facecolor=BG, dpi=200)
    plt.close(fig)


fig1()
fig2()
fig3()
print("written to", OUT)
