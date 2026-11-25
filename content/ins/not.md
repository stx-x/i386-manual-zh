---
id: NOT
title: 求反
en: One's Complement Negation
group: N
page: 356
---

# NOT -- 求反

## 操作码

```
Opcode    Instruction   Clocks    Description

F6   /2   NOT r/m8       2/6      Reverse each bit of r/m byte
F7   /2   NOT r/m16      2/6      Reverse each bit of r/m word
F7   /2   NOT r/m32      2/6      Reverse each bit of r/m dword
```

## 操作

```
r/m := NOT r/m;
```

## 说明

对目的操作数逐位取反（一的补码）；不影响标志。

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

