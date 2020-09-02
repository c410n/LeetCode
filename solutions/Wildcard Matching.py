class Solution:
    def matchNext(self, s, p, si, pi, T):
        if (si, pi) in T:
            return T[((si, pi))]
        
        if si == len(s) and pi == len(p):
            T[(si, pi)] = True
            return True
                
        R = False
        
        if si == len(s) or pi == len(p):
            if si == len(s):
                if p[pi] == '*':
                    R |= self.matchNext(s, p, si, pi+1, T)
                
                T[(si,pi)] = R
                return R
            else:
                T[(si, pi)] = False
                return False
        
        if p[pi] == '?':
            R |= self.matchNext(s, p, si+1, pi+1, T)
        elif p[pi] == '*':
            R |= self.matchNext(s, p, si, pi+1, T)
            R |= self.matchNext(s, p, si+1, pi+1, T)
            R |= self.matchNext(s, p, si+1, pi, T)
        else:
            if s[si] != p[pi]:
                T[(si,pi)] = False
                return False
            R |= self.matchNext(s, p, si+1, pi+1, T)
            
        T[(si, pi)] = R
        
        return R
        
    def isMatch(self, s: str, p: str) -> bool:
        T = dict()
        R = self.matchNext(s, p, 0, 0, T)
        # print(T)
        return R