class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if nums == None or len(nums) < 1:
            return
        i = 0
        z = 0
        p = None
        c = None
        s = 0
        while (i + z) < len(nums):
            if nums[i + z] == c:
                if p != c:
                    p = c
                    nums[i] = nums[i + z]
                    s += 1
                    i += 1
                else:
                    z += 1
            else:
                c = nums[i + z]
                nums[i] = nums[i + z]
                s += 1
                i += 1
        return s