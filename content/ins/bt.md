---
id: BT
title: 位测试
en: Bit Test
group: B
page: 267
---

# BT -- 位测试

## 操作码

```
Opcode         Instruction     Clocks    Description

0F  A3         BT r/m16,r16    3/12      Save bit in carry flag
0F  A3         BT r/m32,r32    3/12      Save bit in carry flag
0F  BA /4 ib   BT r/m16,imm8   3/6       Save bit in carry flag
0F  BA /4 ib   BT r/m32,imm8   3/6       Save bit in carry flag
```

## 操作

```
CF := BIT[LeftSRC, RightSRC];
```

## 说明

把目的操作数中由位偏移指定的位复制到 CF，不改变该位本身。

## 影响的标志

CF，如上述。

## 保护模式异常

- #GP(0)：CS、DS、ES、FS 或 GS 段中的内存操作数有效地址非法。
- #SS(0)：SS 段中的地址非法。
- #PF(fault-code)：页错误。


## 实地址模式异常

中断 13：操作数的任何部分超出 0–0FFFFH 的有效地址空间。


## 虚拟 8086 模式异常

与实地址模式相同；#PF(fault-code)：页错误。

