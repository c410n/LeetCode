class Solution:
    
    p = None
    
    def lookForMin(self, n, d, u):  
        i = d + math.floor((u-d)/2)     
        
        if d == u-1:
            self.p = min(self.p, n[d])
            return
        
        if d == u-2:
            self.p = min(self.p, n[d], n[u-1])
            return
        
        if self.p < n[d] and self.p < n[u-1]:
            return
        
        if n[d] <= n[i] < n[u-1]:
            self.p = min(self.p, n[d])
            return
        if n[d] > n[i] <= n[u-1]:
            self.p = n[i]
            self.lookForMin(n, d, i)
            return
        if n[d] <= n[i] > n[u-1]:
            self.lookForMin(n, i, u)
            return
        if n[d] == n[i] == n[u-1]:
            self.lookForMin(n, d, i)
            self.lookForMin(n, i, u)
            return
            
        
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        self.p = nums[0]
        self.lookForMin(nums, 0, len(nums))
        return self.p