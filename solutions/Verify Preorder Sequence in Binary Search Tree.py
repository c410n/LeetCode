class Solution:
    # first bigger number from the right is the root of the right child aka node.right
    def verifyPreorder(self, preorder: List[int]) -> bool:
        if preorder == None or len(preorder) < 2:
            return True
        
        import enum
        
        s = [preorder[0]]
        l = -sys.maxsize
        for e in preorder[1:]:
            if l >= e:
                return False
            if s[-1] > e:
                s.append(e)
            else:
                while s and s[-1] < e:
                    l = s.pop()
                s.append(e)
        return True
    
#     def partition(self, p, l, r, ll, a):
#         # print(l, r, p[l:r+1])
        
#         if l == r:
#             # print("Exit")
#             return    
        
#         if a[0] == False:
#             return    
        
#         v = p[l]
        
#         i = l+1
#         while v >= p[i]:
#             if p[i] <= ll:
#                 a[0] = False
#                 return
#             i += 1
            
#         if i > r:
#             self.partition(p, l+1, r, ll, a)
#         else:
#             self.partition(p, l, i-1, ll, a)
#             self.partition(p, i, r, v, a)
    
#     # first bigger number from the right is the root of the right child aka node.right
#     def verifyPreorder(self, preorder: List[int]) -> bool:
#         if preorder == None or len(preorder) < 2:
#             return True
        
#         preorder.append(sys.maxsize)
#         a = [True]
#         self.partition(preorder, 0, len(preorder)-1, -sys.maxsize, a)
#         return a[0]