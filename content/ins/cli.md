---
id: CLI
title: 清中断允许标志
en: Clear Interrupt Flag
group: C
page: 284
---

# CLI -- 清中断允许标志

## 操作码

```
Opcode    Instruction    Clocks   Description

FA        CLI            3        Clear interrupt flag; interrupts disabled
```

## 操作

```
IF := 0;
```

## 说明

清零 IF，禁止可屏蔽外部中断；只有 CPL ≤ IOPL 时才能执行。

## 影响的标志

IF := 0。

## 保护模式异常（原文）

::: note
#GP(0) if the current privilege level is greater (has less privilege) than the IOPL in the flags register. IOPL specifies the least privileged level at which I/O can be performed.
:::

## 实地址模式异常（原文）

::: note
None
:::

## 虚拟 8086 模式异常（原文）

::: note
#GP(0) as for Protected Mode
:::
