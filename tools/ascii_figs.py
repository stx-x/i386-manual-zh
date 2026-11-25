#!/usr/bin/env python3
"""Extract the ASCII-art figure blocks from the manual PDF."""
import os, re, pymupdf

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "figures", "ascii")
os.makedirs(OUT, exist_ok=True)

doc = pymupdf.open(os.path.join(ROOT, "source", "i386.pdf"))
captions = []
for pno, page in enumerate(doc):
    text = page.get_text()
    for m in re.finditer(r"^Figure (\d+-\d+)\.\s*(.+)$", text, re.M):
        captions.append((pno, m.start(), m.group(1), m.group(2).strip()))

written = 0
for idx, (pno, start, num, title) in enumerate(captions):
    text = doc[pno].get_text()
    end = len(text)
    # stop at the next figure/table caption on the same page
    tail = text[start:]
    m = re.search(r"^(Figure \d+-\d+\.|Table \d+-\d+\.)", tail[10:], re.M)
    if m:
        end = start + 10 + m.start()
    block = text[start:end]
    # drop page headers/footers
    lines = [l for l in block.split("\n") if not l.startswith("INTEL 80386 PROGRAMMER") and not re.match(r"Page \d+ of", l)]
    # keep only the ASCII art: stop at the first prose line or section heading
    boxchars = set("─│┌┐└┘├┤┬┴┼═║╒╔╕╗╘╚╛╝╞╟╠╡╢╣╤╦╧╨╩╪╫╬")
    art = []
    started = False
    for l in lines[1:]:
        st = l.strip()
        if not started:
            if l.strip():
                started = True
                art.append(l)
            continue
        if st and not any(c in boxchars for c in l):
            words = st.split()
            lower = sum(c.islower() for c in st)
            if st[0].islower() or (len(words) >= 7 and lower > len(st) * 0.45) or re.match(r"^\d+(\.\d+)+\s", st):
                break
        art.append(l)
    lines = art
    block = "\n".join(lines).rstrip()
    path = os.path.join(OUT, f"fig{num}.txt")
    open(path, "w", encoding="utf-8").write(block + "\n")
    written += 1

print("captions", len(captions), "written", written)
for c in captions[:5]:
    print(c)
