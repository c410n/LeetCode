class Solution:
    def checkPosition(self, V, H, y, x):
        for i in range(len(V)):
            if abs(y - V[i]) == abs(x - H[i]):
                return False
        return True
    def iteratePossibilities(self, A, y, R, n, V, H, VS, HS):
        L = []
        for p in range(n):
            if y in VS or p in HS:
                continue
            if not self.checkPosition(V,H,y,p):
                continue
            A[y][p] = 'Q'
            V.append(y)
            VS.add(y)
            H.append(p)
            HS.add(p)
            if y == n-1:
                del L[:]
                for a in A:
                    L.append("".join(a))
                R.append(L)
            else:
                self.iteratePossibilities(A, y+1, R, n, V, H, VS, HS)
            A[y][p] = '.'
            V.pop()
            VS.remove(y)
            H.pop()
            HS.remove(p)
            
            
    def solveNQueens(self, n: int) -> List[List[str]]:
        A = [['.' for _ in range (n)] for _ in range(n)]
        R = []
        V = []
        VS = set()
        H = []
        HS = set()
        self.iteratePossibilities(A, 0, R, n, V, H, VS, HS)
        return R