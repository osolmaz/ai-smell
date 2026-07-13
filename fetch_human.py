"""Download human-written baseline pages and extract readable text."""
import re
import urllib.request
from html.parser import HTMLParser


class TextExtractor(HTMLParser):
    SKIP = {"script", "style", "nav", "header", "footer", "form", "aside"}
    BLOCK = {"p", "div", "li", "h1", "h2", "h3", "h4", "blockquote", "pre", "br", "tr"}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts = []
        self.skip_depth = 0

    def handle_starttag(self, tag, attrs):
        if tag in self.SKIP:
            self.skip_depth += 1
        if tag in self.BLOCK:
            self.parts.append("\n")

    def handle_endtag(self, tag):
        if tag in self.SKIP and self.skip_depth:
            self.skip_depth -= 1
        if tag in self.BLOCK:
            self.parts.append("\n")

    def handle_data(self, data):
        if not self.skip_depth:
            self.parts.append(data)


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read().decode("utf-8", errors="replace")


def extract(html, start_marker=None, end_marker=None):
    p = TextExtractor()
    p.feed(html)
    text = "".join(p.parts)
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n\s*\n+", "\n\n", text).strip()
    if start_marker:
        i = text.find(start_marker)
        if i >= 0:
            text = text[i:]
    if end_marker:
        i = text.find(end_marker)
        if i >= 0:
            text = text[:i]
    return text


jobs = [
    (
        "https://www.joelonsoftware.com/2000/04/06/things-you-should-never-do-part-i/",
        "/tmp/ai-smell/corpus/human/joel-rewrite.md",
        "Netscape 6.0 is finally going",
        "Next:",
    ),
    (
        "http://antirez.com/news/122",
        "/tmp/ai-smell/corpus/human/antirez-terminology.md",
        "Today it happened again",
        "blog comments",
    ),
]

for url, path, start, end in jobs:
    text = extract(fetch(url), start, end)
    with open(path, "w") as f:
        f.write(text)
    print(path, len(text.split()), "words")
