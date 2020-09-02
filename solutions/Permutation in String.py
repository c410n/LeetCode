class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        i = 0
        c = collections.Counter(s1)
        distance = len(s1) - 1
        while i < len(s2):
            if s2[i] in c:
                c[s2[i]] -= 1
                if c[s2[i]] == 0:
                    import functools
                    if functools.reduce(lambda x,y:(x)|y,c.values()) == 0:
                        return True
            if i-distance >= 0 and s2[i-distance] in c:
                c[s2[i-distance]] += 1
            i += 1
        return False