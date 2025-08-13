class SimpleCPU:
    def __init__(self):
        self.registers = {"A": 0, "B": 0, "C": 0, "D": 0}  
        self.memory = [0] * 256  
        self.pc = 0  
        self.running = True

    def load_program(self, program):
        self.memory[:len(program)] = program

    def fetch(self):
        instruction = self.memory[self.pc]
        self.pc += 1
        return instruction

    def execute(self, instruction):
        if instruction == 0x01:  
            self.running = False
        elif instruction == 0x10: 
            self.registers["A"] = (self.registers["A"] + 1) % 256
        elif instruction == 0x11:  
            self.registers["A"] = (self.registers["A"] - 1) % 256
        elif instruction == 0x20:  
            self.registers["A"] = self.fetch()
        elif instruction == 0x21:  
            addr = self.fetch()
            self.memory[addr] = self.registers["A"]
        elif instruction == 0x30: 
            addr = self.fetch()
            self.pc = addr
        else:
            print(f"Unknown instruction: {instruction}")
            self.running = False

    def run(self):
        while self.running:
            instruction = self.fetch()
            self.execute(instruction)

program = [0x20, 5, 0x10, 0x21, 10, 0x01]

cpu = SimpleCPU()
cpu.load_program(program)
cpu.run()

print("Registers:", cpu.registers)
print("Memory:", cpu.memory[:20])