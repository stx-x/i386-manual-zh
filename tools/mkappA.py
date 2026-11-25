#!/usr/bin/env python3
import os, re, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src = open(os.path.join(ROOT, "source", "clean", "appa.md"), encoding="utf-8").read()
parts = re.split(r"^### (.+)$", src, flags=re.M)
secs = {parts[i].strip(): parts[i + 1] for i in range(1, len(parts), 2)}
order = ["One-Byte Opcode Map", "Two-Byte Opcode Map (first byte is 0FH)"]
grids = []
for name in order:
    m = re.search(r"```\n(.*?)\n```", secs[name], re.S)
    grids.append(m.group(1))
# the last two sub-sections share the "Opcodes determined..." prefix
byd = [v for k, v in secs.items() if k.startswith("Opcodes determined")]
for v in byd:
    m = re.search(r"```\n(.*?)\n```", v, re.S)
    grids.append(m.group(1))

def clean(g):
    g = re.sub(r"<[^>]+>", "", g)
    return html.unescape(g).rstrip()

path = os.path.join(ROOT, "content", "app", "a.md")
text = open(path, encoding="utf-8").read()
for i, g in enumerate(grids[:4], 1):
    text = text.replace("@@A%d@@" % i, "```\n" + clean(g) + "\n```")
open(path, "w", encoding="utf-8").write(text)
print("injected", len(grids), "grids; remaining", text.count("@@A"))
