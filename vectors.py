import math

class Vector:
    def __init__(self, x, y, z):
        """Initialize a 3D vector with components x, y, z."""
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        """Represent the vector as a string."""
        return f"Vector({self.x}, {self.y}, {self.z})"

    # 1. Vector Addition
    def add(self, other):
        """Add two vectors."""
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    # 2. Vector Subtraction
    def subtract(self, other):
        """Subtract two vectors."""
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    # 3. Dot Product
    def dot(self, other):
        """Calculate the dot product of two vectors."""
        return self.x * other.x + self.y * other.y + self.z * other.z

    # 4. Cross Product
    def cross(self, other):
        """Calculate the cross product of two vectors."""
        cx = self.y * other.z - self.z * other.y
        cy = self.z * other.x - self.x * other.z
        cz = self.x * other.y - self.y * other.x
        return Vector(cx, cy, cz)

    # 5. Magnitude (Length) of a Vector
    def magnitude(self):
        """Calculate the magnitude (length) of the vector."""
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    # 6. Normalize the Vector
    def normalize(self):
        """Normalize the vector (make its magnitude 1)."""
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("Cannot normalize a zero-length vector")
        return Vector(self.x / mag, self.y / mag, self.z / mag)

    # 7. Scalar Multiplication
    def scale(self, scalar):
        """Scale the vector by a scalar."""
        return Vector(self.x * scalar, self.y * scalar, self.z * scalar)

    # 8. Angle Between Vectors
    def angle_between(self, other):
        """Calculate the angle between two vectors in radians."""
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

    result_add = v1.add(v2)
    print(f"v1 + v2 = {result_add}")

    result_subtract = v1.subtract(v2)
    print(f"v1 - v2 = {result_subtract}")

    result_dot = v1.dot(v2)
    print(f"v1 . v2 = {result_dot}")

    result_cross = v1.cross(v2)
    print(f"v1 x v2 = {result_cross}")

    result_magnitude_v1 = v1.magnitude()
    print(f"|v1| = {result_magnitude_v1}")

    result_normalize_v1 = v1.normalize()
    print(f"Normalized v1 = {result_normalize_v1}")

    result_scale = v1.scale(2)
    print(f"v1 scaled by 2 = {result_scale}")

    result_angle = v1.angle_between(v2)
    print(f"Angle between v1 and v2 (radians) = {result_angle}")
