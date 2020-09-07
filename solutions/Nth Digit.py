class Solution:
    def findNthDigit(self, n: int) -> int:
        c = 9
        l = 1
        while n > l*c:
            n -= l*c
            c *= 10
            l += 1
            
        sn = 10**(l-1)
        
        q, r = divmod(n, l)
        
        # print(n,sn,l,q,r)
        
        if r == 0:
            return int(str(sn + q - 1)[-1])
        else:
            return int(str(sn + q)[r-1])
