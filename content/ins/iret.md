---
id: IRET
title: 中断返回
en: Interrupt Return
group: I
---

# IRET -- 中断返回

## 操作码

```
Opcode  Instruction  Clocks       Description

CF      IRET         22,pm=38     Interrupt return (far return and pop
                                  flags)
CF      IRET         pm=82        Interrupt return to lesser privilege
CF      IRET         ts           Interrupt return, different task (NT = 1)
CF      IRETD        22,pm=38     Interrupt return (far return and pop
                                  flags)
CF      IRETD        pm=82        Interrupt return to lesser privilege
CF      IRETD        pm=60        Interrupt return to V86 mode
CF      IRETD        ts           Interrupt return, different task (NT = 1)
```

## 说明

从栈恢复 EIP、CS 和 EFLAGS 并返回被中断过程；32 位形式 IRETD 还恢复 32 位操作数。

## 影响的标志

全部；标志寄存器从栈中弹出。

## 保护模式异常

#GP、#NP 或 #SS：条件见上文。


## 实地址模式异常

中断 13：被弹出的操作数有任何部分超出地址 0FFFFH。


## 虚拟 8086 模式异常

#GP(0)：IOPL 小于 3，以便进行模拟。

