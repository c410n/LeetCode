"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        data = {}
        start = node
        nodes = [node]
        ne = None
        while len(nodes) > 0:
            ne = []
            for t in nodes:
                a = Node(t.val, [x.val for x in t.neighbors])
                data[a.val] = a
                for d in t.neighbors:
                    if d.val in data:
                        continue
                    ne.append(d)
            nodes = ne[:]
            if len(nodes) == 0:
                break
        retval = None
        for a in data.keys():
            if retval == None:
                retval = data[a]
            data[a].neighbors = [data[x] for x in data[a].neighbors]                
        
        return retval
        