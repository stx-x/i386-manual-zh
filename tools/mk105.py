#!/usr/bin/env python3
import os, re, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src = open(os.path.join(ROOT, "source", "clean", "s10_05.md"), encoding="utf-8").read()
body = src.split("\n", 1)[1].strip()
body = re.sub(r"^```[^\n]*\n", "", body)
body = re.sub(r"\n```\s*$", "", body)
body = re.sub(r"<[^>]+>", "", body)
body = html.unescape(body)

out = """---
id: s10_05
num: "10.5"
title: 初始化示例
en: Initialization Example
page: 180
---

# 10.5 初始化示例

下面是一份完整的 80386 初始化代码清单：从复位后的实地址模式开始，建立 GDT、IDT、初始 TSS 与初始 LDT，切换到保护模式并启动第一个任务。代码中的注释保留原书的英文写法，以便与汇编语法和原书对照。

```asm
""" + body + """
```

::: note
原书代码使用 Intel 汇编语法与 386 汇编器伪指令（`$TITLE`、`SEGMENT`、`ENDS` 等）。若要在现代工具链上重建，应改用 NASM/GAS 语法并自行定义段与描述符布局；本清单的价值在于展示初始化步骤的顺序与各描述符的构造方式。
:::
"""
open(os.path.join(ROOT, "content", "ch10", "05.md"), "w", encoding="utf-8").write(out)
print("wrote", len(body), "chars of code")
