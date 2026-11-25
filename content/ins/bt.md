---
id: BT
title: 位测试
en: Bit Test
group: B
page: 267
---

# BT -- 位测试

## 操作码

```
Opcode         Instruction     Clocks    Description

0F  A3         BT r/m16,r16    3/12      Save bit in carry flag
0F  A3         BT r/m32,r32    3/12      Save bit in carry flag
0F  BA /4 ib   BT r/m16,imm8   3/6       Save bit in carry flag
0F  BA /4 ib   BT r/m32,imm8   3/6       Save bit in carry flag
```

## 操作

```
CF := BIT[LeftSRC, RightSRC];
```

## 说明

把目的操作数中由位偏移指定的位复制到 CF，不改变该位本身。

## 影响的标志

CF，如上述。

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
