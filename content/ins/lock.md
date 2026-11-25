---
id: LOCK
title: 断言 LOCK# 信号前缀
en: Assert LOCK# Signal Prefix
group: L
page: 336
---

# LOCK -- 断言 LOCK# 信号前缀

## 操作码

```
Opcode  Instruction  Clocks  Description

F0      LOCK         0       Assert LOCK# signal for the next instruction
```

## 说明

使随后的读-改-写指令原子地访问内存；只能用于规定的指令，否则产生非法操作码异常。

## 影响的标志

无。

## 保护模式异常

#UD：LOCK 用于上文“说明”节未列出的指令；其后的（被锁定）指令仍可能产生其他异常。


## 实地址模式异常

中断 6：LOCK 用于上文“说明”节未列出的指令；其后的（被锁定）指令仍可能产生异常。


## 虚拟 8086 模式异常

#UD：LOCK 用于上文“说明”节未列出的指令；其后的（被锁定）指令仍可能产生异常。

