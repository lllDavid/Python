def countSubstrings(s):
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    count = 0

    for l in range(n):
        for i in range(n - l):
            j = i + l
            if s[i] == s[j] and (l < 2 or dp[i+1][j-1]):
                dp[i][j] = True
                count += 1
    return count

print(countSubstrings("aaa"))  
