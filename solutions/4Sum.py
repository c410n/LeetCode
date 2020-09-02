class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        N = sorted(nums)
        R = set()
        for l in range(len(N)):
            for r in range(len(N)):
                ir = r-1
                il = l+1
                while il < ir:
                    # print(l,il,ir,r)
                    A = N[l] + N[il] + N[ir] + N[r]
                    if A < target:
                        il += 1
                    elif A > target:
                        ir -= 1
                    else:
                        R.add((N[l], N[il], N[ir], N[r]))
                        il += 1
                        ir -= 1
        return R