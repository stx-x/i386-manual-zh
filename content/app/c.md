---
id: c
letter: C
title: 状态标志汇总
en: Status Flag Summary
desc: 六个状态标志的位置、含义与设置规则。
page: 419
---

# 附录 C　状态标志汇总

## 状态标志的功能

| 位 | 名称 | 功能 |
|---|---|---|
| 0 | CF | 进位标志：最高位产生进位或借位时置位，否则清零。 |
| 2 | PF | 奇偶标志：结果的低 8 位含偶数个 1 时置位，否则清零。 |
| 4 | AF | 调整标志：AL 低 4 位产生进位或借位时置位，否则清零；用于十进制算术。 |
| 6 | ZF | 零标志：结果为零时置位，否则清零。 |
| 7 | SF | 符号标志：等于结果最高位（0 为正，1 为负）。 |
| 11 | OF | 溢出标志：结果作为有符号数太大或太小（不含符号位）而无法放入目的操作数时置位，否则清零。 |

## 代码含义

```
T     = 指令测试该标志
M     = 指令修改该标志（置位或复位取决于操作数）
0     = 指令复位该标志
--    = 指令对该标志的影响未定义
（空白）= 指令不影响该标志
```

```
Instruction            OF   SF   ZF   AF   PF   CF
AAA                    --   --   --   TM   --   M
AAS                    --   --   --   TM   --   M
AAD                    --   M    M    --   M    --
AAM                    --   M    M    --   M    --
DAA                    --   M    M    TM   M    TM
DAS                    --   M    M    TM   M    TM
ADC                    M    M    M    M    M    TM
ADD                    M    M    M    M    M    M
SBB                    M    M    M    M    M    TM
SUB                    M    M    M    M    M    M
CMP                    M    M    M    M    M    M
CMPS                   M    M    M    M    M    M
SCAS                   M    M    M    M    M    M
NEG                    M    M    M    M    M    M
DEC                    M    M    M    M    M
INC                    M    M    M    M    M
IMUL                   M    --   --   --   --   M
MUL                    M    --   --   --   --   M
RCL/RCR 1              M                        TM
RCL/RCR count          --                       TM
ROL/ROR 1              M                        M
ROL/ROR count          --                       M
SAL/SAR/SHL/SHR 1      M    M    M    --   M    M
SAL/SAR/SHL/SHR count  --   M    M    --   M    M
SHLD/SHRD              --   M    M    --   M    M
BSF/BSR                --   --   M    --   --   --
BT/BTS/BTR/BTC         --   --   --   --   --   M
AND                    0    M    M    --   M    0
OR                     0    M    M    --   M    0
TEST                   0    M    M    --   M    0
XOR                    0    M    M    --   M    0
```
