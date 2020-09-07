class Solution:
    def twoCitySchedCost(self, C: List[List[int]]) -> int:
        C = sorted(C, key=lambda x:x[1]-x[0])
        return sum([x[1] for x in C[:int(len(C)/2)]]) + sum([x[0] for x in C[int(len(C)/2):]])