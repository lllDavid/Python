import ctypes

class Point(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int), ("y", ctypes.c_int)]

num_points = 3
points_array = (Point * num_points)(Point(1, 2), Point(3, 4), Point(5, 6))

ptr = ctypes.pointer(points_array)

print(f"Before modification: ({ptr.contents.x}, {ptr.contents.y})")
ptr.contents.x = 10
ptr.contents.y = 20
print(f"After modification: ({points_array[0].x}, {points_array[0].y})")

ptr = ctypes.cast(points_array, ctypes.POINTER(Point))  

for i in range(num_points):
    point = ptr[i]  
    print(f"Point {i}: ({point.x}, {point.y})")