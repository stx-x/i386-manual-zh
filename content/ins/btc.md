---
id: BTC
title: 位测试并求反
en: Bit Test and Complement
group: B
page: 269
---

# BTC -- 位测试并求反

## 操作码

```
Opcode        Instruction     Clocks  Description

0F  BB        BTC r/m16,r16   6/13    Save bit in carry flag and complement
0F  BB        BTC r/m32,r32   6/13    Save bit in carry flag and complement
0F  BA /7 ib  BTC r/m16,imm8  6/8     Save bit in carry flag and complement
0F  BA /7 ib  BTC r/m32,imm8  6/8     Save bit in carry flag and complement
```

## 操作

```
CF := BIT[LeftSRC, RightSRC];
BIT[LeftSRC, RightSRC] := NOT BIT[LeftSRC, RightSRC];
```

## 说明

把指定位复制到 CF，然后对该位取反。

## 影响的标志

CF，如上述。

## 保护模式异常（原文）

::: note
#GP(0) if the result is in a nonwritable segment; #GP(0) for an illegal memory operand effective address in the CS, DS, ES, FS, or GS segments; #SS(0) for an illegal address in the SS segment; #PF(fault-code) for a page fault
:::

## 实地址模式异常（原文）

::: note
Interrupt 13 if any part of the operand would lie outside of the effective address space from 0 to 0FFFFH
:::

## 虚拟 8086 模式异常（原文）

::: note
Same exceptions as in Real Address Mode; #PF(fault-code) for a page fault
:::
