from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])

p = Point(1, 2)

print(p.x)  
print(p.y)  

print(p[0])  
print(p[1])  
