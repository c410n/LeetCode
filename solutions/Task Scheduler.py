import heapq
class UniqueCounterHeap:
    indexes = []
    corr = {}
    max_in = 0
    def add(self, item, count):
        if -count in self.corr:
            if item in self.corr[-count]:
                raise ValueError("Can't add")
            self.corr[-count].add(item)
        else:
            self.corr[-count] = {item}
        heapq.heappush(self.indexes, -count)
        if self.max_in < count:
            self.max_in = count

    def peek(self):
        old_max = self.max_in
        if len(self.indexes) == 0:
            return None
        val = heapq.nsmallest(1, self.indexes)[0]
        item = next(iter(self.corr[val]))
        return item, val
        
    def pop(self):
        old_max = self.max_in
        if len(self.indexes) == 0:
            return None
        val = heapq.heappop(self.indexes)
        item = self.corr[val].pop()
        if len(self.corr[val]) == 0:
            del(self.corr[val])        
        val = (-val)
        if val > 0:
            self.add(item, val-1)
        if len(self.indexes) > 0:
            self.max_in = -(heapq.nsmallest(1, self.indexes)[0])
        else:
            self.max_in = 0
        if old_max != self.max_in:
            return (item, val, True)
        return (item, val, False)
                
    def pop_generation(self):
        old_max = self.max_in
        if len(self.indexes) == 0:
            return None
        val = heapq.heappop(self.indexes)
        item = self.corr[val].pop()
        if len(self.corr[val]) == 0:
            del(self.corr[val])        
        val = (-val)
        if len(self.indexes) > 0:
            self.max_in = -(heapq.nsmallest(1, self.indexes)[0])
        else:
            self.max_in = 0
        if old_max != self.max_in:
            return (item, val, True)
        return (item, val, False)

"""
    ["A","A","A","B","B","B"]
    2
"""
    
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)
        
        if len(tasks) < 2:
            return len(tasks)
            
        retval = 0        
        
        A = collections.Counter(tasks) # {A:4, ...}
        B = max(A.values()) # 3
        C = len([x for x,y in A.items() if y == B]) # 2
        if n > (C-1):
            D = (B-1) * (n - (C-1)) # 2
        else:
            D = 0
        E = len(tasks) # 6
        F = B*C # 6
        retval = max(F+D, E)
            
        return retval