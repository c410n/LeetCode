class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        R = 0
        
        for a in zip(*A):
            if any(a[i] > a[i+1] for i in range(len(a)-1)):
                R += 1
            
        return R