class Solution:
    def longestRepeatingSubstring(self, S: str) -> int:
        D = [[0 for _ in range(len(S)+1)] for _ in range(len(S)+1)]
        R = 0
        for i in range(1, len(S)+1):
            for j in range(i, len(S)+1):
                if i != j and S[i-1] == S[j-1]:
                    D[i][j] = D[i-1][j-1] + 1
                R = max(R, D[i][j])
        return R