class Solution:
    def accumulate(self, ret, nums, i, kind):
        ret.append(kind)
        if i == len(nums):
            return
        while i < len(nums):
            self.accumulate(ret, nums, i+1, kind + [nums[i]])
            i += 1
        
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = [[]]
        if nums == None or len(nums) < 1:
            return nums        
        i = 0
        ne = []
        i = 0
        while i < len(nums):
            self.accumulate(ret, nums, i+1, [nums[i]])
            i += 1
        return ret