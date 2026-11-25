---
id: NEG
title: 求补（取负）
en: Two's Complement Negation
group: N
page: 354
---

# NEG -- 求补（取负）

## 操作码

```
Opcode  Instruction   Clocks    Description

F6  /3  NEG r/m8      2/6       Two's complement negate r/m byte
F7  /3  NEG r/m16     2/6       Two's complement negate r/m word
F7  /3  NEG r/m32     2/6       Two's complement negate r/m dword
```

## 操作

```
IF r/m = 0 THEN CF := 0 ELSE CF := 1; FI;
r/m := - r/m;
```

## 说明

用零减去目的操作数，得到其二进制补码；按结果更新状态标志，CF 在操作数非零时置位。

## 影响的标志

CF 如上述；OF、SF、ZF、PF 按附录 C 所述。

## 保护模式异常

- #GP(0)：结果位于不可写段。
- #GP(0)：CS、DS、ES、FS 或 GS 段中的内存操作数有效地址非法。
- #SS(0)：SS 段中的地址非法。
- #PF(fault-code)：页错误。


## 实地址模式异常

中断 13：操作数的任何部分超出 0–0FFFFH 的有效地址空间。


## 虚拟 8086 模式异常

与实地址模式相同；#PF(fault-code)：页错误。

