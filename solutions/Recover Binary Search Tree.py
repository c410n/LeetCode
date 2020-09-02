# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def IOST(self, node, P):
        if node == None:
            return
        
        self.IOST(node.left, P)
        # print(node.val, P[0].val > node.val, len(P))
        if P[0].val > node.val:
            if len(P) == 1:
                P.append(P[0])
                P.append(node)
            else:
                P.append(node)
                if len(P) >= 4:
                    return
        P[0] = node
        self.IOST(node.right, P)
        
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        P = [TreeNode(-sys.maxsize)]
        self.IOST(root, P)
        
        # print(P[1] if len(P) > 1 else "VOID")
        # print(P[2] if len(P) > 2 else "VOID")
        # print(P[3] if len(P) > 3 else "VOID")
        
        if len(P) == 3:
            t = P[1].val
            P[1].val = P[2].val
            P[2].val = t
            return
        elif len(P) == 1:
            return
        
        t = P[1].val
        P[1].val = P[3].val
        P[3].val = t