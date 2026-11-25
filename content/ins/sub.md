---
id: SUB
title: 整数减法
en: Integer Subtraction
group: S
page: 404
---

# SUB -- 整数减法

## 操作码

```
Opcode      Instruction      Clocks   Description

2C  ib      SUB AL,imm8      2        Subtract immediate byte from AL
2D  iw      SUB AX,imm16     2        Subtract immediate word from AX
2D  id      SUB EAX,imm32    2        Subtract immediate dword from EAX
80  /5 ib   SUB r/m8,imm8    2/7      Subtract immediate byte from r/m byte
81  /5 iw   SUB r/m16,imm16  2/7      Subtract immediate word from r/m word
81  /5 id   SUB r/m32,imm32  2/7      Subtract immediate dword from r/m
                                      dword
83  /5 ib   SUB r/m16,imm8   2/7      Subtract sign-extended immediate byte
                                      from r/m word
83  /5 ib   SUB r/m32,imm8   2/7      Subtract sign-extended immediate byte
                                      from r/m dword
28  /r      SUB r/m8,r8      2/6      Subtract byte register from r/m byte
29  /r      SUB r/m16,r16    2/6      Subtract word register from r/m word
29  /r      SUB r/m32,r32    2/6      Subtract dword register from r/m
                                      dword
2A  /r      SUB r8,r/m8      2/7      Subtract byte register from r/m byte
2B  /r      SUB r16,r/m16    2/7      Subtract word register from r/m word
2B  /r      SUB r32,r/m32    2/7      Subtract dword register from r/m
                                      dword
```

## 操作

```
IF SRC is a byte and DEST is a word or dword
THEN DEST := DEST - SignExtend(SRC);
ELSE DEST := DEST - SRC;
FI;
```

## 说明

从目的操作数减去源操作数，结果写回目的操作数，并按结果设置状态标志。

## 影响的标志

OF、SF、ZF、AF、PF、CF，按附录 C 所述。

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
Same exceptions as in Real Address Mode; #PF(fault-code) for a page fault
:::
