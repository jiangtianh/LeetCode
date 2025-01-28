class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visited = set()
        def dfs(x, y):
            visited.add((x, y))
            res = 0
            for i, j in dirs:
                newX, newY = x + i, y + j 
                if 0 <= newX < m and 0 <= newY < n and grid[newX][newY] != 0 and (newX, newY) not in visited:
                    res += dfs(newX, newY)
            return res + grid[x][y]
        res = 0
        for x in range(m):
            for y in range(n): 
                if grid[x][y] == 0 or (x, y) in visited:
                    continue
                res = max(res, dfs(x, y))
        
        return res