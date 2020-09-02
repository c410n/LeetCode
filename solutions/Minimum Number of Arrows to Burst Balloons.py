class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        D = sorted(points)
        A = 0
        P = []
        for i in range(len(D)):
            if not P:
                P = D[i]
                A += 1
            else:
                if P[1] >= D[i][0]:
                    P[1] = min(P[1], D[i][1])
                else:
                    P = D[i]
                    A += 1
        return A