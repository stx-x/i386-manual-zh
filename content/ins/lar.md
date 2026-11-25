---
id: LAR
title: 装入访问权字节
en: Load Access Rights Byte
group: L
page: 325
---

# LAR -- 装入访问权字节

## 操作码

```
Opcode        Instruction      Clocks      Description

0F  02 /r     LAR r16,r/m16    pm=15/16    r16 := r/m16 masked by FF00
0F  02 /r     LAR r32,r/m32    pm=15/16    r32 := r/m32 masked by 00FxFF00
```

## 说明

若选择子所指描述符在当前特权级可见，则把其访问权字段装入目的寄存器并置位 ZF；否则清零 ZF。

## 影响的标志

ZF，如上述。

## 保护模式异常（原文）

::: note
#GP(0) for an illegal memory operand effective address in the CS, DS, ES, FS, or GS segments; #SS(0) for an illegal address in the SS segment; #PF(fault-code) for a page fault
:::

## 实地址模式异常（原文）

::: note
Interrupt 6; LAR is unrecognized in Real Address Mode
:::

## 虚拟 8086 模式异常（原文）

::: note
Same exceptions as in Real Address Mode
:::
