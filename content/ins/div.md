---
id: DIV
title: 无符号除法
en: Unsigned Divide
group: D
page: 294
---

# DIV -- 无符号除法

## 操作码

```
Opcode    Instruction        Clocks   Description

F6 /6     DIV AL,r/m8        14/17    Unsigned divide AX by r/m byte
                                      (AL=Quo, AH=Rem)
F7 /6     DIV AX,r/m16       22/25    Unsigned divide DX:AX by r/m
                                      word (AX=Quo, DX=Rem)
F7 /6     DIV EAX,r/m32      38/41    Unsigned divide EDX:EAX by r/m
                                      dword (EAX=Quo, EDX=Rem)
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

用源操作数除累加器（AX、DX:AX 或 EDX:EAX），商和余数分别写入规定寄存器；除数为零或商溢出时产生异常 0。

## 影响的标志

OF、SF、ZF、AF、PF、CF 均未定义。

## 保护模式异常（原文）

::: note
Interrupt 0 if the quotient is too large to fit in the designated register (AL, AX, or EAX), or if the divisor is 0; #GP(0) for an illegal memory operand effective address in the CS, DS, ES, FS, or GS segments; #SS(0) for an illegal address in the SS segment; #PF(fault-code) for a page fault
:::

## 实地址模式异常（原文）

::: note
Interrupt 0 if the quotient is too big to fit in the designated register (AL, AX, or EAX), or if the divisor is 0; Interrupt 13 if any part of the operand would lie outside of the effective address space from 0 to 0FFFFH
:::

## 虚拟 8086 模式异常（原文）

::: note
Same exceptions as in Real Address Mode; #PF(fault-code) for a page fault
:::
