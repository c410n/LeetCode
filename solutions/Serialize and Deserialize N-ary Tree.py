class Codec:
    # Left-to-right single-pass list iterator
    class iterList(list):
        def __init__(self, *args, **kwargs):
            super(Codec.iterList, self).__init__(*args, **kwargs)
            self.pos = -1
        def getNext(self):
            self.pos += 1
            if self.pos < len(self):
                return self[self.pos]
            else:
                return None
        def peek(self):
            T = self.pos + 1
            if T < len(self):
                return self[T]
            else:
                return None
        def advance(self):
            self.pos += 1
            
    def deconstruct(self, node, R):
        R.append(str(node.val))
        C = node.children
        if C:
            R.append('{')
            for c in C:
                self.deconstruct(c, R)
            R.append('}')
    
    def serialize(self, root: 'Node') -> str:
        if not root:
            return ""
        Q = [root]
        R = []
        self.deconstruct(root,R)
        return " ".join(R)
        
    def build(self, R: iterList) -> 'Node':
        N = Node(R.getNext(), [])
        
        # Динамо машина
        I = R.peek()
            
        if I == '{':
            R.advance()
            while True:
                I = R.peek()
                if I == '}':
                    R.advance()
                    return N
                N.children.append(self.build(R))
            
        return N
        
    def deserialize(self, data: str) -> 'Node':
        if not data:
            return None
        IL = self.iterList()
        IL.extend(data.split())
        # print(IL)
        return self.build(IL)
        
        
# Implementation for the unique value tree
# """
# # Definition for a Node.
# class Node(object):
#     def __init__(self, val=None, children=None):
#         self.val = val
#         self.children = children
# """

# class Codec:
#     def serialize(self, root: 'Node') -> str:
#         """Encodes a tree to a single string.
        
#         :type root: Node
#         :rtype: str
#         """
#         if root == None:
#             return ""
        
#         Q = [root]
#         R = []
#         while Q:
#             T = []
#             for a in Q:
#                 R.extend([a.val, len(a.children)])
#                 for c in a.children:
#                     R.append(c.val)
#                     T.append(c)
#             Q = T
#         return " ".join(str(x) for x in R)
        
	
#     def deserialize(self, data: str) -> 'Node':
#         """Decodes your encoded data to tree.
        
#         :type data: str
#         :rtype: Node
#         """
#         if not data:
#             return None
        
#         # print(data)
#         data = data.split(' ')
#         P = data[0]
#         R = Node(P, [])
#         HM = {P:R}
#         i = 1
#         while i < len(data):
#             c = i + int(data[i])
#             i += 1
#             while i <= c:
#                 T = Node(int(data[i]), [])
#                 HM[data[i]] = T
#                 HM[P].children.append(T)
#                 i += 1
#             if i < len(data):
#                 P = data[i]
#                 i += 1
#             else:
#                 break
#         # for n in R.children:
#         #     print(n.val, n.children)
#         return R
        

# # Your Codec object will be instantiated and called as such:
# # codec = Codec()
# # codec.deserialize(codec.serialize(root))