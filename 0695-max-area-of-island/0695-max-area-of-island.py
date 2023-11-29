class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        m = len(grid[0])
        n = len(grid)
        
        
        def check(x, y):
            return x in range(n) and y in range(m) and grid[x][y] == 1
        
        
        def bfs(x, y):
            q = collections.deque() 
            q.append((x, y))
            res = 0
            while q:
                curX, curY = q.popleft()
                res += 1
                for i, j in directions:
                    newX, newY = curX + i, curY + j
                    if check(newX, newY):
                        grid[newX][newY] = 0
                        q.append((newX, newY))
            return res
            
        res = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    res = max(res, bfs(i, j))
        
        return res
        
        