---
id: IN
title: 从端口输入
en: Input from Port
group: I
page: 302
---

# IN -- 从端口输入

## 操作码

```
Opcode    Instruction   Clocks            Description

E4  ib    IN AL,imm8    12,pm=6*/26**     Input byte from immediate port
                                          into AL
E5  ib    IN AX,imm8    12,pm=6*/26**     Input word from immediate port
                                          into AX
E5  ib    IN EAX,imm8   12,pm=6*/26**     Input dword from immediate port
                                          into EAX
EC        IN AL,DX      13,pm=7*/27**     Input byte from port DX into AL
ED        IN AX,DX      13,pm=7*/27**     Input word from port DX into AX
ED        IN EAX,DX     13,pm=7*/27**     Input dword from port DX into
                                          EAX
```

## 操作

```
IF (PE = 1) AND ((VM = 1) OR (CPL > IOPL))
THEN (* Virtual 8086 mode, or protected mode with CPL > IOPL *)
   IF NOT I-O-Permission (SRC, width(SRC))
   THEN #GP(0);
   FI;
FI;
DEST := [SRC]; (* Reads from I/O address space *)
```

## 说明

从 I/O 端口读取字节、字或双字到 AL、AX 或 EAX；端口可由立即数或 DX 指定。

## 影响的标志

无。

## 保护模式异常（原文）

::: note
#GP(0) if the current privilege level is larger (has less privilege) than IOPL and any of the corresponding I/O permission bits in TSS equals 1
:::

## 实地址模式异常（原文）

::: note
None
:::

## 虚拟 8086 模式异常（原文）

::: note
#GP(0) fault if any of the corresponding I/O permission bits in TSS equals 1
:::
