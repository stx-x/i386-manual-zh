---
id: IDIV
title: 有符号除法
en: Signed Divide
group: I
page: 298
---

# IDIV -- 有符号除法

## 操作码

```
Opcode      Instruction        Clocks   Description

F6 /7       IDIV r/m8          19       Signed divide AX by r/m byte
                                        (AL=Quo, AH=Rem)
F7 /7       IDIV AX,r/m16      27       Signed divide DX:AX by EA word
                                        (AX=Quo, DX=Rem)
F7 /7       IDIV EAX,r/m32     43       Signed divide EDX:EAX by DWORD
                                        byte (EAX=Quo, EDX=Rem)
```

## 操作

```
temp := dividend / divisor;
IF temp does not fit in quotient
THEN Interrupt 0;
ELSE
   quotient := temp;
   remainder := dividend MOD (r/m);
FI;
```

## 说明

用源操作数对有符号累加器做除法，商向零截断；除数为零或商超出目的范围时产生异常 0。

## 影响的标志

OF、SF、ZF、AF、PF、CF 均未定义。

## 保护模式异常（原文）

::: note
Interrupt 0 if the quotient is too large to fit in the designated register (AL or AX), or if the divisor is 0; #GP (0) for an illegal memory operand effective address in the CS, DS, ES, FS, or GS segments; #SS(0) for an illegal address in the SS segment; #PF(fault-code) for a page fault
:::

## 实地址模式异常（原文）

::: note
Interrupt 0 if the quotient is too large to fit in the designated register (AL or AX), or if the divisor is 0; Interrupt 13 if any part of the operand would lie outside of the effective address space from 0 to 0FFFFH
:::

## 虚拟 8086 模式异常（原文）

::: note
Same exceptions as in Real Address Mode; #PF(fault-code) for a page fault
:::
