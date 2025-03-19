a = 256
b = 256
print(a is b)  

x = -5
y = -5
print(x is y)  

a = 257
b = 257
print(a is b) 

x = -10
y = -10
print(x is y)  

s1 = "hello"
s2 = "hello"
print(s1 is s2)  

s3 = "hello world!"
s4 = "hello world!"
print(s3 is s4)  

import sys

s1 = sys.intern("hello world!")
s2 = sys.intern("hello world!")
print(s1 is s2)  
