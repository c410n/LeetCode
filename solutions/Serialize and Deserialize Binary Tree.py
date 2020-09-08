# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return []
        
        Q = [root]
        R = []
        while Q:
            T = []
            S = None
            for a in Q:
                if a:
                    S = True
                    R.append(a.val)
                    T.append(a.left)
                    T.append(a.right)
                else:
                    R.append(None)
                Q = T
            if not S:
                break
        return R
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        V = TreeNode(data[0])
        Q = [V]
        i = 1
        while i < len(data):
            T = []
            for a in Q:
                if a:
                    if data[i] != None:
                        a.left = TreeNode(data[i])
                    i += 1
                    if data[i] != None:
                        a.right = TreeNode(data[i])
                    i += 1
                    T.append(a.left)
                    T.append(a.right)
            Q = T
        return V

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))