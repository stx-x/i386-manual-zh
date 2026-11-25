---
id: XCHG
title: 寄存器/内存与寄存器交换
en: Exchange Register/Memory with Register
group: X
page: 409
---

# XCHG -- 寄存器/内存与寄存器交换

## 操作码

```
Opcode    Instruction      Clocks     Description

90 + r    XCHG AX,r16      3          Exchange word register with AX
90 + r    XCHG r16,AX      3          Exchange word register with AX
90 + r    XCHG EAX,r32     3          Exchange dword register with EAX
90 + r    XCHG r32,EAX     3          Exchange dword register with EAX
86  /r    XCHG r/m8,r8     3          Exchange byte register with EA byte
86  /r    XCHG r8,r/m8     3/5        Exchange byte register with EA byte
87  /r    XCHG r/m16,r16   3          Exchange word register with EA word
87  /r    XCHG r16,r/m16   3/5        Exchange word register with EA word
87  /r    XCHG r/m32,r32   3          Exchange dword register with EA dword
87  /r    XCHG r32,r/m32   3/5        Exchange dword register with EA dword
```

## 操作

```
temp := DEST
DEST := SRC
SRC := temp
```

## 说明

交换两个操作数的内容；引用内存时自动断言 LOCK。

## 影响的标志

无。

## 保护模式异常

- #GP(0)：任一操作数位于不可写段。
- #GP(0)：CS、DS、ES、FS 或 GS 段中的内存操作数有效地址非法。
- #SS(0)：SS 段中的地址非法。
- #PF(fault-code)：页错误。


## 实地址模式异常

中断 13：操作数的任何部分超出 0–0FFFFH 的有效地址空间。


## 虚拟 8086 模式异常

与实地址模式相同；#PF(fault-code)：页错误。

