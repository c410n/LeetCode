class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        
        A = sorted(intervals)
        
        R = []
        
        C = None
        for i in range(len(A)):
            if C == None:
                C = A[i]
            else:
                if C[1] >= A[i][0]:
                    C[1] = max(C[1], A[i][1])
                else:
                    R.append(C)
                    C = A[i]
        
        if C:
            R.append(C)
        
        return R