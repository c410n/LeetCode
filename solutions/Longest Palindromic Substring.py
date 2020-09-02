class Solution:
    def longestPalindrome(self, s: str) -> str:
        l = len(s)
        D = [[0 for _ in range(l)] for _ in range(l)]
        R = 1
        I = 0      
        for a in range(l):
            D[a][a] = 1
            if a+1 < l and s[a] == s[a+1]:
                D[a+1][a] = D[a][a+1] = D[a][a] + 1
                R = 2
                I = a
        for i in range(l-1,-1,-1):
            for j in range(l-1, i, -1):
                if s[i] == s[j] and i+1 < l:
                    if not D[i][j] and D[i+1][j-1]:
                        D[i][j] = D[i+1][j-1] + 2
                        if R < D[i][j]:
                            R = D[i][j]
                            I = i
        return s[I:I+R]