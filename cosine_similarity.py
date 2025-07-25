import math

def cosine_similarity(vec1, vec2):
    if len(vec1) != len(vec2):
        raise ValueError("Vectors must be of same length")

    dot_product = sum(a * b for a, b in zip(vec1, vec2))
    magnitude1 = math.sqrt(sum(a * a for a in vec1))
    magnitude2 = math.sqrt(sum(b * b for b in vec2))

    if magnitude1 == 0 or magnitude2 == 0:
        return 0.0 

    return dot_product / (magnitude1 * magnitude2)

v1 = [1, 2, 3]
v2 = [4, 5, 6]
print(cosine_similarity(v1, v2))