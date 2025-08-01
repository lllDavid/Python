import unittest

def reverse_string(s):
    return s[::-1]

class TestReverseString(unittest.TestCase):

    def test_regular_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")

    def test_empty_string(self):
        self.assertEqual(reverse_string(""), "")

    def test_palindrome(self):
        self.assertEqual(reverse_string("madam"), "madam")

if __name__ == '__main__':
    unittest.main()