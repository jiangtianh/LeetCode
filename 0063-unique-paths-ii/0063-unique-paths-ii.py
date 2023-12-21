class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        @cache 
        def f(x, y):
            
        
            if x == m or y == n or obstacleGrid[x][y] == 1:
                return math.inf
            
            elif x == m-1 and y == n-1:
                return 1
            
            bottom = f(x+1, y)
            right = f(x, y+1)
            
            if bottom == math.inf and right == math.inf:
                return math.inf 
            elif bottom == math.inf:
                return right
            elif right == math.inf:
                return bottom 
            else:
                return bottom + right
            
        res = f(0, 0)
        if res == math.inf:
            return 0 
        return res
        
        