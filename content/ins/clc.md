---
id: CLC
title: 清进位标志
en: Clear Carry Flag
group: C
page: 282
---

# CLC -- 清进位标志

## 操作码

```
Opcode    Instruction     Clocks          Description

F8        CLC             2               Clear carry flag
```

## 操作

```
CF := 0;
```

## 说明

清零 CF。

## 影响的标志

CF := 0。

## 保护模式异常

无。


## 实地址模式异常

无。


## 虚拟 8086 模式异常

无。

