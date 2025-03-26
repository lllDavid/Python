import sys
import dis
import inspect

def show_call_stack():
    frame = sys._getframe()  
    print("Call Stack (most recent call last):")
    stack = []
    while frame:
        stack.append(frame)
        frame = frame.f_back
    for frame in reversed(stack):
        code = frame.f_code
        print(f"Function: {code.co_name}, Line: {frame.f_lineno}, File: {code.co_filename}")

def show_bytecode(func):

    print(f"\nDisassembly of {func.__name__}:")
    dis.dis(func)

def sample_function(x):

    y = x + 1
    return y * 2

def show_frame_info():

    current_frame = inspect.currentframe()
    info = inspect.getframeinfo(current_frame)
    print("\nCurrent Frame Info:")
    print(f"Filename: {info.filename}")
    print(f"Function: {info.function}")
    print(f"Line Number: {info.lineno}")
    print(f"Code Context: {info.code_context}")

if __name__ == "__main__":
    show_call_stack()

    show_bytecode(sample_function)

    show_frame_info()