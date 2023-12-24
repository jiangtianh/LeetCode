class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        def check(x, y):
            return x in range(len(grid)) and y in range(len(grid[0])) and grid[x][y] == 1
    
        def dfs(x, y):
            res = 1
            grid[x][y] = 0
            for i, j in directions:
                newX, newY = x + i, y + j
                if check(newX, newY):
                    res += dfs(newX, newY)
            return res
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    res = max(res, dfs(i, j))
        return res