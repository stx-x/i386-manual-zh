---
id: SLDT
title: 保存局部描述符表寄存器
en: Store Local Descriptor Table Register
group: S
page: 396
---

# SLDT -- 保存局部描述符表寄存器

## 操作码

```
Opcode      Instruction   Clocks      Description

0F  00 /0   SLDT r/m16    pm=2/2      Store LDTR to EA word
```

## 操作

```
r/m16 := LDTR;
```

## 说明

把 LDTR 的选择子存入通用寄存器或内存字。

## 影响的标志

无。

## 保护模式异常

- #GP(0)：结果位于不可写段。
- #GP(0)：CS、DS、ES、FS 或 GS 段中的内存操作数有效地址非法。
- #SS(0)：SS 段中的地址非法。
- #PF(fault-code)：页错误。


## 实地址模式异常

中断 6；实地址模式不识别 SLDT。


## 虚拟 8086 模式异常

与实地址模式相同；#PF(fault-code)：页错误。

