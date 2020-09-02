class Solution:
    def findPoisonedDuration(self, T: List[int], duration: int) -> int:
        if len(T) < 1:
            return 0
        p = None
        c = 0
        i = 0
        while i < len(T):
            if p != None:
                if (p + duration) > T[i]:
                    c += T[i] - p
                else:
                    c += duration
            
            p = T[i]
            
            i += 1
            
        c += duration
        
        return c