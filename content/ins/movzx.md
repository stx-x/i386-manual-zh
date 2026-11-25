---
id: MOVZX
title: 带零扩展传送
en: Move with Zero-Extend
group: M
page: 351
---

# MOVZX -- 带零扩展传送

## 操作码

```
Opcode      Instruction        Clocks   Description

0F  B6 /r   MOVZX r16,r/m8     3/6      Move byte to word with zero-extend
0F  B6 /r   MOVZX r32,r/m8     3/6      Move byte to dword, zero-extend
0F  B7 /r   MOVZX r32,r/m16    3/6      Move word to dword, zero-extend
```

## 操作

```
DEST := ZeroExtend(SRC);
```

## 说明

把 8 位或 16 位源操作数零扩展到 16 位或 32 位目的操作数。

## 影响的标志

无。

## 保护模式异常（原文）

::: note
#GP(0) for an illegal memory operand effective address in the CS, DS, ES, FS, or GS segments; #SS(0) for an illegal address in the SS segment; #PF(fault-code) for a page fault
:::

## 实地址模式异常（原文）

::: note
Interrupt 13 if any part of the operand would lie outside of the effective address space from 0 to 0FFFFH
:::

## 虚拟 8086 模式异常（原文）

::: note
Same exceptions as in Real Address Mode; #PF(fault-code) for a page fault
:::
