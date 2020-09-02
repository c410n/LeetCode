# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBSTEx(self, root):
        l = None
        r = None
        v = []
        if root.left != None:
            l = self.isValidBSTEx(root.left) # 1,1
            if l == False:
                return False
        if root.right != None:
            r = self.isValidBSTEx(root.right) # 3,3
            if r == False:
                return False
        v = [root.val, root.val] # 2,2
        if l != None:
            if v[0] <= l[1] or l[0] > l[1]: # 2 <= 1 or 1 > 1
                return False
            v[0] = l[0]
        if r != None:
            if v[1] >= r[0] or r[1] < r[0]: # 2 >= 3 or 3 > 3
                return False
            v[1] = r[1]
        print(root.val, v)
        return v
            
        
    def isValidBST(self, root: TreeNode) -> bool:
        if root == None:
            return True
        else:
            return self.isValidBSTEx(root)