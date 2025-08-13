def cg(start=0, step=1, limit=None, filter_func=None):
    current = start
    while True:
        if limit is not None and current > limit:
            break

        if not filter_func or filter_func(current):
            command = yield current
        else:
            command = yield

        if isinstance(command, dict):
            if "reset" in command:
                current = command["reset"]
                continue
            if "skip" in command:
                current += command["skip"]
                continue

        current += step

gen = cg(start=0, step=2, limit=20, filter_func=lambda x: x % 4 == 0)

print(next(gen))      
print(next(gen))      
print(gen.send({"skip": 4}))  
print(next(gen))      
print(gen.send({"reset": 8}))  
print(next(gen))    