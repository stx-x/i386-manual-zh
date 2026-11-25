---
id: CALL
title: 调用过程
en: Call Procedure
group: C
page: 275
---

# CALL -- 调用过程

## 操作码

```
Opcode    Instruction     Clocks
  Values of ts are given by the following table:

                             New Task
              386 TSS         386 TSS         286 TSS
  Old         VM = 0          VM = 1
  Task                     Via Task Gate?

              N     Y         N     Y         N     Y

386          300   309       217   226       273   282
TSS VM=0

286          298   307       217   226       273   282


TSS       Description

E8  cw    CALL rel16       7+m            Call near, displacement relative
                                          to next instruction
FF  /2    CALL r/m16       7+m/10+m       Call near, register
                                          indirect/memory indirect
9A  cd    CALL ptr16:16    17+m,pm=34+m   Call intersegment, to full
                                          pointer given
9A  cd    CALL ptr16:16    pm=52+m        Call gate, same privilege
9A  cd    CALL ptr16:16    pm=86+m        Call gate, more privilege, no
                                          parameters
9A  cd    CALL ptr16:16    pm=94+4x+m     Call gate, more privilege, x
                                          parameters
9A  cd    CALL ptr16:16    ts             Call to task
FF  /3    CALL m16:16      22+m,pm=38+m   Call intersegment, address at
                                          r/m dword
FF  /3    CALL m16:16      pm=56+m        Call gate, same privilege
FF  /3    CALL m16:16      pm=90+m        Call gate, more privilege, no
                                          parameters
FF  /3    CALL m16:16      pm=98+4x+m     Call gate, more privilege, x
                                          parameters
FF  /3    CALL m16:16      5 + ts         Call to task
E8  cd    CALL rel32       7+m            Call near, displacement relative
                                          to next instruction
FF  /2    CALL r/m32       7+m/10+m       Call near, indirect
9A  cp    CALL ptr16:32    17+m,pm=34+m   Call intersegment, to full
                                          pointer given
9A  cp    CALL ptr16:32    pm=52+m        Call gate, same privilege
9A  cp    CALL ptr16:32    pm=86+m        Call gate, more privilege, no
                                          parameters
9A  cp    CALL ptr32:32    pm=94+4x+m     Call gate, more privilege, x
                                          parameters
9A  cp    CALL ptr16:32    ts             Call to task
FF  /3    CALL m16:32      22+m,pm=38+m   Call intersegment, address at
                                          r/m dword
FF  /3    CALL m16:32      pm=56+m        Call gate, same privilege
FF  /3    CALL m16:32      pm=90+m        Call gate, more privilege, no
                                          parameters
FF  /3    CALL m16:32      pm=98+4x+m     Call gate, more privilege, x
                                          parameters
FF  /3    CALL m16:32      5 + ts         Call to task
```

## 操作

```
IF rel16 or rel32 type of call
THEN (* near relative call *)
   IF OperandSize = 16
   THEN
      Push(IP);
      EIP := (EIP + rel16) AND 0000FFFFH;
   ELSE (* OperandSize = 32 *)
      Push(EIP);
      EIP := EIP + rel32;
   FI;
FI;

IF r/m16 or r/m32 type of call
THEN (* near absolute call *)
   IF OperandSize = 16
   THEN
      Push(IP);
      EIP := [r/m16] AND 0000FFFFH;
   ELSE (* OperandSize = 32 *)
      Push(EIP);
      EIP := [r/m32];
   FI;
FI;

IF (PE = 0 OR (PE = 1 AND VM = 1))
(* real mode or virtual 8086 mode *)
   AND instruction = far CALL
   (* i.e., operand type is m16:16, m16:32, ptr16:16, ptr16:32 *)
THEN
   IF OperandSize = 16
   THEN
      Push(CS);
      Push(IP); (* address of next instruction; 16 bits *)
   ELSE
      Push(CS); (* padded with 16 high-order bits *)
      Push(EIP); (* address of next instruction; 32 bits *)
   FI;
   IF operand type is m16:16 or m16:32
   THEN (* indirect far call *)
      IF OperandSize = 16
      THEN
         CS:IP := [m16:16];
         EIP := EIP AND 0000FFFFH; (* clear upper 16 bits *)
      ELSE (* OperandSize = 32 *)
         CS:EIP := [m16:32];
      FI;
   FI;
   IF operand type is ptr16:16 or ptr16:32
   THEN (* direct far call *)
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
   AND instruction = far CALL
THEN
   If indirect, then check access of EA doubleword;
      #GP(0) if limit violation;
   New CS selector must not be null else #GP(0);
   Check that new CS selector index is within its
      descriptor table limits; else #GP(new CS selector);
   Examine AR byte of selected descriptor for various legal values;
      depending on value:
      go to CONFORMING-CODE-SEGMENT;
      go to NONCONFORMING-CODE-SEGMENT;
      go to CALL-GATE;
      go to TASK-GATE;
      go to TASK-STATE-SEGMENT;
   ELSE #GP(code segment selector);
FI;

CONFORMING-CODE-SEGMENT:
   DPL must be <= CPL ELSE #GP(code segment selector);
   Segment must be present ELSE #NP(code segment selector);
   Stack must be big enough for return address ELSE #SS(0);
   Instruction pointer must be in code segment limit ELSE #GP(0);
   Load code segment descriptor into CS register;
   Load CS with new code segment selector;
   Load EIP with zero-extend(new offset);
   IF OperandSize=16 THEN EIP := EIP AND 0000FFFFH; FI;

NONCONFORMING-CODE-SEGMENT:
   RPL must be <= CPL ELSE #GP(code segment selector)
   DPL must be = CPL ELSE #GP(code segment selector)
   Segment must be present ELSE #NP(code segment selector)
   Stack must be big enough for return address ELSE #SS(0)
   Instruction pointer must be in code segment limit ELSE #GP(0)
   Load code segment descriptor into CS register
   Load CS with new code segment selector
   Set RPL of CS to CPL
   Load EIP with zero-extend(new offset);
   IF OperandSize=16 THEN EIP := EIP AND 0000FFFFH; FI;

CALL-GATE:
   Call gate DPL must be >= CPL ELSE #GP(call gate selector)
   Call gate DPL must be >= RPL ELSE #GP(call gate selector)
   Call gate must be present ELSE #NP(call gate selector)
   Examine code segment selector in call gate descriptor:
      Selector must not be null ELSE #GP(0)
      Selector must be within its descriptor table
         limits ELSE #GP(code segment selector)
   AR byte of selected descriptor must indicate code
      segment ELSE #GP(code segment selector)
   DPL of selected descriptor must be <= CPL ELSE
      #GP(code segment selector)
   IF non-conforming code segment AND DPL < CPL
   THEN go to MORE-PRIVILEGE
   ELSE go to SAME-PRIVILEGE
   FI;

MORE-PRIVILEGE:
   Get new SS selector for new privilege level from TSS
      Check selector and descriptor for new SS:
         Selector must not be null ELSE #TS(0)
         Selector index must be within its descriptor
            table limits ELSE #TS(SS selector)
         Selector's RPL must equal DPL of code segment
            ELSE #TS(SS selector)
         Stack segment DPL must equal DPL of code
            segment ELSE #TS(SS selector)
         Descriptor must indicate writable data segment
            ELSE #TS(SS selector)
         Segment present ELSE #SS(SS selector)
      IF OperandSize=32
      THEN
         New stack must have room for parameters plus 16 bytes
            ELSE #SS(0)
         EIP must be in code segment limit ELSE #GP(0)
         Load new SS:eSP value from TSS
         Load new CS:EIP value from gate
      ELSE
         New stack must have room for parameters plus 8 bytes ELSE #SS(0)
         IP must be in code segment limit ELSE #GP(0)
         Load new SS:eSP value from TSS
         Load new CS:IP value from gate
      FI;
      Load CS descriptor
      Load SS descriptor
      Push long pointer of old stack onto new stack
      Get word count from call gate, mask to 5 bits
      Copy parameters from old stack onto new stack
      Push return address onto new stack
      Set CPL to stack segment DPL
      Set RPL of CS to CPL

SAME-PRIVILEGE:
   IF OperandSize=32
   THEN
      Stack must have room for 6-byte return address (padded to 8 bytes)
         ELSE #SS(0)
      EIP must be within code segment limit ELSE #GP(0)
      Load CS:EIP from gate
   ELSE
      Stack must have room for 4-byte return address ELSE #SS(0)
      IP must be within code segment limit ELSE #GP(0)
      Load CS:IP from gate
   FI;
   Push return address onto stack
   Load code segment descriptor into CS register
   Set RPL of CS to CPL

TASK-GATE:
   Task gate DPL must be >= CPL ELSE #TS(gate selector)
   Task gate DPL must be >= RPL ELSE #TS(gate selector)
   Task Gate must be present ELSE #NP(gate selector)
   Examine selector to TSS, given in Task Gate descriptor:
      Must specify global in the local/global bit ELSE #TS(TSS selector)
      Index must be within GDT limits ELSE #TS(TSS selector)
      TSS descriptor AR byte must specify nonbusy TSS
         ELSE #TS(TSS selector)
      Task State Segment must be present ELSE #NP(TSS selector)
   SWITCH-TASKS (with nesting) to TSS
   IP must be in code segment limit ELSE #TS(0)

TASK-STATE-SEGMENT:
   TSS DPL must be >= CPL else #TS(TSS selector)
   TSS DPL must be >= RPL ELSE #TS(TSS selector)
   TSS descriptor AR byte must specify available TSS
      ELSE #TS(TSS selector)
   Task State Segment must be present ELSE #NP(TSS selector)
   SWITCH-TASKS (with nesting) to TSS
   IP must be in code segment limit ELSE #TS(0)
```

## 说明

把返回地址压栈，并把控制转移到过程入口。近调用保存 EIP/IP；远调用还保存 CS。

## 影响的标志

若发生任务切换则影响所有标志；若不发生任务切换则不影响任何标志。

## 保护模式异常

- 远调用：#GP、#NP、#SS 和 #TS，条件见上表。
- 近直接调用：若过程位置超出代码段界限，产生 #GP(0)。
- #SS(0)：压入返回地址时超出栈段界限。
- #PF(fault-code)：页错误。近间接调用：#GP(0)：CS、DS、ES、FS 或 GS 段中的内存操作数有效地址非法。
- #SS(0)：SS 段中的地址非法。
- #GP(0)：取得的间接偏移超出代码段界限。
- #PF(fault-code)：页错误。


## 实地址模式异常

中断 13：操作数的任何部分超出 0–0FFFFH 的有效地址空间。


## 虚拟 8086 模式异常

与实地址模式相同；#PF(fault-code)：页错误。

