---
id: XCHG
title: 寄存器/内存与寄存器交换
en: Exchange Register/Memory with Register
group: X
page: 409
---

# XCHG -- 寄存器/内存与寄存器交换

## 操作码

```
Opcode    Instruction      Clocks     Description

90 + r    XCHG AX,r16      3          Exchange word register with AX
90 + r    XCHG r16,AX      3          Exchange word register with AX
90 + r    XCHG EAX,r32     3          Exchange dword register with EAX
90 + r    XCHG r32,EAX     3          Exchange dword register with EAX
86  /r    XCHG r/m8,r8     3          Exchange byte register with EA byte
86  /r    XCHG r8,r/m8     3/5        Exchange byte register with EA byte
87  /r    XCHG r/m16,r16   3          Exchange word register with EA word
87  /r    XCHG r16,r/m16   3/5        Exchange word register with EA word
87  /r    XCHG r/m32,r32   3          Exchange dword register with EA dword
87  /r    XCHG r32,r/m32   3/5        Exchange dword register with EA dword
```

## 操作

```
temp := DEST
DEST := SRC
SRC := temp
```

## 说明

交换两个操作数的内容；引用内存时自动断言 LOCK。

## 影响的标志

无。

## 保护模式异常（原文）

::: note
#GP(0) if either operand is in a nonwritable segment; #GP(0) for an illegal memory operand effective address in the CS, DS, ES, FS, or GS segments; #SS(0) for an illegal address in the SS segment; #PF(fault-code) for a page fault
:::

## 实地址模式异常（原文）

::: note
Interrupt 13 if any part of the operand would lie outside of the effective address space from 0 to 0FFFFH
:::

## 虚拟 8086 模式异常（原文）

::: note
Same exceptions as in Real Address Mode; #PF(fault-code) for a page fault
:::
