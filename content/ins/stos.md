---
id: STOS
title: 存储串数据
en: Store String Data
group: S
---

# STOS -- 存储串数据

## 操作码

```
Opcode  Instruction  Clocks   Description

AA      STOS m8      4        Store AL in byte ES:[(E)DI], update (E)DI
AB      STOS m16     4        Store AX in word ES:[(E)DI], update (E)DI
AB      STOS m32     4        Store EAX in dword ES:[(E)DI], update (E)DI
AA      STOSB        4        Store AL in byte ES:[(E)DI], update (E)DI
AB      STOSW        4        Store AX in word ES:[(E)DI], update (E)DI
AB      STOSD        4        Store EAX in dword ES:[(E)DI], update (E)DI
```

## 操作

```
IF AddressSize = 16
THEN use ES:DI for DestReg
ELSE (* AddressSize = 32 *) use ES:EDI for DestReg;
FI;
IF byte type of instruction
THEN
   (ES:DestReg) := AL;
   IF DF = 0
   THEN DestReg := DestReg + 1;
   ELSE DestReg := DestReg - 1;
   FI;
ELSE IF OperandSize = 16
   THEN
      (ES:DestReg) := AX;
      IF DF = 0
      THEN DestReg := DestReg + 2;
      ELSE DestReg := DestReg - 2;
      FI;
   ELSE (* OperandSize = 32 *)
      (ES:DestReg) := EAX;
      IF DF = 0
      THEN DestReg := DestReg + 4;
      ELSE DestReg := DestReg - 4;
      FI;
   FI;
FI;
```

## 说明

把 AL、AX 或 EAX 写入 ES:EDI 处的内存，并按 DF 调整 EDI；可配合 REP 填充。

## 影响的标志

无。

## 保护模式异常

- #GP(0)：结果位于不可写段。
- #GP(0)：CS、DS、ES、FS 或 GS 段中的内存操作数有效地址非法。
- #SS(0)：SS 段中的地址非法。
- #PF(fault-code)：页错误。


## 实地址模式异常

中断 13：操作数的任何部分超出 0–0FFFFH 的有效地址空间。


## 虚拟 8086 模式异常

与实地址模式相同；#PF(fault-code)：页错误。

