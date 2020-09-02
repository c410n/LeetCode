from bisect import bisect_left

class Solution:
    def maxEnvelopes(self, p):
        p.sort(key = lambda x: (x[0],-x[-1]))
        
        def f(nums):
            # print(nums)
            dp = []
            for i in range(len(nums)):
                a = bisect_left(dp,nums[i])
                if a == len(dp):
                    dp.append(nums[i])
                else:
                    dp[a] = nums[i]
                        
            return len(dp)
        
        return f([x[1] for x in p])