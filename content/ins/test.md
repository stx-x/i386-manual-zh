---
id: TEST
title: 逻辑比较
en: Logical Compare
group: T
page: 405
---

# TEST -- 逻辑比较

## 操作码

```
Opcode       Instruction       Clocks   Description

A8   ib      TEST AL,imm8      2        AND immediate byte with AL
A9   iw      TEST AX,imm16     2        AND immediate word with AX
A9   id      TEST EAX,imm32    2        AND immediate dword with EAX
F6   /0 ib   TEST r/m8,imm8    2/5      AND immediate byte with r/m byte
F7   /0 iw   TEST r/m16,imm16  2/5      AND immediate word with r/m word
F7   /0 id   TEST r/m32,imm32  2/5      AND immediate dword with r/m dword
84   /r      TEST r/m8,r8      2/5      AND byte register with r/m byte
85   /r      TEST r/m16,r16    2/5      AND word register with r/m word
85   /r      TEST r/m32,r32    2/5      AND dword register with r/m dword
```

## 操作

```
DEST := LeftSRC AND RightSRC;
CF := 0;
OF := 0;
```

## 说明

对两个操作数逐位做逻辑与，只更新标志，不改变任一操作数。

## 影响的标志

OF := 0，CF := 0；SF、ZF、PF 按附录 C 所述。

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
