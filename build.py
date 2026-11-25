#!/usr/bin/env python3
"""
Zero-dependency static site generator for the Chinese edition of the
Intel 80386 Programmer's Reference Manual.

Usage: python3 build.py
Output: site/
"""
import html
import json
import os
import re
import shutil
import unicodedata
from datetime import date

ROOT = os.path.dirname(os.path.abspath(__file__))
CONTENT = os.path.join(ROOT, "content")
SITE = os.path.join(ROOT, "site")
FIGURES = os.path.join(ROOT, "figures")

SITE_TITLE = "80386 程序员参考手册"
SITE_SUBTITLE = "Intel 80386 Programmer's Reference Manual · 中文译本"
SITE_DESC = "《Intel 80386 Programmer's Reference Manual (1986)》中文译本：分段与分页、保护模式、多任务、异常与中断、指令集参考。"


# ---------------------------------------------------------------- utilities
def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def parse_front_matter(text):
    meta = {}
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            block = text[3:end].strip("\n")
            for line in block.splitlines():
                if not line.strip() or line.strip().startswith("#"):
                    continue
                k, _, v = line.partition(":")
                v = v.strip()
                if len(v) >= 2 and v[0] == v[-1] and v[0] in "\"'":
                    v = v[1:-1]
                meta[k.strip()] = v
            text = text[end + 4:]
    return meta, text.lstrip("\n")


def esc(s):
    return html.escape(s, quote=False)


def attr(s):
    return html.escape(s, quote=True)


def slugify(text):
    text = unicodedata.normalize("NFKC", text).strip().lower()
    text = re.sub(r"[^\w\u4e00-\u9fff]+", "-", text)
    return text.strip("-")[:60] or "section"


# ---------------------------------------------------------------- markdown
INLINE_TOKEN = "\x00{}\x00"


def inline(text):
    codes = []

    def stash(m):
        codes.append(m.group(1))
        return INLINE_TOKEN.format(len(codes) - 1)

    text = re.sub(r"`([^`]+)`", stash, text)
    text = esc(text)
    text = re.sub(r"!\[([^\]]*)\]\(([^)\s]+)\)", r'<img src="\2" alt="\1" loading="lazy" decoding="async">', text)
    text = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", r'<a href="\2">\1</a>', text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<![\w*])\*([^*\n]+)\*(?![\w*])", r"<em>\1</em>", text)
    text = re.sub(r"~~([^~]+)~~", r"<del>\1</del>", text)
    text = re.sub(r"\^\(([^)]+)\)", r"<sup>\1</sup>", text)
    text = re.sub(r"\{([^{}]+)\}", r"<sub>\1</sub>", text)
    for i, code in enumerate(codes):
        text = text.replace(INLINE_TOKEN.format(i), f"<code>{esc(code)}</code>")
    # typographic punctuation for Chinese prose
    text = text.replace(" -- ", " —— ")
    return text


def render_table(lines):
    rows = []
    for line in lines:
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        rows.append(cells)
    if len(rows) < 2:
        return "<p>" + inline(lines[0]) + "</p>"
    aligns = []
    for c in rows[1]:
        c = c.strip()
        if c.startswith(":") and c.endswith(":"):
            aligns.append("center")
        elif c.endswith(":"):
            aligns.append("right")
        else:
            aligns.append("left")
    head = rows[0]
    body = rows[2:]
    out = ['<div class="table-wrap"><table>']
    out.append("<thead><tr>" + "".join(f'<th style="text-align:{a}">{inline(c)}</th>' for c, a in zip(head, aligns)) + "</tr></thead><tbody>")
    for row in body:
        cells = row + [""] * (len(head) - len(row))
        out.append("<tr>" + "".join(f'<td style="text-align:{a}">{inline(c)}</td>' for c, a in zip(cells, aligns)) + "</tr>")
    out.append("</tbody></table></div>")
    return "".join(out)


def render_markdown(src, heading_ids=None, id_prefix="", heading_offset=0):
    lines = src.split("\n")
    out = []
    i = 0
    heading_no = [0]

    def heading_id(text, level):
        m = re.match(r"^(\d+(?:\.\d+)*)\s+(.*)$", text)
        if m:
            return "sec-" + m.group(1).replace(".", "-")
        if heading_ids is not None:
            heading_ids.append({"level": level, "id": slugify(text), "text": text})
        return slugify(text)

    while i < len(lines):
        line = lines[i]
        if not line.strip():
            i += 1
            continue
        # fenced code
        if line.startswith("```"):
            lang = line[3:].strip()
            buf = []
            i += 1
            while i < len(lines) and not lines[i].startswith("```"):
                buf.append(lines[i])
                i += 1
            i += 1
            cls = f' class="language-{attr(lang)}"' if lang else ""
            out.append(f'<div class="code-block"><pre><code{cls}>{esc(chr(10).join(buf))}</code></pre></div>')
            continue
        # heading
        m = re.match(r"^(#{1,4})\s+(.*)$", line)
        if m:
            level = len(m.group(1)) + heading_offset
            text = m.group(2).strip()
            hid = heading_id(text, level)
            num = re.match(r"^(\d+(?:\.\d+)*)\s+(.*)$", text)
            inner = f'<span class="h-num">{esc(num.group(1))}</span><span class="h-text">{inline(num.group(2))}</span>' if num else inline(text)
            out.append(f'<h{level} id="{hid}">{inner}<a class="h-anchor" href="#{hid}" aria-label="本节链接">#</a></h{level}>')
            i += 1
            continue
        # callout
        if line.startswith(":::"):
            kind = line[3:].strip() or "note"
            buf = []
            i += 1
            while i < len(lines) and lines[i].strip() != ":::":
                buf.append(lines[i])
                i += 1
            i += 1
            body = render_markdown("\n".join(buf))
            out.append(f'<aside class="callout callout-{attr(kind.split()[0])}">{body}</aside>')
            continue
        # table
        if line.strip().startswith("|") and i + 1 < len(lines) and re.match(r"^\s*\|[\s:|-]+\|\s*$", lines[i + 1]):
            buf = [line]
            i += 1
            while i < len(lines) and lines[i].strip().startswith("|"):
                buf.append(lines[i])
                i += 1
            out.append(render_table(buf))
            continue
        # hr
        if re.match(r"^\s*(---|\*\*\*)\s*$", line):
            out.append("<hr>")
            i += 1
            continue
        # blockquote
        if line.startswith(">"):
            buf = []
            while i < len(lines) and lines[i].startswith(">"):
                buf.append(lines[i][1:].lstrip())
                i += 1
            out.append("<blockquote>" + render_markdown("\n".join(buf)) + "</blockquote>")
            continue
        # figure
        fm = re.match(r'^!\[([^\]]*)\]\(([^)\s]+)\)\s*$', line.strip())
        if fm:
            alt, src = fm.group(1), fm.group(2)
            cap = alt
            cap_html = f"<figcaption>{inline(cap)}</figcaption>" if cap and not re.match(r"^fig", cap) else ""
            svg_name = os.path.splitext(os.path.basename(src))[0] + ".svg"
            svg_path = os.path.join(ROOT, "figures", "svg", svg_name)
            redraw = ""
            if os.path.exists(svg_path):
                redraw = (
                    '<div class="fig-redraw"><img src="../assets/figures/svg/' + attr(svg_name) +
                    '" alt="' + attr(alt) + '（中文重绘）" loading="lazy" decoding="async"></div>'
                )
            out.append(
                f'<figure class="fig"><a class="fig-link" href="{attr(src)}" data-zoom="1">'
                f'<img src="{attr(src)}" alt="{attr(alt)}" loading="lazy" decoding="async"></a>{redraw}{cap_html}</figure>'
            )
            i += 1
            continue
        # list
        lm = re.match(r"^(\s*)([-*]|\d+\.)\s+(.*)$", line)
        if lm:
            ordered = lm.group(2)[0].isdigit()
            base_indent = len(lm.group(1))
            items = []
            while i < len(lines):
                m2 = re.match(r"^(\s*)([-*]|\d+\.)\s+(.*)$", lines[i])
                if not m2 or len(m2.group(1)) < base_indent:
                    break
                indent = len(m2.group(1))
                if indent > base_indent:
                    # nested line: append to previous item
                    if items:
                        items[-1][1].append(lines[i].strip())
                    i += 1
                    continue
                if m2.group(2)[0].isdigit() != ordered and indent == base_indent:
                    break
                items.append([m2.group(3), []])
                i += 1
                while i < len(lines) and lines[i].strip() and not re.match(r"^(\s*)([-*]|\d+\.)\s+", lines[i]) and not lines[i].startswith(("#", "```", "|", ">", ":::")):
                    if lines[i].startswith("  "):
                        items[-1][1].append(lines[i].strip())
                        i += 1
                    else:
                        break
            tag = "ol" if ordered else "ul"
            out.append(f"<{tag}>")
            for text, extra in items:
                body = inline(text)
                if extra:
                    body += "<br>" + " ".join(inline(x) for x in extra)
                out.append(f"<li>{body}</li>")
            out.append(f"</{tag}>")
            continue
        # raw html block
        if line.lstrip().startswith("<"):
            buf = [line]
            i += 1
            while i < len(lines) and lines[i].strip() and not lines[i].startswith(("#", "```", "|", ":::")):
                buf.append(lines[i])
                i += 1
            out.append("\n".join(buf))
            continue
        # paragraph
        buf = [line]
        i += 1
        while i < len(lines) and lines[i].strip() and not re.match(r"^(#{1,4}\s|```|\||>|:::|!\[|\s*([-*]|\d+\.)\s)", lines[i]):
            buf.append(lines[i])
            i += 1
        out.append("<p>" + inline(" ".join(x.strip() for x in buf)) + "</p>")
    return "\n".join(out)


def strip_tags(s):
    s = re.sub(r"<script.*?</script>", " ", s, flags=re.S)
    s = re.sub(r'<a class="h-anchor"[^>]*>.*?</a>', " ", s, flags=re.S)
    s = re.sub(r"<[^>]+>", " ", s)
    s = html.unescape(s)
    return re.sub(r"\s+", " ", s).strip()


# ---------------------------------------------------------------- data
CHAPTERS = [
    # num, zh, en, part, tagline
    (1, "80386 导论", "Introduction to the 80386", "p0", "手册的组织方式、相关文献与记号约定。"),
    (2, "基本编程模型", "Basic Programming Model", "p1", "存储组织、数据类型、寄存器、指令格式与操作数选择。"),
    (3, "应用程序指令集", "Applications Instruction Set", "p1", "数据传送、算术、逻辑、控制转移、串操作与杂项指令。"),
    (4, "系统架构", "Systems Architecture", "p2", "系统寄存器、系统指令与整体架构视图。"),
    (5, "内存管理", "Memory Management", "p2", "段转换、页转换，以及两者如何协同工作。"),
    (6, "保护", "Protection", "p2", "段级保护、页级保护、特权级与访问控制。"),
    (7, "多任务", "Multitasking", "p2", "任务状态段、任务门与硬件任务切换。"),
    (8, "输入/输出", "Input/Output", "p2", "I/O 寻址、I/O 指令与 I/O 特权级。"),
    (9, "异常与中断", "Exceptions and Interrupts", "p2", "中断识别、优先级、IDT、错误码与异常条件。"),
    (10, "初始化", "Initialization", "p2", "复位后的处理器状态、实模式与保护模式初始化。"),
    (11, "协处理与多处理", "Coprocessing and Multiprocessing", "p2", "协处理器接口、多处理器总线与一致性。"),
    (12, "调试", "Debugging", "p2", "调试寄存器、断点与调试异常。"),
    (13, "执行 80286 保护模式代码", "Executing 80286 Protected-Mode Code", "p3", "兼容性、两种执行方式与行为差异。"),
    (14, "80386 实地址模式", "80386 Real-Address Mode", "p3", "物理地址形成、中断处理与模式切换。"),
    (15, "虚拟 8086 模式", "Virtual 8086 Mode", "p3", "V86 任务结构、进入与离开、虚拟 I/O。"),
    (16, "混合 16 位与 32 位代码", "Mixing 16-Bit and 32-Bit Code", "p3", "操作数/地址大小属性与控制转移。"),
    (17, "80386 指令集", "80386 Instruction Set", "p4", "按字母顺序排列的完整指令参考。"),
]

PARTS = [
    ("p0", "导论", "Introduction"),
    ("p1", "第一部分", "应用程序设计"),
    ("p2", "第二部分", "系统程序设计"),
    ("p3", "第三部分", "兼容性"),
    ("p4", "第四部分", "指令集"),
]

CHAPTER_BY_NUM = {c[0]: c for c in CHAPTERS}


def collect_sections():
    """Scan content/chNN/*.md, return {chapter_num: [section dicts]}."""
    result = {n: [] for n in range(1, 18)}
    for num in range(1, 18):
        folder = os.path.join(CONTENT, f"ch{num:02d}")
        if not os.path.isdir(folder):
            continue
        for name in sorted(os.listdir(folder)):
            if not name.endswith(".md"):
                continue
            meta, body = parse_front_matter(read(os.path.join(folder, name)))
            if meta.get("draft") == "true":
                continue
            meta["body"] = body
            meta["file"] = name
            result[num].append(meta)
        result[num].sort(key=lambda m: [int(x) for x in re.findall(r"\d+", m.get("num", "0"))] or [0])
    return result


def collect_simple(folder):
    path = os.path.join(CONTENT, folder)
    items = []
    if not os.path.isdir(path):
        return items
    for name in sorted(os.listdir(path)):
        if name.endswith(".md"):
            meta, body = parse_front_matter(read(os.path.join(path, name)))
            meta["body"] = body
            meta["file"] = name
            items.append(meta)
    return items


# ---------------------------------------------------------------- html shell
def rel_root(depth):
    return "../" * depth


def nav_html(sections_by_ch, active_ch=None, active_ins=None, depth=1, compact=False):
    r = rel_root(depth)
    out = ['<nav class="toc" aria-label="全书目录">']
    for pid, label, zh in PARTS:
        chapters = [c for c in CHAPTERS if c[3] == pid]
        if not chapters:
            continue
        out.append(f'<div class="toc-part"><span class="toc-part-label">{label}</span><span class="toc-part-zh">{zh}</span></div>')
        for num, zh, en, _, _ in chapters:
            secs = sections_by_ch.get(num, [])
            is_active = (active_ch == num)
            open_cls = " is-open" if is_active else ""
            href = f"{r}ch/{num:02d}.html"
            out.append(f'<div class="toc-chapter{open_cls}">')
            out.append(
                f'<a class="toc-ch-link" href="{href}"><span class="toc-num">{num:02d}</span>'
                f'<span class="toc-ch-title">{esc(zh)}</span></a>'
            )
            if secs:
                out.append('<ul class="toc-secs">')
                for s in secs:
                    sid = s.get("id", "")
                    out.append(
                        f'<li><a href="{href}#{sid}"><span class="toc-sec-num">{esc(s.get("num",""))}</span>'
                        f'<span>{esc(s.get("title",""))}</span></a></li>'
                    )
                out.append("</ul>")
            out.append("</div>")
    # extras
    out.append('<div class="toc-part"><span class="toc-part-label">附录</span><span class="toc-part-zh">参考数据</span></div>')
    out.append('<div class="toc-chapter"><a class="toc-ch-link" href="' + r + 'app/index.html"><span class="toc-num">A–D</span><span class="toc-ch-title">附录与速查表</span></a></div>')
    out.append('<div class="toc-part"><span class="toc-part-label">参考</span><span class="toc-part-zh">阅读辅助</span></div>')
    out.append('<div class="toc-chapter"><a class="toc-ch-link" href="' + r + 'ins/index.html"><span class="toc-num">I</span><span class="toc-ch-title">指令索引</span></a></div>')
    out.append('<div class="toc-chapter"><a class="toc-ch-link" href="' + r + 'glossary.html"><span class="toc-num">G</span><span class="toc-ch-title">术语对照表</span></a></div>')
    out.append("</nav>")
    return "\n".join(out)


def page_shell(title, body, sections_by_ch, active_ch=None, depth=1, body_class="", description="", active_ins=None, wide=False):
    r = rel_root(depth)
    css = f"{r}assets/site.css?v={{ASSET_VER}}"
    js = f"{r}assets/site.js?v={{ASSET_VER}}"
    nav = nav_html(sections_by_ch, active_ch=active_ch, active_ins=active_ins, depth=depth)
    desc = attr(description or SITE_DESC)
    import time
    ver = str(int(time.time()))
    return f"""<!DOCTYPE html>
<html lang="zh-CN" data-theme="auto">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="book">
<link rel="icon" href="{r}assets/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="{css.replace("{ASSET_VER}", ver)}">
<script>try{{var t=localStorage.getItem('i386-theme');if(t)document.documentElement.dataset.theme=t;var f=localStorage.getItem('i386-font');if(f)document.documentElement.style.setProperty('--reader-font-scale',f);}}catch(e){{}}</script>
</head>
<body class="{body_class}" data-root="{r}">
<a class="skip-link" href="#main">跳到正文</a>
<header class="topbar">
  <button class="icon-btn menu-btn" type="button" aria-label="打开目录" data-action="menu">
    <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 6h16M4 12h16M4 18h16"/></svg>
  </button>
  <a class="brand" href="{r}index.html" aria-label="返回首页">
    <span class="brand-mark">i386</span>
    <span class="brand-text"><strong>程序员参考手册</strong><em>Programmer's Reference Manual</em></span>
  </a>
  <div class="topbar-spacer"></div>
  <button class="search-trigger" type="button" data-action="search" aria-label="全文检索">
    <svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.6-3.6"/></svg>
    <span>检索全书</span><kbd>⌘K</kbd>
  </button>
  <button class="icon-btn" type="button" aria-label="调整字号" data-action="font" title="调整字号">
    <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 19 9.5 5h1L16 19M6.2 14.5h7.6M17 19l3-7 3 7M18 16.6h4"/></svg>
  </button>
  <button class="icon-btn" type="button" aria-label="切换主题" data-action="theme" title="切换浅色/深色">
    <svg class="i-sun" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="4.2"/><path d="M12 2v2.4M12 19.6V22M2 12h2.4M19.6 12H22M4.9 4.9l1.7 1.7M17.4 17.4l1.7 1.7M19.1 4.9l-1.7 1.7M6.6 17.4l-1.7 1.7"/></svg>
    <svg class="i-moon" viewBox="0 0 24 24" aria-hidden="true"><path d="M20 14.5A8.2 8.2 0 0 1 9.5 4a8.3 8.3 0 1 0 10.5 10.5Z"/></svg>
  </button>
  <button class="icon-btn" type="button" aria-label="打印本章" data-action="print" title="打印">
    <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M7 9V3h10v6M7 17H5a2 2 0 0 1-2-2v-4a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2v4a2 2 0 0 1-2 2h-2"/><rect x="7" y="14" width="10" height="7"/></svg>
  </button>
</header>
<div class="progress" aria-hidden="true"><span id="progress-bar"></span></div>
<div class="layout{' layout-wide' if wide else ''}">
  <aside class="sidebar" id="sidebar">
    <div class="sidebar-head">
      <span class="sidebar-kicker">目录</span>
      <button class="icon-btn sidebar-close" type="button" aria-label="关闭目录" data-action="menu">
        <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 6l12 12M18 6 6 18"/></svg>
      </button>
    </div>
    {nav}
    <div class="sidebar-foot">
      <a href="{r}about.html">关于本译本</a>
      <a href="https://pdos.csail.mit.edu/6.828/2018/readings/i386/toc.htm" target="_blank" rel="noopener">英文原书 ↗</a>
    </div>
  </aside>
  <div class="scrim" data-action="menu" hidden></div>
  <main id="main" class="main">{body}</main>
</div>
<div class="search-modal" id="search-modal" hidden>
  <div class="search-backdrop" data-action="search-close"></div>
  <div class="search-panel" role="dialog" aria-modal="true" aria-label="全文检索">
    <div class="search-box">
      <svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.6-3.6"/></svg>
      <input type="search" id="search-input" placeholder="检索章节、术语或指令，如：段描述符、分页、MOV" autocomplete="off" spellcheck="false">
      <kbd class="search-esc">ESC</kbd>
    </div>
    <div class="search-hint" id="search-hint">输入关键词开始检索。支持中文与英文术语。</div>
    <div class="search-results" id="search-results"></div>
    <div class="search-foot"><span><kbd>↑</kbd><kbd>↓</kbd> 选择</span><span><kbd>↵</kbd> 打开</span><span id="search-count"></span></div>
  </div>
</div>
<button class="to-top" type="button" aria-label="回到顶部" data-action="top">
  <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 19V5M5 12l7-7 7 7"/></svg>
</button>
<script src="{js.replace("{ASSET_VER}", ver)}" defer></script>
</body>
</html>
"""


# ---------------------------------------------------------------- pages
def build_chapter(num, secs, sections_by_ch):
    zh, en, part, tagline = CHAPTER_BY_NUM[num][1], CHAPTER_BY_NUM[num][2], CHAPTER_BY_NUM[num][3], CHAPTER_BY_NUM[num][4]
    part_label = next(p[1] for p in PARTS if p[0] == part)
    part_zh = next(p[2] for p in PARTS if p[0] == part)
    total_chars = sum(len(strip_tags(render_markdown(s["body"], heading_offset=1))) for s in secs)
    pages = [int(s["page"]) for s in secs if s.get("page", "").isdigit()]
    page_span = f"pp. {min(pages)}–{max(pages)}" if pages else ""
    toc_items = []
    for s in secs:
        heads = []
        render_markdown(s["body"], heads, heading_offset=1)
        subs = [h for h in heads if h["level"] == 3]
        toc_items.append((s, subs))
    sec_toc = ['<ol class="page-toc">']
    for s, subs in toc_items:
        sec_toc.append(f'<li><a href="#{s["id"]}"><span>{esc(s.get("num",""))}</span>{esc(s.get("title",""))}</a>')
        if subs:
            sec_toc.append("<ul>" + "".join(f'<li><a href="#{h["id"]}">{esc(re.sub(r"^\d+(\.\d+)*\s*", "", h["text"]))}</a></li>' for h in subs) + "</ul>")
        sec_toc.append("</li>")
    sec_toc.append("</ol>")

    body = [f'<article class="chapter" data-chapter="{num}">']
    body.append(f'''<header class="chapter-head">
  <p class="eyebrow">{part_zh if part_label == part_zh else part_label + " · " + part_zh}</p>
  <div class="chapter-title-row">
    <div class="chapter-num" aria-hidden="true">{num:02d}</div>
    <div class="chapter-titles">
      <h1>{esc(zh)}</h1>
      <p class="chapter-en">{esc(en)}</p>
    </div>
  </div>
  <p class="chapter-tagline">{esc(tagline)}</p>
  <dl class="chapter-meta">
    <div><dt>原书页码</dt><dd>{page_span}</dd></div>
    <div><dt>小节</dt><dd>{len(secs)}</dd></div>
    <div><dt>正文</dt><dd>约 {total_chars // 1000 if total_chars >= 1000 else 1},000 字</dd></div>
  </dl>
</header>''')
    body.append(f'<details class="inline-toc" open><summary>本章目录</summary>{sec_toc[0]}{"".join(sec_toc[1:])}</details>')
    body.append('<div class="chapter-body">')
    for s in secs:
        sid = s["id"]
        body.append(f'<section class="sec" id="{sid}" data-sec="{esc(s.get("num",""))}">')
        rendered_sec = render_markdown(s["body"], heading_offset=1)
        rendered_sec = rendered_sec.replace('src="fig', 'src="../assets/figures/fig').replace('href="fig', 'href="../assets/figures/fig')
        body.append(rendered_sec)
        if s.get("page"):
            body.append(f'<p class="sec-source">原书 p. {esc(s["page"])}</p>')
        body.append("</section>")
    body.append("</div>")
    # prev / next
    prev_c = CHAPTER_BY_NUM.get(num - 1)
    next_c = CHAPTER_BY_NUM.get(num + 1)
    body.append('<nav class="pager" aria-label="章节翻页">')
    if prev_c:
        body.append(f'<a class="pager-prev" href="{num-1:02d}.html"><span>上一章</span><strong>{esc(prev_c[1])}</strong></a>')
    else:
        body.append('<span class="pager-empty"></span>')
    if next_c:
        body.append(f'<a class="pager-next" href="{num+1:02d}.html"><span>下一章</span><strong>{esc(next_c[1])}</strong></a>')
    else:
        body.append('<a class="pager-next" href="../ins/index.html"><span>继续</span><strong>指令索引</strong></a>')
    body.append("</nav>")
    body.append("</article>")
    # right rail
    rail = ['<aside class="rail" aria-label="本章小节">', '<div class="rail-inner"><p class="rail-title">本章</p><ol class="rail-list">']
    for s, _ in toc_items:
        rail.append(f'<li><a href="#{s["id"]}" data-spy="{s["id"]}">{esc(s.get("num",""))} {esc(s.get("title",""))}</a></li>')
    rail.append("</ol></div></aside>")
    content = "".join(body) + "".join(rail)
    title = f"{zh} · 第 {num} 章 — {SITE_TITLE}"
    return page_shell(title, content, sections_by_ch, active_ch=num, depth=1, body_class="reading", description=f"{zh}（{en}）：{tagline}")


def build_index(sections_by_ch):
    stats_sections = sum(len(v) for v in sections_by_ch.values())
    ins_count = len(collect_simple("ins"))
    toc = []
    for pid, label, zh in PARTS:
        chs = [c for c in CHAPTERS if c[3] == pid]
        if not chs:
            continue
        toc.append(f'<section class="toc-block"><div class="toc-block-head"><span>{label}</span><h2>{zh}</h2></div><ol class="toc-books">')
        for num, czh, cen, _, tagline in chs:
            n = len(sections_by_ch.get(num, []))
            toc.append(
                f'<li><a href="ch/{num:02d}.html"><span class="tb-num">{num:02d}</span>'
                f'<span class="tb-main"><strong>{esc(czh)}</strong><em>{esc(cen)}</em><small>{esc(tagline)}</small></span>'
                f'<span class="tb-count">{n} 节</span></a></li>'
            )
        toc.append("</ol></section>")
    hero = f'''<section class="cover">
  <div class="cover-inner">
    <p class="cover-kicker">INTEL · 1986 · 中文译本</p>
    <h1><span class="cover-386">80386</span>程序员参考手册</h1>
    <p class="cover-en">INTEL 80386 PROGRAMMER'S REFERENCE MANUAL</p>
    <p class="cover-lead">理解 x86 保护模式的第一手文献。分段与分页、特权级与保护、硬件任务切换、异常与中断，以及完整的指令编码参考。</p>
    <div class="cover-actions">
      <a class="btn btn-primary" href="ch/01.html">开始阅读<span>→</span></a>
      <a class="btn" href="ch/05.html">直接看内存管理</a>
    </div>
    <dl class="cover-stats">
      <div><dt>{len(CHAPTERS)}</dt><dd>章</dd></div>
      <div><dt>{stats_sections}</dt><dd>节</dd></div>
      <div><dt>{ins_count}</dt><dd>条指令</dd></div>
      <div><dt>421</dt><dd>页原书</dd></div>
    </dl>
  </div>
  <div class="cover-art" aria-hidden="true">
    <div class="die">
      <span class="die-label">80386</span>
      <span class="die-sub">32-BIT MICROPROCESSOR</span>
    </div>
  </div>
</section>
<section class="intro-grid">
  <div><h2>为什么读这本</h2><p>这是 Intel 官方在 1986 年给出的 80386 体系结构定义。今天所有 x86-64 处理器仍然从复位那一刻起兼容它：实模式、段描述符、页表、IDT、任务切换。读懂这本，再读现代内核代码，很多“历史包袱”会变成清晰的设计决策。</p></div>
  <div><h2>怎么读</h2><p>应用程序员从第 2、3 章开始；系统程序员按第 4→6→9→10 章顺序推进；第 17 章与附录作为案头速查。每节末尾标注原书页码，便于核查。</p></div>
</section>
<section class="toc-full">
  <div class="section-head"><p class="eyebrow">CONTENTS</p><h2>全书目录</h2></div>
  {"".join(toc)}
  <section class="toc-block"><div class="toc-block-head"><span>附录</span><h2>参考数据</h2></div>
  <ol class="toc-books">
    <li><a href="app/index.html"><span class="tb-num">A–D</span><span class="tb-main"><strong>操作码表、标志位对照、条件码</strong><em>Appendices</em><small>指令编码速查与标志位语义汇总。</small></span><span class="tb-count">4 篇</span></a></li>
    <li><a href="ins/index.html"><span class="tb-num">I</span><span class="tb-main"><strong>指令索引</strong><em>Instruction Index</em><small>94 条指令，按字母顺序排列。</small></span><span class="tb-count">A–Z</span></a></li>
    <li><a href="glossary.html"><span class="tb-num">G</span><span class="tb-main"><strong>术语对照表</strong><em>Glossary</em><small>英中术语、缩写与关键概念索引。</small></span><span class="tb-count">术语</span></a></li>
  </ol></section>
</section>'''
    return page_shell(SITE_TITLE, hero, sections_by_ch, depth=0, body_class="home", description=SITE_DESC, wide=True)


def build_instruction_pages(items, sections_by_ch):
    by_letter = {}
    for it in items:
        letter = it.get("group", it["id"][0]).upper()
        by_letter.setdefault(letter, []).append(it)
    for letter in by_letter:
        by_letter[letter].sort(key=lambda x: x["id"])
    # index page
    blocks = []
    for letter in sorted(by_letter):
        blocks.append(f'<div class="ins-group"><h2 id="g-{letter}">{letter}</h2><ul class="ins-list">')
        for it in by_letter[letter]:
            blocks.append(f'<li><a href="{it["id"].lower()}.html"><code>{esc(it["id"])}</code><span>{esc(it.get("title",""))}</span><em>{esc(it.get("en",""))}</em></a></li>')
        blocks.append("</ul></div>")
    letters = "".join(f'<a href="#g-{l}">{l}</a>' for l in sorted(by_letter))
    body = f'''<article class="chapter">
<header class="chapter-head">
  <p class="eyebrow">第四部分 · 指令集</p>
  <div class="chapter-title-row"><div class="chapter-num">17</div>
  <div class="chapter-titles"><h1>指令索引</h1><p class="chapter-en">Instruction Set Index</p></div></div>
  <p class="chapter-tagline">按助记符字母顺序排列的 94 条指令。每条包含操作码、时钟数、操作语义、标志位与异常。</p>
</header>
<nav class="letter-nav" aria-label="字母索引">{letters}</nav>
<div class="ins-groups">{"".join(blocks)}</div>
</article>'''
    pages = {"ins/index.html": page_shell("指令索引 — " + SITE_TITLE, body, sections_by_ch, active_ch=17, depth=1)}

    order = [it for l in sorted(by_letter) for it in by_letter[l]]
    for idx, it in enumerate(order):
        prev_it = order[idx - 1] if idx > 0 else None
        next_it = order[idx + 1] if idx + 1 < len(order) else None
        body_md = re.sub(r"^#\s+.*?\n", "", it["body"], count=1)
        rendered = render_markdown(body_md)
        meta = []
        if it.get("page"):
            meta.append(f'原书 p. {esc(it["page"])}')
        if it.get("clocks"):
            meta.append(f'时钟数 {esc(it["clocks"])}')
        art = f'''<article class="chapter ins-page">
<header class="ins-head">
  <p class="eyebrow">指令参考 · 第 17 章</p>
  <h1><code>{esc(it["id"])}</code> <span>{esc(it.get("title",""))}</span></h1>
  <p class="chapter-en">{esc(it.get("en",""))}</p>
  <p class="ins-meta">{" · ".join(meta)}</p>
</header>
<div class="chapter-body">{rendered}</div>
<nav class="pager" aria-label="指令翻页">
  {f'<a class="pager-prev" href="{prev_it["id"].lower()}.html"><span>上一条</span><strong>{esc(prev_it["id"])} {esc(prev_it.get("title",""))}</strong></a>' if prev_it else '<a class="pager-prev" href="index.html"><span>返回</span><strong>指令索引</strong></a>'}
  {f'<a class="pager-next" href="{next_it["id"].lower()}.html"><span>下一条</span><strong>{esc(next_it["id"])} {esc(next_it.get("title",""))}</strong></a>' if next_it else '<a class="pager-next" href="../app/index.html"><span>继续</span><strong>附录</strong></a>'}
</nav>
</article>'''
        pages[f'ins/{it["id"].lower()}.html'] = page_shell(
            f'{it["id"]} — {it.get("title","")} · {SITE_TITLE}', art, sections_by_ch,
            active_ch=17, depth=1, body_class="reading", description=f'{it["id"]}（{it.get("en","")}）指令参考。'
        )
    return pages


def build_appendices(items, sections_by_ch):
    index_cards = []
    pages = {}
    for it in items:
        index_cards.append(f'''<a class="app-card" href="{it["id"]}.html">
  <span class="app-letter">{esc(it.get("letter", it["id"].upper()))}</span>
  <span class="app-main"><strong>{esc(it.get("title",""))}</strong><em>{esc(it.get("en",""))}</em><small>{esc(it.get("desc",""))}</small></span>
  <span class="app-arrow">→</span></a>''')
        art = f'''<article class="chapter">
<header class="chapter-head">
  <p class="eyebrow">附录 · {esc(it.get("letter", ""))}</p>
  <div class="chapter-title-row"><div class="chapter-num">{esc(it.get("letter",""))}</div>
  <div class="chapter-titles"><h1>{esc(it.get("title",""))}</h1><p class="chapter-en">{esc(it.get("en",""))}</p></div></div>
  <p class="chapter-tagline">{esc(it.get("desc",""))}</p>
</header>
<div class="chapter-body">{render_markdown(re.sub(r"^#\s+.*?\n", "", it["body"], count=1))}</div>
<nav class="pager"><a class="pager-prev" href="index.html"><span>返回</span><strong>附录索引</strong></a>
<a class="pager-next" href="../glossary.html"><span>继续</span><strong>术语对照表</strong></a></nav>
</article>'''
        pages[f'app/{it["id"]}.html'] = page_shell(f'{it.get("title","")} — {SITE_TITLE}', art, sections_by_ch, depth=1, body_class="reading")
    idx = f'''<article class="chapter">
<header class="chapter-head"><p class="eyebrow">参考数据</p>
<div class="chapter-title-row"><div class="chapter-num">A–D</div>
<div class="chapter-titles"><h1>附录</h1><p class="chapter-en">Appendices</p></div></div>
<p class="chapter-tagline">操作码表、标志位交叉引用、状态标志汇总与条件码。</p></header>
<div class="app-grid">{"".join(index_cards)}</div>
</article>'''
    pages["app/index.html"] = page_shell("附录 — " + SITE_TITLE, idx, sections_by_ch, depth=1)
    return pages


def build_static_pages(sections_by_ch):
    pages = {}
    # glossary
    rows = []
    gpath = os.path.join(CONTENT, "glossary.md")
    if os.path.exists(gpath):
        meta, body = parse_front_matter(read(gpath))
        content = render_markdown(body)
    else:
        content = "<p>术语表尚未生成。</p>"
    pages["glossary.html"] = page_shell("术语对照表 — " + SITE_TITLE, f'<article class="chapter prose-page"><header class="chapter-head"><p class="eyebrow">参考</p><div class="chapter-title-row"><div class="chapter-num">G</div><div class="chapter-titles"><h1>术语对照表</h1><p class="chapter-en">Glossary</p></div></div><p class="chapter-tagline">全书的术语译法约定。正文首次出现时以「中文（English）」标注。</p></header><div class="chapter-body">{content}</div></article>', sections_by_ch, depth=0, body_class="reading")
    # about
    apath = os.path.join(CONTENT, "about.md")
    about = render_markdown(parse_front_matter(read(apath))[1]) if os.path.exists(apath) else "<p>缺少 about.md</p>"
    pages["about.html"] = page_shell("关于本译本 — " + SITE_TITLE, f'<article class="chapter prose-page"><header class="chapter-head"><p class="eyebrow">COLOPHON</p><div class="chapter-title-row"><div class="chapter-num">i</div><div class="chapter-titles"><h1>关于本译本</h1><p class="chapter-en">About this edition</p></div></div><p class="chapter-tagline">底本、翻译原则、术语约定与技术实现。</p></header><div class="chapter-body">{about}</div></article>', sections_by_ch, depth=0, body_class="reading")
    # 404
    pages["404.html"] = page_shell("页面未找到 — " + SITE_TITLE, '<article class="chapter prose-page"><header class="chapter-head"><p class="eyebrow">404</p><h1>这一页不在手册里</h1></header><div class="chapter-body"><p>链接可能已经变更。回到<a href="./index.html">目录</a>，或按 <kbd>⌘K</kbd> 检索全书。</p></div></article>', sections_by_ch, depth=0)
    return pages


def build_search_index(pages_text):
    docs = []
    for item in pages_text:
        docs.append({
            "u": item["url"],
            "t": item["title"],
            "c": item.get("chapter", ""),
            "n": item.get("num", ""),
            "x": item["text"][:6000],
        })
    return json.dumps({"docs": docs}, ensure_ascii=False, separators=(",", ":"))


def main():
    if os.path.isdir(SITE):
        shutil.rmtree(SITE)
    os.makedirs(os.path.join(SITE, "assets"), exist_ok=True)
    os.makedirs(os.path.join(SITE, "ch"), exist_ok=True)
    os.makedirs(os.path.join(SITE, "ins"), exist_ok=True)
    os.makedirs(os.path.join(SITE, "app"), exist_ok=True)
    open(os.path.join(SITE, ".nojekyll"), "w").close()
    open(os.path.join(SITE, ".nojekyll"), "w").close()

    sections_by_ch = collect_sections()
    search_docs = []
    written = 0

    for num in range(1, 18):
        secs = sections_by_ch[num]
        html_page = build_chapter(num, secs, sections_by_ch)
        path = os.path.join(SITE, "ch", f"{num:02d}.html")
        with open(path, "w", encoding="utf-8") as f:
            f.write(html_page)
        written += 1
        for s in secs:
            text = strip_tags(render_markdown(s["body"], heading_offset=1))
            search_docs.append({
                "url": f"ch/{num:02d}.html#{s['id']}",
                "title": f'{s.get("num","")} {s.get("title","")}'.strip(),
                "chapter": f"第 {num} 章 {CHAPTER_BY_NUM[num][1]}",
                "num": s.get("num", ""),
                "text": text,
            })

    ins_items = collect_simple("ins")
    for url, page in build_instruction_pages(ins_items, sections_by_ch).items():
        with open(os.path.join(SITE, url), "w", encoding="utf-8") as f:
            f.write(page)
        written += 1
    for it in ins_items:
        m = re.search(r"## 说明[ \t]*\n(.*?)(?=\n## |\Z)", it["body"], re.S)
        ins_text = strip_tags(render_markdown(m.group(1))) if m else strip_tags(render_markdown(it["body"]))
        search_docs.append({
            "url": f"ins/{it['id'].lower()}.html",
            "title": f'{it["id"]} {it.get("title","")}',
            "chapter": "指令参考",
            "num": it["id"],
            "text": ins_text,
        })

    app_items = collect_simple("app")
    for url, page in build_appendices(app_items, sections_by_ch).items():
        with open(os.path.join(SITE, url), "w", encoding="utf-8") as f:
            f.write(page)
        written += 1
    for it in app_items:
        search_docs.append({
            "url": f'app/{it["id"]}.html',
            "title": it.get("title", ""),
            "chapter": "附录",
            "num": it.get("letter", ""),
            "text": strip_tags(render_markdown(it["body"])),
        })

    index_html = build_index(sections_by_ch)
    with open(os.path.join(SITE, "index.html"), "w", encoding="utf-8") as f:
        f.write(index_html)
    written += 1

    for url, page in build_static_pages(sections_by_ch).items():
        with open(os.path.join(SITE, url), "w", encoding="utf-8") as f:
            f.write(page)
        written += 1

    # assets
    for name in ("site.css", "site.js", "favicon.svg"):
        src = os.path.join(ROOT, "assets", name)
        if os.path.exists(src):
            shutil.copy2(src, os.path.join(SITE, "assets", name))
    fig_out = os.path.join(SITE, "assets", "figures")
    os.makedirs(os.path.join(fig_out, "svg"), exist_ok=True)
    svg_src = os.path.join(ROOT, "figures", "svg")
    if os.path.isdir(svg_src):
        for name in os.listdir(svg_src):
            if name.endswith(".svg"):
                shutil.copy2(os.path.join(svg_src, name), os.path.join(fig_out, "svg", name))
    if os.path.isdir(FIGURES):
        for name in os.listdir(FIGURES):
            if name.lower().endswith((".gif", ".png", ".jpg", ".svg")):
                shutil.copy2(os.path.join(FIGURES, name), os.path.join(fig_out, name))

    with open(os.path.join(SITE, "assets", "search.json"), "w", encoding="utf-8") as f:
        f.write(build_search_index(search_docs))

    with open(os.path.join(SITE, "robots.txt"), "w", encoding="utf-8") as f:
        f.write("User-agent: *\nAllow: /\nSitemap: sitemap.xml\n")
    print(f"built {written} pages, {len(search_docs)} search docs")
    total_chars = sum(len(d["text"]) for d in search_docs)
    print(f"content: {total_chars:,} chars")


if __name__ == "__main__":
    main()
