import ctypes

class Point(ctypes.Structure):
    _fields_ = [("x", ctypes.c_double), ("y", ctypes.c_double)]

PointArray = Point * 5
points = PointArray(
    Point(1, 2),
    Point(3, 4),
    Point(5, 6),
    Point(7, 8),
    Point(9, 10)
)

ptr = ctypes.cast(points, ctypes.POINTER(ctypes.c_double))

print("Memory before modification:")
for i in range(5 * 2):  
    print(ptr[i], end=" ")
print("\n")

for i in range(0, 10, 2):
    ptr[i] *= 10

for i in range(1, 10, 2):
    ptr[i] += 100

print("Memory after modification:")
for i in range(5):
    print(f"Point {i}: ({points[i].x}, {points[i].y})")