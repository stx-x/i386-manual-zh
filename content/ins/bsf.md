---
id: BSF
title: 向前位扫描
en: Bit Scan Forward
group: B
page: 265
---

# BSF -- 向前位扫描

## 操作码

```
Opcode    Instruction          Clocks    Description

0F  BC    BSF r16,r/m16        10+3n     Bit scan forward on r/m word
0F  BC    BSF r32,r/m32        10+3n     Bit scan forward on r/m dword
```

## 操作

```
IF r/m = 0
THEN
   ZF := 1;
   register := UNDEFINED;
ELSE
   temp := 0;
   ZF := 0;
   WHILE BIT[r/m, temp = 0]
   DO
      temp := temp + 1;
      register := temp;
   OD;
FI;
```

## 说明

从低位向高位扫描源操作数，把第一个置位位的索引写入目的寄存器；若源为零则清零 ZF，目的值未定义。

## 影响的标志

ZF，如上述。

## 保护模式异常（原文）

::: note
#GP(0) for an illegal memory operand effective address in the CS, DS, ES, FS, or GS segments; #SS(0) for an illegal address in the SS segment; #PF(fault-code) for a page fault
:::

## 实地址模式异常（原文）

::: note
Interrupt 13 if any part of the operand would lie outside of the effective address space from 0 to 0FFFFH
:::

## 虚拟 8086 模式异常（原文）

::: note
Same exceptions as in Real Address Mode; #PF(fault-code) for a page fault
:::
