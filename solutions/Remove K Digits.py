class Solution:
    def diminish_by_one(self, data): # case with k >= len(data) was resolved
        i1 = 0
        i2 = 1
        while i2 < len(data):
            if data[i1] > data[i2]:
                del(data[i1])
                return        
            i1 += 1
            i2 += 1
        del(data[i1])
            
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) <= k:
            return "0"
        
        retval = list(num)
        
        # Remove consecutively biggest numbers from the series starting from up-front
        for i in range(k):
            self.diminish_by_one(retval)
        print(retval)
        while len(retval) > 1 and retval[0] == '0':
            del(retval[0])
        
        return "".join(retval)