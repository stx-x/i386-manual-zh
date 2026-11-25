---
id: WAIT
title: 等待 BUSY# 引脚无效
en: Wait until BUSY# Pin is Inactive (HIGH)
group: W
page: 408
---

# WAIT -- 等待 BUSY# 引脚无效

## 操作码

```
Opcode   Instruction   Clocks     Description

9B       WAIT          6 min.     Wait until BUSY pin is inactive (HIGH)
```

## 说明

挂起处理器直到协处理器的 BUSY# 无效；若 ERROR# 有效则产生异常 16。

## 影响的标志

无。

## 保护模式异常（原文）

::: note
#NM if the task-switched flag in the machine status word (the lower 16 bits of register CR0) is set; #MF if the ERROR# input pin is asserted (i.e., the 80287 has detected an unmasked numeric error)
:::

## 实地址模式异常（原文）

::: note
Same exceptions as in Protected Mode
:::

## 虚拟 8086 模式异常（原文）

::: note
Same exceptions as in Protected Mode
:::
