class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        D = [1 for _ in range(len(nums))]
        for a in range(1, len(nums)):
            for b in range(0, a):
                if nums[a] > nums[b] and D[b] >= D[a]:
                    D[a] = D[b] + 1
        return max(D)