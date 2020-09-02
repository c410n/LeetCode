class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        L = [0] * len(nums)
        C = [1] * len(nums)
        for i in range(len(nums)):
            for i2 in range(i):
                t = L[i2] + 1
                if nums[i2] < nums[i]:
                    if L[i2] >= L[i]:
                        L[i] = t
                        C[i] = C[i2] # that's in fact like calculating a derivative kind of function
                    elif L[i] == t:
                        C[i] += C[i2] # it's in fact doing combinatorics by counting
        
        #print(L, C)                
        
        if len(L) < 1:
            return 0
        
        m = max(L)
        
        return sum([x for i, x in enumerate(C) if L[i] == m])
        