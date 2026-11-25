# MOV -- Move to/from Special Registers

```
Opcode      Instruction           Clocks   Description

0F  20 /r   MOV r32,CR0/CR2/CR3   6        Move (control register) to
                                           (register)
0F  22 /r   MOV CR0/CR2/CR3,r32   10/4/5   Move (register) to (control
                                           register)
0F  21 /r   MOV r32,DR0 -- 3      22       Move (debug register) to
                                           (register)
0F  21 /r   MOV r32,DR6/DR7       14       Move (debug register) to
                                           (register)
0F  23 /r   MOV DR0 -- 3,r32      22       Move (register) to (debug
                                           register)
0F  23 /r   MOV DR6/DR7,r32       16       Move (register) to (debug
                                           register)
0F  24 /r   MOV r32,TR6/TR7       12       Move (test register) to
                                           (register)
0F  26 /r   MOV TR6/TR7,r32       12       Move (register) to (test
                                           register)
```

## Operation

```
DEST := SRC;
```

## Description

The above forms of MOV store or load the following special registers in or from a general purpose register:

- Control registers CR0, CR2, and CR3

- Debug Registers DR0, DR1, DR2, DR3, DR6, and DR7

- Test Registers TR6 and TR7

32-bit operands are always used with these instructions, regardless of the operand-size attribute.

## Flags Affected

OF, SF, ZF, AF, PF, and CF are undefined

## Protected Mode Exceptions

#GP(0) if the current privilege level is not 0

## Real Address Mode Exceptions

None

## Virtual 8086 Mode Exceptions

#GP(0) if instruction execution is attempted

## Notes

The instructions must be executed at privilege level 0 or in real-address mode; otherwise, a protection exception will be raised.

The reg field within the ModRM byte specifies which of the special registers in each category is involved. The two bits in the field are always 11. The r/m field specifies the general register involved.
