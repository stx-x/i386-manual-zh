---
id: LEA
title: 装入有效地址
en: Load Effective Address
group: L
page: 327
---

# LEA -- 装入有效地址

## 操作码

```
Opcode  Instruction  Clocks  Description

8D  /r  LEA r16,m    2       Store effective address for m in register r16
8D  /r  LEA r32,m    2       Store effective address for m in register r32
8D  /r  LEA r16,m    2       Store effective address for m in register r16
8D  /r  LEA r32,m    2       Store effective address for m in register r32
```

## 操作

```
IF OperandSize = 16 AND AddressSize = 16
THEN r16 := Addr(m);
ELSE
   IF OperandSize = 16 AND AddressSize = 32
   THEN
      r16 := Truncate_to_16bits(Addr(m));   (* 32-bit address *)
   ELSE
      IF OperandSize = 32 AND AddressSize = 16
      THEN
         r32 := Truncate_to_16bits(Addr(m));
      ELSE
         IF OperandSize = 32 AND AddressSize = 32
         THEN  r32 := Addr(m);
         FI;
      FI;
   FI;
FI;
```

## 说明

把源内存操作数的有效地址（偏移）而不是其内容装入目的通用寄存器。

## 影响的标志

无。

## 保护模式异常

#UD：第二操作数为寄存器。


## 实地址模式异常

中断 6：第二操作数为寄存器。


## 虚拟 8086 模式异常

与实地址模式相同。

