---
id: SBB
title: 带借位整数减法
en: Integer Subtraction with Borrow
group: S
page: 386
---

# SBB -- 带借位整数减法

## 操作码

```
Opcode       Instruction       Clocks  Description

1C  ib       SBB AL,imm8       2       Subtract with borrow immediate byte
                                       from AL
1D  iw       SBB AX,imm16      2       Subtract with borrow immediate word
                                       from AX
1D  id       SBB EAX,imm32     2       Subtract with borrow immediate
                                       dword from EAX
80  /3 ib    SBB r/m8,imm8     2/7     Subtract with borrow immediate byte
                                       from r/m byte
81  /3 iw    SBB r/m16,imm16   2/7     Subtract with borrow immediate word
                                       from r/m word
81  /3 id    SBB r/m32,imm32   2/7     Subtract with borrow immediate
                                       dword from r/m dword
83  /3 ib    SBB r/m16,imm8    2/7     Subtract with borrow sign-extended
                                       immediate byte from r/m word
83  /3 ib    SBB r/m32,imm8    2/7     Subtract with borrow sign-extended
                                       immediate byte from r/m dword
18  /r       SBB r/m8,r8       2/6     Subtract with borrow byte register
                                       from r/m byte
19  /r       SBB r/m16,r16     2/6     Subtract with borrow word register
                                       from r/m word
19  /r       SBB r/m32,r32     2/6     Subtract with borrow dword register
                                       from r/m dword
1A  /r       SBB r8,r/m8       2/7     Subtract with borrow byte register
                                       from r/m byte
1B  /r       SBB r16,r/m16     2/7     Subtract with borrow word register
                                       from r/m word
1B  /r       SBB r32,r/m32     2/7     Subtract with borrow dword register
                                       from r/m dword
```

## 操作

```
IF SRC is a byte and DEST is a word or dword
THEN DEST := DEST - (SignExtend(SRC) + CF)
ELSE DEST := DEST - (SRC + CF);
```

## 说明

从目的操作数减去源操作数和 CF，结果写回目的操作数；与 SUB 配合可实现多倍精度减法。

## 影响的标志

OF、SF、ZF、AF、PF、CF，按附录 C 所述。

## 保护模式异常

- #GP(0)：结果位于不可写段。
- #GP(0)：CS、DS、ES、FS 或 GS 段中的内存操作数有效地址非法。
- #SS(0)：SS 段中的地址非法。
- #PF(fault-code)：页错误。


## 实地址模式异常

中断 13：操作数的任何部分超出 0–0FFFFH 的有效地址空间。


## 虚拟 8086 模式异常

与实地址模式相同；#PF(fault-code)：页错误。

