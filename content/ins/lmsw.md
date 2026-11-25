---
id: LMSW
title: 装入机器状态字
en: Load Machine Status Word
group: L
page: 335
---

# LMSW -- 装入机器状态字

## 操作码

```
Opcode      Instruction      Clocks   Description

0F  01 /6   LMSW r/m16       10/13    Load r/m16 in machine status word
```

## 操作

```
MSW := r/m16; (* 16 bits is stored in the machine status word *)
```

## 说明

把源操作数装入 CR0 的低 16 位（MSW）；为兼容 80286 而提供。

## 影响的标志

无。

## 保护模式异常（原文）

::: note
#GP(0) if the current privilege level is not 0; #GP(0) for an illegal memory operand effective address in the CS, DS, ES, FS, or GS segments; #SS(0) for an illegal address in the SS segment; #PF(fault-code) for a page fault
:::

## 实地址模式异常（原文）

::: note
Interrupt 13 if any part of the operand would lie outside of the effective address space from 0 to 0FFFFH
:::

## 虚拟 8086 模式异常（原文）

::: note
Same exceptions as in Real Address Mode; #PF(fault-code) for a page fault
:::
