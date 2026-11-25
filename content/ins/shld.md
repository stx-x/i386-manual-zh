---
id: SHLD
title: 双精度左移
en: Double Precision Shift Left
group: S
page: 392
---

# SHLD -- 双精度左移

## 操作码

```
Opcode   Instruction          Clocks   Description

0F  A4   SHLD r/m16,r16,imm8  3/7      r/m16 gets SHL of r/m16 concatenated
                                       with r16
0F  A4   SHLD r/m32,r32,imm8  3/7      r/m32 gets SHL of r/m32 concatenated
                                       with r32
0F  A5   SHLD r/m16,r16,CL    3/7      r/m16 gets SHL of r/m16 concatenated
                                       with r16
0F  A5   SHLD r/m32,r32,CL    3/7      r/m32 gets SHL of r/m32 concatenated
                                       with r32
```

## 操作

```
(* count is an unsigned integer corresponding to the last operand of the
instruction, either an immediate byte or the byte in register CL *)
ShiftAmt := count MOD 32;
inBits := register; (* Allow overlapped operands *)
IF ShiftAmt = 0
THEN no operation
ELSE
   IF ShiftAmt >= OperandSize
   THEN (* Bad parameters *)
      r/m := UNDEFINED;
      CF, OF, SF, ZF, AF, PF := UNDEFINED;
   ELSE (* Perform the shift *)
      CF := BIT[Base, OperandSize - ShiftAmt];
         (* Last bit shifted out on exit *)
   FOR i := OperandSize - 1 DOWNTO ShiftAmt
   DO
      BIT[Base, i] := BIT[Base, i - ShiftAmt];
   OF;
   FOR i := ShiftAmt - 1 DOWNTO 0
   DO
      BIT[Base, i] := BIT[inBits, i - ShiftAmt + OperandSize];
   OD;
   Set SF, ZF, PF (r/m);
      (* SF, ZF, PF are set according to the value of the result *)
   AF := UNDEFINED;
   FI;
FI;
```

## 说明

把目的操作数左移，同时把源寄存器的高位从右侧移入；结果写回目的操作数。

## 影响的标志

OF、SF、ZF、PF、CF 如上述；AF 与 OF 未定义。

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
