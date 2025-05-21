import sys
import ctypes
from ctypes import wintypes

# NOTE: run like: python i.py <PID> <Path to dll>
try:
    dll = ctypes.CDLL(r'') # Path to dll
    print("DLL loaded successfully!")
except OSError as e:
    print(f"Error loading DLL: {e}")

PROCESS_ALL_ACCESS = (0x000F0000 | 0x00100000 | 0xFFF)
PAGE_READWRITE = 0x04
MEM_COMMIT = 0x1000
MEM_RESERVE = 0x2000

kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)

OpenProcess = kernel32.OpenProcess
OpenProcess.argtypes = [wintypes.DWORD, wintypes.BOOL, wintypes.DWORD]
OpenProcess.restype = wintypes.HANDLE

VirtualAllocEx = kernel32.VirtualAllocEx
VirtualAllocEx.argtypes = [wintypes.HANDLE, wintypes.LPVOID, ctypes.c_size_t, 
                         wintypes.DWORD, wintypes.DWORD]
VirtualAllocEx.restype = wintypes.LPVOID

WriteProcessMemory = kernel32.WriteProcessMemory
WriteProcessMemory.argtypes = [wintypes.HANDLE, wintypes.LPVOID, wintypes.LPCVOID, 
                             ctypes.c_size_t, ctypes.POINTER(ctypes.c_size_t)]
WriteProcessMemory.restype = wintypes.BOOL

GetProcAddress = kernel32.GetProcAddress
GetProcAddress.argtypes = [wintypes.HMODULE, wintypes.LPCSTR]
GetProcAddress.restype = wintypes.LPVOID

CreateRemoteThread = kernel32.CreateRemoteThread
CreateRemoteThread.argtypes = [wintypes.HANDLE, wintypes.LPVOID, ctypes.c_size_t,
                             wintypes.LPVOID, wintypes.LPVOID, wintypes.DWORD,
                             wintypes.LPDWORD]
CreateRemoteThread.restype = wintypes.HANDLE

CloseHandle = kernel32.CloseHandle
CloseHandle.argtypes = [wintypes.HANDLE]
CloseHandle.restype = wintypes.BOOL

def inject(pid, dll_path):
    try:
        dll_path_bytes = dll_path.encode('ascii')
        dll_path_len = len(dll_path_bytes) + 1 

        process_handle = OpenProcess(PROCESS_ALL_ACCESS, False, pid)
        if not process_handle:
            raise ctypes.WinError(ctypes.get_last_error())

        remote_memory = VirtualAllocEx(
            process_handle,
            None,
            dll_path_len,
            MEM_COMMIT | MEM_RESERVE,
            PAGE_READWRITE
        )
        if not remote_memory:
            raise ctypes.WinError(ctypes.get_last_error())

        written = ctypes.c_size_t(0)
        success = WriteProcessMemory(
            process_handle,
            remote_memory,
            dll_path_bytes,
            dll_path_len,
            ctypes.byref(written)
        )
        if not success:
            raise ctypes.WinError(ctypes.get_last_error())

        kernel32_handle = kernel32.GetModuleHandleW("kernel32.dll")
        load_library = GetProcAddress(kernel32_handle, b"LoadLibraryA")
        if not load_library:
            raise ctypes.WinError(ctypes.get_last_error())

        thread_handle = CreateRemoteThread(
            process_handle,
            None,
            0,
            load_library,
            remote_memory,
            0,
            None
        )
        if not thread_handle:
            raise ctypes.WinError(ctypes.get_last_error())

        print(f"Successfully injected DLL into process {pid}")
        

        CloseHandle(thread_handle)
        CloseHandle(process_handle)

    except Exception as e:
        print(f"Error during injection: {str(e)}")
        
        if 'process_handle' in locals():
            CloseHandle(process_handle)
        if 'thread_handle' in locals():
            CloseHandle(thread_handle)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python i.py <PID> <DLL_PATH>")
        sys.exit(1)

    try:
        target_pid = int(sys.argv[1])
        dll_path = sys.argv[2]
        inject(target_pid, dll_path)
    except ValueError:
        print("PID must be a number")
        sys.exit(1)