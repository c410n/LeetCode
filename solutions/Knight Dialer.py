class Solution:
    def knightDialer(self, N: int) -> int:
        MOD = 10**9 + 7
        M = [[4,6],[6,8],[7,9],[4,8],[0,9,3],[],
             [0,7,1],[2,6],[1,3],[4,2]]
        D = [1] * 10 # The first number was already pressed
        for n in range(N-1): # Checking rest of the numbers
            T = [0] * 10
            for i in range(10):
                for E in M[i]:
                    T[E] += D[i]
                    T[E] %= MOD
            D = T
        return sum(D) % MOD
