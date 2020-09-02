class Solution:
    def iterateOverPositions(self, y, V, VS, H, HS, n):
        r = 0
        if y in VS:
            return 0
                
        for p in range(n):
            if p in HS:
                continue
                
            if not len(VS):
                V.append(y)
                VS.add(y)     
                H.append(p)
                HS.add(p)
                r += self.iterateOverPositions(y+1, V, VS, H, HS, n)
                V.pop()
                VS.remove(y)
                H.pop() 
                HS.remove(p)
            else:
                failed = False
                for i in range(len(VS)):
                    if abs(y - V[i]) == abs(p - H[i]):
                        failed = True
                        break
                if failed == True:
                    continue
                    
                if y == n-1:
                    r += 1
                else:
                    V.append(y)
                    VS.add(y)     
                    H.append(p)
                    HS.add(p)
                    r += self.iterateOverPositions(y+1, V, VS, H, HS, n)
                    V.pop()
                    VS.remove(y)
                    H.pop() 
                    HS.remove(p)
        return r
    
    def totalNQueens(self, n: int) -> int:
        if n < 4:
            if n < 2:
                return 1
            else:
                return 0
        V = []
        VS = set()
        H = []
        HS = set()
        r = self.iterateOverPositions(0, V, VS, H, HS, n)
        return r