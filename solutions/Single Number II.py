class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums_unique_3sum = sum(set(nums))*3
        return int((nums_unique_3sum - sum(nums)) / 2)