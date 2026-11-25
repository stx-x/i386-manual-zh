---
id: DEC
title: 减 1
en: Decrement by 1
group: D
page: 293
---

# DEC -- 减 1

## 操作码

```
Opcode    Instruction        Clocks   Description

FE /1     DEC r/m8           2/6      Decrement r/m byte by 1
FF /1     DEC r/m16          2/6      Decrement r/m word by 1
          DEC r/m32          2/6      Decrement r/m dword by 1
48+rw     DEC r16            2        Decrement word register by 1
48+rw     DEC r32            2        Decrement dword register by 1
```

## 操作

```
DEST := DEST - 1;
```

## 说明

把目的操作数减 1；更新 OF、SF、ZF、AF、PF，但不影响 CF。

## 影响的标志

OF、SF、ZF、AF、PF 按附录 C 所述。

## 保护模式异常（原文）

::: note
#GP(0) if the result is a nonwritable segment; #GP(0) for an illegal memory operand effective address in the CS, DS, ES, FS, or GS segments; #SS(0) for an illegal address in the SS segment; #PF(fault-code) for a page fault
:::

## 实地址模式异常（原文）

::: note
Interrupt 13 if any part of the operand would lie outside of the effective address space from 0 to 0FFFFH
:::

## 虚拟 8086 模式异常（原文）

::: note
Same exceptions as in Real Address Mode; #PF(fault-code) for a page fault
:::
