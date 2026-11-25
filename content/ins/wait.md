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

## 保护模式异常

- #NM：机器状态字（CR0 的低 16 位）中的任务已切换标志已置位。
- #MF：ERROR# 输入引脚有效，即 80287 检测到未屏蔽的数值错误。


## 实地址模式异常

与保护模式相同。


## 虚拟 8086 模式异常

与保护模式相同。

