---
id: BSR
title: 反向位扫描
en: Bit Scan Reverse
group: B
page: 266
---

# BSR -- 反向位扫描

## 操作码

```
Opcode    Instruction          Clocks    Description

0F  BD    BSR r16,r/m16        10+3n     Bit scan reverse on r/m word
0F  BD    BSR r32,r/m32        10+3n     Bit scan reverse on r/m dword
```

## 操作

```
IF r/m = 0
THEN
   ZF := 1;
   register := UNDEFINED;
ELSE
   temp := OperandSize - 1;
   ZF := 0;
   WHILE BIT[r/m, temp] = 0
   DO
      temp := temp - 1;
      register := temp;
   OD;
FI;
```

## 说明

从高位向低位扫描源操作数，把第一个置位位的索引写入目的寄存器；若源为零则清零 ZF，目的值未定义。

## 影响的标志

ZF，如上述。

## 保护模式异常

- #GP(0)：结果位于不可写段。
- #GP(0)：CS、DS、ES、FS 或 GS 段中的内存操作数有效地址非法。
- #SS(0)：SS 段中的地址非法。
- #PF(fault-code)：页错误。


## 实地址模式异常

中断 13：操作数的任何部分超出 0–0FFFFH 的有效地址空间。


## 虚拟 8086 模式异常

与实地址模式相同；#PF(fault-code)：页错误。

