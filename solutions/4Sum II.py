class Solution:
    def collectLRResults(self, A, B):
        r = collections.defaultdict(int)
        for a in A:
            for b in B:
                c = a + b
                r[c] += 1
        return r
                
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        l = self.collectLRResults(A,B)
        r = self.collectLRResults(C,D)
        count = 0
        for a in l.keys():
            v = 0-a
            if v in r.keys():
                count += l[a]*r[v]
        return count