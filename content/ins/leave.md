---
id: LEAVE
title: 高级过程退出
en: High Level Procedure Exit
group: L
page: 329
---

# LEAVE -- 高级过程退出

## 操作码

```
Opcode  Instruction  Clocks  Description

C9      LEAVE        4       Set SP to BP, then pop BP
C9      LEAVE        4       Set ESP to EBP, then pop EBP
```

## 操作

```
IF StackAddrSize = 16
THEN
   SP := BP;
ELSE (* StackAddrSize = 32 *)
   ESP := EBP;
FI;
IF OperandSize = 16
THEN
   BP := Pop();
ELSE (* OperandSize = 32 *)
   EBP := Pop();
FI;
```

## 说明

把 EBP 复制到 ESP，释放当前栈帧，然后弹出保存的 EBP；与 ENTER 配对。

## 影响的标志

无。

## 保护模式异常（原文）

::: note
#SS(0) if BP does not point to a location within the limits of the current stack segment
:::

## 实地址模式异常（原文）

::: note
Interrupt 13 if any part of the operand would lie outside of the effective address space from 0 to 0FFFFH
:::

## 虚拟 8086 模式异常（原文）

::: note
Same exceptions as in Real Address Mode
:::
