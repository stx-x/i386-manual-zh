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

## 保护模式异常

#GP(0)：当前特权级不为 0 时执行 CLTS。


## 实地址模式异常

无（在实地址模式中有效，以便为保护模式做初始化）。


## 虚拟 8086 模式异常

与实地址模式相同。

