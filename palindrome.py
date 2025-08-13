def longest_palindrome(s):
    def expand_from_center(s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]
    
    if not s:
        return ""
    
    longest = ""
    for i in range(len(s)):
        odd_palindrome = expand_from_center(s, i, i)
        if len(odd_palindrome) > len(longest):
            longest = odd_palindrome
        
        even_palindrome = expand_from_center(s, i, i + 1)
        if len(even_palindrome) > len(longest):
            longest = even_palindrome
    
    return longest

test_string = input("Enter a string: ")
result = longest_palindrome(test_string)
print("The longest substring is:", result)