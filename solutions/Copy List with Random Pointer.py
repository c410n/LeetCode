"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:    
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head == None:
            return None
        ret_head = None
        seti = {}
        node = head
        node_clone = Node(node.val, None, None)
        if node.random != None:
            node_clone.random = node.random.val
        seti[node_clone.val] = node_clone
        ret_head = node_clone
        while node.next != None:
            node = node.next
            parent_clone = node_clone
            node_clone = Node(node.val, None, None)
            if node.random != None:
                node_clone.random = node.random.val            
            parent_clone.next = node_clone
            seti[node_clone.val] = node_clone
                
        #--------------------------------------------
        
        node = ret_head
        while node != None:
            if node.random != None:
                node.random = seti[node.random]
            node = node.next
        
        return ret_head