---
id: RET
title: 从过程返回
en: Return from Procedure
group: R
page: 378
---

# RET -- 从过程返回

## 操作码

```
Opcode     Instruction  Clocks         Description

C3         RET          10+m           Return (near) to caller
CB         RET          18+m,pm=32+m   Return (far) to caller, same
                                       privilege
CB         RET          pm=68          Return (far), lesser privilege,
                                       switch stacks
C2  iw     RET imm16    10+m           Return (near), pop imm16 bytes of
                                       parameters
CA  iw     RET imm16    18+m,pm=32+m   Return (far), same privilege, pop
                                       imm16 bytes
CA  iw     RET imm16    pm=68          Return (far), lesser privilege, pop
                                       imm16 bytes
```

## 说明

从栈弹出返回地址并转移控制；可选立即数用于释放调用者压入的参数。

## 影响的标志

无。

## 保护模式异常（原文）

::: note
#GP, #NP, or #SS, as described under "
:::

## 实地址模式异常（原文）

::: note
Interrupt 13 if any part of the operand would be outside the effective address space from 0 to 0FFFFH
:::

## 虚拟 8086 模式异常（原文）

::: note
Same exceptions as in Real Address Mode; #PF(fault-code) for a page fault
:::
