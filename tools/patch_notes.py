import os
p = 'tools/redraw.py'
s = open(p).read()
insert = '''
NOTES = {
    "3-6": ["SHL（同义助记符 SAL）把寄存器或内存操作数中的位左移指定的位数。CF 接收从", "操作数左端移出的最后一位；空出的低位补 0。这些指令可作用于字节、字和双字。"],
    "3-7": ["SHR 把寄存器或内存操作数中的位右移指定的位数。CF 接收从操作数右端移出的", "最后一位；空出的高位补 0。"],
    "3-22": ["LAHF 把标志寄存器中的五个标志装入 AH；SAHF 把 AH 中的同样五个标志写回", "标志寄存器。每个标志在 AH 与标志寄存器中的位位置相同。标为 UU 的其余位保留，未定义。"],
    "3-23": ["标为 0 和 1 的位由 Intel 保留，未定义。系统标志（包括 IOPL 字段以及 VM、", "RF、IF 标志）会被压栈，并对应用程序可见；但应用程序弹出标志时，这些项不会改变，", "无论弹出的值是什么。"],
}
'''
s = s.replace('CW, CH = 9, 16', 'CW, CH = 9, 16\n' + insert)
s = s.replace('''    w, h = cols * CW + pad * 2, rows * CH + pad * 2''','''    notes = NOTES.get(fig, [])
    w, h = cols * CW + pad * 2, rows * CH + pad * 2 + (len(notes) * 18 + 8 if notes else 0)''')
s = s.replace('''            if len(label_en) == 1 and not label_en.isdigit() and label_en != "+":
                continue''','''            if len(label_en) == 1 and not label_en.isdigit() and label_en != "+":
                continue
            if fig in NOTES and len(label_en) > 24:
                continue''')
s = s.replace('''    out.append("</g>")
    out.append("</svg>")''','''    out.append("</g>")
    if notes:
        out.append('<g class="rd-note" font-size="11">')
        for i, line in enumerate(notes):
            y = pad + rows * CH + 18 + i * 18
            out.append(f'<text x="{pad}" y="{y}" fill="currentColor">{esc(line)}</text>')
        out.append("</g>")
    out.append("</svg>")''')
open(p, 'w').write(s)
print('notes added')
