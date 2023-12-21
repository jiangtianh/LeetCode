class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        @cache
        def f(x, y):
            
            if x == m-1 and y == n-1:
                return grid[x][y]

            elif x == m or y == n:
                return math.inf 
            
            return min(f(x+1, y), f(x, y+1)) + grid[x][y]
    
        return f(0, 0)
            
            