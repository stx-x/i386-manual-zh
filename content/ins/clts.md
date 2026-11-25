---
id: CLTS
title: 清除 CR0 中的任务已切换标志
en: Clear Task-Switched Flag in CR0
group: C
page: 285
---

# CLTS -- 清除 CR0 中的任务已切换标志

## 操作码

```
Opcode    Instruction    Clocks   Description

OF  06    CLTS           5        Clear task-switched flag
```

## 操作

```
TS Flag in CR0 := 0;
```

## 说明

清零 CR0 的 TS 位，供任务切换后处理协处理器上下文；特权指令。

## 影响的标志

TS := 0（TS 在 CR0 中，不在标志寄存器中）。

## 保护模式异常（原文）

::: note
#GP(0) if CLTS is executed with a current privilege level other than 0
:::

## 实地址模式异常（原文）

::: note
None (valid in Real Address Mode to allow initialization for Protected Mode)
:::

## 虚拟 8086 模式异常（原文）

::: note
Same exceptions as in Real Address Mode
:::
