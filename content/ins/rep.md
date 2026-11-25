---
id: REP
title: 重复后续串操作
en: Repeat Following String Operation
group: R
---

# REP -- 重复后续串操作

## 操作码

```
Opcode    Instruction         Clocks          Description

F3  6C    REP INS r/m8, DX    13+6*(E)CX,
                              pm=7+6*(E)CX
If CPL <= IOPL/
                              27+6*(E)CX
If CPL > IOPL or if in virtual 8086 mode      Input (E)CX bytes from port
                                               DX into ES:[(E)DI]
F3  6D    REP INS r/m16,DX    13+6*(E)CX,
                              pm=7+6*(E)CX
If CPL <= IOPL/
                              27+6*(E)CX
If CPL > IOPL or if in virtual 8086 mode      Input (E)CX words from port
                                               DX into ES:[(E)DI]
F3  6D    REP INS r/m32,DX    13+6*(E)CX,
                              pm=7+6*(E)CX
If CPL <= IOPL/
                              27+6*(E)CX
If CPL > IOPL or if in virtual 8086 mode      Input (E)CX dwords from port
                                               DX into ES:[(E)DI]
F3  A4    REP MOVS m8,m8      5+4*(E)CX        Move (E)CX bytes from
                                               [(E)SI] to ES:[(E)DI]
F3  A5    REP MOVS m16,m16    5+4*(E)CX        Move (E)CX words from
                                               [(E)SI] to ES:[(E)DI]
F3  A5    REP MOVS m32,m32    5+4*(E)CX        Move (E)CX dwords from
                                               [(E)SI] to ES:[(E)DI]
F3  6E    REP OUTS DX,r/m8    5+12*(E)CX,
                              pm=6+5*(E)CX
If CPL <= IOPL/
                              26+5*(E)CX
If CPL > IOPL or if in virtual 8086 mode      Output (E)CX bytes from
                                               [(E)SI] to port DX
F3  6F    REP OUTS DX,r/m16   5+12*(E)CX,
                              pm=6+5*(E)CX
If CPL <= IOPL/
                              26+5*(E)CX
If CPL > IOPL or if in virtual 8086 mode      Output (E)CX words from
                                               [(E)SI] to port DX
F3  6F    REP OUTS DX,r/m32   5+12*(E)CX,
                              pm=6+5*(E)CX
If CPL <= IOPL/
                              26+5*(E)CX
If CPL > IOPL or if in virtual 8086 mode      Output (E)CX dwords from
                                               [(E)SI] to port DX
F3  AA    REP STOS m8         5+5*(E)CX        Fill (E)CX bytes at
                                               ES:[(E)DI] with AL
F3  AB    REP STOS m16        5+5*(E)CX        Fill (E)CX words at
                                               ES:[(E)DI] with AX
F3  AB    REP STOS m32        5+5*(E)CX        Fill (E)CX dwords at
                                               ES:[(E)DI] with EAX
F3  A6    REPE CMPS m8,m8     5+9*N            Find nonmatching bytes in
                                               ES:[(E)DI] and [(E)SI]
F3  A7    REPE CMPS m16,m16   5+9*N            Find nonmatching words in
                                               ES:[(E)DI] and [(E)SI]
F3  A7    REPE CMPS m32,m32   5+9*N            Find nonmatching dwords in
                                               ES:[(E)DI] and [(E)SI]
F3  AE    REPE SCAS m8        5+8*N            Find non-AL byte starting
                                               at ES:[(E)DI]
F3  AF    REPE SCAS m16       5+8*N            Find non-AX word starting
                                               at ES:[(E)DI]
F3  AF    REPE SCAS m32       5+8*N            Find non-EAX dword starting
                                               at ES:[(E)DI]
F2  A6    REPNE CMPS m8,m8    5+9*N            Find matching bytes in
                                               ES:[(E)DI] and [(E)SI]
F2  A7    REPNE CMPS m16,m16  5+9*N            Find matching words in
                                               ES:[(E)DI] and [(E)SI]
F2  A7    REPNE CMPS m32,m32  5+9*N            Find matching dwords in
                                               ES:[(E)DI] and [(E)SI]
F2  AE    REPNE SCAS m8       5+8*N            Find AL, starting at
                                               ES:[(E)DI]
F2  AF    REPNE SCAS m16      5+8*N            Find AX, starting at
                                               ES:[(E)DI]
F2  AF    REPNE SCAS m32      5+8*N            Find EAX, starting at
                                               ES:[(E)DI]
```

## 操作

```
IF AddressSize = 16
THEN use CX for CountReg;
ELSE (* AddressSize = 32 *) use ECX for CountReg;
FI;
WHILE CountReg <> 0
DO
   service pending interrupts (if any);
   perform primitive string instruction;
   CountReg := CountReg - 1;
   IF primitive operation is CMPB, CMPW, SCAB, or SCAW
   THEN
      IF (instruction is REP/REPE/REPZ) AND (ZF=1)
      THEN exit WHILE loop
      ELSE
         IF (instruction is REPNZ or REPNE) AND (ZF=0)
         THEN exit WHILE loop;
         FI;
      FI;
   FI;
OD;
```

## 说明

重复执行随后的串指令直到 ECX=0；REPE/REPZ 还在 ZF=0 时停止，REPNE/REPNZ 在 ZF=1 时停止。

## 影响的标志

ZF 由 REP CMPS 与 REP SCAS 按上述方式设置。

## 保护模式异常

#UD：在上文列表之外的指令前使用了重复前缀；执行串操作时还可能产生其他异常；参见各串指令自身的说明。


## 实地址模式异常

中断 6：在上文列表之外的指令前使用了重复前缀；执行串操作时还可能产生其他异常；参见各串指令自身的说明。


## 虚拟 8086 模式异常

#UD：在上文列表之外的指令前使用了重复前缀；执行串操作时还可能产生其他异常；参见各串指令自身的说明。

