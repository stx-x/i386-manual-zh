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

## 保护模式异常

#GP(0)：当前特权级高于（即特权低于）标志寄存器中的 IOPL。IOPL 规定可以执行 I/O 的最低特权级。


## 实地址模式异常

无。


## 虚拟 8086 模式异常

#GP(0)：与保护模式相同。

