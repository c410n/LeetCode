class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        if len(timePoints) < 2:
            return 0
        
        bucket = [0] * (24*60)
                    
        for time_mark in timePoints:
            i = int(time_mark.split(":")[0]) * 60 + int(time_mark.split(":")[1])
            if bucket[i] != 0:
                return 0
            bucket[i] = 1
            
        first = 0
        last = 0
            
        i = 0
        while bucket[i] == 0:
            i = i + 1
        
        first = i
        
        tmp = (23*60) + 59        
        while bucket[tmp] == 0:
            tmp = tmp - 1
            
        last = tmp
        
        ret_min = min(abs(last - first), abs(24*60 - last + first))
        
        i = i+1
        while i <= tmp:
            if bucket[i] != 0:
                diff = i - first
                if ret_min > diff:
                    ret_min = diff
                first = i
            i = i + 1
        
        return ret_min