class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        R = 0
        S = [-1]
        for h in range(len(heights)):
            while S[-1] != -1 and heights[S[-1]] >= heights[h]:
                R = max(R, heights[S.pop()] * (h - S[-1] - 1))
            S.append(h)
        while S[-1] != -1:
            R = max(R, heights[S.pop()] * (len(heights) - S[-1] - 1))
        return R