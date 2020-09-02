# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def reconstructTree(self, R, P, i, U):
        ri = i[0]
        if ri >= len(P):
            return
        if P[ri] > U:
            return
        if P[ri] <= R.val:
            R.left = TreeNode(P[ri])
            i[0] = ri+1
            self.reconstructTree(R.left, P, i, R.val)
        ri = i[0]
        if ri >= len(P):
            return
        if P[ri] > U:
            return
        R.right = TreeNode(P[ri])
        i[0] = ri+1
        self.reconstructTree(R.right, P, i, U)
        
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return None
        
        R = TreeNode(preorder[0])
        
        self.reconstructTree(R, preorder, [1], sys.maxsize)
        return R