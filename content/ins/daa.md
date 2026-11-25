---
id: DAA
title: 加法后的十进制调整
en: Decimal Adjust AL after Addition
group: D
page: 291
---

# DAA -- 加法后的十进制调整

## 操作码

```
Opcode    Instruction        Clocks   Description

27        DAA                4        Decimal adjust AL after addition
```

## 操作

```
IF ((AL AND 0FH) > 9) OR (AF = 1)
THEN
   AL := AL + 6;
   AF := 1;
ELSE
   AF := 0;
FI;
IF (AL > 9FH) OR (CF = 1)
THEN
   AL := AL + 60H;
   CF := 1;
ELSE CF := 0;
FI;
```

## 说明

调整 AL 中两个压缩 BCD 数相加的结果，使其成为有效的压缩十进制字节；必要时置位 CF。

## 影响的标志

AF、CF 如上述；SF、ZF、PF、CF 按附录 C 所述。

## 保护模式异常（原文）

::: note
None
:::

## 实地址模式异常（原文）

::: note
None
:::

## 虚拟 8086 模式异常（原文）

::: note
None
:::
