---
id: PUSHA
title: 压入全部通用寄存器
en: Push all General Registers
group: P
---

# PUSHA -- 压入全部通用寄存器

## 操作码

```
Opcode  Instruction  Clocks   Description

60      PUSHA        18       Push AX, CX, DX, BX, original SP, BP, SI, and
                              DI
60      PUSHAD       18       Push EAX, ECX, EDX, EBX, original ESP, EBP,
                              ESI, and EDI
```

## 操作

```
IF OperandSize = 16 (* PUSHA instruction *)
THEN
   Temp := (SP);
   Push(AX);
   Push(CX);
   Push(DX);
   Push(BX);
   Push(Temp);
   Push(BP);
   Push(SI);
   Push(DI);
ELSE (* OperandSize = 32, PUSHAD instruction *)
   Temp := (ESP);
   Push(EAX);
   Push(ECX);
   Push(EDX);
   Push(EBX);
   Push(Temp);
   Push(EBP);
   Push(ESI);
   Push(EDI);
FI;
```

## 说明

按 EAX、ECX、EDX、EBX、原 ESP、EBP、ESI、EDI 的顺序把通用寄存器压栈。

## 影响的标志

无。

## 保护模式异常（原文）

::: note
#SS(0) if the starting or ending stack address is outside the stack segment limit; #PF(fault-code) for a page fault
:::

## 实地址模式异常（原文）

::: note
Before executing PUSHA or PUSHAD, the 80386 shuts down if SP or ESP equals 1, 3, or 5; if SP or ESP equals 7, 9, 11, 13, or 15, exception 13 occurs
:::

## 虚拟 8086 模式异常（原文）

::: note
Same exceptions as in real-address mode; #PF(fault-code) for a page fault
:::
