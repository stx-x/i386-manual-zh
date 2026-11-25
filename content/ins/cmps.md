---
id: CMPS
title: 比较串操作数
en: Compare String Operands
group: C
---

# CMPS -- 比较串操作数

## 操作码

```
Opcode    Instruction        Clocks   Description

A6        CMPS m8,m8         10       Compare bytes ES:[(E)DI] (second
                                      operand) with   [(E)SI] (first 
                                      operand)
A7        CMPS m16,m16       10       Compare words ES:[(E)DI] (second
                                      operand) with   [(E)SI] (first 
                                      operand)
A7        CMPS m32,m32       10       Compare dwords ES:[(E)DI]
                                      (second operand) with [(E)SI] 
                                      (first operand)
A6        CMPSB              10       Compare bytes ES:[(E)DI] with
                                      DS:[SI]
A7        CMPSW              10       Compare words ES:[(E)DI] with
                                      DS:[SI]
A7        CMPSD              10       Compare dwords ES:[(E)DI] with
                                      DS:[SI]
```

## 操作

```
IF (instruction = CMPSD) OR
   (instruction has operands of type DWORD)
THEN OperandSize := 32;
ELSE OperandSize := 16;
FI;
IF AddressSize = 16
THEN
   use SI for source-index and DI for destination-index
ELSE (* AddressSize = 32 *)
   use ESI for source-index and EDI for destination-index;
FI;
IF byte type of instruction
THEN
   [source-index] - [destination-index]; (* byte comparison *)
   IF DF = 0 THEN IncDec := 1 ELSE IncDec := -1; FI;
ELSE
   IF OperandSize = 16
   THEN
      [source-index] - [destination-index]; (* word comparison *)
      IF DF = 0 THEN IncDec := 2 ELSE IncDec := -2; FI;
   ELSE (* OperandSize = 32 *)
      [source-index] - [destination-index]; (* dword comparison *)
      IF DF = 0 THEN IncDec := 4 ELSE IncDec := -4; FI;
   FI;
FI;
source-index := source-index + IncDec;
destination-index := destination-index + IncDec;
```

## 说明

比较 DS:ESI 与 ES:EDI 处的串元素，更新标志；可配合 REPE/REPNE 重复，并按 DF 递增或递减索引。

## 影响的标志

OF、SF、ZF、AF、PF、CF，按附录 C 所述。

## 保护模式异常

- #GP(0)：CS、DS、ES、FS 或 GS 段中的内存操作数有效地址非法。
- #SS(0)：SS 段中的地址非法。
- #PF(fault-code)：页错误。


## 实地址模式异常

中断 13：操作数的任何部分超出 0–0FFFFH 的有效地址空间。


## 虚拟 8086 模式异常

与实地址模式相同；#PF(fault-code)：页错误。

