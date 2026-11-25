# 术语对照表

本表约定全书的关键译法。正文首次出现时以「中文（English）」标注，之后一般只用中文；寄存器名、指令助记符、操作码与描述符字段名保持原文。

## 存储与分段

| 英文 | 中文 | 说明 |
|---|---|---|
| segment | 段 | 一段连续的线性地址空间，由段描述符定义。 |
| segmentation | 分段 | 用段选择子与偏移形成线性地址的机制。 |
| descriptor | 描述符 | 描述段或门的 8 字节数据结构。 |
| selector | 选择子 | 16 位值，含索引、表指示位与 RPL，用于选择描述符。 |
| offset | 偏移 | 段内的字节位置。 |
| base address | 基地址 | 段在线性地址空间中的起点。 |
| limit | 界限 | 段内可访问的最后一个字节偏移；通常等于段长减一。 |
| granularity | 粒度 | 界限字段的解释单位：1 字节或 4 KB。 |
| GDT / LDT | 全局/局部描述符表 | 存放段描述符的表。 |
| GDTR / LDTR | 全局/局部描述符表寄存器 | 存放相应表的基地址与界限。 |
| flat model | 平坦模型 | 所有段覆盖整个 4 GB 线性空间的存储组织方式。 |
| linear address | 线性地址 | 段转换的结果、页转换的输入。 |
| physical address | 物理地址 | 出现在地址总线上的地址。 |
| logical address | 逻辑地址 | 选择子:偏移形式、程序可见的地址。 |
| effective address | 有效地址 | 加段基址之前，由基址、变址、比例、位移算出的偏移。 |

## 分页

| 英文 | 中文 | 说明 |
|---|---|---|
| paging | 分页 | 把线性地址转换为物理地址的第二阶段。 |
| page | 页 | 4 KB 对齐的线性地址单元。 |
| page frame | 页框 | 4 KB 对齐的物理内存单元。 |
| page directory | 页目录 | 最高一级页表，含 1K 个页目录项。 |
| page table | 页表 | 第二级页表，含 1K 个页表项。 |
| PDE / PTE | 页目录项 / 页表项 | 含页框地址与保护、状态位的 32 位表项。 |
| present bit | 存在位 | 表项是否可用于地址转换。 |
| accessed bit | 已访问位 | 页被读写时由硬件置位。 |
| dirty bit | 脏位 | 页被写入时由硬件置位。 |
| TLB | 转换后备缓冲器 | 缓存页表信息的片上存储器。 |
| page fault | 页错误 | 页不存在或访问权不足引起的异常 14。 |

## 保护与特权

| 英文 | 中文 | 说明 |
|---|---|---|
| protection | 保护 | 检查内存访问与指令执行是否合规的机制。 |
| privilege level | 特权级 | 0（最高）到 3（最低）。 |
| CPL / DPL / RPL | 当前/描述符/请求者特权级 | 保护检查使用的三个级别。 |
| conforming segment | 一致段 | 可在调用者特权级执行的可执行段。 |
| call gate | 调用门 | 受保护的过程入口，含选择子、偏移、DPL 与参数计数。 |
| interrupt gate / trap gate | 中断门 / 陷阱门 | IDT 中的门；前者清除 IF，后者不改变 IF。 |
| task gate | 任务门 | 间接引用 TSS 的门。 |
| stack switch | 栈切换 | 跨级调用时切换到新特权级的栈。 |
| ARPL | 调整请求者特权级 | 提升选择子 RPL 以校验指针完整性。 |

## 任务与中断

| 英文 | 中文 | 说明 |
|---|---|---|
| task | 任务 | 拥有独立 TSS、LDT 与地址空间的控制流。 |
| TSS | 任务状态段 | 保存任务寄存器状态与栈指针的段。 |
| TR | 任务寄存器 | 指向当前任务 TSS 的寄存器。 |
| task switch | 任务切换 | 保存当前任务状态并装入新任务状态。 |
| back-link | 回链 | TSS 中指向前一任务的 TSS 选择子。 |
| NT flag | 嵌套任务标志 | 指示回链是否有效。 |
| interrupt | 中断 | 异步事件，通常来自外部设备。 |
| exception | 异常 | 指令执行引起的同步事件。 |
| fault / trap / abort | 故障 / 陷阱 / 中止 | 按返回地址与可重启性划分的异常类别。 |
| IDT | 中断描述符表 | 把向量号映射到门描述符的表。 |
| vector | 向量号 | 0–255 的中断或异常标识。 |
| error code | 错误码 | 部分异常压栈的诊断信息。 |

## 指令与调试

| 英文 | 中文 | 说明 |
|---|---|---|
| opcode | 操作码 | 指定操作的编码。 |
| ModR/M byte | ModR/M 字节 | 指定寄存器/内存操作数与寻址方式。 |
| SIB byte | SIB 字节 | 指定比例、变址、基址。 |
| displacement | 位移 | 地址计算中的常数分量。 |
| immediate operand | 立即操作数 | 编码在指令中的数据。 |
| sign extension | 符号扩展 | 用符号位填充高位。 |
| zero extension | 零扩展 | 用零填充高位。 |
| string instruction | 串指令 | 对连续元素批量操作，使用 ESI/EDI 与 DF。 |
| repeat prefix | 重复前缀 | `REP`、`REPE`/`REPZ`、`REPNE`/`REPNZ`。 |
| breakpoint | 断点 | 使处理器转入调试处理程序的地址或指令。 |
| debug register | 调试寄存器 | DR0–DR3 地址、DR6 状态、DR7 控制。 |
| resume flag (RF) | 恢复标志 | 使指令在调试异常后可重新执行而不再次触发。 |
| trap flag (TF) | 陷阱标志 | 单步执行。 |

## 缩写

| 缩写 | 全称 | 中文 |
|---|---|---|
| BCD | Binary-Coded Decimal | 二进制编码十进制 |
| DPL | Descriptor Privilege Level | 描述符特权级 |
| GDT | Global Descriptor Table | 全局描述符表 |
| IDT | Interrupt Descriptor Table | 中断描述符表 |
| LDT | Local Descriptor Table | 局部描述符表 |
| PDBR | Page Directory Base Register | 页目录基址寄存器 |
| RPL | Requested Privilege Level | 请求者特权级 |
| TLB | Translation Lookaside Buffer | 转换后备缓冲器 |
| TSS | Task State Segment | 任务状态段 |
