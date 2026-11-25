---
id: SAL
title: 移位指令
en: Shift Instructions
group: S
---

# SAL -- 移位指令

## 操作码

```
Opcode          Instruction       Clocks  Description

D0   /4         SAL r/m8,1        3/7     Multiply r/m byte by 2, once
D2   /4         SAL r/m8,CL       3/7     Multiply r/m byte by 2, CL times
C0   /4 ib      SAL r/m8,imm8     3/7     Multiply r/m byte by 2, imm8
                                          times
D1   /4         SAL r/m16,1       3/7     Multiply r/m word by 2, once
D3   /4         SAL r/m16,CL      3/7     Multiply r/m word by 2, CL times
C1   /4 ib      SAL r/m16,imm8    3/7     Multiply r/m word by 2, imm8
                                          times
D1   /4         SAL r/m32,1       3/7     Multiply r/m dword by 2, once
D3   /4         SAL r/m32,CL      3/7     Multiply r/m dword by 2, CL
                                          times
C1   /4 ib      SAL r/m32,imm8    3/7     Multiply r/m dword by 2, imm8
                                          times
D0   /7         SAR r/m8,1        3/7     Signed divide^(1) r/m byte by 2,
                                          once
D2   /7         SAR r/m8,CL       3/7     Signed divide^(1) r/m byte by 2,
                                          CL times
C0   /7 ib      SAR r/m8,imm8     3/7     Signed divide^(1) r/m byte by 2,
                                          imm8 times
D1   /7         SAR r/m16,1       3/7     Signed divide^(1) r/m word by 2,
                                          once
D3   /7         SAR r/m16,CL      3/7     Signed divide^(1) r/m word by 2,
                                          CL times
C1   /7 ib      SAR r/m16,imm8    3/7     Signed divide^(1) r/m word by 2,
                                          imm8 times
D1   /7         SAR r/m32,1       3/7     Signed divide^(1) r/m dword by 2,
                                          once
D3   /7         SAR r/m32,CL      3/7     Signed divide^(1) r/m dword by 2,
                                          CL times
C1   /7 ib      SAR r/m32,imm8    3/7     Signed divide^(1) r/m dword by 2,
                                          imm8 times
D0   /4         SHL r/m8,1        3/7     Multiply r/m byte by 2, once
D2   /4         SHL r/m8,CL       3/7     Multiply r/m byte by 2, CL times
C0   /4 ib      SHL r/m8,imm8     3/7     Multiply r/m byte by 2, imm8
                                          times
D1   /4         SHL r/m16,1       3/7     Multiply r/m word by 2, once
D3   /4         SHL r/m16,CL      3/7     Multiply r/m word by 2, CL times
C1   /4 ib      SHL r/m16,imm8    3/7     Multiply r/m word by 2, imm8
                                          times
D1   /4         SHL r/m32,1       3/7     Multiply r/m dword by 2, once
D3   /4         SHL r/m32,CL      3/7     Multiply r/m dword by 2, CL
                                          times
C1   /4 ib      SHL r/m32,imm8    3/7     Multiply r/m dword by 2, imm8
                                          times
D0   /5         SHR r/m8,1        3/7     Unsigned divide r/m byte by 2,
                                          once
D2   /5         SHR r/m8,CL       3/7     Unsigned divide r/m byte by 2,
                                          CL times
C0   /5 ib      SHR r/m8,imm8     3/7     Unsigned divide r/m byte by 2,
                                          imm8 times
D1   /5         SHR r/m16,1       3/7     Unsigned divide r/m word by 2,
                                          once
D3   /5         SHR r/m16,CL      3/7     Unsigned divide r/m word by 2,
                                          CL times
C1   /5 ib      SHR r/m16,imm8    3/7     Unsigned divide r/m word by 2,
                                          imm8 times
D1   /5         SHR r/m32,1       3/7     Unsigned divide r/m dword by 2,
                                          once
D3   /5         SHR r/m32,CL      3/7     Unsigned divide r/m dword by 2,
                                          CL times
C1   /5 ib      SHR r/m32,imm8    3/7     Unsigned divide r/m dword by 2,
                                          imm8 times
```

## 操作

```
(* COUNT is the second parameter *)
(temp) := COUNT;
WHILE (temp <> 0)
DO
   IF instruction is SAL or SHL
   THEN CF := high-order bit of r/m;
   FI;
   IF instruction is SAR or SHR
   THEN CF := low-order bit of r/m;
   FI;
   IF instruction = SAL or SHL
   THEN r/m := r/m * 2;
   FI;
   IF instruction = SAR
   THEN r/m := r/m /2 (*Signed divide, rounding toward negative infinity*);
   FI;
   IF instruction = SHR
   THEN r/m := r/m / 2; (* Unsigned divide *);
   FI;
   temp := temp - 1;
OD;
(* Determine overflow for the various instructions *)
IF COUNT = 1
THEN
   IF instruction is SAL or SHL
   THEN OF := high-order bit of r/m <> (CF);
   FI;
   IF instruction is SAR
   THEN OF := 0;
   FI;
   IF instruction is SHR
   THEN OF := high-order bit of operand;
   FI;
ELSE OF := undefined;
FI;
```

## 说明

SAL/SHL 左移，SHR 逻辑右移，SAR 算术右移；计数可为 1、立即数或 CL，CF 保存最后移出的位。

## 影响的标志

单次移位时设置 OF；多次移位时 OF 未定义；CF、ZF、PF、SF 按附录 C 所述。

## 保护模式异常（原文）

::: note
#GP(0) if the result is in a nonwritable segment; #GP(0) for an illegal memory operand effective address in the CS, DS, ES, FS, or GS segments; #SS(0) for an illegal address in the SS segment; #PF(fault-code) for a page fault
:::

## 实地址模式异常（原文）

::: note
Interrupt 13 if any part of the operand would lie outside of the effective address space from 0 to 0FFFFH
:::

## 虚拟 8086 模式异常（原文）

::: note
Same exceptions as in Real Address Mode; #PF(fault-code) for a page fault
:::
