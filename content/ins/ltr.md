---
id: LTR
title: 装入任务寄存器
en: Load Task Register
group: L
page: 344
---

# LTR -- 装入任务寄存器

## 操作码

```
Opcode       Instruction    Clocks    Description

0F  00 /3    LTR r/m16      pm=23/27  Load EA word into task register
```

## 说明

用选择子所指 TSS 描述符装入 TR，并把该 TSS 标记为忙；特权指令。

## 影响的标志

无。

## 保护模式异常（原文）

::: note
#GP(0) for an illegal memory operand effective address in the CS, DS, ES, FS, or GS segments; #SS(0) for an illegal address in the SS segment; #GP(0) if the current privilege level is not 0; #GP(selector) if the object named by the source selector is not a TSS or is already busy; #NP(selector) if the TSS is marked "not present"; #PF(fault-code) for a page fault
:::

## 实地址模式异常（原文）

::: note
Interrupt 6; LTR is not recognized in Real Address Mode
:::

## 虚拟 8086 模式异常（原文）

::: note
Same exceptions as in Real Address Mode
:::
