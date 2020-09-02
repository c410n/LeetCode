class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        a = set(nums)

        mmax = 0
        count = 0
        
        while len(a) > 0:
            el = a.pop()
            i = 1
            count = 1
            while el - i in a:
                count+=1
                a.remove(el - i)
                i += 1
                
            i = 1
            while el + i in a:
                count+=1
                a.remove(el + i)
                i += 1
                
            if mmax < count:
                mmax = count
                
        return mmax
            