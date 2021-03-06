# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        if bool(root1) ^ bool(root2):
            return False
        
        if root1 == None:
            return True
        
        if root1.val != root2.val:
            return False
        
        return (self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left)) or \
                (self.flipEquiv(root1.right, root2.right) and self.flipEquiv(root1.left, root2.left))