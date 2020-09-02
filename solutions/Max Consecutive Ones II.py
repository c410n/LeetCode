class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return 0
        elif len(nums) == 1:
            return 1
        
        answer = 0
        
        i = 0        
        z = 0
        while  i < len(nums) and nums[i] == 0:
            i += 1
            z += 0
        prev = i
        middle = i
        if i == len(nums):
            return 1
        while i < len(nums):
            while i < len(nums) and nums[i] == 1:
                i += 1
            res = i - prev
            if answer < res:
                answer = res
                if middle == prev:
                    if middle != 0 or (i < len(nums) and nums[i] == 0):
                        answer += 1
                    
            z = 0
            while  i < len(nums) and nums[i] == 0:
                i += 1
                z += 1
            if middle != prev:
                prev = middle
            if z > 1:
                prev = i
                
            middle = i
        
        return answer