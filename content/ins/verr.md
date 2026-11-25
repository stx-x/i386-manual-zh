---
id: VERR
title: 验证段是否可读/可写
en: Verify a Segment for Reading or Writing
group: V
---

# VERR -- 验证段是否可读/可写

## 操作码

```
Opcode       Instruction   Clocks      Description

0F  00 /4    VERR r/m16    pm=10/11    Set ZF=1 if segment can be read,
                                       selector in r/m16
0F  00 /5    VERW r/m16    pm=15/16    Set ZF=1 if segment can be written,
                                       selector in r/m16
```

## 操作

```
IF segment with selector at (r/m) is accessible
   with current protection level
   AND ((segment is readable for VERR) OR
      (segment is writable for VERW))
THEN ZF := 0;
ELSE ZF := 1;
FI;
```

## 说明

检查选择子所指段在当前特权级能否读（VERR）或写（VERW）；结果反映在 ZF 中，不产生保护异常。

## 影响的标志

ZF，如上述。

## 保护模式异常

- 若包含选择子的内存操作数寻址非法，选择子不会被装入任何段寄存器，也不会产生归因于该选择子操作数的故障。
- #GP(0)：CS、DS、ES、FS 或 GS 段中的内存操作数有效地址非法。
- #SS(0)：SS 段中的地址非法。
- #PF(fault-code)：页错误。


## 实地址模式异常

中断 6；实地址模式不识别 VERR 和 VERW。


## 虚拟 8086 模式异常

与实地址模式相同；#PF(fault-code)：页错误。

