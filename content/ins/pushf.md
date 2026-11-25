---
id: PUSHF
title: 把标志寄存器压栈
en: Push Flags Register onto the Stack
group: P
---

# PUSHF -- 把标志寄存器压栈

## 操作码

```
Opcode  Instruction  Clocks   Description

9C      PUSHF        4        Push FLAGS
9C      PUSHFD       4        Push EFLAGS
```

## 操作

```
IF OperandSize = 32
THEN push(EFLAGS);
ELSE push(FLAGS);
FI;
```

## 说明

递减 ESP/SP，并把 FLAGS/EFLAGS 写入栈顶；PUSHFD 为 32 位形式。

## 影响的标志

无。

## 保护模式异常（原文）

::: note
#SS(0) if the new value of eSP is outside the stack segment boundaries
:::

## 实地址模式异常（原文）

::: note
None; the 80386 shuts down due to a lack of stack space
:::

## 虚拟 8086 模式异常（原文）

::: note
#GP(0) fault if IOPL is less than 3, to permit emulation
:::
