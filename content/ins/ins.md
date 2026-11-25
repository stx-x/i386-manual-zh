---
id: INS
title: 从端口输入串
en: Input from Port to String
group: I
---

# INS -- 从端口输入串

## 操作码

```
Opcode  Instruction    Clocks         Description

6C      INS r/m8,DX    15,pm=9*/29**  Input byte from port DX into ES:(E)DI
6D      INS r/m16,DX   15,pm=9*/29**  Input word from port DX into ES:(E)DI
6D      INS r/m32,DX   15,pm=9*/29**  Input dword from port DX into ES:(E)DI
6C      INSB           15,pm=9*/29**  Input byte from port DX into ES:(E)DI
6D      INSW           15,pm=9*/29**  Input word from port DX into ES:(E)DI
6D      INSD           15,pm=9*/29**  Input dword from port DX into ES:(E)DI
```

## 操作

```
IF AddressSize = 16
THEN use DI for dest-index;
ELSE (* AddressSize = 32 *)
   use EDI for dest-index;
FI;
IF (PE = 1) AND ((VM = 1) OR (CPL > IOPL))
THEN (* Virtual 8086 mode, or protected mode with CPL > IOPL *)
   IF NOT I-O-Permission (SRC, width(SRC))
   THEN #GP(0);
   FI;
FI;
IF byte type of instruction
THEN
   ES:[dest-index] := [DX]; (* Reads byte at DX from I/O address space *)
   IF DF = 0 THEN IncDec := 1 ELSE IncDec := -1; FI;
FI;
IF OperandSize = 16
THEN
   ES:[dest-index] := [DX]; (* Reads word at DX from I/O address space *)
   IF DF = 0 THEN IncDec := 2 ELSE IncDec := -2; FI;
FI;
IF OperandSize = 32
THEN
   ES:[dest-index] := [DX]; (* Reads dword at DX from I/O address space *)
   IF DF = 0 THEN IncDec := 4 ELSE IncDec := -4; FI;
FI;
dest-index := dest-index + IncDec;
```

## 说明

从 DX 指定的 I/O 端口读取字节、字或双字，写入 ES:EDI 指向的内存；可配合 REP 重复。

## 影响的标志

无。

## 保护模式异常（原文）

::: note
#GP(0) if CPL is numerically greater than IOPL and any of the corresponding I/O permission bits in TSS equals 1; #GP(0) if the destination is in a nonwritable segment; #GP(0) for an illegal memory operand effective address in the CS, DS, ES, FS, or GS segments; #SS(0) for an illegal address in the SS segment; #PF(fault-code) for a page fault
:::

## 实地址模式异常（原文）

::: note
Interrupt 13 if any part of the operand would lie outside of the effective address space from 0 to 0FFFFH
:::

## 虚拟 8086 模式异常（原文）

::: note
#GP(0) fault if any of the corresponding I/O permission bits in TSS equals 1; #PF(fault-code) for a page fault
:::
