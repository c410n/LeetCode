class Solution:
    T = None
    
    def build_occurences(self, s1, s2, s3, i1, i2, i3):
        if self.T[i1][i2] != None:
            return self.T[i1][i2]
        
        # print("{} {} {}".format(i1,i2,i3))
        retval = False
        
        if i1 >= len(s1) and i3 >= len(s3) and i2 >= len(s2) and i3 >= len(s3):
            return True        
        
        if i3 >= len(s3):
            return False
        
        if i1 < len(s1):
            if s1[i1] == s3[i3]:
                retval |= self.build_occurences(s1, s2, s3, i1+1, i2, i3+1)
        
        if i2 < len(s2):
            if s2[i2] == s3[i3]:
                retval |= self.build_occurences(s1, s2, s3, i1, i2+1, i3+1)
            
        self.T[i1][i2] = retval
        
        return retval
    
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        self.T = [[None]*(len(s2)+1) for _ in range(len(s1)+1)]
        
        return self.build_occurences(s1, s2, s3, 0, 0, 0)