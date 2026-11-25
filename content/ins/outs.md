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

## 保护模式异常

- #GP(0)：CPL 大于 IOPL，且 TSS 中相应的 I/O 许可位为 1。
- #GP(0)：CS、DS 或 ES 段中的内存操作数有效地址非法。
- #SS(0)：SS 段中的地址非法。
- #PF(fault-code)：页错误。


## 实地址模式异常

中断 13：操作数的任何部分超出 0–0FFFFH 的有效地址空间。


## 虚拟 8086 模式异常

#GP(0)：TSS 中相应的 I/O 许可位为 1；#PF(fault-code)：页错误。

