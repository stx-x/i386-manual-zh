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

## 保护模式异常（原文）

::: note
#GP, #NP, #SS, and #TS as indicated under "
:::

## 实地址模式异常（原文）

::: note
None; if the SP or ESP = 1, 3, or 5 before executing INT or INTO, the 80386 will shut down due to insufficient stack space
:::

## 虚拟 8086 模式异常（原文）

::: note
#GP(0) fault if IOPL is less than 3, for INT only, to permit emulation; Interrupt 3 (0CCH) generates Interrupt 3; INTO generates Interrupt 4 if the overflow flag equals 1
:::
