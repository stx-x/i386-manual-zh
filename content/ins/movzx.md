---
id: MOVZX
title: 带零扩展传送
en: Move with Zero-Extend
group: M
page: 351
---

# MOVZX -- 带零扩展传送

## 操作码

```
Opcode      Instruction        Clocks   Description

0F  B6 /r   MOVZX r16,r/m8     3/6      Move byte to word with zero-extend
0F  B6 /r   MOVZX r32,r/m8     3/6      Move byte to dword, zero-extend
0F  B7 /r   MOVZX r32,r/m16    3/6      Move word to dword, zero-extend
```

## 操作

```
DEST := ZeroExtend(SRC);
```

## 说明

把 8 位或 16 位源操作数零扩展到 16 位或 32 位目的操作数。

## 影响的标志

无。

## 保护模式异常

- #GP(0)：CS、DS、ES、FS 或 GS 段中的内存操作数有效地址非法。
- #SS(0)：SS 段中的地址非法。
- #PF(fault-code)：页错误。


## 实地址模式异常

中断 13：操作数的任何部分超出 0–0FFFFH 的有效地址空间。


## 虚拟 8086 模式异常

与实地址模式相同；#PF(fault-code)：页错误。

