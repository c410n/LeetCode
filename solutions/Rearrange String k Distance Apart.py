class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if len(s) < 2:
            return s
        
        c = collections.Counter(s)
        d = []
        for a in c:
            heapq.heappush(d, (-c[a], a))
        n = []
        ts = set()
        c = 0
        i = 0
        while len(d):             
            e = heapq.heappop(d)                
            v = (e[0] + 1, e[1])
            
            n.append(v[1])
            ts.add(v)
            i += 1
            
            c += 1
            if c >= k:
                c = 0
                for a in ts:
                    if a[0] < 0:
                        heapq.heappush(d, a)
                ts = set()
        if i == len(s):
            return "".join(n)
        else:
            return ""