#!/usr/bin/env python3
"""Convert mirrored HTML pages into clean, structure-preserving text for translation."""
import os, re, html, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "source", "6.828", "2018", "readings", "i386")
OUT = os.path.join(ROOT, "source", "clean")
os.makedirs(OUT, exist_ok=True)


def inline(s):
    s = re.sub(r'<A HREF="[^"]*">(.*?)</A>', r"\1", s, flags=re.S | re.I)
    s = re.sub(r"<[^>]+>", "", s)
    return html.unescape(s)


def convert(path):
    raw = open(path, encoding="latin-1").read()
    raw = raw.split("<HR>", 1)[-1]  # drop nav header
    raw = raw.rsplit("<HR>", 1)[0]  # drop nav footer
    raw = re.sub(r"<P>\s*$", "", raw, flags=re.I)
    out = []
    tokens = re.split(r"(<H1>.*?</H1>|<H2>.*?</H2>|<H3>.*?</H3>|<PRE>.*?</PRE>|<OL>.*?</OL>|<UL>.*?</UL>|<A NAME=\"[^\"]+\">\s*<IMG[^>]*SRC=\"([^\"]+)\"[^>]*>)", raw, flags=re.S | re.I)
    i = 0
    while i < len(tokens):
        t = tokens[i]
        if not t:
            i += 1
            continue
        m = re.match(r"<H([123])>(.*?)</H\1>", t, re.S | re.I)
        if m:
            out.append("#" * int(m.group(1)) + " " + inline(m.group(2)).strip())
        elif re.match(r"<PRE>", t, re.I):
            body = re.sub(r"^<PRE>|</PRE>$", "", t, flags=re.I)
            out.append("```\n" + html.unescape(body).strip("\n") + "\n```")
        elif re.match(r"<OL>", t, re.I):
            items = re.findall(r"<LI>(.*?)(?=<LI>|</OL>)", t, re.S | re.I)
            for n, it in enumerate(items, 1):
                txt = inline(it).strip()
                txt = re.sub(r"\s*\n\s*", " ", txt)
                out.append(f"{n}. {txt}")
        elif re.match(r"<UL>", t, re.I):
            items = re.findall(r"<LI>(.*?)(?=<LI>|</UL>)", t, re.S | re.I)
            for it in items:
                txt = inline(it).strip()
                txt = re.sub(r"\s*\n\s*", " ", txt)
                out.append(f"- {txt}")
        elif re.match(r"<A NAME", t, re.I):
            name = re.search(r'NAME="([^"]+)"', t).group(1)
            src = re.search(r'SRC="([^"]+)"', t)
            if src:
                out.append(f"![{name}]({src.group(1)})")
        else:
            paragraphs = re.split(r"<P>", t, flags=re.I)
            for p in paragraphs:
                txt = inline(p).strip()
                txt = re.sub(r"[ \t]*\n[ \t]*", " ", txt)
                txt = re.sub(r"\s{2,}", " ", txt).strip()
                if txt:
                    out.append(txt)
        i += 1
    if len(tokens) and re.match(r"<A NAME", tokens[-1] or "", re.I):
        pass
    return "\n\n".join(out)


def main():
    for path in sorted(glob.glob(os.path.join(SRC, "*.htm"))):
        name = os.path.splitext(os.path.basename(path))[0]
        if name in ("toc",) or name in ("PI","PII","PIII","PIV") or re.match(r"c\d\d", name):
            continue
        text = convert(path)
        with open(os.path.join(OUT, name + ".md"), "w", encoding="utf-8") as f:
            f.write(text + "\n")
    files = glob.glob(os.path.join(OUT, "*.md"))
    print(len(files), "files", sum(os.path.getsize(f) for f in files) // 1024, "KB")


if __name__ == "__main__":
    main()
