import math

# 1. Vector Operations
def add_vectors(v1, v2):
    """Add two vectors (represented as tuples or lists of 3D coordinates)."""
    return (v1[0] + v2[0], v1[1] + v2[1], v1[2] + v2[2])

def subtract_vectors(v1, v2):
    """Subtract vector v2 from v1."""
    return (v1[0] - v2[0], v1[1] - v2[1], v1[2] - v2[2])

def dot_product(v1, v2):
    """Calculate the dot product of two vectors."""
    return v1[0] * v2[0] + v1[1] * v2[1] + v1[2] * v2[2]

def cross_product(v1, v2):
    """Calculate the cross product of two vectors."""
    return (
        v1[1] * v2[2] - v1[2] * v2[1],
        v1[2] * v2[0] - v1[0] * v2[2],
        v1[0] * v2[1] - v1[1] * v2[0]
    )

def magnitude(v):
    """Calculate the magnitude (length) of a vector."""
    return math.sqrt(v[0]**2 + v[1]**2 + v[2]**2)

def normalize(v):
    """Normalize a vector (i.e., make its magnitude 1)."""
    mag = magnitude(v)
    if mag == 0:
        raise ValueError("Cannot normalize a zero-length vector")
    return (v[0] / mag, v[1] / mag, v[2] / mag)

# 2. Rotation Operations

def rotate_vector(v, axis, theta):
    """
    Rotate a vector v around a given axis by an angle theta (in radians).
    The axis is expected to be a unit vector (x, y, z).
    """
    cos_theta = math.cos(theta)
    sin_theta = math.sin(theta)
    dot = dot_product(v, axis)
    cross = cross_product(axis, v)

    return (
        cos_theta * v[0] + sin_theta * cross[0] + (1 - cos_theta) * dot * axis[0],
        cos_theta * v[1] + sin_theta * cross[1] + (1 - cos_theta) * dot * axis[1],
        cos_theta * v[2] + sin_theta * cross[2] + (1 - cos_theta) * dot * axis[2]
    )

# 3. Transformation Operations

def translate_vector(v, translation):
    """Translate (move) a vector by a given translation vector."""
    return add_vectors(v, translation)

def scale_vector(v, scale_factor):
    """Scale a vector by a given scale factor."""
    return (v[0] * scale_factor, v[1] * scale_factor, v[2] * scale_factor)

# 4. Miscellaneous Operations

def angle_between(v1, v2):
    """Calculate the angle between two vectors in radians."""
    dot_prod = dot_product(v1, v2)
    mag_v1 = magnitude(v1)
    mag_v2 = magnitude(v2)
    if mag_v1 == 0 or mag_v2 == 0:
        raise ValueError("Cannot compute angle with zero-length vector")
    
    cos_angle = dot_prod / (mag_v1 * mag_v2)
    cos_angle = max(-1.0, min(1.0, cos_angle))  
    return math.acos(cos_angle)

def is_parallel(v1, v2):
    """Check if two vectors are parallel (or anti-parallel)."""
    cross_prod = cross_product(v1, v2)
    return cross_prod == (0, 0, 0)

def is_perpendicular(v1, v2):
    """Check if two vectors are perpendicular."""
    return dot_product(v1, v2) == 0

if __name__ == "__main__":
    v1 = (1, 2, 3)
    v2 = (4, 5, 6)
    
    print("Add Vectors:", add_vectors(v1, v2))
    print("Subtract Vectors:", subtract_vectors(v1, v2))
    print("Dot Product:", dot_product(v1, v2))
    print("Cross Product:", cross_product(v1, v2))
    print("Magnitude of v1:", magnitude(v1))
    print("Normalized v1:", normalize(v1))
    
    axis = (0, 0, 1)  # z-axis
    angle = math.radians(90)  
    print("Rotate v1 by 90 degrees around z-axis:", rotate_vector(v1, axis, angle))
    
    translation = (1, 1, 1)
    print("Translated v1:", translate_vector(v1, translation))
    
    scale_factor = 2
    print("Scaled v1 by a factor of 2:", scale_vector(v1, scale_factor))
    
    print("Angle between v1 and v2 (radians):", angle_between(v1, v2))
    print("Are v1 and v2 parallel?", is_parallel(v1, v2))
    print("Are v1 and v2 perpendicular?", is_perpendicular(v1, v2))
