class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        @cache
        def f(x, y):
            if x == len(grid) - 1 and y == len(grid[0]) - 1:
                return grid[x][y]
            elif x == len(grid) - 1:
                return grid[x][y] + f(x, y + 1)
            elif y == len(grid[0]) - 1:
                return grid[x][y] + f(x + 1, y)
            
            return grid[x][y] + min(f(x + 1, y), f(x, y+1))
        return f(0,0)
            
            
            
            