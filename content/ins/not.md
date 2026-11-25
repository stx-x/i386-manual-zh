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

## 保护模式异常（原文）

::: note
#GP(0) if the result is in a nonwritable segment; #GP(0) for an illegal memory operand effective address in the CS, DS, ES, FS, or GS segments; #SS(0) for an illegal address in the SS segment; #PF(fault-code) for a page fault
:::

## 实地址模式异常（原文）

::: note
Interrupt 13 if any part of the operand would lie outside of the effective address space from 0 to 0FFFFH
:::

## 虚拟 8086 模式异常（原文）

::: note
Same exceptions as in real-address mode; #PF(fault-code) for a page fault
:::
