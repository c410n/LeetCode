# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        r = []
        node = root
        b = []
        while True:
            # print(r, node.val if node != None else 'None', [x.val for x in b])
            if node == None:
                if not b:
                    return r
                node = b.pop()
            else:
                b.append(node)
                r.append(node.val)
            if node.left != None:
                base = node
                node = node.left
                base.left = None                
                continue
            if node.right != None:
                base = node
                node = node.right
                base.right = None
                continue
            node = None
            
        return r