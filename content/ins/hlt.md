---
id: HLT
title: 停止处理器
en: Halt
group: H
page: 297
---

# HLT -- 停止处理器

## 操作码

```
Opcode      Instruction        Clocks     Description

F4          HLT                5          Halt
```

## 说明

使处理器停止取指，直到收到 INTR、NMI 或 RESET；特权指令。

## 影响的标志

无。

## 保护模式异常

HLT 是特权指令；#GP(0)：当前特权级不为 0。


## 实地址模式异常

无。


## 虚拟 8086 模式异常

#GP(0)；HLT 是特权指令。

