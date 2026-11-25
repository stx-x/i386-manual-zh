---
id: HLT
title: 停止处理器
en: Halt
group: H
page: 297
---

# HLT -- 停止处理器

## 操作码

```
Opcode      Instruction        Clocks     Description

F4          HLT                5          Halt
```

## 说明

使处理器停止取指，直到收到 INTR、NMI 或 RESET；特权指令。

## 影响的标志

无。

## 保护模式异常（原文）

::: note
HLT is a privileged instruction; #GP(0) if the current privilege level is not 0
:::

## 实地址模式异常（原文）

::: note
None
:::

## 虚拟 8086 模式异常（原文）

::: note
#GP(0); HLT is a privileged instruction
:::
