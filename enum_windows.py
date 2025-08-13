import ctypes
from ctypes import wintypes

user32 = ctypes.windll.user32

EnumWindowsProc = ctypes.WINFUNCTYPE(ctypes.c_bool, wintypes.HWND, wintypes.LPARAM)

def get_window_text(hwnd):
    length = user32.GetWindowTextLengthW(hwnd)
    buffer = ctypes.create_unicode_buffer(length + 1)
    user32.GetWindowTextW(hwnd, buffer, length + 1)
    return buffer.value

def foreach_window(hwnd, lParam):
    if user32.IsWindowVisible(hwnd):
        title = get_window_text(hwnd)
        if title:
            print(f"HWND: {hwnd} | Title: {title}")
    return True  

user32.EnumWindows(EnumWindowsProc(foreach_window), 0)