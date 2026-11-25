---
id: STR
title: 保存任务寄存器
en: Store Task Register
group: S
page: 403
---

# STR -- 保存任务寄存器

## 操作码

```
Opcode        Instruction   Clocks       Description

0F  00 /1     STR r/m16     pm=23/27     Load EA word into task register
```

## 操作

```
r/m := task register;
```

## 说明

把 TR 的选择子存入通用寄存器或内存字。

## 影响的标志

无。

## 保护模式异常（原文）

::: note
#GP(0) if the result is in a nonwritable segment; #GP(0) for an illegal memory operand effective address in the CS, DS, ES, FS, or GS segments; #SS(0) for an illegal address in the SS segment; #PF(fault-code) for a page fault
:::

## 实地址模式异常（原文）

::: note
Interrupt 6; STR is not recognized in Real Address Mode
:::

## 虚拟 8086 模式异常（原文）

::: note
Same exceptions as in Real Address Mode
:::
