import collections, sys
class Solution:
    def mincostTickets(self, D: List[int], C: List[int]) -> int:
        L = len(D)
        if L < 2:
            return min(C[0])
        @lru_cache(None)
        def recurse(s):
            if s >= L:
                return 0
            ans = sys.maxsize
            i = s
            for c,d in zip(C,[1,7,30]):
                while i < L and D[i] < D[s] + d:
                    i += 1
                ans = min(ans, recurse(i) + c)
            return ans
                                    
        return recurse(0)