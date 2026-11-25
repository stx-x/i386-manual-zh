---
id: CWD
title: 字转换为双字 / 双字转换为四字
en: Convert Word to Doubleword/Convert Doubleword to
group: C
---

# CWD -- 字转换为双字 / 双字转换为四字

## 操作码

```
Opcode    Instruction        Clocks   Description

99        CWD                2        DX:AX := sign-extend of AX
99        CDQ                2        EDX:EAX := sign-extend of EAX
```

## 操作

```
IF OperandSize = 16 (* CWD instruction *)
THEN
   IF AX < 0 THEN DX := 0FFFFH; ELSE DX := 0; FI;
ELSE (* OperandSize = 32, CDQ instruction *)
   IF EAX < 0 THEN EDX := 0FFFFFFFFH; ELSE EDX := 0; FI;
FI;
```

## 说明

CWD 把 AX 的符号扩展到 DX:AX；CDQ 把 EAX 的符号扩展到 EDX:EAX，用于产生双倍长度的被除数。

## 影响的标志

无。

## 保护模式异常（原文）

::: note
None
:::

## 实地址模式异常（原文）

::: note
None
:::

## 虚拟 8086 模式异常（原文）

::: note
None
:::
