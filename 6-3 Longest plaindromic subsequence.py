def longest_plaindromic_subsequence(s: str):
    n = len(s)
    dp = [['' for i in range(n)] for j in range(n)]
    for i in range(n):
        dp[i][i] = s[i]
    for i in range(n-1, -1, -1):
        for j in range(i+1, n):
            if s[i] == s[j]:
                dp[i][j] +=  s[i] + dp[i+1][j-1] + s[j]
            else:
               dp[i][j] = dp[i+1][j] if len(dp[i+1][j]) > len(dp[i][j-1]) else dp[i][j-1]
    return (dp[0][n-1])

if __name__ == '__main__':
    s = 'character'
    print(longest_plaindromic_subsequence(s))