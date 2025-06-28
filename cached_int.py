def check_int_identity(value):
    a = int(value)
    b = int(value)
    return a is b

def test_integer_caching():
    test_values = [256, 257, -5, -6, 1000, -1000]

    for val in test_values:
        result = check_int_identity(val)
        status = "cached" if result else "not cached"
        print(f"Integer {val} is {val} -> {status}")

    print("\nTesting integers created with expressions:")
    expressions = [
        (128 + 128),
        (200 + 57),
        (-3 - 2),
        (-3 - 3),
        (500 * 2),
        (-500 * 2),
    ]

    for val in expressions:
        result = check_int_identity(val)
        status = "cached" if result else "not cached"
        print(f"Integer {val} created by expression -> {status}")

test_integer_caching()