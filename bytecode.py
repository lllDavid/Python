import dis

def co_function(x, y):
    if x > y:
        z = x - y
    else:
        z = x + y
    
    result = 0
    for i in range(5):
        result += i
    
    return z + result

dis.dis(co_function)
