class Solution:
    def asteroidCollision(self, A: List[int]) -> List[int]:
        L = []
        R = []
        S = []
        for a in A:
            if a > 0:
                L.append(a)
            else:
                R.append(a)
            
            # print("T: ", S,L,R)
            
            if R and L:
                while R and L:
                    r = R.pop()
                    l = L.pop()
                    s = r + l
                    if s > 0:
                        L.append(l)
                    elif s < 0:
                        R.append(r)
                    # pass for a == 0
                    
            if R and not L:
                S.extend(R)
                R = []
                
            # print(S,L,R)
                    
        return S + L + R