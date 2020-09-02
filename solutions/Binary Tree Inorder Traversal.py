# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        node = root
        b = []
        r = []
        while True:
            # print([x.val for x in b], r, node.val if node != None else 'None')
            if node == None:
                if b:
                    node = b.pop()
                else:
                    return r
            else:
                if node.left != None:
                    b.append(node)
                    t = node
                    node = node.left
                    t.left = None
                    continue
                r.append(node.val)
                if node.right != None:
                    t = node
                    node = node.right
                    t.right = None
                    continue
                node = None