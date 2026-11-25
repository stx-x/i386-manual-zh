---
id: SAHF
title: 把 AH 存入标志
en: Store AH into Flags
group: S
page: 382
---

# SAHF -- 把 AH 存入标志

## 操作码

```
Opcode  Instruction  Clocks   Description

9E      SAHF         3        Store AH into flags SF ZF xx AF xx PF xx CF
```

## 操作

```
SF:ZF:xx:AF:xx:PF:xx:CF := AH;
```

## 说明

把 AH 的位 7、6、4、2、0 分别装入 SF、ZF、AF、PF、CF。

## 影响的标志

SF、ZF、AF、PF、CF 如上述。

## 保护模式异常

无。


## 实地址模式异常

无。


## 虚拟 8086 模式异常

无。

