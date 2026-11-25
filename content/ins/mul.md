---
id: MUL
title: 无符号乘法
en: Unsigned Multiplication of AL or AX
group: M
page: 352
---

# MUL -- 无符号乘法

## 操作码

```
Opcode  Instruction     Clocks       Description

F6  /4  MUL AL,r/m8     9-14/12-17   Unsigned multiply (AX := AL * r/m byte)
F7  /4  MUL AX,r/m16    9-22/12-25   Unsigned multiply (DX:AX := AX * r/m
                                     word)
F7  /4  MUL EAX,r/m32   9-38/12-41   Unsigned multiply (EDX:EAX := EAX * r/m
                                     dword)
```

## 操作

```
IF byte-size operation
THEN AX := AL * r/m8
ELSE (* word or doubleword operation *)
   IF OperandSize = 16
   THEN DX:AX := AX * r/m16
   ELSE (* OperandSize = 32 *)
      EDX:EAX := EAX * r/m32
   FI;
FI;
```

## 说明

用源操作数乘累加器（AL、AX 或 EAX），双倍长度结果写入 AX、DX:AX 或 EDX:EAX；高半部分非零时置位 CF、OF。

## 影响的标志

OF、CF 如上述；SF、ZF、AF、PF、CF 未定义。

## 保护模式异常

- #GP(0)：CS、DS、ES、FS 或 GS 段中的内存操作数有效地址非法。
- #SS(0)：SS 段中的地址非法。
- #PF(fault-code)：页错误。


## 实地址模式异常

中断 13：操作数的任何部分超出 0–0FFFFH 的有效地址空间。


## 虚拟 8086 模式异常

与实地址模式相同；#PF(fault-code)：页错误。

