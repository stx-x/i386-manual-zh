---
id: INT
title: 调用中断过程
en: Call to Interrupt Procedure
group: I
---

# INT -- 调用中断过程

## 操作码

```
Opcode    Instruction  Clocks          Description

CC        INT 3        33              Interrupt 3--trap to debugger
CC        INT 3        pm=59           Interrupt 3--Protected Mode, same
                                       privilege
CC        INT 3        pm=99           Interrupt 3--Protected Mode, more
                                       privilege
CC        INT 3        pm=119          Interrupt 3--from V86 mode to PL 0
CC        INT 3        ts              Interrupt 3--Protected Mode, via
                                       task gate
CD ib     INT imm8     37              Interrupt numbered by immediate
                                       byte
CD ib     INT imm8     pm=59           Interrupt--Protected Mode, same
                                       privilege
CD ib     INT imm8     pm=99           Interrupt--Protected Mode, more
                                       privilege
CD ib     INT imm8     pm=119          Interrupt--from V86 mode to PL 0
CD ib     INT imm8     ts              Interrupt--Protected Mode, via task
                                       gate
CE        INTO         Fail:3,pm=3;
                       Pass:35         Interrupt 4--if overflow flag is 1
CE        INTO         pm=59           Interrupt 4--Protected Mode, same
                                       privilege
CE        INTO         pm=99           Interrupt 4--Protected Mode, more
                                       privilege
CE        INTO         pm=119          Interrupt 4--from V86 mode to PL 0
CE        INTO         ts              Interrupt 4--Protected Mode, via
                                       task gate
```

## 说明

INT n 产生软件中断 n；INTO 在 OF 置位时产生中断 4。二者都通过 IDT 转向处理程序。

## 影响的标志

无。

## 保护模式异常

#GP、#NP、#SS 和 #TS：条件见上文。


## 实地址模式异常

无；执行 INT 或 INTO 之前，若 SP 或 ESP 为 1、3 或 5，80386 会因栈空间不足而关机。


## 虚拟 8086 模式异常

- #GP(0)：仅对 INT 而言，IOPL 小于 3，以便进行模拟。
- 中断 3（0CCH）产生中断 3。
- 若溢出标志为 1，INTO 产生中断 4。

