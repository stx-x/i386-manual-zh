---
id: CMP
title: 比较两个操作数
en: Compare Two Operands
group: C
page: 287
---

# CMP -- 比较两个操作数

## 操作码

```
Opcode          Instruction        Clocks   Description

3C  ib          CMP AL,imm8        2        Compare immediate byte to AL
3D  iw          CMP AX,imm16       2        Compare immediate word to AX
3D  id          CMP EAX,imm32      2        Compare immediate dword to EAX
80  /7 ib       CMP r/m8,imm8      2/5      Compare immediate byte to r/m
                                            byte
81  /7 iw       CMP r/m16,imm16    2/5      Compare immediate word to r/m
                                            word
81  /7 id       CMP r/m32,imm32    2/5      Compare immediate dword to r/m
                                            dword
83  /7 ib       CMP r/m16,imm8     2/5      Compare sign extended immediate
                                            byte to r/m word
83  /7 ib       CMP r/m32,imm8     2/5      Compare sign extended immediate
                                            byte to r/m dword
38  /r          CMP r/m8,r8        2/5      Compare byte register to r/m
                                            byte
39  /r          CMP r/m16,r16      2/5      Compare word register to r/m
                                            word
39  /r          CMP r/m32,r32      2/5      Compare dword register to r/m
                                            dword
3A  /r          CMP r8,r/m8        2/6      Compare r/m byte to byte
                                            register
3B  /r          CMP r16,r/m16      2/6      Compare r/m word to word
                                            register
3B  /r          CMP r32,r/m32      2/6      Compare r/m dword to dword
                                            register
```

## 操作

```
LeftSRC - SignExtend(RightSRC);
(* CMP does not store a result; its purpose is to set the flags *)
```

## 说明

从目的操作数减去源操作数，只更新标志（OF、SF、ZF、AF、PF、CF），不改变两个操作数。

## 影响的标志

OF、SF、ZF、AF、PF、CF，按附录 C 所述。

## 保护模式异常（原文）

::: note
#GP(0) for an illegal memory operand effective address in the CS, DS, ES, FS, or GS segments; #SS(0) for an illegal address in the SS segment; #PF(fault-code) for a page fault
:::

## 实地址模式异常（原文）

::: note
Interrupt 13 if any part of the operand would lie outside of the effective address space from 0 to 0FFFFH
:::

## 虚拟 8086 模式异常（原文）

::: note
Same exceptions as in Real Address Mode; #PF(fault-code) for a page fault
:::
