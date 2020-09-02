class Solution:
    def lookForMin(self, n, b, u):
        if b == (u - 1):
            return n[b]
        r = n[b] > n[u-1] 
        if r:
            m = b + math.floor((u - b) / 2)
            return min(self.lookForMin(n, b, m), self.lookForMin(n, m, u))
        else:
            return n[b]
        
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            return nums[0]
        return self.lookForMin(nums, 0, len(nums))