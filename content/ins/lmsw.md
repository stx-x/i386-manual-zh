---
id: LMSW
title: 装入机器状态字
en: Load Machine Status Word
group: L
page: 335
---

# LMSW -- 装入机器状态字

## 操作码

```
Opcode      Instruction      Clocks   Description

0F  01 /6   LMSW r/m16       10/13    Load r/m16 in machine status word
```

## 操作

```
MSW := r/m16; (* 16 bits is stored in the machine status word *)
```

## 说明

把源操作数装入 CR0 的低 16 位（MSW）；为兼容 80286 而提供。

## 影响的标志

无。

## 保护模式异常

- #GP(0)：当前特权级不为 0。
- #GP(0)：CS、DS、ES、FS 或 GS 段中的内存操作数有效地址非法。
- #SS(0)：SS 段中的地址非法。
- #PF(fault-code)：页错误。


## 实地址模式异常

中断 13：操作数的任何部分超出 0–0FFFFH 的有效地址空间。


## 虚拟 8086 模式异常

与实地址模式相同；#PF(fault-code)：页错误。

