from collections import namedtuple

Point = namedtuple('Point', ['x', 'y', 'label'])

p1 = Point(1, 2, 'A')

print(p1.x)
print(p1.y)
print(p1.label)

print(p1[0])
print(p1[1])
print(p1[2])

p_dict = p1._asdict()
print(p_dict)

p2 = p1._replace(x=10, label='B')
print(p2)

x, y, label = p2
print(f"x={x}, y={y}, label={label}")