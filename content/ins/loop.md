---
id: LOOP
title: 用 CX 计数循环
en: Loop Control with CX Counter
group: L
---

# LOOP -- 用 CX 计数循环

## 操作码

```
Opcode   Instruction  Clocks  Description

E2  cb   LOOP rel8    11+m    DEC count; jump short if count <> 0
E1  cb   LOOPE rel8   11+m    DEC count; jump short if count <> 0 and ZF=1
E1  cb   LOOPZ rel8   11+m    DEC count; jump short if count <> 0 and ZF=1
E0  cb   LOOPNE rel8  11+m    DEC count; jump short if count <> 0 and ZF=0
E0  cb   LOOPNZ rel8  11+m    DEC count; jump short if count <> 0 and ZF=0
```

## 操作

```
IF AddressSize = 16 THEN CountReg is CX ELSE CountReg is ECX; FI;
CountReg := CountReg - 1;
IF instruction <> LOOP
THEN
   IF (instruction = LOOPE) OR (instruction = LOOPZ)
   THEN BranchCond := (ZF = 1) AND (CountReg <> 0);
   FI;
   IF (instruction = LOOPNE) OR (instruction = LOOPNZ)
   THEN BranchCond := (ZF = 0) AND (CountReg <> 0);
   FI;
FI;

IF BranchCond
THEN
   IF OperandSize = 16
   THEN
      IP := IP + SignExtend(rel8);
   ELSE (* OperandSize = 32 *)
      EIP := EIP + SignExtend(rel8);
   FI;
FI;
```

## 说明

递减 ECX/CX，若不为零则跳转到目标；LOOPE/LOOPNE 还测试 ZF。

## 影响的标志

无。

## 保护模式异常（原文）

::: note
#GP(0) if the offset jumped to is beyond the limits of the current code segment
:::

## 实地址模式异常（原文）

::: note
None
:::

## 虚拟 8086 模式异常（原文）

::: note
None
:::
