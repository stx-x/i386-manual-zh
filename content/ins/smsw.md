---
id: SMSW
title: 保存机器状态字
en: Store Machine Status Word
group: S
page: 397
---

# SMSW -- 保存机器状态字

## 操作码

```
Opcode      Instruction     Clocks          Description

0F  01 /4   SMSW r/m16      2/3,pm=2/2      Store machine status word to EA
                                            word
```

## 操作

```
r/m16 := MSW;
```

## 说明

把 CR0 的低 16 位（MSW）存入目的操作数。

## 影响的标志

无。

## 保护模式异常

- #GP(0)：结果位于不可写段。
- #GP(0)：CS、DS、ES、FS 或 GS 段中的内存操作数有效地址非法。
- #SS(0)：SS 段中的地址非法。
- #PF(fault-code)：页错误。


## 实地址模式异常

中断 13：操作数的任何部分超出 0–0FFFFH 的有效地址空间。


## 虚拟 8086 模式异常

与实地址模式相同；#PF(fault-code)：页错误。

