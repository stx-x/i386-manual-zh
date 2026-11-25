---
id: BOUND
title: 检查数组下标是否越界
en: Check Array Index Against Bounds
group: B
page: 264
---

# BOUND -- 检查数组下标是否越界

## 操作码

```
Opcode    Instruction          Clocks    Description

62 /r     BOUND r16,m16&16     10        Check if r16 is within bounds
                                         (passes test)
62 /r     BOUND r32,m32&32     10        Check if r32 is within bounds
                                         (passes test)
```

## 操作

```
IF (LeftSRC < [RightSRC] OR LeftSRC > [RightSRC + OperandSize/8])
   (* Under lower bound or over upper bound *)
THEN Interrupt 5;
FI;
```

## 说明

检查寄存器中的有符号下标是否落在内存中相邻存放的下界与上界之间；越界则产生异常 5。

## 影响的标志

无。

## 保护模式异常

- 中断 5：界限检查失败，如上文所述。
- #GP(0)：CS、DS、ES、FS 或 GS 段中的内存操作数有效地址非法。
- #SS(0)：SS 段中的地址非法。
- #PF(fault-code)：页错误。
- 第二操作数必须是内存操作数，不能是寄存器。若执行 BOUND 时 ModR/M 字节把第二操作数表示为寄存器，产生 #UD。


## 实地址模式异常

- 中断 5：界限检查失败。
- 中断 13：操作数的任何部分超出 0–0FFFFH 的有效地址空间。
- 中断 6：第二操作数为寄存器。


## 虚拟 8086 模式异常

与实地址模式相同；#PF(fault-code)：页错误。

