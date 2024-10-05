class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        visited = set()
        m, n = len(grid), len(grid[0])

        def dfs(x, y):
            visited.add((x, y))
            res = 1
            for i in range(m):
                if grid[i][y] == 1 and (i, y) not in visited:
                    res += dfs(i, y)
            for i in range(n):
                if grid[x][i] == 1 and (x, i) not in visited:
                    res += dfs(x, i)
            return res
        res = 0
        for x in range(m):
            for y in range(n):
                if grid[x][y] == 1 and (x, y) not in visited:
                    p = dfs(x, y)
                    if p != 1:
                        res += p

        return res
