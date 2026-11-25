#!/usr/bin/env python3
"""Localize the exception blocks in generated instruction pages."""
import glob, json, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IN = os.path.join(ROOT, "content", "ins")
exc = json.load(open(os.path.join(IN, "_exc.json"), encoding="utf-8"))
norm = {k.strip().rstrip(".").lower(): v for k, v in exc.items()}

NOTES = {
    "The operand-size attribute has no effect on this instruction.": "操作数大小属性对该指令没有影响。",
    "These instructions are valid in Real Address Mode to allow power-up initialization for Protected Mode": "这些指令在实地址模式中有效，以便上电时为保护模式做初始化。",
}

unmatched = {}


def tr_clause(c):
    c = c.strip().rstrip(".")
    if not c:
        return ""
    key = re.sub(r"\s+", " ", c).lower()
    if key in norm:
        return norm[key].rstrip("。")
    # tolerate a leading exception name merged into a sentence
    for k, v in norm.items():
        if key.startswith(k) and len(k) > 20:
            return v.rstrip("。")
    unmatched[c] = unmatched.get(c, 0) + 1
    return c


def translate(body):
    note = ""
    m = re.search(r"\n*### Note\s*\n+(.*)$", body, re.S)
    if m:
        note = m.group(1).strip()
        body = body[: m.start()]
    body = body.strip()
    if body.lower() == "none":
        out = "无。"
    else:
        clauses = [x for x in re.split(r";\s*|\n+", body) if x.strip()]
        parts = [tr_clause(c) for c in clauses]
        out = "；".join(p for p in parts if p) + "。"
        out = out.replace("。。", "。")
    if note:
        out += "\n\n" + NOTES.get(note, note)
    return out


count = 0
for path in glob.glob(os.path.join(IN, "*.md")):
    text = open(path, encoding="utf-8").read()
    changed = False

    def repl(m):
        global count
        count += 1
        return f"## {m.group(1)}\n\n" + translate(m.group(2)) + "\n"

    new = re.sub(r"## (保护模式异常|实地址模式异常|虚拟 8086 模式异常)（原文）\n\n::: note\n(.*?)\n:::", repl, text, flags=re.S)
    if new != text:
        open(path, "w", encoding="utf-8").write(new)
        changed = True

print("localized", count, "blocks")
print("unmatched", len(unmatched))
for k, v in sorted(unmatched.items(), key=lambda x: -x[1])[:30]:
    print(f"x{v} {k[:140]}")
