class Solution:
    def minWindow(self, S: str, T: str) -> str:
        if len(T) < 1:
            return ""

        R = dict()
        
        D = [[0 for _ in range(len(S)+1)] for _ in range(len(T)+1)]
        
        i1n = 0
        i2n = 0
        for i1 in range(len(T)):
            i1n = i1+1
            for i2 in range(len(S)):
                i2n = i2+1
                if T[i1] == S[i2]:
                    if i1 == 0:
                        D[i1n][i2n] = 1
                    elif D[i1][i2] > 0:
                        D[i1n][i2n] = D[i1][i2] + 1                    
                    if i1n == len(T) and D[i1n][i2n] >= len(T) and D[i1n][i2n] not in R:
                        R[D[i1n][i2n]] = i2
                else:
                    if D[i1n][i2] > 0:
                        D[i1n][i2n] = D[i1n][i2] + 1

        # for l in D:
        #     print(l)
        # print(R)

        if len(R) < 1:
            return ""
        m = min(R.keys())
        if m == 0:
            return ""
        
        return S[R[m]-m+1:R[m]+1]