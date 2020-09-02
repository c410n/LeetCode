class Solution:
    def calcH(self, H):
        R = 0
        S = [-1]
        for i in range(len(H)):
            while S[-1] != -1 and H[S[-1]] >= H[i]:
                R = max(R, H[S.pop()] * (i - 1 - S[-1]))
            S.append(i)
        while S[-1] != -1:
            R = max(R, H[S.pop()] * (len(H) - 1 - S[-1]))
        return R
        
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        L = len(matrix)
        if L < 1 or len(matrix[0]) < 1:
            return 0    
        D = [0 for _ in range(len(matrix[0]))]
        R = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                D[j] = D[j] + 1 if matrix[i][j] == '1' else 0
            
            R = max(R, self.calcH(D))
        return R