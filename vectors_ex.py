import torch
import math

class Vector:
    def __init__(self, x, y, z):
        self.v = torch.tensor([x, y, z], dtype=torch.float32)

    def __repr__(self):
        x, y, z = self.v.tolist()
        return f"Vector({x}, {y}, {z})"

    def add(self, other):
        return Vector(*(self.v + other.v))

    def subtract(self, other):
        return Vector(*(self.v - other.v))

    def dot(self, other):
        return torch.dot(self.v, other.v).item()

    def cross(self, other):
        return Vector(*torch.linalg.cross(self.v, other.v))

    def magnitude(self):
        return torch.norm(self.v).item()

    def normalize(self):
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("Cannot normalize a zero-length vector")
        normalized = self.v / mag
        return Vector(*normalized)

    def scale(self, scalar):
        return Vector(*(self.v * scalar))

    def angle_between(self, other):
        dot_prod = self.dot(other)
        mag_self = self.magnitude()
        mag_other = other.magnitude()
        if mag_self == 0 or mag_other == 0:
            raise ValueError("Cannot compute angle with zero-length vector")

        cos_theta = dot_prod / (mag_self * mag_other)
        cos_theta = max(-1.0, min(1.0, cos_theta))  
        return math.acos(cos_theta)

if __name__ == "__main__":
    v1 = Vector(1, 2, 3)
    v2 = Vector(4, 5, 6)

    print(f"v1 = {v1}")
    print(f"v2 = {v2}")

    print(f"v1 + v2 = {v1.add(v2)}")
    print(f"v1 - v2 = {v1.subtract(v2)}")
    print(f"v1 . v2 = {v1.dot(v2)}")
    print(f"v1 x v2 = {v1.cross(v2)}")
    print(f"|v1| = {v1.magnitude()}")
    print(f"Normalized v1 = {v1.normalize()}")
    print(f"v1 scaled by 2 = {v1.scale(2)}")
    print(f"Angle between v1 and v2 (radians) = {v1.angle_between(v2)}")
