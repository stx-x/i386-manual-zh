#!/usr/bin/env python3
"""Hand-built redraws for the two code-listing figures."""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "figures", "svg")
os.makedirs(OUT, exist_ok=True)


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def card(name, title, lines, code=False, width=720):
    lh = 22
    h = 44 + len(lines) * lh + 24
    out = [f'<svg class="redraw-svg" width="{width}" height="{h}" viewBox="0 0 {width} {h}" xmlns="http://www.w3.org/2000/svg" role="img">']
    out.append(f'<text x="24" y="30" font-size="15" font-weight="600" fill="currentColor" font-family="sans-serif">{esc(title)}</text>')
    out.append('<line x1="24" y1="42" x2="696" y2="42" stroke="currentColor" stroke-opacity="0.25"/>')
    for i, line in enumerate(lines):
        y = 66 + i * lh
        if code:
            if ";" in line:
                code_part, comment = line.split(";", 1)
                out.append(f'<text x="24" y="{y}" font-size="12.5" fill="currentColor" font-family="monospace" xml:space="preserve">{esc(code_part)}</text>')
                out.append(f'<text x="{24 + max(1, len(code_part)) * 7.5:.0f}" y="{y}" font-size="11.5" fill="currentColor" fill-opacity="0.6" font-family="sans-serif">;{esc(comment)}</text>')
            else:
                out.append(f'<text x="24" y="{y}" font-size="12.5" fill="currentColor" font-family="monospace">{esc(line)}</text>')
        else:
            out.append(f'<text x="24" y="{y}" font-size="13" fill="currentColor" font-family="sans-serif" xml:space="preserve">{esc(line)}</text>')
    out.append("</svg>")
    open(os.path.join(OUT, f"fig{name}.svg"), "w", encoding="utf-8").write("\n".join(out))
    print("wrote", name)


card("3-9", "用 SAR 模拟 IDIV（N 为 2 的幂）", [
    "; 假设 N 在 ECX 中，被除数在 EAX 中",
    "CMP  EAX, 0      ; 置符号标志",
    "JGE  NoAdjust    ; 符号为零则跳转",
    "ADD  EAX, ECX    ; 加上偏移量",
    "DEC  EAX         ; EAX := EAX + (N-1)",
    "NoAdjust:",
    "SAR  EAX, CL     ; 算术右移，完成除法",
    "; 总计约 12 或 18 个时钟",
], code=True)

card("3-16", "ENTER 指令的形式化定义", [
    "LEVEL 表示第二个操作数的值。",
    "",
    "压入 EBP",
    "FRAME_PTR := ESP",
    "若 LEVEL > 0：",
    "    重复 (LEVEL−1) 次：",
    "        EBP := EBP − 4",
    "        压入 EBP 所指的双字",
    "    结束重复",
    "    压入 FRAME_PTR",
    "结束若",
    "EBP := FRAME_PTR",
    "ESP := ESP − 第一个操作数",
])
