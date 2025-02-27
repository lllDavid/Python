class Solution:
    def longestCommonSubstring(self, sentence1: str, sentence2: str) -> str:
        len1, len2 = len(sentence1), len(sentence2)
        max_len = 0
        max_substr = ""
        
        for i in range(len1):
            for j in range(len2):
                temp_substr = ""
                k = i
                l = j
                
                while k < len1 and l < len2 and sentence1[k] == sentence2[l]:
                    temp_substr += sentence1[k]
                    k += 1
                    l += 1
                
                if len(temp_substr) > max_len:
                    max_len = len(temp_substr)
                    max_substr = temp_substr
        
        return max_substr

sentence1 = "The quick brown fox jumps over the lazy dog."
sentence2 = "The fast brown fox jumps over the lazy dog."

solution = Solution()
longest_substr = solution.longestCommonSubstring(sentence1, sentence2)
print(f"Longest common substring: '{longest_substr}'")
