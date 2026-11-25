---
id: SCAS
title: 扫描串数据
en: Compare String Data
group: S
---

# SCAS -- 扫描串数据

## 操作码

```
Opcode  Instruction  Clocks  Description

AE      SCAS m8      7       Compare bytes AL-ES:[DI], update (E)DI
AF      SCAS m16     7       Compare words AX-ES:[DI], update (E)DI
AF      SCAS m32     7       Compare dwords EAX-ES:[DI], update (E)DI
AE      SCASB        7       Compare bytes AL-ES:[DI], update (E)DI
AF      SCASW        7       Compare words AX-ES:[DI], update (E)DI
AF      SCASD        7       Compare dwords EAX-ES:[DI], update (E)DI
```

## 操作

```
IF AddressSize = 16
THEN use DI for dest-index;
ELSE (* AddressSize = 32 *) use EDI for dest-index;
FI;
IF byte type of instruction
THEN
   AL - [dest-index]; (* Compare byte in AL and dest *)
   IF DF = 0 THEN IndDec := 1 ELSE IncDec := -1; FI;
ELSE
   IF OperandSize = 16
   THEN
      AX - [dest-index]; (* compare word in AL and dest *)
      IF DF = 0 THEN IncDec := 2 ELSE IncDec := -2; FI;
   ELSE (* OperandSize = 32 *)
      EAX - [dest-index];(* compare dword in EAX & dest *)
      IF DF = 0 THEN IncDec := 4 ELSE IncDec := -4; FI;
   FI;
FI;
dest-index := dest-index + IncDec
```

## 说明

用 AL、AX 或 EAX 减去 ES:EDI 处的串元素并更新标志；可配合 REPE/REPNE 查找匹配。

## 影响的标志

OF、SF、ZF、AF、PF、CF，按附录 C 所述。

## 保护模式异常

- #GP(0)：CS、DS、ES、FS 或 GS 段中的内存操作数有效地址非法。
- #SS(0)：SS 段中的地址非法。
- #PF(fault-code)：页错误。


## 实地址模式异常

中断 13：操作数的任何部分超出 0–0FFFFH 的有效地址空间。


## 虚拟 8086 模式异常

与实地址模式相同；#PF(fault-code)：页错误。

