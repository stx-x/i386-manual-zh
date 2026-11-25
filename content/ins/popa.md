---
id: POPA
title: 弹出全部通用寄存器
en: Pop all General Registers
group: P
---

# POPA -- 弹出全部通用寄存器

## 操作码

```
Opcode   Instruction   Clocks   Description

61       POPA          24       Pop DI, SI, BP, SP, BX, DX, CX, and AX
61       POPAD         24       Pop EDI, ESI, EBP, ESP, EDX, ECX, and EAX
```

## 操作

```
IF OperandSize = 16 (* instruction = POPA *)
THEN
   DI := Pop();
   SI := Pop();
   BP := Pop();
   throwaway := Pop (); (* Skip SP *)
   BX := Pop();
   DX := Pop();
   CX := Pop();
   AX := Pop();
ELSE (* OperandSize = 32, instruction = POPAD *)
   EDI := Pop();
   ESI := Pop();
   EBP := Pop();
   throwaway := Pop (); (* Skip ESP *)
   EBX := Pop();
   EDX := Pop();
   ECX := Pop();
   EAX := Pop();
FI;
```

## 说明

按 PUSHA 的逆序恢复 EDI、ESI、EBP、ESP（忽略）、EBX、EDX、ECX、EAX。

## 影响的标志

无。

## 保护模式异常

#SS(0)：栈的起始或结束地址不在栈段内；#PF(fault-code)：页错误。


## 实地址模式异常

中断 13：操作数的任何部分超出 0–0FFFFH 的有效地址空间。


## 虚拟 8086 模式异常

与实地址模式相同；#PF(fault-code)：页错误。

