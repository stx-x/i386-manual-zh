---
id: MOVS
title: 串传送
en: Move Data from String to String
group: M
---

# MOVS -- 串传送

## 操作码

```
Opcode  Instruction      Clocks   Description

A4      MOVS m8,m8       7        Move byte [(E)SI] to ES:[(E)DI]
A5      MOVS m16,m16     7        Move word [(E)SI] to ES:[(E)DI]
A5      MOVS m32,m32     7        Move dword [(E)SI] to ES:[(E)DI]
A4      MOVSB            7        Move byte DS:[(E)SI] to ES:[(E)DI]
A5      MOVSW            7        Move word DS:[(E)SI] to ES:[(E)DI]
A5      MOVSD            7        Move dword DS:[(E)SI] to ES:[(E)DI]
```

## 操作

```
IF (instruction = MOVSD) OR (instruction has doubleword operands)
THEN OperandSize := 32;
ELSE OperandSize := 16;
IF AddressSize = 16
THEN use SI for source-index and DI for destination-index;
ELSE (* AddressSize = 32 *)
   use ESI for source-index and EDI for destination-index;
FI;
IF byte type of instruction
THEN
   [destination-index] := [source-index]; (* byte assignment *)
   IF DF = 0 THEN IncDec := 1 ELSE IncDec := -1; FI;
ELSE
   IF OperandSize = 16
   THEN
      [destination-index] := [source-index]; (* word assignment *)
      IF DF = 0 THEN IncDec := 2 ELSE IncDec := -2; FI;
   ELSE (* OperandSize = 32 *)
      [destination-index] := [source-index]; (* doubleword assignment *)
      IF DF = 0 THEN IncDec := 4 ELSE IncDec := -4; FI;
   FI;
FI;
source-index := source-index + IncDec;
destination-index := destination-index + IncDec;
```

## 说明

把 DS:ESI 处的串元素传送到 ES:EDI，并按 DF 调整两个索引；可配合 REP 做块传送。

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
