# O(n), O(1) in space

class Solution:
    def calculate(self, a, l, r, val):
        v = 0
        l += 1
        while l < r:
            s = val - a[l]
            v += s
            l += 1
        return v
    def trap(self, h: List[int]) -> int:
        if len(h) < 3:
            return 0
        l = 0
        r = l+1
        count = 0
        lm = h[l]
        while l < len(h) and r < len(h):
            rfound = False
            while r < len(h) and lm <= h[r]:
                l = r
                r += 1
                lm = h[l]
            m = 0
            n = 0
            while r < len(h) and lm > h[r]:
                n = min(h[r], n)
                if h[r] > n:
                    m = max(h[r], m)
                r += 1
            if r < len(h) and lm <= h[r]:
                rfound = True
            r = min(len(h)-1,r)
            if rfound == True:
                count += self.calculate(h,l,r,lm)
                l = r
                lm = h[l]
            else:
                if lm == 0:
                    return count
                lm = m
                r = l
            r += 1
            
        return count