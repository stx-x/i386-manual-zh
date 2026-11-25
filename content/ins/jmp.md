---
id: JMP
title: 跳转
en: Jump
group: J
page: 319
---

# JMP -- 跳转

## 操作码

```
Opcode    Instruction     Clocks          Description

EB  cb    JMP rel8        7+m             Jump short
E9  cw    JMP rel16       7+m             Jump near, displacement relative
                                          to next instruction
FF  /4    JMP r/m16       7+m/10+m        Jump near indirect
EA  cd    JMP ptr16:16    12+m,pm=27+m    Jump intersegment, 4-byte
                                          immediate address
EA  cd    JMP ptr16:16    pm=45+m         Jump to call gate, same
                                          privilege
EA  cd    JMP ptr16:16    ts              Jump via task state segment
EA  cd    JMP ptr16:16    ts              Jump via task gate
FF  /5    JMP m16:16      43+m,pm=31+m    Jump r/m16:16 indirect and
                                          intersegment
FF  /5    JMP m16:16      pm=49+m         Jump to call gate, same
                                          privilege
FF  /5    JMP m16:16      5 + ts          Jump via task state segment
FF  /5    JMP m16:16      5 + ts          Jump via task gate
E9  cd    JMP rel32       7+m             Jump near, displacement relative
                                          to next instruction
FF  /4    JMP r/m32       7+m,10+m        Jump near, indirect
EA  cp    JMP ptr16:32    12+m,pm=27+m    Jump intersegment, 6-byte
                                          immediate address
EA  cp    JMP ptr16:32    pm=45+m         Jump to call gate, same
                                          privilege
EA  cp    JMP ptr16:32    ts              Jump via task state segment
EA  cp    JMP ptr16:32    ts              Jump via task gate
FF  /5    JMP m16:32      43+m,pm=31+m    Jump intersegment, address at
                                          r/m dword
FF  /5    JMP m16:32      pm=49+m         Jump to call gate, same
                                          privilege
FF  /5    JMP m16:32      5 + ts          Jump via task state segment
FF  /5    JMP m16:32      5 + ts          Jump via task gate
```

## 操作

```
IF instruction = relative JMP
   (* i.e. operand is rel8, rel16, or rel32 *)
THEN
   EIP := EIP + rel8/16/32;
   IF OperandSize = 16
   THEN EIP := EIP AND 0000FFFFH;
   FI;
FI;
IF instruction = near indirect JMP
   (* i.e. operand is r/m16 or r/m32 *)
THEN
   IF OperandSize = 16
   THEN
      EIP := [r/m16] AND 0000FFFFH;
   ELSE (* OperandSize = 32 *)
      EIP := [r/m32];
   FI;
FI;

IF (PE = 0 OR (PE = 1 AND VM = 1)) (* real mode or V86 mode *)
   AND instruction = far JMP
   (* i.e., operand type is m16:16, m16:32, ptr16:16, ptr16:32 *)
THEN GOTO REAL-OR-V86-MODE;
   IF operand type = m16:16 or m16:32
   THEN (* indirect *)
      IF OperandSize = 16
      THEN
         CS:IP := [m16:16];
         EIP := EIP AND 0000FFFFH; (* clear upper 16 bits *)
      ELSE (* OperandSize = 32 *)
         CS:EIP := [m16:32];
      FI;
   FI;
   IF operand type = ptr16:16 or ptr16:32
   THEN
      IF OperandSize = 16
      THEN
         CS:IP := ptr16:16;
         EIP := EIP AND 0000FFFFH; (* clear upper 16 bits *)
      ELSE (* OperandSize = 32 *)
         CS:EIP := ptr16:32;
      FI;
   FI;
FI;

IF (PE = 1 AND VM = 0) (* Protected mode, not V86 mode *)
   AND instruction = far JMP
THEN
   IF operand type = m16:16 or m16:32
   THEN (* indirect *)
      check access of EA dword;
      #GP(0) or #SS(0) IF limit violation;
   FI;
   Destination selector is not null ELSE #GP(0)
   Destination selector index is within its descriptor table limits ELSE
#GP(selector)
   Depending on AR byte of destination descriptor:
      GOTO CONFORMING-CODE-SEGMENT;
      GOTO NONCONFORMING-CODE-SEGMENT;
      GOTO CALL-GATE;
      GOTO TASK-GATE;
      GOTO TASK-STATE-SEGMENT;
   ELSE #GP(selector); (* illegal AR byte in descriptor *)
FI;

CONFORMING-CODE-SEGMENT:
   Descriptor DPL must be <= CPL ELSE #GP(selector);
   Segment must be present ELSE #NP(selector);
   Instruction pointer must be within code-segment limit ELSE #GP(0);
   IF OperandSize = 32
   THEN Load CS:EIP from destination pointer;
   ELSE Load CS:IP from destination pointer;
   FI;
   Load CS register with new segment descriptor;

NONCONFORMING-CODE-SEGMENT:
   RPL of destination selector must be <= CPL ELSE #GP(selector);
   Descriptor DPL must be = CPL ELSE #GP(selector);
   Segment must be present ELSE # NP(selector);
   Instruction pointer must be within code-segment limit ELSE #GP(0);
   IF OperandSize = 32
   THEN Load CS:EIP from destination pointer;
   ELSE Load CS:IP from destination pointer;
   FI;
   Load CS register with new segment descriptor;
   Set RPL field of CS register to CPL;

CALL-GATE:
   Descriptor DPL must be >= CPL ELSE #GP(gate selector);
   Descriptor DPL must be >= gate selector RPL ELSE #GP(gate selector);
   Gate must be present ELSE #NP(gate selector);
   Examine selector to code segment given in call gate descriptor:
      Selector must not be null ELSE #GP(0);
      Selector must be within its descriptor table limits ELSE
         #GP(CS selector);
      Descriptor AR byte must indicate code segment
         ELSE #GP(CS selector);
      IF non-conforming
      THEN code-segment descriptor, DPL must = CPL
      ELSE #GP(CS selector);
      FI;
      IF conforming
      THEN code-segment descriptor DPL must be <= CPL;
      ELSE #GP(CS selector);
      Code segment must be present ELSE #NP(CS selector);
      Instruction pointer must be within code-segment limit ELSE #GP(0);
      IF OperandSize = 32
      THEN Load CS:EIP from call gate;
      ELSE Load CS:IP from call gate;
      FI;
   Load CS register with new code-segment descriptor;
   Set RPL of CS to CPL

TASK-GATE:
   Gate descriptor DPL must be >= CPL ELSE #GP(gate selector);
   Gate descriptor DPL must be >= gate selector RPL ELSE #GP(gate
     selector);
   Task Gate must be present ELSE #NP(gate selector);
   Examine selector to TSS, given in Task Gate descriptor:
   Must specify global in the local/global bit ELSE #GP(TSS selector);
   Index must be within GDT limits ELSE #GP(TSS selector);
   Descriptor AR byte must specify available TSS (bottom bits 00001);
      ELSE #GP(TSS selector);
   Task State Segment must be present ELSE #NP(TSS selector);
SWITCH-TASKS (without nesting) to TSS;
Instruction pointer must be within code-segment limit ELSE #GP(0);

TASK-STATE-SEGMENT:
   TSS DPL must be >= CPL ELSE #GP(TSS selector);
   TSS DPL must be >= TSS selector RPL ELSE #GP(TSS selector);
   Descriptor AR byte must specify available TSS (bottom bits 00001)
      ELSE #GP(TSS selector);
   Task State Segment must be present ELSE #NP(TSS selector);
   SWITCH-TASKS (without nesting) to TSS;
   Instruction pointer must be within code-segment limit ELSE #GP(0);
```

## 说明

无条件把控制转移到目标地址；不保存返回地址。支持近/远、直接/间接形式。

## 影响的标志

若发生任务切换则全部影响；若不发生则无影响。

## 保护模式异常（原文）

::: note
Far jumps: #GP, #NP, #SS, and #TS, as indicated in the list above.

Near direct jumps: #GP(0) if procedure location is beyond the code segment limits.

Near indirect jumps: #GP(0) for an illegal memory operand effective address in the CS, DS, ES, FS, or GS segments: #SS(0) for an illegal address in the SS segment; #GP if the indirect offset obtained is beyond the code segment limits; #PF(fault-code) for a page fault.
:::

## 实地址模式异常（原文）

::: note
Interrupt 13 if any part of the operand would be outside of the effective address space from 0 to 0FFFFH
:::

## 虚拟 8086 模式异常（原文）

::: note
Same exceptions as under Real Address Mode; #PF(fault-code) for a page fault
:::
