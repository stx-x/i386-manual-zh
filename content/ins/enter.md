---
id: ENTER
title: 为过程参数建立栈帧
en: Make Stack Frame for Procedure Parameters
group: E
page: 295
---

# ENTER -- 为过程参数建立栈帧

## 操作码

```
Opcode      Instruction        Clocks     Description

C8 iw 00    ENTER imm16,0      10         Make procedure stack frame
C8 iw 01    ENTER imm16,1      12         Make stack frame for procedure
                                          parameters
C8 iw ib    ENTER imm16,imm8   15+4(n-1)  Make stack frame for
                                          procedure parameters
```

## 操作

```
level := level MOD 32
IF OperandSize = 16 THEN Push(BP) ELSE Push (EBP) FI;
   (* Save stack pointer *)
frame-ptr := eSP
IF level > 0
THEN (* level is rightmost parameter *)
   FOR i := 1 TO level - 1
   DO
      IF OperandSize = 16
      THEN
         BP := BP - 2;
         Push[BP]
      ELSE (* OperandSize = 32 *)
         EBP := EBP - 4;
         Push[EBP];
      FI;
   OD;
   Push(frame-ptr)
FI;
IF OperandSize = 16 THEN BP := frame-ptr ELSE EBP := frame-ptr; FI;
IF StackAddrSize = 16
THEN SP := SP - First operand;
ELSE ESP := ESP - ZeroExtend(First operand);
FI;
```

## 说明

按词法嵌套层级建立栈帧，保存 EBP 与外层栈帧指针，并分配指定字节数的局部空间。

## 影响的标志

无。

## 保护模式异常（原文）

::: note
#SS(0) if SP or ESP would exceed the stack limit at any point during instruction execution; #PF(fault-code) for a page fault
:::

## 实地址模式异常（原文）

::: note
None
:::

## 虚拟 8086 模式异常（原文）

::: note
None
:::
