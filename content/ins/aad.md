---
id: AAD
title: 除法前的 ASCII 调整
en: ASCII Adjust AX before Division
group: A
page: 257
---

# AAD -- 除法前的 ASCII 调整

## 操作码

```
Opcode    Instruction    Clocks    Description

D5 0A     AAD            19        ASCII adjust AX before division
```

## 操作

```
AL := AH * 10 + AL;
AH := 0;
```

## 说明

在除法之前调整 AH:AL 中的非压缩 BCD 被除数：AL := AL + 10×AH，AH := 0。随后可用 DIV 得到有效的非压缩十进制商。

## 影响的标志

SF、ZF、PF 按附录 C 所述；OF、AF、CF 未定义。

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
