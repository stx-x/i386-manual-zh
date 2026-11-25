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

## 保护模式异常

- #GP(0)：CPL 在数值上大于 IOPL，且 TSS 中相应的 I/O 许可位为 1。
- #GP(0)：目的位于不可写段。
- #GP(0)：CS、DS、ES、FS 或 GS 段中的内存操作数有效地址非法。
- #SS(0)：SS 段中的地址非法。
- #PF(fault-code)：页错误。


## 实地址模式异常

中断 13：操作数的任何部分超出 0–0FFFFH 的有效地址空间。


## 虚拟 8086 模式异常

#GP(0)：TSS 中相应的 I/O 许可位为 1；#PF(fault-code)：页错误。

