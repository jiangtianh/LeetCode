class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        @cache
        def f(x, y):
            if x == len(grid) or y == len(grid[0]) or grid[x][y] == 1:
                return 0 
            elif x == len(grid) - 1 and y == len(grid[0]) - 1:
                return 1
            
            return f(x+1, y) + f(x, y+1)


            
  
        
        return f(0,0)