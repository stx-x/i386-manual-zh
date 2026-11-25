---
id: MOVCR
title: 与特殊寄存器之间传送
en: Move to/from Special Registers
group: M
---

# MOVCR -- 与特殊寄存器之间传送

## 操作码

```
Opcode      Instruction           Clocks   Description

0F  20 /r   MOV r32,CR0/CR2/CR3   6        Move (control register) to
                                           (register)
0F  22 /r   MOV CR0/CR2/CR3,r32   10/4/5   Move (register) to (control
                                           register)
0F  21 /r   MOV r32,DR0 -- 3      22       Move (debug register) to
                                           (register)
0F  21 /r   MOV r32,DR6/DR7       14       Move (debug register) to
                                           (register)
0F  23 /r   MOV DR0 -- 3,r32      22       Move (register) to (debug
                                           register)
0F  23 /r   MOV DR6/DR7,r32       16       Move (register) to (debug
                                           register)
0F  24 /r   MOV r32,TR6/TR7       12       Move (test register) to
                                           (register)
0F  26 /r   MOV TR6/TR7,r32       12       Move (register) to (test
                                           register)
```

## 操作

```
DEST := SRC;
```

## 说明

在通用寄存器与 CRn、DRn 或 TRn 之间传送数据；特权指令，只能在 CPL=0 执行。

## 影响的标志

OF、SF、ZF、AF、PF、CF 均未定义。

## 保护模式异常（原文）

::: note
#GP(0) if the current privilege level is not 0
:::

## 实地址模式异常（原文）

::: note
None
:::

## 虚拟 8086 模式异常（原文）

::: note
#GP(0) if instruction execution is attempted
:::
