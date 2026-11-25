#!/usr/bin/env python3
import os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src = open(os.path.join(ROOT, "source", "clean", "s17_02.md"), encoding="utf-8").read()
blocks = {}
for m in re.finditer(r"```\n(Table 17-([234])\..*?)\n```", src, re.S):
    blocks[m.group(2)] = m.group(1).strip("\n")

notes = {
    "2": "注：`disp8` 表示 ModR/M 字节之后的 8 位位移，需符号扩展后加到索引上；`disp16` 表示 ModR/M 字节之后的 16 位位移，直接加到索引上。有效地址含 BP 索引时默认段寄存器为 SS，其他有效地址默认为 DS。",
    "3": "注：`[--] [--]` 表示 ModR/M 字节之后跟有 SIB 字节。`disp8` 表示 SIB 字节之后的 8 位位移，需符号扩展；`disp32` 表示 ModR/M 字节之后的 32 位位移。",
    "4": "注：`disp8` 表示 SIB 字节之后的 8 位位移，需符号扩展；`disp32` 表示 SIB 字节之后的 32 位位移。无基址时，`disp32` 为绝对的 32 位位移。",
}
path = os.path.join(ROOT, "content", "ch17", "02.md")
text = open(path, encoding="utf-8").read()
for n in ("2", "3", "4"):
    if "@@T17%s@@" % n in text:
        text = text.replace("@@T17%s@@" % n, "```\n" + blocks[n] + "\n```\n\n" + notes[n])
open(path, "w", encoding="utf-8").write(text)
print("injected tables", {k: len(v) for k, v in blocks.items()}, "remaining markers", text.count("@@T17"))
