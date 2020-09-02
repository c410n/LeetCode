class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        a = list(itertools.chain(*matrix))
        if len(a) == 0:
            return False
        b = bisect.bisect_left(a, target)
        if b < len(a) and a[b] == target:
            return True
        else:
            return False
        