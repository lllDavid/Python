import ctypes
import time
import subprocess

c_code = """
#include <stdio.h>

__declspec(dllexport) long long sum_c(int n) {
    volatile long long s = 0; 
    for (int i = 0; i < n; i++) {
        s += i;
    }
    return s;
}
"""

with open("sum.c", "w") as f:
    f.write(c_code)

subprocess.run([
    "clang", "-O3", "-shared", "-o", "sum.dll", "sum.c", "-target", "x86_64-pc-windows-msvc"
], check=True)

lib = ctypes.CDLL("./sum.dll")
lib.sum_c.argtypes = [ctypes.c_int]
lib.sum_c.restype = ctypes.c_longlong


def sum_py(n):
    s = 0
    for i in range(n):
        s += i
    return s

N = 100_000_000

start = time.time()
sum_py(N)
py_time = time.time() - start

start = time.time()
lib.sum_c(N)
c_time = time.time() - start

print(f"Python time: {py_time:.4f} seconds")
print(f"C via ctypes time: {c_time:.4f} seconds")