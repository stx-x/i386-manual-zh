---
id: PUSH
title: 把操作数压栈
en: Push Operand onto the Stack
group: P
page: 367
---

# PUSH -- 把操作数压栈

## 操作码

```
Opcode     Instruction   Clocks   Description

FF   /6    PUSH m16      5        Push memory word
FF   /6    PUSH m32      5        Push memory dword
50 + /r    PUSH r16      2        Push register word
50 + /r    PUSH r32      2        Push register dword
6A         PUSH imm8     2        Push immediate byte
68         PUSH imm16    2        Push immediate word
68         PUSH imm32    2        Push immediate dword
0E         PUSH CS       2        Push CS
16         PUSH SS       2        Push SS
1E         PUSH DS       2        Push DS
06         PUSH ES       2        Push ES
0F   A0    PUSH FS       2        Push FS
OF   A8    PUSH GS       2        Push GS
```

## 操作

```
IF StackAddrSize = 16
THEN
   IF OperandSize = 16 THEN
      SP := SP - 2;
      (SS:SP) := (SOURCE); (* word assignment *)
   ELSE
      SP := SP - 4;
      (SS:SP) := (SOURCE); (* dword assignment *)
   FI;
ELSE (* StackAddrSize = 32 *)
   IF OperandSize = 16
   THEN
      ESP := ESP - 2;
      (SS:ESP) := (SOURCE); (* word assignment *)
   ELSE
      ESP := ESP - 4;
      (SS:ESP) := (SOURCE); (* dword assignment *)
   FI;
FI;
```

## 说明

递减 ESP/SP，然后把源操作数写入新栈顶。

## 影响的标志

无。

## 保护模式异常

- #SS(0)：SP 或 ESP 的新值超出栈段界限。
- #GP(0)：CS、DS、ES、FS 或 GS 段中的内存操作数有效地址非法。
- #SS(0)：SS 段中的地址非法。
- #PF(fault-code)：页错误。


## 实地址模式异常

无；若 SP 或 ESP 为 1，80386 因栈空间不足而关机。


## 虚拟 8086 模式异常

与实地址模式相同；#PF(fault-code)：页错误。

