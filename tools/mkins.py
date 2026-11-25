#!/usr/bin/env python3
"""Generate Chinese instruction-reference pages from the cleaned manual text."""
import os, re, json, glob
import pymupdf

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CLEAN = os.path.join(ROOT, "source", "clean")
OUT = os.path.join(ROOT, "content", "ins")
os.makedirs(OUT, exist_ok=True)

desc = json.load(open(os.path.join(OUT, "_desc.json"), encoding="utf-8"))

# printed page numbers from the PDF bookmarks
pages = {}
doc = pymupdf.open(os.path.join(ROOT, "source", "i386.pdf"))
for lvl, title, page in doc.get_toc():
    if lvl == 5 and " -- " in title:
        pages[title.split(" -- ")[0].strip()] = page

FLAGS = {
    "None": "无。",
    "ZF as described above": "ZF，如上述。",
    "CF as described above": "CF，如上述。",
    "OF, SF, ZF, AF, PF, and CF as described in Appendix C": "OF、SF、ZF、AF、PF、CF，按附录 C 所述。",
    "OF, SF, ZF, AF, CF, and PF as described in Appendix C": "OF、SF、ZF、AF、CF、PF，按附录 C 所述。",
    "OF, SF, ZF, PF, and CF as described above; AF and OF are undefined": "OF、SF、ZF、PF、CF 如上述；AF 与 OF 未定义。",
    "SF, ZF, and PF as described in Appendix C; OF, AF, and CF are undefined": "SF、ZF、PF 按附录 C 所述；OF、AF、CF 未定义。",
    "AF and CF as described above; OF, SF, ZF, and PF are undefined": "AF、CF 如上述；OF、SF、ZF、PF 未定义。",
    "OF, SF, ZF, AR, PF, CF are undefined.": "OF、SF、ZF、AF、PF、CF 均未定义。",
    "CF := 0, OF := 0; SF, ZF, and PF as described in Appendix C; AF is undefined": "CF := 0，OF := 0；SF、ZF、PF 按附录 C 所述；AF 未定义。",
    "OF and CF as described above; SF, ZF, AF, PF, and CF are undefined": "OF、CF 如上述；SF、ZF、AF、PF、CF 未定义。",
    "OF, SF, ZF, AF, and PF as described in Appendix C": "OF、SF、ZF、AF、PF 按附录 C 所述。",
    "All; the flags register is popped from stack": "全部；标志寄存器从栈中弹出。",
    "AF and CF as described above; SF, ZF, PF, and CF as described in Appendix C.": "AF、CF 如上述；SF、ZF、PF、CF 按附录 C 所述。",
    "IF := 0": "IF := 0。",
    "CF := 1": "CF := 1。",
    "OF for single shifts; OF is undefined for multiple shifts; CF, ZF, PF, and SF as described in Appendix C": "单次移位时设置 OF；多次移位时 OF 未定义；CF、ZF、PF、SF 按附录 C 所述。",
    "TS := 0 (TS is in CR0, not the flag register)": "TS := 0（TS 在 CR0 中，不在标志寄存器中）。",
    "CF := 0, OF := 0; PF, SF, and ZF as described in Appendix C": "CF := 0，OF := 0；PF、SF、ZF 按附录 C 所述。",
    "ZF by REP CMPS and REP SCAS as described above": "ZF 由 REP CMPS 与 REP SCAS 按上述方式设置。",
    "OF and CF as described above; SF, ZF, AF, and PF are undefined": "OF、CF 如上述；SF、ZF、AF、PF 未定义。",
    "OF only for single rotates; OF is undefined for multi-bit rotates; CF as described above": "仅单次循环移位时设置 OF；多位移位时 OF 未定义；CF 如上述。",
    "CF := 0": "CF := 0。",
    "All flags are affected if a task switch occurs; no flags are affected if a task switch does not occur": "若发生任务切换则影响所有标志；若不发生任务切换则不影响任何标志。",
    "AF and CF as described above; SF, ZF, and PF as described in Appendix C.": "AF、CF 如上述；SF、ZF、PF 按附录 C 所述。",
    "IF := 1": "IF := 1。",
    "DF := 0": "DF := 0。",
    "SF, ZF, AF, PF, and CF as described above": "SF、ZF、AF、PF、CF 如上述。",
    "CF as described above; OF, SF, ZF, and PF as described in Appendix C": "CF 如上述；OF、SF、ZF、PF 按附录 C 所述。",
    "OF, SF, ZF, AF, PF, and CF are undefined": "OF、SF、ZF、AF、PF、CF 均未定义。",
    "All if a task switch takes place; none if no task switch occurs": "若发生任务切换则全部影响；若不发生则无影响。",
    "DF := 1": "DF := 1。",
    "OF := 0, CF := 0; SF, ZF, and PF as described in Appendix C": "OF := 0，CF := 0；SF、ZF、PF 按附录 C 所述。",
    "OF, SF, ZF, AF, and PF as described in Appendix C.": "OF、SF、ZF、AF、PF 按附录 C 所述。",
    "All flags except VM and RF": "除 VM 和 RF 之外的所有标志。",
    "OF := 0, CF := 0; SF, ZF, and PF as described in Appendix C; AF is undefined": "OF := 0，CF := 0；SF、ZF、PF 按附录 C 所述；AF 未定义。",
}


def section_map(text):
    parts = re.split(r"^## (.+)$", text, flags=re.M)
    out = {"_intro": parts[0]}
    for i in range(1, len(parts), 2):
        out[parts[i].strip()] = parts[i + 1].strip()
    return out


def fenced(s):
    m = re.search(r"```[^\n]*\n(.*?)```", s, re.S)
    return m.group(1).strip("\n") if m else ""


def plain(s):
    s = re.sub(r"```[^\n]*\n.*?```", "", s, flags=re.S)
    s = re.sub(r"\n{2,}", "\n\n", s)
    return s.strip()


for path in sorted(glob.glob(os.path.join(CLEAN, "[A-Z]*.md"))):
    iid = os.path.splitext(os.path.basename(path))[0]
    raw = open(path, encoding="utf-8").read()
    head = raw.split("\n", 1)[0].lstrip("# ").strip()
    en = head.split(" -- ", 1)[1] if " -- " in head else head
    secs = section_map(raw)
    opcode = fenced(secs.get("_intro", ""))
    operation = fenced(secs.get("Operation", ""))
    zh_title, zh_desc = desc.get(iid, (en, ""))
    flags_raw = plain(secs.get("Flags Affected", "")).replace("\n", " ")
    flags_zh = FLAGS.get(flags_raw, flags_raw)

    def exc(name):
        return plain(secs.get(name, "")).strip()

    body = [f"# {iid} -- {zh_title}", "", "## 操作码", "", "```", opcode, "```", ""]
    if operation:
        body += ["## 操作", "", "```", operation, "```", ""]
    body += ["## 说明", "", zh_desc, ""]
    if flags_zh:
        body += ["## 影响的标志", "", flags_zh, ""]
    for label, key in (("保护模式异常", "Protected Mode Exceptions"),
                       ("实地址模式异常", "Real Address Mode Exceptions"),
                       ("虚拟 8086 模式异常", "Virtual 8086 Mode Exceptions")):
        val = exc(key)
        if val:
            body += [f"## {label}（原文）", "", "::: note", val, ":::", ""]
    page = pages.get(iid, "")
    fm = ["---", f"id: {iid}", f"title: {zh_title}", f"en: {en}", f"group: {iid[0]}"]
    if page:
        fm.append(f"page: {page}")
    fm.append("---")
    out = "\n".join(fm) + "\n\n" + "\n".join(body).rstrip() + "\n"
    open(os.path.join(OUT, iid.lower() + ".md"), "w", encoding="utf-8").write(out)

print("generated", len(glob.glob(os.path.join(OUT, "*.md"))), "instruction pages")
