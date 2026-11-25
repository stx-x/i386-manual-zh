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

## 保护模式异常

#SS(0)：栈的起始或结束地址超出栈段界限；#PF(fault-code)：页错误。


## 实地址模式异常

- 执行 PUSHA 或 PUSHAD 之前，若 SP 或 ESP 等于 1、3 或 5，80386 将关机。
- 若 SP 或 ESP 等于 7、9、11、13 或 15，产生异常 13。


## 虚拟 8086 模式异常

与实地址模式相同；#PF(fault-code)：页错误。

