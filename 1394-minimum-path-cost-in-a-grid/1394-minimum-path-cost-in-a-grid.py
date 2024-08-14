class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        
        lastRow = set()
        for num in grid[-1]:
            lastRow.add(num)
        row = len(grid)
        col = len(grid[0])

        @cache
        def f(x, y):
            n = grid[x][y]
            if n in lastRow:
                return n 
            
            res = math.inf 
            for j in range(col):
                res = min(res, f(x+1, j) + moveCost[n][j])
            return res + n
        res = math.inf
        for i in range(col):
            res = min(res, f(0, i))
    
        return res