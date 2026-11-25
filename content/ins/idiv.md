---
id: IDIV
title: 有符号除法
en: Signed Divide
group: I
page: 298
---

# IDIV -- 有符号除法

## 操作码

```
Opcode      Instruction        Clocks   Description

F6 /7       IDIV r/m8          19       Signed divide AX by r/m byte
                                        (AL=Quo, AH=Rem)
F7 /7       IDIV AX,r/m16      27       Signed divide DX:AX by EA word
                                        (AX=Quo, DX=Rem)
F7 /7       IDIV EAX,r/m32     43       Signed divide EDX:EAX by DWORD
                                        byte (EAX=Quo, EDX=Rem)
```

## 操作

```
temp := dividend / divisor;
IF temp does not fit in quotient
THEN Interrupt 0;
ELSE
   quotient := temp;
   remainder := dividend MOD (r/m);
FI;
```

## 说明

用源操作数对有符号累加器做除法，商向零截断；除数为零或商超出目的范围时产生异常 0。

## 影响的标志

OF、SF、ZF、AF、PF、CF 均未定义。

## 保护模式异常

- 中断 0：商超出指定寄存器（AL 或 AX）的表示范围，或除数为 0。
- #GP(0)：CS、DS、ES、FS 或 GS 段中的内存操作数有效地址非法。
- #SS(0)：SS 段中的地址非法。
- #PF(fault-code)：页错误。


## 实地址模式异常

- 中断 0：商超出指定寄存器（AL 或 AX）的表示范围，或除数为 0。
- 中断 13：操作数的任何部分超出 0–0FFFFH 的有效地址空间。


## 虚拟 8086 模式异常

与实地址模式相同；#PF(fault-code)：页错误。

