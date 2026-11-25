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

## 保护模式异常（原文）

::: note
#GP(0) for an illegal memory operand effective address in the CS, DS, ES, FS, or GS segments; #SS(0) for an illegal address in the SS segment; the second operand must be a memory operand, not a register; #GP(0) if a null selector is loaded into SS; #PF(fault-code) for a page fault
:::

## 实地址模式异常（原文）

::: note
The second operand must be a memory operand, not a register; Interrupt 13 if any part of the operand would lie outside of the effective address space from 0 to 0FFFFH
:::

## 虚拟 8086 模式异常（原文）

::: note
Same exceptions as in Real Address Mode; #PF(fault-code) for a page fault
:::
