class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return [0,0]
        
        int_data = set()
        for num in nums:
            if num in int_data:
                int_data.remove(num)
            else:
                int_data.add(num)
        return list(int_data)