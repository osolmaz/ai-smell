"""Build determinative per-account samples of long-form tweets.

Reads the private xtap-store archive, keeps original (non-retweet)
long-form tweets (>280 chars), and writes one markdown sample per
account into corpus/tweets/ when the account has at least MIN_WORDS
words of long-form text. Tweets are sorted by creation date so the
sample is deterministic, and each tweet carries its source URL.
"""
import json
import re
from collections import defaultdict
from pathlib import Path

STORE = Path.home() / "repos/xtap-store/data/tweets"
OUT = Path(__file__).resolve().parent / "corpus" / "tweets"
MIN_WORDS = 2000
MAX_TWEETS = 40

seen = set()
by_user = defaultdict(list)

for f in sorted(STORE.glob("*/*/*.jsonl")):
    for line in f.read_text().splitlines():
        if not line.strip():
            continue
        t = json.loads(line)
        if t["id"] in seen or t.get("is_retweet"):
            continue
        seen.add(t["id"])
        if len(t.get("text") or "") <= 280:
            continue
        by_user[t["author"]["username"]].append(t)

OUT.mkdir(parents=True, exist_ok=True)
kept = []
for user, tweets in by_user.items():
    tweets.sort(key=lambda t: t["created_at"])
    tweets = tweets[:MAX_TWEETS]
    words = sum(len(re.findall(r"[\w'’-]+", re.sub(r"https?://\S+", "", t["text"])))
                for t in tweets)
    if words < MIN_WORDS:
        continue
    lines = [f"# @{user} — long-form tweets", ""]
    for t in tweets:
        lines.append(f"## {t['created_at'][:10]} ({t['url']})")
        lines.append("")
        lines.append(t["text"].strip())
        lines.append("")
    (OUT / f"{user}.md").write_text("\n".join(lines))
    kept.append((words, len(tweets), user))

kept.sort(reverse=True)
print(f"{len(kept)} accounts sampled (>= {MIN_WORDS} long-form words):")
for words, n, user in kept:
    print(f"  {user}: {n} tweets, {words} words")
