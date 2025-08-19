def NAND(a, b):
    """Returns the NAND of two boolean inputs a and b."""
    return not (a and b)

inputs = [(0, 0), (0, 1), (1, 0), (1, 1)]

print("A B | NAND")
for a, b in inputs:
    print(f"{a} {b} | {int(NAND(a, b))}")

def AND(a, b):
    return int(not NAND(a, b))

def OR(a, b):
    return int(NAND(not a, not b))

def NOT(a):
    return int(NAND(a, a))

print("\nDerived gates:")
for a, b in inputs:
    print(f"A={a}, B={b} -> AND={AND(a,b)}, OR={OR(a,b)}, NOT A={NOT(a)}, NOT B={NOT(b)}")