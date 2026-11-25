---
id: CMC
title: 进位标志求反
en: Complement Carry Flag
group: C
page: 286
---

# CMC -- 进位标志求反

## 操作码

```
Opcode    Instruction    Clocks   Description

F5        CMC            2        Complement carry flag
```

## 操作

```
CF := NOT CF;
```

## 说明

对 CF 取反。

## 影响的标志

CF，如上述。

## 保护模式异常

无。


## 实地址模式异常

无。


## 虚拟 8086 模式异常

无。

