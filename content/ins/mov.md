---
id: MOV
title: 传送数据
en: Move Data
group: M
page: 347
---

# MOV -- 传送数据

## 操作码

```
Opcode   Instruction       Clocks        Description

88  /r   MOV r/m8,r8       2/2           Move byte register to r/m byte
89  /r   MOV r/m16,r16     2/2           Move word register to r/m word
89  /r   MOV r/m32,r32     2/2           Move dword register to r/m dword
8A  /r   MOV r8,r/m8       2/4           Move r/m byte to byte register
8B  /r   MOV r16,r/m16     2/4           Move r/m word to word register
8B  /r   MOV r32,r/m32     2/4           Move r/m dword to dword register
8C  /r   MOV r/m16,Sreg    2/2           Move segment register to r/m word
8D  /r   MOV Sreg,r/m16    2/5,pm=18/19  Move r/m word to segment register
A0       MOV AL,moffs8     4             Move byte at (seg:offset) to AL
A1       MOV AX,moffs16    4             Move word at (seg:offset) to AX
A1       MOV EAX,moffs32   4             Move dword at (seg:offset) to EAX
A2       MOV moffs8,AL     2             Move AL to (seg:offset)
A3       MOV moffs16,AX    2             Move AX to (seg:offset)
A3       MOV moffs32,EAX   2             Move EAX to (seg:offset)
B0 + rb  MOV reg8,imm8     2             Move immediate byte to register
B8 + rw  MOV reg16,imm16   2             Move immediate word to register
B8 + rd  MOV reg32,imm32   2             Move immediate dword to register
C6       MOV r/m8,imm8     2/2           Move immediate byte to r/m byte
C7       MOV r/m16,imm16   2/2           Move immediate word to r/m word
C7       MOV r/m32,imm32   2/2           Move immediate dword to r/m dword
```

## 操作

```
DEST := SRC;
```

## 说明

把字节、字或双字从源操作数传送到目的操作数；不能内存到内存，也不能段寄存器到段寄存器。

## 影响的标志

无。

## 保护模式异常

- 装入段寄存器时可能产生 #GP、#SS 和 #NP。
- 否则，若目的位于不可写段，产生 #GP(0)。
- #GP(0)：CS、DS、ES、FS 或 GS 段中的内存操作数有效地址非法。
- #SS(0)：SS 段中的地址非法。
- #PF(fault-code)：页错误。


## 实地址模式异常

中断 13：操作数的任何部分超出 0–0FFFFH 的有效地址空间。


## 虚拟 8086 模式异常

与实地址模式相同；#PF(fault-code)：页错误。

