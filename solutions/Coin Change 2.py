class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        M = [0 for _ in range(amount+1)]
        
        M[0] = 1
        for c in coins:
            for n in range(c, amount+1):
                M[n] = M[n] + M[n-c]
        
        return M[len(M)-1]