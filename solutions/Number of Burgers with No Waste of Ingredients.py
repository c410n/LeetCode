class Solution:
    def numOfBurgers(self, T: int, C: int) -> List[int]:
        if T == 0 and C == 0:
            return [0,0]
        if (bool(T) != bool(C)) or T % 2 > 0 or (T / C) > 4.0 or (T / C) < 2.0:
            return []
        
        D = T // 2
        A = D - C
        
        print(D,A)
        
        return [A,C-A]