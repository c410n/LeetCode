class Solution:
    class DJS:
        parent = {}      
        def __init__(self, s):
            for a in s:
                self.add(a)
        def add(self, item):
            self.parent[item] = None
            self.parent[item] = item
        def join(self, item_left, item_right):
            while self.parent[item_right] != item_right: # Understood why I need find operation, cause I'm looking for root
                item_right = self.parent[item_right]
            
            while self.parent[item_left] != item_left: # Understood why I need find operation, cause I'm looking for root
                item_left = self.parent[item_left]  
            
            self.parent[item_right] = item_left
        def __str__(self):
            return str(self.parent)
        def __getitem__(self, id):
            return self.parent[id]
    
    def findCircleNum(self, M: List[List[int]]) -> int:
        if M == None or len(M) < 1:
            return 0  
        elif len(M) == 1:
            return M[0][0]
        
        d = Solution.DJS(range(0, len(M)))
        
        print(d)
        for x in range(len(M)):
            for y in range(x+1, len(M[0])):
                if x == y:
                    continue
                if M[x][y] == 1:
                    d.join(x,y)
        count = 0
        for i in range(len(M)):
            if d[i] == i:
                count += 1
        print(d)
        
        return count