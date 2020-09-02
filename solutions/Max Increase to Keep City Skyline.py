class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        skyline_top = [0] * len(grid)
        skyline_left = [0] * len(grid)
        msum = 0
        
        # O(n) + O(n)
        i1 = 0
        i2 = 0
        while i1 < len(grid):
            i2 = 0
            while i2 < len(grid):
                skyline_left[i1] = max(skyline_left[i1], grid[i1][i2])
                skyline_top[i2] = max(skyline_top[i2], grid[i1][i2])
                i2 += 1
            msum += sum(grid[i1])
            i1 += 1
        
        added = 0
        i1 = 0     
        while i1 < len(grid):
            i2 = 0
            while i2 < len(grid):
                prev_val = grid[i1][i2]
                grid[i1][i2] = min(skyline_left[i1],skyline_top[i2])
                added += grid[i1][i2] - prev_val
                i2 += 1
            i1 += 1
        
        return added