from capstone import Cs, CS_ARCH_X86, CS_MODE_64

def operand_to_str(op):
    if op.type == 1:  # Register operand
        return str(op.reg)
    elif op.type == 2:  # Immediate operand
        return str(op.imm)
    elif op.type == 3:  # Memory operand
        return hex(op.mem.disp)
    else:
        return 'N/A'

def disassemble_x86_64(code, address=0x1000):
    md = Cs(CS_ARCH_X86, CS_MODE_64)
    md.detail = True  
    
    for instr in md.disasm(code, address):
        operands = f"Operands: {', '.join(operand_to_str(op) for op in instr.operands)}" if instr.operands else ""
        print(f"0x{instr.address:x}:\t{instr.mnemonic}\t{instr.op_str} {operands}")
        
        if instr.groups:
            print(f"  Groups: {', '.join(map(str, instr.groups))}")
        if instr.operands:
            print(f"  Operands Count: {len(instr.operands)}\n")

code = b"\x55\x48\x8b\x05\xb8\x13\x00\x00\x48\x83\xec\x08\xc3"
disassemble_x86_64(code)