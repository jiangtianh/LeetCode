class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        n = len(grid)
        m = len(grid[0])
        
        def check(x, y):
            return x in range(n) and y in range(m) and grid[x][y] == "1"
            
        
        def bfs(x, y):
            q = collections.deque()
            q.append((x, y))
            visited = set()
            visited.add((x, y))
            
            while q:
                curX, curY = q.popleft()
                
                for i, j in directions:
                    newX = curX + i
                    newY = curY + j
                    if check(newX, newY) and (newX, newY) not in visited:
                        visited.add((newX, newY))
                        q.append((newX, newY))
                        grid[newX][newY] = "0"
        res = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    res += 1
                    grid[i][j] = "0"
                    bfs(i, j)
        return res 
                    
        
        
        
        
        