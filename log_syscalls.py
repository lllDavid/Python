#!/usr/bin/env python3

import os
import sys
import ctypes
import signal

PTRACE_TRACEME = 0
PTRACE_SYSCALL = 24
PTRACE_GETREGS = 12

SYSCALLS = {
    0: "read", 1: "write", 2: "open", 3: "close", 4: "stat", 5: "fstat", 6: "lstat",
    9: "mmap", 10: "mprotect", 11: "munmap", 12: "brk",
    59: "execve", 60: "exit", 61: "wait4", 63: "uname", 72: "fcntl", 80: "chdir",
    87: "unlink", 89: "readlink", 90: "chmod", 92: "chown", 94: "umask",
    102: "getuid", 104: "getgid", 105: "setuid", 106: "setgid",
    202: "futex", 218: "set_tid_address", 231: "exit_group", 257: "openat",
    262: "newfstatat", 263: "unlinkat", 266: "renameat", 270: "faccessat", 291: "mkdirat",
}

class user_regs_struct(ctypes.Structure):
    _fields_ = [
        ("r15", ctypes.c_ulonglong),
        ("r14", ctypes.c_ulonglong),
        ("r13", ctypes.c_ulonglong),
        ("r12", ctypes.c_ulonglong),
        ("rbp", ctypes.c_ulonglong),
        ("rbx", ctypes.c_ulonglong),
        ("r11", ctypes.c_ulonglong),
        ("r10", ctypes.c_ulonglong),
        ("r9", ctypes.c_ulonglong),
        ("r8", ctypes.c_ulonglong),
        ("rax", ctypes.c_ulonglong),
        ("rcx", ctypes.c_ulonglong),
        ("rdx", ctypes.c_ulonglong),
        ("rsi", ctypes.c_ulonglong),
        ("rdi", ctypes.c_ulonglong),
        ("orig_rax", ctypes.c_ulonglong),
        ("rip", ctypes.c_ulonglong),
        ("cs", ctypes.c_ulonglong),
        ("eflags", ctypes.c_ulonglong),
        ("rsp", ctypes.c_ulonglong),
        ("ss", ctypes.c_ulonglong),
        ("fs_base", ctypes.c_ulonglong),
        ("gs_base", ctypes.c_ulonglong),
        ("ds", ctypes.c_ulonglong),
        ("es", ctypes.c_ulonglong),
        ("fs", ctypes.c_ulonglong),
        ("gs", ctypes.c_ulonglong),
    ]

libc = ctypes.CDLL("libc.so.6", use_errno=True)

def ptrace(request, pid, addr=0, data=0):
    ret = libc.ptrace(request, pid, ctypes.c_void_p(addr), ctypes.c_void_p(data))
    if ret != 0:
        err = ctypes.get_errno()
        if err:
            raise OSError(err, os.strerror(err))
    return ret

def trace(program):
    pid = os.fork()
    if pid == 0:
        libc.ptrace(PTRACE_TRACEME, 0, 0, 0)
        os.kill(os.getpid(), signal.SIGSTOP)
        os.execvp(program[0], program)
    else:
        os.waitpid(pid, 0)
        ptrace(PTRACE_SYSCALL, pid, 0, 0)
        while True:
            _, status = os.waitpid(pid, 0)
            if os.WIFEXITED(status):
                break
            regs = user_regs_struct()
            libc.ptrace(PTRACE_GETREGS, pid, 0, ctypes.byref(regs))
            scnum = regs.orig_rax
            name = SYSCALLS.get(scnum, f"sys_{scnum}")
            print(f"syscall: {name} ({scnum})")
            ptrace(PTRACE_SYSCALL, pid, 0, 0)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"usage: {sys.argv[0]} <program> [args...]")
        sys.exit(1)
    trace(sys.argv[1:])