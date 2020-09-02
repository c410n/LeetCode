# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def traverse(self, node, d, ret):
        if node == None:
            return '$'
        else:
            val = " ".join([str(node.val),self.traverse(node.left, d, ret),self.traverse(node.right, d, ret)])
            d[val] += 1
            if d[val] == 2:
                ret.append(node)
            return val
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        from collections import defaultdict
        d = defaultdict(int)
        ret = []
        a = self.traverse(root, d, ret)
        return ret
            