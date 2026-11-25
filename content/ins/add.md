---
id: ADD
title: 整数加法
en: Add
group: A
page: 261
---

# ADD -- 整数加法

## 操作码

```
Opcode    Instruction         Clocks    Description

04 ib     ADD AL,imm8          2        Add immediate byte to AL
05 iw     ADD AX,imm16         2        Add immediate word to AX
05 id     ADD EAX,imm32        2        Add immediate dword to EAX
80 /0 ib  ADD r/m8,imm8        2/7      Add immediate byte to r/m byte
81 /0 iw  ADD r/m16,imm16      2/7      Add immediate word to r/m word
81 /0 id  ADD r/m32,imm32      2/7      Add immediate dword to r/m dword
83 /0 ib  ADD r/m16,imm8       2/7      Add sign-extended immediate byte
                                        to r/m word
83 /0 ib  ADD r/m32,imm8       2/7      Add sign-extended immediate byte
                                        to r/m dword
00 /r     ADD r/m8,r8          2/7      Add byte register to r/m byte
01 /r     ADD r/m16,r16        2/7      Add word register to r/m word
01 /r     ADD r/m32,r32        2/7      Add dword register to r/m dword
02 /r     ADD r8,r/m8          2/6      Add r/m byte to byte register
03 /r     ADD r16,r/m16        2/6      Add r/m word to word register
03 /r     ADD r32,r/m32        2/6      Add r/m dword to dword register
```

## 操作

```
DEST := DEST + SRC;
```

## 说明

对两个操作数做整数加法，结果写入目的操作数，并按结果设置 OF、SF、ZF、AF、CF 和 PF。

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

