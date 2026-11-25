#!/usr/bin/env python3
"""Redraw the manual's ASCII-art figures as clean SVGs with Chinese labels."""
import os, re, sys, json

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CONN = {
    "─": "LR", "│": "UD", "|": "UD",
    "┌": "RD", "┐": "LD", "└": "RU", "┘": "LU",
    "├": "UDR", "┤": "UDL", "┬": "LRD", "┴": "LRU", "┼": "LRUD",
    "╴": "L", "╵": "U", "╶": "R", "╷": "D",
    "═": "LR", "║": "UD",
    "╒": "RD", "╕": "LD", "╘": "RU", "╛": "LU",
    "╔": "RD", "╗": "LD", "╚": "RU", "╝": "LU",
    "╞": "UDR", "╡": "UDL", "╤": "LRD", "╧": "LRU", "╪": "LRUD",
    "╟": "UDR", "╢": "UDL", "╥": "LRD", "╨": "LRU", "╫": "LRUD",
    "╠": "UDR", "╣": "UDL", "╦": "LRD", "╩": "LRU", "╬": "LRUD",
}
DOUBLE = set("═║╒╕╘╛╔╗╚╝╞╡╤╧╪╟╢╥╨╫╠╣╦╩╬")
ARROWS = {"►": "R", "◄": "L", "▲": "U", "▼": "D"}
BOX = set(CONN) | set(ARROWS) | set("▒·")
CW, CH = 9, 16

NOTES = {
    "3-6": ["SHL（同义助记符 SAL）把寄存器或内存操作数中的位左移指定的位数。CF 接收从", "操作数左端移出的最后一位；空出的低位补 0。这些指令可作用于字节、字和双字。"],
    "3-7": ["SHR 把寄存器或内存操作数中的位右移指定的位数。CF 接收从操作数右端移出的", "最后一位；空出的高位补 0。"],
    "3-22": ["LAHF 把标志寄存器中的五个标志装入 AH；SAHF 把 AH 中的同样五个标志写回", "标志寄存器。每个标志在 AH 与标志寄存器中的位位置相同。标为 UU 的其余位保留，未定义。"],
    "3-23": ["标为 0 和 1 的位由 Intel 保留，未定义。系统标志（包括 IOPL 字段以及 VM、", "RF、IF 标志）会被压栈，并对应用程序可见；但应用程序弹出标志时，这些项不会改变，", "无论弹出的值是什么。"],
}



def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


KEEP = set("EAX EBX ECX EDX ESI EDI ESP EBP AX BX CX DX SI DI SP BP AL AH BL BH CL CH DL DH CS DS ES SS FS GS EIP IP EFLAGS FLAGS CR0 CR1 CR2 CR3 CR4 DR0 DR1 DR2 DR3 DR6 DR7 TR TR6 TR7 GDTR LDTR IDTR TSS LDT GDT IDT PTE PDE PDBR TLB MSW PSW DPL RPL CPL IOPL NT VM RF TF IF DF OF SF ZF AF PF CF DIR SIB MOD R/M R/W LOCK REP MOV".split())
FUNC = {"THE":"","A":"","AN":"","OF":"的","AND":"与","OR":"或","FOR":"用于","TO":"到","IN":"在","BY":"由","AT":"在","AS":"作为","BE":"","IS":"","ARE":"","WAS":"","WERE":"","THAT":"","THIS":"此","THESE":"这些","IF":"若","WITH":"与","FROM":"来自","WHEN":"当","MAY":"可","CAN":"可","NOT":"不","ALL":"全部","ONE":"1","USED":"已用","ON":"在","IT":"","ITS":"其"}

def make_tr():
    phrases = json.load(open(os.path.join(ROOT, "figures", "phrases.json"), encoding="utf-8"))
    words = json.load(open(os.path.join(ROOT, "figures", "words.json"), encoding="utf-8"))
    P = {k.upper(): v for k, v in phrases.items()}
    W = {k.upper(): v for k, v in words.items()}

    def tr(s):
        key = s.strip().upper()
        if key in P:
            return P[key]
        out = []
        for tok in re.findall(r"[A-Za-z][A-Za-z0-9_.:]*|[^A-Za-z]+", s):
            if not tok or not tok[0].isalpha():
                out.append(tok)
                continue
            up = tok.upper()
            if ":" in tok or up in KEEP:
                out.append(tok)
            elif up in W:
                out.append(W[up])
            elif up in FUNC:
                out.append(FUNC[up])
            else:
                out.append(tok)
        res = "".join(out)
        res = re.sub(r"\s+", " ", res).strip()
        res = re.sub(r"(?<=[一-鿿])\s+(?=[一-鿿])", "", res)
        return res
    return tr


def load(fig):
    path = os.path.join(ROOT, "figures", "ascii", f"fig{fig}.txt")
    lines = open(path, encoding="utf-8").read().split("\n")
    if lines and lines[0].startswith("Figure "):
        lines = lines[1:]
    # trim trailing empty lines
    while lines and not lines[-1].strip():
        lines.pop()
    indent = min((len(l) - len(l.lstrip(" ")) for l in lines if l.strip()), default=0)
    return [l[indent:].rstrip("\n") for l in lines]


def render(fig, tr):
    lines = load(fig)
    rows = len(lines)
    cols = max(len(l) for l in lines)
    pad = 12
    notes = NOTES.get(fig, [])
    w, h = cols * CW + pad * 2, rows * CH + pad * 2 + (len(notes) * 18 + 8 if notes else 0)
    out = [f'<svg class="redraw-svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" role="img">']
    out.append('<g class="rd-lines" fill="none" stroke="currentColor" stroke-linecap="square">')
    for y, line in enumerate(lines):
        for x, ch in enumerate(line):
            if ch not in CONN:
                continue
            cx, cy = pad + x * CW + CW / 2, pad + y * CH + CH / 2
            sw = 2.2 if ch in DOUBLE else 1.1
            c = CONN[ch]
            if "L" in c:
                out.append(f'<line x1="{cx-CW/2}" y1="{cy}" x2="{cx}" y2="{cy}" stroke-width="{sw}"/>')
            if "R" in c:
                out.append(f'<line x1="{cx}" y1="{cy}" x2="{cx+CW/2}" y2="{cy}" stroke-width="{sw}"/>')
            if "U" in c:
                out.append(f'<line x1="{cx}" y1="{cy-CH/2}" x2="{cx}" y2="{cy}" stroke-width="{sw}"/>')
            if "D" in c:
                out.append(f'<line x1="{cx}" y1="{cy}" x2="{cx}" y2="{cy+CH/2}" stroke-width="{sw}"/>')
    out.append("</g>")
    # shading
    out.append('<g class="rd-shade">')
    for y, line in enumerate(lines):
        for x, ch in enumerate(line):
            if ch == "▒":
                out.append(f'<rect x="{pad+x*CW}" y="{pad+y*CH}" width="{CW}" height="{CH}" fill="currentColor" fill-opacity="0.08"/>')
    out.append("</g>")
    # arrows and dots
    out.append('<g class="rd-marks" fill="currentColor">')
    for y, line in enumerate(lines):
        for x, ch in enumerate(line):
            cx, cy = pad + x * CW + CW / 2, pad + y * CH + CH / 2
            if ch in ARROWS:
                d = ARROWS[ch]
                pts = {
                    "R": f"{cx-2},{cy-4} {cx+4},{cy} {cx-2},{cy+4}",
                    "L": f"{cx+2},{cy-4} {cx-4},{cy} {cx+2},{cy+4}",
                    "U": f"{cx-4},{cy+2} {cx},{cy-4} {cx+4},{cy+2}",
                    "D": f"{cx-4},{cy-2} {cx},{cy+4} {cx+4},{cy-2}",
                }[d]
                out.append(f'<polygon points="{pts}"/>')
            elif ch == "·":
                out.append(f'<circle cx="{cx}" cy="{cy}" r="1.6"/>')
    out.append("</g>")
    # text
    out.append('<g class="rd-text">')
    boxpat = "[" + "".join(re.escape(c) for c in BOX) + "]"
    tokpat = re.compile(r"[^\s" + "".join(re.escape(c) for c in BOX) + r"]+")
    for y, line in enumerate(lines):
        toks = list(tokpat.finditer(line))
        groups = []
        for t in toks:
            if groups:
                prev = groups[-1][-1]
                gap = line[prev.end():t.start()]
                a, b = prev.group(0), t.group(0)
                if gap == " " and not (a.isdigit() and b.isdigit()):
                    groups[-1].append(t)
                    continue
            groups.append([t])
        for g in groups:
            label_en = " ".join(x.group(0) for x in g)
            if len(label_en) == 1 and not label_en.isdigit() and label_en != "+":
                continue
            if fig in NOTES and len(label_en) > 24 and any(c.isalpha() for c in label_en):
                continue
            x0, x1 = g[0].start(), g[-1].end()
            cx = pad + (x0 + x1) / 2 * CW
            cy = pad + y * CH + CH * 0.72
            label = tr(label_en)
            avail = max(1, (x1 - x0) * CW)
            units = sum(1.0 if ord(ch) > 127 else 0.58 for ch in label)
            fs = max(7, min(12, avail / max(units, 1) * 0.92))
            out.append(f'<text x="{cx:.1f}" y="{cy:.1f}" text-anchor="middle" font-size="{fs}">{esc(label)}</text>')
    out.append("</g>")
    # vertical single-letter labels (e.g. DIRECTION / EXPANSION)
    out.append('<g class="rd-text rd-vertical">')
    for x in range(cols):
        run = []
        def flush():
            if len(run) >= 4:
                word = "".join(c for _, c in run)
                label = tr(word)
                if label != word:
                    cx = pad + x * CW + CW / 2
                    y0 = pad + run[0][0] * CH + CH * 0.72
                    for i, ch in enumerate(label):
                        out.append(f'<text x="{cx:.1f}" y="{y0 + i*CH:.1f}" text-anchor="middle" font-size="11">{esc(ch)}</text>')
            run.clear()
        blank = 0
        for y, line in enumerate(lines):
            ch = line[x] if x < len(line) else " "
            if ch.isalpha() and ch.isupper():
                prev = line[x-1] if x > 0 else " "
                nxt = line[x+1] if x+1 < len(line) else " "
                if not prev.isalnum() and not nxt.isalnum():
                    run.append((y, ch)); blank = 0
                else:
                    flush()
            elif ch == " " and run:
                blank += 1
                if blank > 2:
                    flush()
            else:
                flush()
        flush()
    out.append("</g>")
    if notes:
        out.append('<g class="rd-note" font-size="11">')
        for i, line in enumerate(notes):
            y = pad + rows * CH + 18 + i * 18
            out.append(f'<text x="{pad}" y="{y}" fill="currentColor">{esc(line)}</text>')
        out.append("</g>")
    out.append("</svg>")
    return "\n".join(out)


if __name__ == "__main__":
    fig = sys.argv[1]
    tr = make_tr()
    svg = render(fig, tr)
    open(os.path.join(ROOT, "figures", "svg", f"fig{fig}.svg"), "w", encoding="utf-8").write(svg)
    print("wrote", len(svg), "bytes")
