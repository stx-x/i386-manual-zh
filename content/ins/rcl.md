---
id: RCL
title: 循环移位
en: Rotate
group: R
---

# RCL -- 循环移位

## 操作码

```
Opcode       Instruction       Clocks  Description

D0  /2       RCL r/m8,1        9/10    Rotate 9 bits (CF,r/m byte) left
                                       once
D2  /2       RCL r/m8,CL       9/10    Rotate 9 bits (CF,r/m byte) left CL
                                       times
C0  /2 ib    RCL r/m8,imm8     9/10    Rotate 9 bits (CF,r/m byte) left
                                       imm8 times
D1  /2       RCL r/m16,1       9/10    Rotate 17 bits (CF,r/m word) left
                                       once
D3  /2       RCL r/m16,CL      9/10    Rotate 17 bits (CF,r/m word) left
                                       CL times
C1  /2 ib    RCL r/m16,imm8    9/10    Rotate 17 bits (CF,r/m word) left
                                       imm8 times
D1  /2       RCL r/m32,1       9/10    Rotate 33 bits (CF,r/m dword) left
                                       once
D3  /2       RCL r/m32,CL      9/10    Rotate 33 bits (CF,r/m dword) left
                                       CL times
C1  /2 ib    RCL r/m32,imm8    9/10    Rotate 33 bits (CF,r/m dword) left
                                       imm8 times
D0  /3       RCR r/m8,1        9/10    Rotate 9 bits (CF,r/m byte) right
                                       once
D2  /3       RCR r/m8,CL       9/10    Rotate 9 bits (CF,r/m byte) right
                                       CL times
C0  /3 ib    RCR r/m8,imm8     9/10    Rotate 9 bits (CF,r/m byte) right
                                       imm8 times
D1  /3       RCR r/m16,1       9/10    Rotate 17 bits (CF,r/m word) right
                                       once
D3  /3       RCR r/m16,CL      9/10    Rotate 17 bits (CF,r/m word) right
                                       CL times
C1  /3 ib    RCR r/m16,imm8    9/10    Rotate 17 bits (CF,r/m word) right
                                       imm8 times
D1  /3       RCR r/m32,1       9/10    Rotate 33 bits (CF,r/m dword) right
                                       once
D3  /3       RCR r/m32,CL      9/10    Rotate 33 bits (CF,r/m dword) right
                                       CL times
C1  /3 ib    RCR r/m32,imm8    9/10    Rotate 33 bits (CF,r/m dword) right
                                       imm8 times
D0  /0       ROL r/m8,1        3/7     Rotate 8 bits r/m byte left once
D2  /0       ROL r/m8,CL       3/7     Rotate 8 bits r/m byte left CL
                                       times
C0  /0 ib    ROL r/m8,imm8     3/7     Rotate 8 bits r/m byte left imm8
                                       times
D1  /0       ROL r/m16,1       3/7     Rotate 16 bits r/m word left once
D3  /0       ROL r/m16,CL      3/7     Rotate 16 bits r/m word left CL
                                       times
C1  /0 ib    ROL r/m16,imm8    3/7     Rotate 16 bits r/m word left imm8
                                       times
D1  /0       ROL r/m32,1       3/7     Rotate 32 bits r/m dword left once
D3  /0       ROL r/m32,CL      3/7     Rotate 32 bits r/m dword left CL
                                       times
C1  /0 ib    ROL r/m32,imm8    3/7     Rotate 32 bits r/m dword left imm8
                                       times
D0  /1       ROR r/m8,1        3/7     Rotate 8 bits r/m byte right once
D2  /1       ROR r/m8,CL       3/7     Rotate 8 bits r/m byte right CL
                                       times
C0  /1 ib    ROR r/m8,imm8     3/7     Rotate 8 bits r/m word right imm8
                                       times
D1  /1       ROR r/m16,1       3/7     Rotate 16 bits r/m word right once
D3  /1       ROR r/m16,CL      3/7     Rotate 16 bits r/m word right CL
                                       times
C1  /1 ib    ROR r/m16,imm8    3/7     Rotate 16 bits r/m word right imm8
                                       times
D1  /1       ROR r/m32,1       3/7     Rotate 32 bits r/m dword right once
D3  /1       ROR r/m32,CL      3/7     Rotate 32 bits r/m dword right CL
                                       times
C1  /1 ib    ROR r/m32,imm8    3/7     Rotate 32 bits r/m dword right imm8
                                       times
```

## 操作

```
(* ROL - Rotate Left *)
temp := COUNT;
WHILE (temp <> 0)
DO
   tmpcf := high-order bit of (r/m);
   r/m := r/m * 2 + (tmpcf);
   temp := temp - 1;
OD;
IF COUNT = 1
THEN
   IF high-order bit of r/m <> CF
   THEN OF := 1;
   ELSE OF := 0;
   FI;
ELSE OF := undefined;
FI;
(* ROR - Rotate Right *)
temp := COUNT;
WHILE (temp <> 0 )
DO
   tmpcf := low-order bit of (r/m);
   r/m := r/m / 2 + (tmpcf * 2^(width(r/m)));
   temp := temp - 1;
DO;
IF COUNT = 1
THEN
   IF (high-order bit of r/m) <> (bit next to high-order bit of r/m)
   THEN OF := 1;
   ELSE OF := 0;
   FI;
ELSE OF := undefined;
FI;
```

## 说明

RCL/RCR 通过 CF 循环左/右移；ROL/ROR 在操作数内部循环移位。计数可为 1、立即数或 CL。

## 影响的标志

仅单次循环移位时设置 OF；多位移位时 OF 未定义；CF 如上述。

## 保护模式异常

- #GP(0)：结果位于不可写段。
- #GP(0)：CS、DS、ES、FS 或 GS 段中的内存操作数有效地址非法。
- #SS(0)：SS 段中的地址非法。
- #PF(fault-code)：页错误。


## 实地址模式异常

中断 13：操作数的任何部分超出 0–0FFFFH 的有效地址空间。


## 虚拟 8086 模式异常

与实地址模式相同；#PF(fault-code)：页错误。

