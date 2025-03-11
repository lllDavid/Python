a = 0b1100  
b = 0b1010  

print(bin(a & b))  
print(bin(a | b))  
print(bin(a ^ b)) 
print(bin(~a))     

#hw
def count_set_bits(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count

print(count_set_bits(29))  

def reverse_bits(n):
    result = 0
    for _ in range(32):  
        result = (result << 1) | (n & 1)
        n >>= 1
    return result

print(bin(reverse_bits(0b00000000000000000000000000001011)))
