class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        dirs = [[0,1,"R"], [0,-1,"L"], [1,0,"D"], [-1,0,"U"]]
        m, n = len(grid), len(grid[0])
        def check(x, y):
            return 0 <= x < m and 0 <= y < n and grid[x][y] == 1
        
        
        def f(x, y):
            path = []
            def dfs(x, y):
                grid[x][y] = 0
                for i, j, c in dirs:
                    newX, newY = x + i, y + j
                    if check(newX, newY):
                        path.append(c)
                        dfs(newX, newY)
                path.append("|")
            dfs(x, y)
            return "".join(path)
        islands = set()
        for x in range(m):
            for y in range(n):
                if grid[x][y] == 1:
                    islands.add(f(x, y))
        return len(islands)