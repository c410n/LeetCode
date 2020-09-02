class Solution:
    def maxPoints(self, P: List[List[int]]) -> int:
        S = len(P)
        if S < 2:
            return S
        P = sorted(P)
        
        # print(P) # 1
        
        m = 0
        for y in range(S-1):
            
            # print("ITERATION") # 2
            
            R = collections.defaultdict(lambda:1)
            c = 0
            for x in range(y+1, S):
                t1 = P[x][0] - P[y][0]
                t2 = P[x][1] - P[y][1]
                if t1 == 0 and t2 == 0:
                    c += 1
                elif t1 == 0: # verticals
                    R[(0, P[x][0])] += 1
                elif t2 == 0: # horizontals
                    R[(sys.maxsize, P[x][1])] += 1
                else:
                    gcd = math.gcd(t1, t2)
                    k = (int(t1 / gcd), int(t2 / gcd))
                    
                    # print(k, gcd) # 3
                    
                    R[k] += 1
                    
                # print("R:", R, " t1:", t1, " t2:", t2, " c:", c, " y:", y, " x:", x) # 4
                
            if len(R):
                m = max(max(R.values())+c, m)                
            else:
                m = max(1+c, m)
        
        return m