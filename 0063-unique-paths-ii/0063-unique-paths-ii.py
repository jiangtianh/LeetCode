class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        @cache
        def f(x, y):
            if x >= len(obstacleGrid) or y >= len(obstacleGrid[0]) or obstacleGrid[x][y] == 1:
                return 0 
            if x == len(obstacleGrid) - 1 and y == len(obstacleGrid[0]) - 1:
                return 1
            return f(x+1, y) + f(x, y+1)
        
        return f(0, 0)
            
            
        
        