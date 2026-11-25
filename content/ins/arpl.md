---
id: ARPL
title: 调整选择子的 RPL 字段
en: Adjust RPL Field of Selector
group: A
page: 263
---

# ARPL -- 调整选择子的 RPL 字段

## 操作码

```
Opcode    Instruction          Clocks    Description

63 /r     ARPL r/m16,r16       pm=20/21  Adjust RPL of r/m16 to not
                                         less than RPL of r16
```

## 操作

```
IF RPL bits(0,1) of DEST < RPL bits(0,1) of SRC
THEN
   ZF := 1;
   RPL bits(0,1) of DEST := RPL bits(0,1) of SRC;
ELSE
   ZF := 0;
FI;
```

## 说明

若目的操作数（选择子）的 RPL 小于源操作数的 RPL，则把目的 RPL 提升为源 RPL 并置位 ZF；否则清零 ZF。用于指针完整性检查。

## 影响的标志

ZF，如上述。

## 保护模式异常（原文）

::: note
#GP(0) if the result is in a nonwritable segment; #GP(0) for an illegal memory operand effective address in the CS, DS, ES, FS, or GS segments; #SS(0) for an illegal address in the SS segment; #PF(fault-code) for a page fault
:::

## 实地址模式异常（原文）

::: note
Interrupt 6; ARPL is not recognized in Real Address Mode
:::

## 虚拟 8086 模式异常（原文）

::: note
Same exceptions as in Real Address Mode; #PF(fault-code) for a page fault
:::
