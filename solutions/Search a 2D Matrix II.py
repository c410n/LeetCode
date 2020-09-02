# class Solution:
#     @classmethod
#     def performSearch(self, m, t, y, x):
#         if self.found == True:
#             return self.found
#         if y >= len(m) or x >= len(m[0]):
#             return self.found
        
#         if m[y][x] == t:
#             self.found = True
#             return self.found
#         elif m[y][x] < t:
#             return self.performSearch(m, t, y+1, x) or self.performSearch(m, t, y, x+1)
#         elif m[y][x] > t:
#             return self.found
#     @classmethod
#     def searchMatrix(self, matrix, target):
#         """
#         :type matrix: List[List[int]]
#         :type target: int
#         :rtype: bool
#         """
#         if len(matrix) == 0 or len(matrix[0]) == 0:
#             return False
#         if matrix[0][0] == target:
#             return True

#         self.found = False
#         return self.performSearch(matrix, target, 1, 0) or self.performSearch(matrix, target, 0, 1)

class Solution:# 
    @classmethod
    def searchMatrix(self, matrix, target):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        ym = len(matrix)
        xm = len(matrix[0])
        for y in range(ym):
            for x in range(xm):
                # print(matrix[y][x])
                if matrix[y][x] == target:
                    return True
                elif matrix[y][x] > target:
                    break
                else:
                    continue
                
        return False