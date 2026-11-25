---
id: STR
title: 保存任务寄存器
en: Store Task Register
group: S
page: 403
---

# STR -- 保存任务寄存器

## 操作码

```
Opcode        Instruction   Clocks       Description

0F  00 /1     STR r/m16     pm=23/27     Load EA word into task register
```

## 操作

```
r/m := task register;
```

## 说明

把 TR 的选择子存入通用寄存器或内存字。

## 影响的标志

无。

## 保护模式异常

- #GP(0)：结果位于不可写段。
- #GP(0)：CS、DS、ES、FS 或 GS 段中的内存操作数有效地址非法。
- #SS(0)：SS 段中的地址非法。
- #PF(fault-code)：页错误。


## 实地址模式异常

中断 6；实地址模式不识别 STR。


## 虚拟 8086 模式异常

与实地址模式相同。

