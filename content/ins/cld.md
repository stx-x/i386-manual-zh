---
id: CLD
title: 清方向标志
en: Clear Direction Flag
group: C
page: 283
---

# CLD -- 清方向标志

## 操作码

```
Opcode    Instruction     Clocks   Description

FC        CLD             2        Clear direction flag; SI and DI
                                   will increment during string
                                   instructions
```

## 操作

```
DF := 0;
```

## 说明

清零 DF，使串指令按地址递增方向处理。

## 影响的标志

DF := 0。

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
