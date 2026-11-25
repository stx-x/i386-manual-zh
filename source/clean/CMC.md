# CMC -- Complement Carry Flag

```
Opcode    Instruction    Clocks   Description

F5        CMC            2        Complement carry flag
```

## Operation

```
CF := NOT CF;
```

## Description

CMC reverses the setting of the carry flag. No other flags are affected.

## Flags Affected

CF as described above

## Protected Mode Exceptions

None

## Real Address Mode Exceptions

None

## Virtual 8086 Mode Exceptions

None
