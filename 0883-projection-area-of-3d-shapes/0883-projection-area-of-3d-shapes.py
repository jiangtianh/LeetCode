class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        top = 0
        xView = [0] * len(grid)
        yView = [0] * len(grid[0])
        
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] != 0:
                    top += 1
                
                xView[x] = max(xView[x], grid[x][y])
                yView[y] = max(yView[y], grid[x][y])
                
        return top + sum(xView) + sum(yView)
        
        