---
id: OUTS
title: 向端口输出串
en: Output String to Port
group: O
---

# OUTS -- 向端口输出串

## 操作码

```
Opcode   Instruction     Clocks          Description

6E       OUTS DX,r/m8    14,pm=8*/28**   Output byte [(E)SI] to port in DX
6F       OUTS DX,r/m16   14,pm=8*/28**   Output word [(E)SI] to port in DX
6F       OUTS DX,r/m32   14,pm=8*/28**   Output dword [(E)SI] to port in DX
6E       OUTSB           14,pm=8*/28**   Output byte DS:[(E)SI] to port in
                                         DX
6F       OUTSW           14,pm=8*/28**   Output word DS:[(E)SI] to port in
                                         DX
6F       OUTSD           14,pm=8*/28**   Output dword DS:[(E)SI] to port in
                                         DX
```

## 操作

```
IF AddressSize = 16
THEN use SI for source-index;
ELSE (* AddressSize = 32 *)
   use ESI for source-index;
FI;

IF (PE = 1) AND ((VM = 1) OR (CPL > IOPL))
THEN (* Virtual 8086 mode, or protected mode with CPL > IOPL *)
   IF NOT I-O-Permission (DEST, width(DEST))
   THEN #GP(0);
   FI;
FI;
IF byte type of instruction
THEN
   [DX] := [source-index]; (* Write byte at DX I/O address *)
   IF DF = 0 THEN IncDec := 1 ELSE IncDec := -1; FI;
FI;
IF OperandSize = 16
THEN
   [DX] := [source-index]; (* Write word at DX I/O address *)
   IF DF = 0 THEN IncDec := 2 ELSE IncDec := -2; FI;
FI;
IF OperandSize = 32
THEN
   [DX] := [source-index]; (* Write dword at DX I/O address *)
   IF DF = 0 THEN IncDec := 4 ELSE IncDec := -4; FI;
   FI;
FI;
source-index := source-index + IncDec;
```

## 说明

把 DS:ESI 处的串元素写到 DX 指定的 I/O 端口；可配合 REP 重复。

## 影响的标志

无。

## 保护模式异常（原文）

::: note
#GP(0) if CPL is greater than IOPL and any of the corresponding I/O permission bits in TSS equals 1; #GP(0) for an illegal memory operand effective address in the CS, DS, or ES segments; #SS(0) for an illegal address in the SS segment; #PF(fault-code) for a page fault
:::

## 实地址模式异常（原文）

::: note
Interrupt 13 if any part of the operand would lie outside of the effective address space from 0 to 0FFFFH
:::

## 虚拟 8086 模式异常（原文）

::: note
#GP(0) fault if any of the corresponding I/O permission bits in TSS equals 1; #PF(fault-code) for a page fault
:::
