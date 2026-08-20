class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ''
        L = [[False] * n for _ in range(n)]
        best_len = 1
        best_i = 0


        for i in range(n-1, -1, -1):
            for j in range(i,n):
                if s[i] == s[j]:
                    if j - i < 2:
                        L[i][j] = True
                    else:
                        L[i][j] = L[i+1][j-1]
                if L[i][j] and j - i + 1 > best_len:
                    best_len, best_i = j - i + 1, i
        return s[best_i : best_i + best_len]
