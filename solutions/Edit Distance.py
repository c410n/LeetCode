class Solution:
    T = None
    
    def calculateMinDistance(self, left, right, li, ri): # test tust
        if (li,ri) in self.T:
            return self.T[(li,ri)]
            
        if li == len(left) and ri == len(right):
            return 0
        
        A = pow(2,32)
        B = pow(2,32)
        C = pow(2,32)
          
        if li != len(left):
            B = self.calculateMinDistance(left, right, li+1, ri) + 1
        if ri != len(right):
            A = self.calculateMinDistance(left, right, li, ri+1) + 1
        if li != len(left) and ri != len(right):
            if left[li] == right[ri]:
                C = self.calculateMinDistance(left, right, li+1, ri+1)
            else:
                C = self.calculateMinDistance(left, right, li+1, ri+1) + 1
        
        R = min(A,B,C)
        self.T[(li,ri)] = R        
        return R
        
    def minDistance(self, word1: str, word2: str) -> int:
        self.T = dict()
        return self.calculateMinDistance(word1, word2, 0, 0)
        return self.T[(len(word1)-1,len(word2)-1)]