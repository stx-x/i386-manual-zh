---
id: ADC
title: 带进位整数加法
en: Add with Carry
group: A
page: 260
---

# ADC -- 带进位整数加法

## 操作码

```
Opcode    Instruction      Clocks    Description

14 ib     ADC AL,imm8      2         Add with carry immediate byte to AL
15 iw     ADC AX,imm16     2         Add with carry immediate word to AX
15 id     ADC EAX,imm32    2         Add with carry immediate dword to EAX
80 /2 ib  ADC r/m8,imm8    2/7       Add with carry immediate byte to r/m
                                     byte
81 /2 iw  ADC r/m16,imm16  2/7       Add with carry immediate word to r/m
                                     word
81 /2 id  ADC r/m32,imm32  2/7       Add with CF immediate dword to r/m
                                     dword
83 /2 ib  ADC r/m16,imm8   2/7       Add with CF sign-extended immediate
                                     byte to r/m word
83 /2 ib  ADC r/m32,imm8   2/7       Add with CF sign-extended immediate
                                     byte into r/m dword
10 /r     ADC r/m8,r8      2/7       Add with carry byte register to r/m
                                     byte
11 /r     ADC r/m16,r16    2/7       Add with carry word register to r/m
                                     word
11 /r     ADC r/m32,r32    2/7       Add with CF dword register to r/m dword
12 /r     ADC r8,r/m8      2/6       Add with carry r/m byte to byte
                                     register
13 /r     ADC r16,r/m16    2/6       Add with carry r/m word to word
                                     register
13 /r     ADC r32,r/m32    2/6       Add with CF r/m dword to dword register
```

## 操作

```
DEST := DEST + SRC + CF;
```

## 说明

把源操作数、目的操作数与 CF 相加，结果写回目的操作数。与 ADD 配合可实现多倍精度加法。

## 影响的标志

OF、SF、ZF、AF、CF、PF，按附录 C 所述。

## 保护模式异常

- #GP(0)：结果位于不可写段。
- #GP(0)：CS、DS、ES、FS 或 GS 段中的内存操作数有效地址非法。
- #SS(0)：SS 段中的地址非法。
- #PF(fault-code)：页错误。


## 实地址模式异常

中断 13：操作数的任何部分超出 0–0FFFFH 的有效地址空间。


## 虚拟 8086 模式异常

与实地址模式相同；#PF(fault-code)：页错误。

