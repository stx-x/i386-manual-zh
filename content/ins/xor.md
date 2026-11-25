---
id: XOR
title: 逻辑异或
en: Logical Exclusive OR
group: X
page: 411
---

# XOR -- 逻辑异或

## 操作码

```
Opcode      Instruction      Clocks   Description

34  ib      XOR AL,imm8      2        Exclusive-OR immediate byte to AL
35  iw      XOR AX,imm16     2        Exclusive-OR immediate word to AX
35  id      XOR EAX,imm32    2        Exclusive-OR immediate dword to EAX
80  /6 ib   XOR r/m8,imm8    2/7      Exclusive-OR immediate byte to r/m
                                      byte
81  /6 iw   XOR r/m16,imm16  2/7      Exclusive-OR immediate word to r/m
                                      word
81  /6 id   XOR r/m32,imm32  2/7      Exclusive-OR immediate dword to r/m
                                      dword
83  /6 ib   XOR r/m16,imm8   2/7      XOR sign-extended immediate byte
                                      with r/m word
83  /6 ib   XOR r/m32,imm8   2/7      XOR sign-extended immediate byte
                                      with r/m dword
30  /r      XOR r/m8,r8      2/6      Exclusive-OR byte register to r/m
                                      byte
31  /r      XOR r/m16,r16    2/6      Exclusive-OR word register to r/m
                                      word
31  /r      XOR r/m32,r32    2/6      Exclusive-OR dword register to r/m
                                      dword
32  /r      XOR r8,r/m8      2/7      Exclusive-OR byte register to r/m
                                      byte
33  /r      XOR r16,r/m16    2/7      Exclusive-OR word register to r/m
                                      word
33  /r      XOR r32,r/m32    2/7      Exclusive-OR dword register to r/m
                                      dword
```

## 操作

```
DEST := LeftSRC XOR RightSRC
CF := 0
OF := 0
```

## 说明

对两个操作数逐位做异或，结果写入目的操作数；清零 OF、CF，更新 SF、ZF、PF。

## 影响的标志

CF := 0，OF := 0；SF、ZF、PF 按附录 C 所述；AF 未定义。

## 保护模式异常

- #GP(0)：结果位于不可写段。
- #GP(0)：CS、DS、ES、FS 或 GS 段中的内存操作数有效地址非法。
- #SS(0)：SS 段中的地址非法。
- #PF(fault-code)：页错误。


## 实地址模式异常

中断 13：操作数的任何部分超出 0–0FFFFH 的有效地址空间。


## 虚拟 8086 模式异常

与实地址模式相同；#PF(fault-code)：页错误。

