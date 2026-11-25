---
id: BOUND
title: 检查数组下标是否越界
en: Check Array Index Against Bounds
group: B
page: 264
---

# BOUND -- 检查数组下标是否越界

## 操作码

```
Opcode    Instruction          Clocks    Description

62 /r     BOUND r16,m16&16     10        Check if r16 is within bounds
                                         (passes test)
62 /r     BOUND r32,m32&32     10        Check if r32 is within bounds
                                         (passes test)
```

## 操作

```
IF (LeftSRC < [RightSRC] OR LeftSRC > [RightSRC + OperandSize/8])
   (* Under lower bound or over upper bound *)
THEN Interrupt 5;
FI;
```

## 说明

检查寄存器中的有符号下标是否落在内存中相邻存放的下界与上界之间；越界则产生异常 5。

## 影响的标志

无。

## 保护模式异常（原文）

::: note
Interrupt 5 if the bounds test fails, as described above; #GP(0) for an illegal memory operand effective address in the CS, DS, ES, FS, or GS segments; #SS(0) for an illegal address in the SS segment; #PF(fault-code) for a page fault

The second operand must be a memory operand, not a register. If BOUND is executed with a ModRM byte representing a register as the second operand, #UD occurs.
:::

## 实地址模式异常（原文）

::: note
Interrupt 5 if the bounds test fails; Interrupt 13 if any part of the operand would lie outside of the effective address space from 0 to 0FFFFH; Interrupt 6 if the second operand is a register
:::

## 虚拟 8086 模式异常（原文）

::: note
Same exceptions as in Real Address Mode; #PF(fault-code) for a page fault
:::
