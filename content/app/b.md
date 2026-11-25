---
id: b
letter: B
title: 标志位交叉引用
en: Complete Flag Cross-Reference
desc: 每条指令对每个标志位的影响一览。
page: 417
---

# 附录 B　标志位交叉引用

## 代码含义

```
T     = 指令测试该标志
M     = 指令修改该标志（置位或复位取决于操作数）
0     = 指令复位该标志
1     = 指令置位该标志
--    = 指令对该标志的影响未定义
R     = 指令恢复该标志的先前值
（空白）= 指令不影响该标志
```

```
Instruction            OF   SF   ZF   AF   PF   CF   TF   IF   DF   NT   RF

AAA                    --   --   --   TM   --   M
AAD                    --   M    M    --   M    --
AAM                    --   M    M    --   M    --
AAS                    --   --   --   TM   --   M
ADC                    M    M    M    M    M    TM
ADD                    M    M    M    M    M    M
AND                    0    M    M    --   M    0
ARPL                             M
BOUND
BSF/BSR                --   --   M    --   --   --
BT/BTS/BTR/BTC         --   --   --   --   --   M
CALL
CBW
CLC                                             0
CLD                                                            0
CLI                                                       0
CLTS
CMC                                             M
CMP                    M    M    M    M    M    M
CMPS                   M    M    M    M    M    M              T
CWD
DAA                    --   M    M    TM   M    TM
DAS                    --   M    M    TM   M    TM
DEC                    M    M    M    M    M
DIV                    --   --   --   --   --   --
ENTER
ESC
HLT
IDIV                   --   --   --   --   --   --
IMUL                   M    --   --   --   --   M
IN
INC                    M    M    M    M    M
INS                                                            T
INT                                                  0              0
INTO                   T                             0              0
IRET                   R    R    R    R    R    R    R    R    R    T
Jcond                  T    T    T    T    T
JCXZ
JMP
LAHF
LAR                              M
LDS/LES/LSS/LFS/LGS
LEA
LEAVE
LGDT/LIDT/LLDT/LMSW
LOCK
LODS                                                           T
LOOP
LOOPE/LOOPNE                     T
LSL                              M
LTR
MOV
MOV control, debug     --   --   --   --   --   --
MOVS                                                           T
MOVSX/MOVZX
MUL                    M    --   --   --   --   M
NEG                    M    M    M    M    M    M
NOP
NOT
OR                     0    M    M    --   M    0
OUT
OUTS                                                           T
POP/POPA
POPF                   R    R    R    R    R    R    R    R    R    R
PUSH/PUSHA/PUSHF
RCL/RCR 1              M                        TM
RCL/RCR count          --                       TM
REP/REPE/REPNE
RET
ROL/ROR 1              M                        M
ROL/ROR count          --                       M
SAHF                        R    R    R    R    R
SAL/SAR/SHL/SHR 1      M    M    M    --   M    M
SAL/SAR/SHL/SHR count  --   M    M    --   M    M
SBB                    M    M    M    M    M    TM
SCAS                   M    M    M    M    M    M              T
SET cond               T    T    T         T    T
SGDT/SIDT/SLDT/SMSW
SHLD/SHRD              --   M    M    --   M    M
STC                                             1
STD                                                            1
STI                                                       1
STOS                                                           T
STR
SUB                    M    M    M    M    M    M
TEST                   0    M    M    --   M    0
VERR/VERRW                       M
WAIT
XCHG
XLAT
XOR                    0    M    M    --   M    0
```
