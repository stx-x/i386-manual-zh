---
id: STI
title: 置中断允许标志
en: Set Interrupt Flag
group: S
page: 400
---

# STI -- 置中断允许标志

## 操作码

```
Opcode  Instruction   Clocks   Description

F13     STI           3        Set interrupt flag; interrupts enabled at the
                               end of the next instruction
```

## 操作

```
IF := 1
```

## 说明

置位 IF，允许可屏蔽外部中断；只有 CPL ≤ IOPL 时才能执行。

## 影响的标志

IF := 1。

## 保护模式异常（原文）

::: note
#GP(0) if the current privilege level is greater (has less privilege) than the I/O privilege level
:::

## 实地址模式异常（原文）

::: note
None
:::

## 虚拟 8086 模式异常（原文）

::: note
None
:::
