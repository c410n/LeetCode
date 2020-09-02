class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        a = collections.Counter(p)
        
        retval = []
        
        distance = len(p)-1
        i = 0
        while i < len(s):
            if s[i] in a:
                a[s[i]] -= 1 
                import functools
                if a[s[i]] == 0 and i-distance >=0:
                    if functools.reduce(lambda x,y: x | y, a.values()) == 0:
                        retval.append(i-distance)
            if i-distance >=0 and s[i-distance] in a:
                a[s[i-distance]] += 1               
            i += 1
        return retval