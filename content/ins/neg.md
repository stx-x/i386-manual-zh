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
