class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount < 1:
            return 0
        if min(coins) > amount:
            return -1
        D = [0 for _ in range(amount+1)]
        D[0] = 1
        for l in range(amount+1):
            if D[l] == 0:
                continue
            for c in coins:
                if (l + c) <= amount:
                    t = l + c
                    if D[t] == 0:
                        D[t] = D[l]+1
                    else:
                        D[t] = min(D[l]+1, D[t])
        return D[-1]-1
        