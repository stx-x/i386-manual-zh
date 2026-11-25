---
id: CBW
title: 字节转换为字 / 字转换为双字
en: Convert Byte to Word/Convert Word to Doubleword
group: C
---

# CBW -- 字节转换为字 / 字转换为双字

## 操作码

```
Opcode    Instruction     Clocks          Description

98        CBW             3               AX := sign-extend of AL
98        CWDE            3               EAX := sign-extend of AX
```

## 操作

```
IF OperandSize = 16 (* instruction = CBW *)
THEN AX := SignExtend(AL);
ELSE (* OperandSize = 32, instruction = CWDE *)
   EAX := SignExtend(AX);
FI;
```

## 说明

CBW 把 AL 的符号扩展到 AX；CWDE 把 AX 的符号扩展到 EAX。用于产生除法所需的双倍长度操作数。

## 影响的标志

无。

## 保护模式异常

无。


## 实地址模式异常

无。


## 虚拟 8086 模式异常

无。

