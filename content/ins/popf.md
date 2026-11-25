---
id: POPF
title: 从栈弹出标志
en: Pop Stack into FLAGS or EFLAGS Register
group: P
---

# POPF -- 从栈弹出标志

## 操作码

```
Opcode   Instruction   Clocks   Description

9D       POPF          5        Pop top of stack FLAGS
9D       POPFD         5        Pop top of stack into EFLAGS
```

## 说明

把栈顶字或双字装入 FLAGS/EFLAGS 的相应位；POPFD 为 32 位形式。

## 影响的标志

除 VM 和 RF 之外的所有标志。

## 保护模式异常（原文）

::: note
#SS(0) if the top of stack is not within the stack segment
:::

## 实地址模式异常（原文）

::: note
Interrupt 13 if any part of the operand would lie outside of the effective address space from 0 to 0FFFFH
:::

## 虚拟 8086 模式异常（原文）

::: note
#GP(0) fault if IOPL is less than 3, to permit emulation
:::
