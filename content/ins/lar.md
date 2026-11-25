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

## 保护模式异常

- #GP(0)：CS、DS、ES、FS 或 GS 段中的内存操作数有效地址非法。
- #SS(0)：SS 段中的地址非法。
- #PF(fault-code)：页错误。


## 实地址模式异常

中断 6；实地址模式不识别 LAR。


## 虚拟 8086 模式异常

与实地址模式相同。

