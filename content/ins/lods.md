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

## 保护模式异常

- #GP(0)：CS、DS、ES、FS 或 GS 段中的内存操作数有效地址非法。
- #SS(0)：SS 段中的地址非法。
- #PF(fault-code)：页错误。


## 实地址模式异常

中断 13：操作数的任何部分超出 0–0FFFFH 的有效地址空间。


## 虚拟 8086 模式异常

与实地址模式相同；#PF(fault-code)：页错误。

