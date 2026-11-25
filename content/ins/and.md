---
id: AND
title: 逻辑与
en: Logical AND
group: A
page: 262
---

# AND -- 逻辑与

## 操作码

```
Opcode    Instruction          Clocks    Description

24 ib     AND AL,imm8          2         AND immediate byte to AL
25 iw     AND AX,imm16         2         AND immediate word to AX
25 id     AND EAX,imm32        2         AND immediate dword to EAX
80 /4 ib  AND r/m8,imm8        2/7       AND immediate byte to r/m byte
81 /4 iw  AND r/m16,imm16      2/7       AND immediate word to r/m word
81 /4 id  AND r/m32,imm32      2/7       AND immediate dword to r/m dword
83 /4 ib  AND r/m16,imm8       2/7       AND sign-extended immediate byte
                                         with r/m word
83 /4 ib  AND r/m32,imm8       2/7       AND sign-extended immediate byte
                                         with r/m dword
20 /r     AND r/m8,r8          2/7       AND byte register to r/m byte
21 /r     AND r/m16,r16        2/7       AND word register to r/m word
21 /r     AND r/m32,r32        2/7       AND dword register to r/m dword
22 /r     AND r8,r/m8          2/6       AND r/m byte to byte register
23 /r     AND r16,r/m16        2/6       AND r/m word to word register
23 /r     AND r32,r/m32        2/6       AND r/m dword to dword register
```

## 操作

```
DEST := DEST AND SRC;
CF := 0;
OF := 0;
```

## 说明

对两个操作数逐位做逻辑与，结果写入目的操作数；清零 OF 和 CF，AF 未定义，更新 SF、ZF、PF。

## 影响的标志

CF := 0，OF := 0；PF、SF、ZF 按附录 C 所述。

## 保护模式异常

- #GP(0)：结果位于不可写段。
- #GP(0)：CS、DS、ES、FS 或 GS 段中的内存操作数有效地址非法。
- #SS(0)：SS 段中的地址非法。
- #PF(fault-code)：页错误。


## 实地址模式异常

中断 13：操作数的任何部分超出 0–0FFFFH 的有效地址空间。


## 虚拟 8086 模式异常

与实地址模式相同；#PF(fault-code)：页错误。

