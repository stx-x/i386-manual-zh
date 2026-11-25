---
id: LODS
title: 装入串操作数
en: Load String Operand
group: L
---

# LODS -- 装入串操作数

## 操作码

```
Opcode  Instruction   Clocks   Description

AC      LODS m8       5        Load byte [(E)SI] into AL
AD      LODS m16      5        Load word [(E)SI] into AX
AD      LODS m32      5        Load dword [(E)SI] into EAX
AC      LODSB         5        Load byte DS:[(E)SI] into AL
AD      LODSW         5        Load word DS:[(E)SI] into AX
AD      LODSD         5        Load dword DS:[(E)SI] into EAX
```

## 操作

```
IF AddressSize = 16
THEN use SI for source-index
ELSE (* AddressSize = 32 *)
   use ESI for source-index;
FI;
IF byte type of instruction
THEN
   AL := [source-index]; (* byte load *)
   IF DF = 0 THEN IncDec := 1 ELSE IncDec := -1; FI;
ELSE
   IF OperandSize = 16
   THEN
      AX := [source-index]; (* word load *)
      IF DF = 0 THEN IncDec := 2 ELSE IncDec := -2; FI;
   ELSE (* OperandSize = 32 *)
      EAX := [source-index]; (* dword load *)
      IF DF = 0 THEN IncDec := 4 ELSE IncDec := -4; FI;
   FI;
FI;
source-index := source-index + IncDec
```

## 说明

把 DS:ESI 处的串元素装入 AL、AX 或 EAX，并按 DF 调整 ESI。

## 影响的标志

无。

## 保护模式异常（原文）

::: note
#GP(0) for an illegal memory operand effective address in the CS, DS, ES, FS, or GS segments; #SS(0) for an illegal address in the SS segment; #PF(fault-code) for a page fault
:::

## 实地址模式异常（原文）

::: note
Interrupt 13 if any part of the operand would lie outside of the effective address space from 0 to 0FFFFH
:::

## 虚拟 8086 模式异常（原文）

::: note
Same exceptions as in Real Address Mode; #PF(fault-code) for a page fault
:::
