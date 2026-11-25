---
id: LGDT
title: 装入全局/中断描述符表寄存器
en: Load Global/Interrupt Descriptor Table Register
group: L
---

# LGDT -- 装入全局/中断描述符表寄存器

## 操作码

```
Opcode       Instruction      Clocks        Description

0F  01 /2    LGDT m16&32      11            Load m into GDTR
0F  01 /3    LIDT m16&32      11            Load m into IDTR
```

## 操作

```
IF instruction = LIDT
THEN
   IF OperandSize = 16
   THEN IDTR.Limit:Base := m16:24 (* 24 bits of base loaded *)
   ELSE IDTR.Limit:Base := m16:32
   FI;
ELSE (* instruction = LGDT *)
   IF OperandSize = 16
   THEN GDTR.Limit:Base := m16:24 (* 24 bits of base loaded *)
   ELSE GDTR.Limit:Base := m16:32;
   FI;
FI;
```

## 说明

从内存操作数装入 GDTR（LGDT）或 IDTR（LIDT）的基地址与界限；特权指令。

## 影响的标志

无。

## 保护模式异常

- #GP(0)：当前特权级不为 0。
- #UD：源操作数为寄存器。
- #GP(0)：CS、DS、ES、FS 或 GS 段中的内存操作数有效地址非法。
- #SS(0)：SS 段中的地址非法。
- #PF(fault-code)：页错误。


## 实地址模式异常

中断 13：操作数的任何部分超出 0–0FFFFH 的有效地址空间；中断 6：源操作数为寄存器。

这些指令在实地址模式中有效，以便上电时为保护模式做初始化。


## 虚拟 8086 模式异常

与实地址模式相同；#PF(fault-code)：页错误。

