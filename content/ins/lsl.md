---
id: LSL
title: 装入段界限
en: Load Segment Limit
group: L
page: 342
---

# LSL -- 装入段界限

## 操作码

```
Opcode       Instruction      Clocks      Description

0F  03 /r    LSL r16,r/m16    pm=20/21    Load: r16 := segment limit,
                                          selector r/m16 (byte granular)
0F  03 /r    LSL r32,r/m32    pm=20/21    Load: r32 := segment limit,
                                          selector r/m32 (byte granular)
0F  03 /r    LSL r16,r/m16    pm=25/26    Load: r16 := segment limit,
                                          selector r/m16 (page granular)
0F  03 /r    LSL r32,r/m32    pm=25/26    Load: r32 := segment limit,
                                          selector r/m32 (page granular)
```

## 说明

若选择子所指描述符可见，则把按字节粒度还原的 32 位段界限装入目的寄存器并置位 ZF。

## 影响的标志

ZF，如上述。

## 保护模式异常

- #GP(0)：CS、DS、ES、FS 或 GS 段中的内存操作数有效地址非法。
- #SS(0)：SS 段中的地址非法。
- #PF(fault-code)：页错误。


## 实地址模式异常

中断 6；实地址模式不识别 LSL。


## 虚拟 8086 模式异常

与实地址模式相同。

