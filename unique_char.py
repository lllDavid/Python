def first_unique_char(s: str) -> int:
    for i in range(len(s)):
        if s[i] not in s[i+1:] and s[i] not in s[:i]:
            return i
    return -1
    
import unittest

class TestFirstUniqueChar(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(first_unique_char("leetcode"), 0)
        self.assertEqual(first_unique_char("loveleetcode"), 2)
        self.assertEqual(first_unique_char("aabb"), -1)
        self.assertEqual(first_unique_char("abcabcde"), 6)
        self.assertEqual(first_unique_char("xxyz"), 2)
        self.assertEqual(first_unique_char("z"), 0)

if __name__ == "__main__":
    unittest.main()
