---
id: POP
title: 从栈弹出字
en: Pop a Word from the Stack
group: P
page: 361
---

# POP -- 从栈弹出字

## 操作码

```
Opcode      Instruction   Clocks     Description

8F   /0     POP m16       5          Pop top of stack into memory word
8F   /0     POP m32       5          Pop top of stack into memory dword
58 + rw     POP r16       4          Pop top of stack into word register
58 + rd     POP r32       4          Pop top of stack into dword register
1F          POP DS        7,pm=21    Pop top of stack into DS
07          POP ES        7,pm=21    Pop top of stack into ES
17          POP SS        7,pm=21    Pop top of stack into SS
0F   A1     POP FS        7,pm=21    Pop top of stack into FS
0F   A9     POP GS        7,pm=21    Pop top of stack into GS
```

## 操作

```
IF StackAddrSize = 16
THEN
   IF OperandSize = 16
   THEN
      DEST := (SS:SP); (* copy a word *)
      SP := SP + 2;
   ELSE (* OperandSize = 32 *)
      DEST := (SS:SP); (* copy a dword *)
      SP := SP + 4;
   FI;
ELSE (* StackAddrSize = 32 * )
   IF OperandSize = 16
   THEN
      DEST := (SS:ESP); (* copy a word *)
      ESP := ESP + 2;
   ELSE (* OperandSize = 32 *)
      DEST := (SS:ESP); (* copy a dword *)
      ESP := ESP + 4;
   FI;
FI;
```

## 说明

把栈顶的字或双字装入目的操作数，然后递增 ESP/SP。

## 影响的标志

无。

## 保护模式异常

- 装入段寄存器时可能产生 #GP、#SS 和 #NP。
- #SS(0)：当前栈顶不在栈段内。
- #GP(0)：结果位于不可写段。
- #GP(0)：CS、DS、ES、FS 或 GS 段中的内存操作数有效地址非法。
- #SS(0)：SS 段中的地址非法。
- #PF(fault-code)：页错误。


## 实地址模式异常

中断 13：操作数的任何部分超出 0–0FFFFH 的有效地址空间。


## 虚拟 8086 模式异常

与实地址模式相同；#PF(fault-code)：页错误。

