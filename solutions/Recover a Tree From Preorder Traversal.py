# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def fillTheTree(self, a, level):
        if not len(a):
            return None
        
        node = None
        if a[-1][0] == level:
            node = TreeNode(a.pop()[1])            
            node.left = self.fillTheTree(a, level+1)
            node.right = self.fillTheTree(a, level+1)
        elif a[-1][0] < level:
            return None
        return node
                
    def recoverFromPreorder(self, S: str) -> TreeNode:
        if len(S) == 0:
            return None 
        if len(S) == 1:
            return TreeNode(S[0])
        i = [0]
        ns = ""
        while i[0] < len(S) and S[i[0]] != '-':
            ns += S[i[0]]
            i[0] += 1
            n = None
            if ns != None:
                n = int(ns)
        a = collections.deque()
        a.appendleft((0, n))
        while i[0] < len(S):
            p = [0]
            while i[0] < len(S) and S[i[0]] == '-':
                p[0] += 1
                i[0] += 1
            ns = None
            while i[0] < len(S) and S[i[0]] != '-':
                if ns == None:
                    ns = ""
                ns += S[i[0]]
                i[0] += 1
            n = None
            if ns != None:
                n = int(ns)
            a.appendleft((p[0],n))
        
        return self.fillTheTree(a, 0)