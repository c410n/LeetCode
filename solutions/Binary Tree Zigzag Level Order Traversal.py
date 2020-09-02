# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        p = [root]
        n = None
        
        retval = []
        retval.append([root.val])
        direction = True

        while True:
            n = []
            while len(p) > 0:
                nn = p.pop(0)
                if nn.left != None:
                    n.append(nn.left)
                if nn.right != None:
                    n.append(nn.right)
            tmp = [x.val for x in n]
            if direction == True:
                tmp = tmp[::-1]
            if len(tmp) > 0:
                retval.append(tmp)
            direction = not direction
            p = n[:]
            if len(p) == 0:
                break
        
        return retval