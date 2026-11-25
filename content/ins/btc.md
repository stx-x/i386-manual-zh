---
id: BTC
title: 位测试并求反
en: Bit Test and Complement
group: B
page: 269
---

# BTC -- 位测试并求反

## 操作码

```
Opcode        Instruction     Clocks  Description

0F  BB        BTC r/m16,r16   6/13    Save bit in carry flag and complement
0F  BB        BTC r/m32,r32   6/13    Save bit in carry flag and complement
0F  BA /7 ib  BTC r/m16,imm8  6/8     Save bit in carry flag and complement
0F  BA /7 ib  BTC r/m32,imm8  6/8     Save bit in carry flag and complement
```

## 操作

```
CF := BIT[LeftSRC, RightSRC];
BIT[LeftSRC, RightSRC] := NOT BIT[LeftSRC, RightSRC];
```

## 说明

把指定位复制到 CF，然后对该位取反。

## 影响的标志

CF，如上述。

## 保护模式异常

- #GP(0)：结果位于不可写段。
- #GP(0)：CS、DS、ES、FS 或 GS 段中的内存操作数有效地址非法。
- #SS(0)：SS 段中的地址非法。
- #PF(fault-code)：页错误。


## 实地址模式异常

中断 13：操作数的任何部分超出 0–0FFFFH 的有效地址空间。


## 虚拟 8086 模式异常

与实地址模式相同；#PF(fault-code)：页错误。

