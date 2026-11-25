---
id: LLDT
title: 装入局部描述符表寄存器
en: Load Local Descriptor Table Register
group: L
page: 334
---

# LLDT -- 装入局部描述符表寄存器

## 操作码

```
Opcode      Instruction      Clocks   Description

0F  00 /2   LLDT r/m16       20       Load selector r/m16 into LDTR
```

## 操作

```
LDTR := SRC;
```

## 说明

用选择子所指 LDT 描述符装入 LDTR；特权指令。

## 影响的标志

无。

## 保护模式异常（原文）

::: note
#GP(0) if the current privilege level is not 0; #GP(selector) if the selector operand does not point into the Global Descriptor Table, or if the entry in the GDT is not a Local Descriptor Table; #NP(selector) if the LDT descriptor is not present; #GP(0) for an illegal memory operand effective address in the CS, DS, ES, FS, or GS segments; #SS(0) for an illegal address in the SS segment; #PF(fault-code) for a page fault
:::

## 实地址模式异常（原文）

::: note
Interrupt 6; LLDT is not recognized in Real Address Mode
:::

## 虚拟 8086 模式异常（原文）

::: note
Same exceptions as in Real Address Mode (because the instruction is not recognized, it will not execute or perform a memory reference)

### Note

The operand-size attribute has no effect on this instruction.
:::
