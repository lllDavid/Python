import ctypes

# Minimal machine code for: int add(int a, int b) { return a + b; }
#   mov eax, ecx    => 0x89, 0xC8
#   add eax, edx    => 0x01, 0xD0
#   ret             => 0xC3
code = bytearray([0x89, 0xC8, 0x01, 0xD0, 0xC3])

PAGE_EXECUTE_READWRITE = 0x40
MEM_COMMIT            = 0x1000
MEM_RESERVE           = 0x2000

kernel32 = ctypes.windll.kernel32
kernel32.VirtualAlloc.restype = ctypes.c_void_p

ptr = kernel32.VirtualAlloc(
    None,
    len(code),
    MEM_COMMIT | MEM_RESERVE,
    PAGE_EXECUTE_READWRITE
)
if not ptr:
    raise MemoryError("VirtualAlloc failed")

src = (ctypes.c_char * len(code)).from_buffer(code)
ctypes.memmove(ptr, ctypes.cast(src, ctypes.c_void_p), len(code))

FUNC_TYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
add_func  = FUNC_TYPE(ptr)

result = add_func(10, 32)
print(result)  

result = add_func(1, 1)
print(result)  

result = add_func(-10, 255)
print(result)  