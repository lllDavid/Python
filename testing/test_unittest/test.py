import unittest

def add(a, b):
    return a + b

class TestAddFunction(unittest.TestCase):

    def test_add_positive_numbers(self):
        self.assertEqual(add(3, 5), 8)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-2, -4), -6)

    def test_add_zero(self):
        self.assertEqual(add(0, 7), 7)

if __name__ == '__main__':
    unittest.main()
