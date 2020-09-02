class Solution:       
    def alignNumbers(self, N):
        if len(N) < 2:
            return
        
        m = math.floor(len(N)/2)
        lA = N[:m]
        rA = N[m:]
        
        self.alignNumbers(lA)
        self.alignNumbers(rA)
        
        il = 0
        ir = 0
        i = 0
        ret = [0] * len(N)
        while il < len(lA) and ir < len(rA):
            if lA[il] < rA[ir]:
                ret[i] = lA[il]
                il += 1
                i += 1
            else:
                ret[i] = rA[ir]
                ir += 1
                i += 1
       
        if il < len(lA):
            ret[i:] = lA[il:]
        if ir < len(rA):
            ret[i:] = rA[ir:]
        N[:] = ret[:]
        
    def sortArray(self, nums: List[int]) -> List[int]:
        self.alignNumbers(nums)
        return nums