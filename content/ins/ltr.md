---
id: LTR
title: 装入任务寄存器
en: Load Task Register
group: L
page: 344
---

# LTR -- 装入任务寄存器

## 操作码

```
Opcode       Instruction    Clocks    Description

0F  00 /3    LTR r/m16      pm=23/27  Load EA word into task register
```

## 说明

用选择子所指 TSS 描述符装入 TR，并把该 TSS 标记为忙；特权指令。

## 影响的标志

无。

## 保护模式异常

- #GP(0)：CS、DS、ES、FS 或 GS 段中的内存操作数有效地址非法。
- #SS(0)：SS 段中的地址非法。
- #GP(0)：当前特权级不为 0。
- #GP(selector)：源选择子所指对象不是 TSS，或已处于忙状态。
- #NP(selector)：TSS 被标记为“不存在”。
- #PF(fault-code)：页错误。


## 实地址模式异常

中断 6；实地址模式不识别 LTR。


## 虚拟 8086 模式异常

与实地址模式相同。

