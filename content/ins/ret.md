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

## 保护模式异常

#GP、#NP 或 #SS：条件见上文。


## 实地址模式异常

中断 13：操作数的任何部分超出 0–0FFFFH 的有效地址空间。


## 虚拟 8086 模式异常

与实地址模式相同；#PF(fault-code)：页错误。

