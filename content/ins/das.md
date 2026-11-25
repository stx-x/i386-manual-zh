---
id: DAS
title: 减法后的十进制调整
en: Decimal Adjust AL after Subtraction
group: D
page: 292
---

# DAS -- 减法后的十进制调整

## 操作码

```
Opcode    Instruction        Clocks   Description

2F        DAS                4        Decimal adjust AL after subtraction
```

## 操作

```
IF (AL AND 0FH) > 9 OR AF = 1
THEN
   AL := AL - 6;
   AF := 1;
ELSE
   AF := 0;
FI;
IF (AL > 9FH) OR (CF = 1)
THEN
   AL := AL - 60H;
   CF := 1;
ELSE CF := 0;
FI;
```

## 说明

调整 AL 中两个压缩 BCD 数相减的结果，使其成为有效的压缩十进制字节；必要时置位 CF。

## 影响的标志

AF、CF 如上述；SF、ZF、PF 按附录 C 所述。

## 保护模式异常

无。


## 实地址模式异常

无。


## 虚拟 8086 模式异常

无。

