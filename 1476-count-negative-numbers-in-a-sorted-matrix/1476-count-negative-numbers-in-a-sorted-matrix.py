class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        res = 0
        i = len(grid[0]) - 1
        for row in grid:
            while i >= 0 and row[i] < 0:
                i -= 1
            res += len(grid[0]) - i - 1
        return res

# [[4,3,2,-1],
#  [3,2,1,-1],
#  [1,1,-1,-2],
#  [-1,-1,-2,-3]]