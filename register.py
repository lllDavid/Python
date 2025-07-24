class CPURegister:
    def __init__(self, bits: int = 32):
        if bits not in (8, 16, 32, 64):
            raise ValueError("Bits must be one of: 8, 16, 32, 64")
        self.bits = bits
        self.max_value = (1 << bits) - 1
        self.value = 0

    def write(self, val: int):
        if not (0 <= val <= self.max_value):
            raise ValueError(f"Value must fit in {self.bits} bits")
        self.value = val

    def read(self) -> int:
        return self.value

    def clear(self):
        self.value = 0

    def __repr__(self):
        return f"CPURegister({self.bits}-bit): 0x{self.value:0{self.bits // 4}X}"

reg = CPURegister(16)   
reg.write(0xABCD)
print(reg)             
print(hex(reg.read()))  