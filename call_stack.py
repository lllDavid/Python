import sys
import inspect

def trace_calls(frame, event, arg):
    if event == 'call':
        stack = inspect.stack()
        print("Call stack:")
        for s in reversed(stack):
            func_name = s.function
            filename = s.filename
            lineno = s.lineno
            module = s.frame.f_globals.get("__name__", "<unknown>")
            code_context = s.code_context[0].strip() if s.code_context else ''
            print(f"  {func_name}() in {module} - {filename}:{lineno}")
            print(f"    >> {code_context}")
            
            try:
                sig = inspect.signature(s.frame.f_code)
            except Exception:
                sig = "<unknown signature>"
            print(f"    Locals: {list(s.frame.f_locals.keys())}")
        
        print("Arguments to current function:")
        try:
            arg_info = inspect.getargvalues(frame)
            for arg_name in arg_info.args:
                val = arg_info.locals.get(arg_name, '<not found>')
                print(f"  {arg_name} = {val!r}")
            if arg_info.varargs:
                print(f"  *{arg_info.varargs} = {arg_info.locals.get(arg_info.varargs)}")
            if arg_info.keywords:
                print(f"  **{arg_info.keywords} = {arg_info.locals.get(arg_info.keywords)}")
        except Exception as e:
            print(f"  Failed to get arguments: {e}")
        print("-" * 60)
    return trace_calls

def function(a, b, c):
    return a + b * c

sys.settrace(trace_calls)
function(2, 3, 4)
sys.settrace(None)