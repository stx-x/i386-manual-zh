---
id: DIV
title: 无符号除法
en: Unsigned Divide
group: D
page: 294
---

# DIV -- 无符号除法

## 操作码

```
Opcode    Instruction        Clocks   Description

F6 /6     DIV AL,r/m8        14/17    Unsigned divide AX by r/m byte
                                      (AL=Quo, AH=Rem)
F7 /6     DIV AX,r/m16       22/25    Unsigned divide DX:AX by r/m
                                      word (AX=Quo, DX=Rem)
F7 /6     DIV EAX,r/m32      38/41    Unsigned divide EDX:EAX by r/m
                                      dword (EAX=Quo, EDX=Rem)
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

用源操作数除累加器（AX、DX:AX 或 EDX:EAX），商和余数分别写入规定寄存器；除数为零或商溢出时产生异常 0。

## 影响的标志

OF、SF、ZF、AF、PF、CF 均未定义。

## 保护模式异常

- 中断 0：商超出指定寄存器（AL、AX 或 EAX）的表示范围，或除数为 0。
- #GP(0)：CS、DS、ES、FS 或 GS 段中的内存操作数有效地址非法。
- #SS(0)：SS 段中的地址非法。
- #PF(fault-code)：页错误。


## 实地址模式异常

- 中断 0：商超出指定寄存器（AL、AX 或 EAX）的表示范围，或除数为 0。
- 中断 13：操作数的任何部分超出 0–0FFFFH 的有效地址空间。


## 虚拟 8086 模式异常

与实地址模式相同；#PF(fault-code)：页错误。

