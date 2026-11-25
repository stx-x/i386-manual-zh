---
id: LAHF
title: 把标志装入 AH
en: Load Flags into AH Register
group: L
page: 324
---

# LAHF -- 把标志装入 AH

## 操作码

```
Opcode  Instruction   Clocks   Description

9F      LAHF          2        Load: AH := flags SF ZF xx AF xx PF xx CF
```

## 操作

```
AH := SF:ZF:xx:AF:xx:PF:xx:CF;
```

## 说明

把 SF、ZF、AF、PF、CF 分别复制到 AH 的位 7、6、4、2、0。

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
