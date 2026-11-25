---
id: LGDT
title: 装入全局/中断描述符表寄存器
en: Load Global/Interrupt Descriptor Table Register
group: L
---

# LGDT -- 装入全局/中断描述符表寄存器

## 操作码

```
Opcode       Instruction      Clocks        Description

0F  01 /2    LGDT m16&32      11            Load m into GDTR
0F  01 /3    LIDT m16&32      11            Load m into IDTR
```

## 操作

```
IF instruction = LIDT
THEN
   IF OperandSize = 16
   THEN IDTR.Limit:Base := m16:24 (* 24 bits of base loaded *)
   ELSE IDTR.Limit:Base := m16:32
   FI;
ELSE (* instruction = LGDT *)
   IF OperandSize = 16
   THEN GDTR.Limit:Base := m16:24 (* 24 bits of base loaded *)
   ELSE GDTR.Limit:Base := m16:32;
   FI;
FI;
```

## 说明

从内存操作数装入 GDTR（LGDT）或 IDTR（LIDT）的基地址与界限；特权指令。

## 影响的标志

无。

## 保护模式异常（原文）

::: note
#GP(0) if the current privilege level is not 0; #UD if the source operand is a register; #GP(0) for an illegal memory operand effective address in the CS, DS, ES, FS, or GS segments; #SS(0) for an illegal address in the SS segment; #PF(fault-code) for a page fault
:::

## 实地址模式异常（原文）

::: note
Interrupt 13 if any part of the operand would lie outside of the effective address space from 0 to 0FFFFH; Interrupt 6 if the source operand is a register

### Note

These instructions are valid in Real Address Mode to allow power-up initialization for Protected Mode
:::

## 虚拟 8086 模式异常（原文）

::: note
Same exceptions as in Real Address Mode; #PF(fault-code) for a page fault
:::
