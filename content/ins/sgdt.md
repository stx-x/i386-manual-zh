---
id: SGDT
title: 保存全局/中断描述符表寄存器
en: Store Global/Interrupt Descriptor Table Register
group: S
---

# SGDT -- 保存全局/中断描述符表寄存器

## 操作码

```
Opcode       Instruction   Clocks   Description

0F  01 /0    SGDT m        9        Store GDTR to m
0F  01 /1    SIDT m        9        Store IDTR to m
```

## 操作

```
DEST := 48-bit BASE/LIMIT register contents;
```

## 说明

把 GDTR（SGDT）或 IDTR（SIDT）的基地址与界限存入内存。

## 影响的标志

无。

## 保护模式异常

- 中断 6：目的操作数为寄存器。
- #GP(0)：目的位于不可写段。
- #GP(0)：CS、DS、ES、FS 或 GS 段中的内存操作数有效地址非法。
- #SS(0)：SS 段中的地址非法。
- #PF(fault-code)：页错误。


## 实地址模式异常

中断 6：目的操作数为寄存器；中断 13：操作数的任何部分超出 0–0FFFFH 的有效地址空间。


## 虚拟 8086 模式异常

与实地址模式相同；#PF(fault-code)：页错误。

