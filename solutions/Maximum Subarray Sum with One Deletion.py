class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        if len(arr) == 0:
            return -1
        if len(arr) == 1:
            return arr[0]
        R1 = [0 for _ in range(len(arr)+1)]
        for i in range(len(arr)):
            c = R1[i] + arr[i]
            if c < arr[i]:
                R1[i+1] = arr[i]
            else:
                R1[i+1] = c
        R2 = [0 for _ in range(len(arr)+1)]
        for i in reversed(range(len(arr))):
            c = R2[i+1] + arr[i]
            if c < arr[i]:
                R2[i] = arr[i]
            else:
                R2[i] = c
        il = 1
        ir = 2
        m = max(R2[0], R2[1])
        while ir < len(R2)-1:
            m = max(R1[il] + R2[ir], m, R1[il], R2[ir])
            il += 1
            ir += 1
        m = max(R1[il] + R2[ir], m, R1[il])
            
        return m