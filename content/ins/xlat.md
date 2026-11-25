---
id: XLAT
title: 查表转换
en: Table Look-up Translation
group: X
---

# XLAT -- 查表转换

## 操作码

```
D7    XLAT m8    5     Set AL to memory byte DS:[(E)BX + unsigned AL]
D7    XLATB      5     Set AL to memory byte DS:[(E)BX + unsigned AL]
```

## 操作

```
IF AddressSize = 16
THEN
   AL := (BX + ZeroExtend(AL))
ELSE (* AddressSize = 32 *)
   AL := (EBX + ZeroExtend(AL));
FI;
```

## 说明

用 AL 作为索引，从 EBX 所指的 256 字节表中取出字节替换 AL。

## 影响的标志

无。

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
