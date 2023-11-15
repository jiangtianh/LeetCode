class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        @cache
        def f(x, prevY):
            if x == len(grid):
                return 0

            res = math.inf
            for i in range(len(grid[0])):
                if i != prevY:
                    res = min(res, f(x+1, i) + grid[x][i])
            
            return res
        
        res = math.inf
        for i in range(len(grid[0])):
            res = min(res, f(0, -1))
        
        return res
                

            


