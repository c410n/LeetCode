class Solution:
    def calculateMinimumHP(self, D: List[List[int]]) -> int:
        if len(D) < 1 or len(D[0]) < 1:
            return 0
        
        M = [[sys.maxsize for x in range(len(D[0])+1)] for y in range(len(D)+1)]
        
        s = len(D)-1
        si = len(D[0])-1
        M[s+1][si] = 0
        M[s][si+1] = 0
        
        for y in range(s, -1, -1):
            for x in range(si, -1, -1):
                c = D[y][x]
                d = min(M[y+1][x], M[y][x+1])
                if c < 0:
                    c = abs(c) + d
                else:
                    if c >= d:
                        c = 0
                    else:
                        c = d - c
                M[y][x] = c
        # for a in M:
        #    print(a)
        return M[0][0] + 1