---
id: SGDT
title: 保存全局/中断描述符表寄存器
en: Store Global/Interrupt Descriptor Table Register
group: S
---

# SGDT -- 保存全局/中断描述符表寄存器

## 操作码

```
Opcode       Instruction   Clocks   Description

0F  01 /0    SGDT m        9        Store GDTR to m
0F  01 /1    SIDT m        9        Store IDTR to m
```

## 操作

```
DEST := 48-bit BASE/LIMIT register contents;
```

## 说明

把 GDTR（SGDT）或 IDTR（SIDT）的基地址与界限存入内存。

## 影响的标志

无。

## 保护模式异常（原文）

::: note
Interrupt 6 if the destination operand is a register; #GP(0) if the destination is in a nonwritable segment; #GP(0) for an illegal memory operand effective address in the CS, DS, ES, FS, or GS segments; #SS(0) for an illegal address in the SS segment; #PF(fault-code) for a page fault
:::

## 实地址模式异常（原文）

::: note
Interrupt 6 if the destination operand is a register; Interrupt 13 if any part of the operand would lie outside of the effective address space from 0 to 0FFFFH
:::

## 虚拟 8086 模式异常（原文）

::: note
Same exceptions as in Real Address Mode; #PF(fault-code) for a page fault
:::
