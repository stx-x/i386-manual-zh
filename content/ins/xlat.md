---
id: XLAT
title: 查表转换
en: Table Look-up Translation
group: X
---

# XLAT -- 查表转换

## 操作码

```
D7    XLAT m8    5     Set AL to memory byte DS:[(E)BX + unsigned AL]
D7    XLATB      5     Set AL to memory byte DS:[(E)BX + unsigned AL]
```

## 操作

```
IF AddressSize = 16
THEN
   AL := (BX + ZeroExtend(AL))
ELSE (* AddressSize = 32 *)
   AL := (EBX + ZeroExtend(AL));
FI;
```

## 说明

用 AL 作为索引，从 EBX 所指的 256 字节表中取出字节替换 AL。

## 影响的标志

无。

## 保护模式异常

- #GP(0)：CS、DS、ES、FS 或 GS 段中的内存操作数有效地址非法。
- #SS(0)：SS 段中的地址非法。
- #PF(fault-code)：页错误。


## 实地址模式异常

中断 13：操作数的任何部分超出 0–0FFFFH 的有效地址空间。


## 虚拟 8086 模式异常

与实地址模式相同；#PF(fault-code)：页错误。

