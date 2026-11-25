---
id: SMSW
title: 保存机器状态字
en: Store Machine Status Word
group: S
page: 397
---

# SMSW -- 保存机器状态字

## 操作码

```
Opcode      Instruction     Clocks          Description

0F  01 /4   SMSW r/m16      2/3,pm=2/2      Store machine status word to EA
                                            word
```

## 操作

```
r/m16 := MSW;
```

## 说明

把 CR0 的低 16 位（MSW）存入目的操作数。

## 影响的标志

无。

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
