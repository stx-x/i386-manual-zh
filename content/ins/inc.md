---
id: INC
title: 加 1
en: Increment by 1
group: I
page: 303
---

# INC -- 加 1

## 操作码

```
Opcode      Instruction        Clocks      Description

FE  /0      INC r/m8                       Increment r/m byte by 1
FF  /0      INC r/m16                      Increment r/m word by 1
FF  /6      INC r/m32                      Increment r/m dword by 1
40 + rw     INC r16                        Increment word register by 1
40 + rd     INC r32                        Increment dword register by 1
```

## 操作

```
DEST := DEST + 1;
```

## 说明

把目的操作数加 1；更新 OF、SF、ZF、AF、PF，但不影响 CF。

## 影响的标志

OF、SF、ZF、AF、PF 按附录 C 所述。

## 保护模式异常

- #GP(0)：操作数位于不可写段。
- #GP(0)：CS、DS、ES、FS 或 GS 段中的内存操作数有效地址非法。
- #SS(0)：SS 段中的地址非法。
- #PF(fault-code)：页错误。


## 实地址模式异常

中断 13：操作数的任何部分超出 0–0FFFFH 的有效地址空间。


## 虚拟 8086 模式异常

与实地址模式相同；#PF(fault-code)：页错误。

