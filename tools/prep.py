#!/usr/bin/env python3
"""Parse the mirrored manual: build outline.json and map sections to printed pages."""
import json, re, os, sys
from html.parser import HTMLParser
import pymupdf

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "source", "6.828", "2018", "readings", "i386")


class TocParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []
        self.chapters = []
        self.sections = []
        self.cur_part = None
        self.last_href = None
        self.cur_tag = None
        self.buf = ""
        self.in_link = False

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in ("h2", "h3", "li"):
            self.cur_tag = tag
            self.buf = ""
        if tag == "a" and "href" in a:
            self.last_href = a["href"]
            self.in_link = True

    def handle_data(self, data):
        if self.in_link:
            self.buf += data

    def handle_endtag(self, tag):
        if tag == "a" and self.in_link:
            self.in_link = False
            text = " ".join(self.buf.split())
            href = self.last_href
            if href and href.endswith(".htm"):
                if re.match(r"c\d\d\.htm", href):
                    m = re.match(r"Chapter (\d+) -- (.*)", text)
                    if m:
                        self.chapters.append({"id": href[:-4], "num": int(m.group(1)), "en": m.group(2).strip(), "part": self.cur_part})
                elif re.match(r"s\d\d_\d\d\.htm", href):
                    m = re.match(r"(\d+\.\d+)\s+(.*)", text)
                    if m:
                        self.sections.append({"id": href[:-4], "num": m.group(1), "en": m.group(2).strip(), "chapter": href[:3]})
                elif href.startswith("app"):
                    self.sections.append({"id": href[:-4], "num": href[:-4].upper(), "en": text.split("--")[-1].strip(), "chapter": "app"})
        if tag == "h2" and self.cur_tag == "h2":
            text = " ".join(self.buf.split())
            self.parts.append(text)
            self.cur_part = text
            self.buf = ""


text_pages = []


def main():
    with open(os.path.join(SRC, "toc.htm"), encoding="latin-1") as f:
        html = f.read()
    p = TocParser()
    p.feed(html)
    doc = pymupdf.open(os.path.join(ROOT, "source", "i386.pdf"))
    page_text = []
    for i in range(len(doc)):
        page_text.append(doc[i].get_text())
    outline = {"parts": [x for x in p.parts if x.startswith("Part")], "chapters": p.chapters, "sections": p.sections}
    # page lookup
    missing = []
    for item in p.chapters + p.sections:
        num = item["num"]
        pat = re.compile(r"^\s*" + (r"Chapter\s+%d\b" % num if isinstance(num, int) else re.escape(str(num)) + r"\s"), re.M)
        found = None
        for i, t in enumerate(page_text):
            if i < 8:
                continue
            if pat.search(t):
                found = i + 1
                break
        item["page"] = found
        if not found:
            missing.append((num, item["en"]))
    print(json.dumps(outline, indent=2)[:1200])
    print("chapters", len(p.chapters), "sections", len(p.sections), "missing", len(missing))
    for m in missing[:20]:
        print("MISS", m)
    with open(os.path.join(ROOT, "content", "outline.json"), "w", encoding="utf-8") as f:
        json.dump(outline, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main()
