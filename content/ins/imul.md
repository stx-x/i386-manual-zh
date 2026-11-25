---
id: IMUL
title: 有符号乘法
en: Signed Multiply
group: I
page: 300
---

# IMUL -- 有符号乘法

## 操作码

```
Opcode      Instruction            Clocks      Description

F6  /5      IMUL r/m8              9-14/12-17  AX= AL * r/m byte
F7  /5      IMUL r/m16             9-22/12-25  DX:AX := AX * r/m word
F7  /5      IMUL r/m32             9-38/12-41  EDX:EAX := EAX * r/m dword
0F  AF /r   IMUL r16,r/m16         9-22/12-25  word register := word
                                               register * r/m word
0F  AF /r   IMUL r32,r/m32         9-38/12-41  dword register := dword
                                               register * r/m dword
6B  /r ib   IMUL r16,r/m16,imm8    9-14/12-17  word register := r/m16 *
                                               sign-extended immediate byte
6B  /r ib   IMUL r32,r/m32,imm8    9-14/12-17  dword register := r/m32 *
                                               sign-extended immediate byte
6B  /r ib   IMUL r16,imm8          9-14/12-17  word register := word
                                               register * sign-extended
                                               immediate byte
6B  /r ib   IMUL r32,imm8          9-14/12-17  dword register := dword
                                               register * sign-extended
                                               immediate byte
69  /r iw   IMUL r16,r/m16,imm16   9-22/12-25  word register := r/m16 *
                                               immediate word
69  /r id   IMUL r32,r/m32,imm32   9-38/12-41  dword register := r/m32 *
                                               immediate dword
69  /r iw   IMUL r16,imm16         9-22/12-25  word register := r/m16 *
                                               immediate word
69  /r id   IMUL r32,imm32         9-38/12-41  dword register := r/m32 *
                                               immediate dword
```

## 操作

```
result := multiplicand * multiplier;
```

## 说明

执行有符号乘法，支持单操作数、双操作数和三操作数形式；结果的高半部分非零时置位 CF 和 OF。

## 影响的标志

OF、CF 如上述；SF、ZF、AF、PF 未定义。

## 保护模式异常

- #GP(0)：CS、DS、ES、FS 或 GS 段中的内存操作数有效地址非法。
- #SS(0)：SS 段中的地址非法。
- #PF(fault-code)：页错误。


## 实地址模式异常

中断 13：操作数的任何部分超出 0–0FFFFH 的有效地址空间。


## 虚拟 8086 模式异常

与实地址模式相同；#PF(fault-code)：页错误。

