class Solution:
    T = None
    def checkDistance(self, s, t, si, ti, count):
        if (si,ti) in self.T:
            return self.T[(si,ti)]
        if si == len(s) and ti == len(t):
            if count == 1:
                self.T[(si,ti)] = True
                return True
            else:
                return False
            
        if count > 1:
            return False
            
        R = False

        if si != len(s) and ti != len(t):
            if s[si] == t[ti]:
                R = self.checkDistance(s,t,si+1,ti+1,count)
            else:
                R = self.checkDistance(s,t,si+1,ti+1,count+1) or self.checkDistance(s,t,si+1,ti,count+1) or self.checkDistance(s,t,si,ti+1,count+1)
        else:
            if si != len(s):
                R = R or self.checkDistance(s,t,si+1,ti,count+1)
            if ti != len(t):
                R = R or self.checkDistance(s,t,si,ti+1,count+1)
        
        self.T[(si,ti)] = R
        return self.T[(si,ti)]
        
    def isOneEditDistance(self, s: str, t: str) -> bool:
        self.T = dict()
        return self.checkDistance(s, t, 0, 0, 0)