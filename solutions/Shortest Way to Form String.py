class Solution:
#     def explore(self, b, d, i, l):
#         if i == l:
#             return 0
#         ar = set()
#         if i in b:
#             for t in b[i]:
#                 print(t)
#                 ar.add(self.explore(b, d, i + d[t], l))
#         print(ar)
        
#         if len(ar) == 0:
#             return None
        
#         return 1 + min(ar)
    
    def shortestWay(self, source: str, target: str) -> int:
        # T = [[0 for _ in range(len(source)+1)] for _ in range(len(target)+1)]
        # d = collections.defaultdict(int)
        # b = collections.defaultdict(set)
        # for i1 in range(len(target)):
        #     for i2 in range(len(source)):
        #         if target[i1] == source[i2]:
        #             c = T[i1][i2] + 1
        #             T[i1+1][i2+1] = c
                    # if T[i1-(c-2)][i2-(c-2)] != 0:
                    #     l = i1-(c-2)
                    #     r = i2-(c-2) 
                    #     T[l][r] = c
                    #     d[(l,r)] = c
                    #     if c == 1:
                    #         b[i1].add((l,r))
               
        a = 0
        c = 0
        while a < len(target):
            d = 0
            f = False
            while d < len(source):
                if target[a] == source[d]:
                    a += 1
                    f = True
                d += 1
                if a == len(target):
                    break
                    
            if f == True:
                c += 1
            else:
                return -1
        
        return c
                
                
        # for a in range(len(target)):
        #     print(target[a], T[a+1][1:])