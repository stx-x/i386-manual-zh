---
id: LLDT
title: 装入局部描述符表寄存器
en: Load Local Descriptor Table Register
group: L
page: 334
---

# LLDT -- 装入局部描述符表寄存器

## 操作码

```
Opcode      Instruction      Clocks   Description

0F  00 /2   LLDT r/m16       20       Load selector r/m16 into LDTR
```

## 操作

```
LDTR := SRC;
```

## 说明

用选择子所指 LDT 描述符装入 LDTR；特权指令。

## 影响的标志

无。

## 保护模式异常

- #GP(0)：当前特权级不为 0。
- #GP(selector)：选择子操作数未指向全局描述符表，或 GDT 中的表项不是局部描述符表。
- #NP(selector)：LDT 描述符不存在。
- #GP(0)：CS、DS、ES、FS 或 GS 段中的内存操作数有效地址非法。
- #SS(0)：SS 段中的地址非法。
- #PF(fault-code)：页错误。


## 实地址模式异常

中断 6；实地址模式不识别 LLDT。


## 虚拟 8086 模式异常

与实地址模式相同（指令不被识别，因此不会执行，也不会访问内存）。

操作数大小属性对该指令没有影响。

