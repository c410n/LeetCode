# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return 1
        nodes = set()
        b = (1, root.val)
        if root.left != None:
            nodes.add(root.left)
        if root.right != None:
            nodes.add(root.right)
        ind = 2
        while len(nodes) > 0:
            val = 0
            cand = set()
            for a in nodes:
                val += a.val
                if a.left != None:
                    cand.add(a.left)
                if a.right != None:
                    cand.add(a.right)
            if b[1] < val:
                b = (ind, val)
            ind += 1
            nodes.clear()
            nodes = cand
        return b[0]
