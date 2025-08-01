import unittest

def add(a, b):
    return a + b

class TestAdd(unittest.TestCase):

    def test_add_subtests(self):
        test_cases = [
            (1, 2, 3),
            (0, 0, 0),
            (-1, -1, -2),
            (100, 200, 300),
            (5, 5, 11),
        ]

        for a, b, expected in test_cases:
            with self.subTest(a=a, b=b, expected=expected):
                result = add(a, b)
                self.assertEqual(result, expected)