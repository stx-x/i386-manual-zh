---
id: OUT
title: 输出到端口
en: Output to Port
group: O
page: 358
---

# OUT -- 输出到端口

## 操作码

```
Opcode    Instruction     Clocks          Description

E6  ib    OUT imm8,AL     10,pm=4*/24**   Output byte AL to immediate port
                                          number
E7  ib    OUT imm8,AX     10,pm=4*/24**   Output word AL to immediate port
                                          number
E7  ib    OUT imm8,EAX    10,pm=4*/24**   Output dword AL to immediate
                                          port number
EE        OUT DX,AL       11,pm=5*/25**   Output byte AL to port number in
DX
EF        OUT DX,AX       11,pm=5*/25**   Output word AL to port number in
DX
EF        OUT DX,EAX      11,pm=5*/25**   Output dword AL to port number
                                          in DX
```

## 操作

```
IF (PE = 1) AND ((VM = 1) OR (CPL > IOPL))
THEN (* Virtual 8086 mode, or protected mode with CPL > IOPL *)
   IF NOT I-O-Permission (DEST, width(DEST))
   THEN #GP(0);
   FI;
FI;
[DEST] := SRC; (* I/O address space used *)
```

## 说明

把 AL、AX 或 EAX 中的字节、字或双字写入 I/O 端口；端口可由立即数或 DX 指定。

## 影响的标志

无。

## 保护模式异常（原文）

::: note
#GP(0) if the current privilege level is higher (has less privilege) than IOPL and any of the corresponding I/O permission bits in TSS equals 1
:::

## 实地址模式异常（原文）

::: note
None
:::

## 虚拟 8086 模式异常（原文）

::: note
#GP(0) fault if any of the corresponding I/O permission bits in TSS equals 1
:::
