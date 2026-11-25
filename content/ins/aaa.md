---
id: AAA
title: 加法后的 ASCII 调整
en: ASCII Adjust after Addition
group: A
page: 256
---

# AAA -- 加法后的 ASCII 调整

## 操作码

```
Opcode    Instruction    Clocks    Description

37        AAA            4         ASCII adjust AL after addition
```

## 操作

```
IF ((AL AND 0FH) > 9) OR (AF = 1)
THEN
   AL := (AL + 6) AND 0FH;
   AH := AH + 1;
   AF := 1;
   CF := 1;
ELSE
   CF := 0;
   AF := 0;
FI;
```

## 说明

调整 AL 中两个非压缩 BCD 数相加的结果，使 AL 成为有效的非压缩十进制数，高 4 位清零。若需要进位，则置位 CF 并递增 AH。

## 影响的标志

AF、CF 如上述；OF、SF、ZF、PF 未定义。

## 保护模式异常（原文）

::: note
None
:::

## 实地址模式异常（原文）

::: note
None
:::
