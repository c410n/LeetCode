class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if nums == None or len(nums) < 3:
            return []
        import bisect
        a = sorted(nums)
        print(a)
        mmin = a[0]
        mmax = a[len(a)-1]
        retval = set()
        b = len(a)
        k = 0
        for i in range(b):
            target = -(a[i])
            left = i+1
            right = b-1
            prevl = None
            prevr = None
            while left < right:
                val = a[left] + a[right]
                if val == target:
                    retval.add((a[i],a[left],a[right]))
                    prevl = a[left]
                    prevr = a[right]
                    left += 1
                    while left < right and prevl == a[left]:
                        left += 1
                elif val < target:
                    left += 1
                    while left < right and prevl == a[left]:
                        left += 1
                else:
                    right -= 1
                    while left < right and prevr == a[right]:
                        right -= 1
                
        return list(retval)