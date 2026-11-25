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
