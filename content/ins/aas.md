---
id: AAS
title: 减法后的 ASCII 调整
en: ASCII Adjust AL after Subtraction
group: A
page: 259
---

# AAS -- 减法后的 ASCII 调整

## 操作码

```
Opcode    Instruction    Clocks    Description

3F        AAS            4         ASCII adjust AL after subtraction
```

## 操作

```
IF (AL AND 0FH) > 9 OR AF = 1
THEN
   AL := AL - 6;
   AL := AL AND 0FH;
   AH := AH - 1;
   AF := 1;
   CF := 1;
ELSE
   CF := 0;
   AF := 0;
FI;
```

## 说明

调整 AL 中两个非压缩 BCD 数相减的结果，使 AL 成为有效的非压缩十进制数，高 4 位清零。若需要借位，则置位 CF 并递减 AH。

## 影响的标志

AF、CF 如上述；OF、SF、ZF、PF 未定义。

## 保护模式异常

无。


## 实地址模式异常

无。


## 虚拟 8086 模式异常

无。

