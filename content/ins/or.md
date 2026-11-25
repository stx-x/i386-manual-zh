---
id: OR
title: 逻辑或
en: Logical Inclusive OR
group: O
page: 357
---

# OR -- 逻辑或

## 操作码

```
Opcode       Instruction       Clocks    Description

0C  ib       OR AL,imm8        2         OR immediate byte to AL
0D  iw       OR AX,imm16       2         OR immediate word to AX
0D  id       OR EAX,imm32      2         OR immediate dword to EAX
80  /1 ib    OR r/m8,imm8      2/7       OR immediate byte to r/m byte
81  /1 iw    OR r/m16,imm16    2/7       OR immediate word to r/m word
81  /1 id    OR r/m32,imm32    2/7       OR immediate dword to r/m dword
83  /1 ib    OR r/m16,imm8     2/7       OR sign-extended immediate byte
                                         with r/m word
83  /1 ib    OR r/m32,imm8     2/7       OR sign-extended immediate byte
                                         with r/m dword
08  /r       OR r/m8,r8        2/6       OR byte register to r/m byte
09  /r       OR r/m16,r16      2/6       OR word register to r/m word
09  /r       OR r/m32,r32      2/6       OR dword register to r/m dword
0A  /r       OR r8,r/m8        2/7       OR byte register to r/m byte
0B  /r       OR r16,r/m16      2/7       OR word register to r/m word
0B  /r       OR r32,r/m32      2/7       OR dword register to r/m dword
```

## 操作

```
DEST := DEST OR SRC;
CF := 0;
OF := 0
```

## 说明

对两个操作数逐位做逻辑或，结果写入目的操作数；清零 OF、CF，更新 SF、ZF、PF。

## 影响的标志

OF := 0，CF := 0；SF、ZF、PF 按附录 C 所述；AF 未定义。

## 保护模式异常

- #GP(0)：结果位于不可写段。
- #GP(0)：CS、DS、ES、FS 或 GS 段中的内存操作数有效地址非法。
- #SS(0)：SS 段中的地址非法。
- #PF(fault-code)：页错误。


## 实地址模式异常

中断 13：操作数的任何部分超出 0–0FFFFH 的有效地址空间。


## 虚拟 8086 模式异常

与实地址模式相同；#PF(fault-code)：页错误。

