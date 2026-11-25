---
id: BTR
title: 位测试并复位
en: Bit Test and Reset
group: B
page: 271
---

# BTR -- 位测试并复位

## 操作码

```
Opcode        Instruction     Clocks  Description

0F  B3        BTR r/m16,r16   6/13    Save bit in carry flag and reset
0F  B3        BTR r/m32,r32   6/13    Save bit in carry flag and reset
0F  BA /6 ib  BTR r/m16,imm8  6/8     Save bit in carry flag and reset
0F  BA /6 ib  BTR r/m32,imm8  6/8     Save bit in carry flag and reset
```

## 操作

```
CF := BIT[LeftSRC, RightSRC];
BIT[LeftSRC, RightSRC] := 0;
```

## 说明

把指定位复制到 CF，然后清零该位。

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
