---
id: POPF
title: 从栈弹出标志
en: Pop Stack into FLAGS or EFLAGS Register
group: P
---

# POPF -- 从栈弹出标志

## 操作码

```
Opcode   Instruction   Clocks   Description

9D       POPF          5        Pop top of stack FLAGS
9D       POPFD         5        Pop top of stack into EFLAGS
```

## 说明

把栈顶字或双字装入 FLAGS/EFLAGS 的相应位；POPFD 为 32 位形式。

## 影响的标志

除 VM 和 RF 之外的所有标志。

## 保护模式异常

#SS(0)：栈顶不在栈段内。


## 实地址模式异常

中断 13：操作数的任何部分超出 0–0FFFFH 的有效地址空间。


## 虚拟 8086 模式异常

#GP(0)：IOPL 小于 3，以便进行模拟。

