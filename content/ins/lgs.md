---
id: LGS
title: 装入完整指针
en: Load Full Pointer
group: L
---

# LGS -- 装入完整指针

## 操作码

```
Opcode      Instruction      Clocks   Description

C5  /r      LDS r16,m16:16   7,p=22   Load DS:r16 with pointer from memory
C5  /r      LDS r32,m16:32   7,p=22   Load DS:r32 with pointer from memory
0F  B2 /r   LSS r16,m16:16   7,p=22   Load SS:r16 with pointer from memory
0F  B2 /r   LSS r32,m16:32   7,p=22   Load SS:r32 with pointer from memory
C4  /r      LES r16,m16:16   7,p=22   Load ES:r16 with pointer from memory
C4  /r      LES r32,m16:32   7,p=22   Load ES:r32 with pointer from memory
0F  B4 /r   LFS r16,m16:16   7,p=25   Load FS:r16 with pointer from memory
0F  B4 /r   LFS r32,m16:32   7,p=25   Load FS:r32 with pointer from memory
0F  B5 /r   LGS r16,m16:16   7,p=25   Load GS:r16 with pointer from memory
0F  B5 /r   LGS r32,m16:32   7,p=25   Load GS:r32 with pointer from memory
```

## 操作

```
CASE instruction OF
   LSS: Sreg is SS; (* Load SS register *)
   LDS: Sreg is DS; (* Load DS register *)
   LES: Sreg is ES; (* Load ES register *)
   LFS: Sreg is FS; (* Load FS register *)
   LGS: Sreg is DS; (* Load GS register *)
ESAC;
IF (OperandSize = 16)
THEN
   r16 := [Effective Address]; (* 16-bit transfer *)
   Sreg := [Effective Address + 2]; (* 16-bit transfer *)
   (* In Protected Mode, load the descriptor into the segment register *)
ELSE (* OperandSize = 32 *)
   r32 := [Effective Address]; (* 32-bit transfer *)
   Sreg := [Effective Address + 4]; (* 16-bit transfer *)
   (* In Protected Mode, load the descriptor into the segment register *)
FI;
```

## 说明

从内存装入一个远指针：偏移部分进入指定通用寄存器，段选择子进入 FS/SS/DS/ES/GS 中相应的段寄存器。

## 影响的标志

无。

## 保护模式异常

- #GP(0)：CS、DS、ES、FS 或 GS 段中的内存操作数有效地址非法。
- #SS(0)：SS 段中的地址非法。
- 第二操作数必须是内存操作数，不能是寄存器。
- #GP(0)：向 SS 装入空选择子。
- #PF(fault-code)：页错误。


## 实地址模式异常

第二操作数必须是内存操作数，不能是寄存器；中断 13：操作数的任何部分超出 0–0FFFFH 的有效地址空间。


## 虚拟 8086 模式异常

与实地址模式相同；#PF(fault-code)：页错误。

