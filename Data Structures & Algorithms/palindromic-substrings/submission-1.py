class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        P = [[0] * n for _ in range(n)]

        for i in range(n-1, -1, -1):
            for j in range(i,n):
                if s[i] == s[j]:
                    if j-i<2:
                        P[i][j] = 1
                    else:
                        P[i][j] = P[i+1][j-1] 
        
        return sum(sum(row) for row in P)