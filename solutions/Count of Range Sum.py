class Solution:        
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        if len(nums) < 1:
            return 0
        if len(nums) < 2:
            return 1 if nums[0] >= lower and nums[0] <= upper else 0

        P = [0]
        R = 0
        
        s = 0
        for i in range(len(nums)):
            s += nums[i]
            
            lt = s - lower
            rt = s - upper
            
            lv = bisect.bisect_right(P, lt)
            rv = bisect.bisect_left(P, rt)
            
            R += lv - rv
            
            bisect.insort(P, s)
        
        return R