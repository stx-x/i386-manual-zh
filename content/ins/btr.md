---
id: BTR
title: 位测试并复位
en: Bit Test and Reset
group: B
page: 271
---

# BTR -- 位测试并复位

## 操作码

```
Opcode        Instruction     Clocks  Description

0F  B3        BTR r/m16,r16   6/13    Save bit in carry flag and reset
0F  B3        BTR r/m32,r32   6/13    Save bit in carry flag and reset
0F  BA /6 ib  BTR r/m16,imm8  6/8     Save bit in carry flag and reset
0F  BA /6 ib  BTR r/m32,imm8  6/8     Save bit in carry flag and reset
```

## 操作

```
CF := BIT[LeftSRC, RightSRC];
BIT[LeftSRC, RightSRC] := 0;
```

## 说明

把指定位复制到 CF，然后清零该位。

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

