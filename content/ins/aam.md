---
id: AAM
title: 乘法后的 ASCII 调整
en: ASCII Adjust AX after Multiply
group: A
page: 258
---

# AAM -- 乘法后的 ASCII 调整

## 操作码

```
Opcode    Instruction    Clocks    Description

D4 0A     AAM            17        ASCII adjust AX after multiply
```

## 操作

```
AH := AL / 10;
AL := AL MOD 10;
```

## 说明

调整两个非压缩 BCD 数相乘后 AX 中的结果：AH := AX DIV 10，AL := AX MOD 10，从而得到两位有效的非压缩十进制数。

## 影响的标志

SF、ZF、PF 按附录 C 所述；OF、AF、CF 未定义。

## 保护模式异常

无。


## 实地址模式异常

无。


## 虚拟 8086 模式异常

无。

