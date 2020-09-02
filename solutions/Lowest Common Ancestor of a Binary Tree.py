# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:    
    answer = None
    
    def find_both_values_and_return_when_both_where_retrieved(self, node, p_val, q_val):
        if node == None:
            return [False, False]
        if self.answer != None:
            return [False, False]
        
        retval = [False, False]
                
        if node.val == p_val:
            retval[0] = True
        elif node.val == q_val:
            retval[1] = True
        
        tmp_l = self.find_both_values_and_return_when_both_where_retrieved(node.left, p_val, q_val)
        tmp_r = self.find_both_values_and_return_when_both_where_retrieved(node.right, p_val, q_val)
        
        retval[0] |= tmp_l[0]
        retval[1] |= tmp_l[1]
        retval[0] |= tmp_r[0]
        retval[1] |= tmp_r[1]
        
        if self.answer == None and retval[0] == True and retval[1] == True:
            self.answer = node
        
        return retval
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.answer = None
        
        if root == None or (root.left == None and root.right == None):
            return None
                
        self.find_both_values_and_return_when_both_where_retrieved(root, p.val, q.val)
        
        return self.answer

