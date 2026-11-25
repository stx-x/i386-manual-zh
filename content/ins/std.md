---
id: STD
title: 置方向标志
en: Set Direction Flag
group: S
page: 399
---

# STD -- 置方向标志

## 操作码

```
Opcode  Instruction   Clocks    Description

FD      STD           2         Set direction flag so (E)SI and/or (E)DI
                                decrement
```

## 操作

```
DF := 1;
```

## 说明

置位 DF，使串指令按地址递减方向处理。

## 影响的标志

DF := 1。

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
