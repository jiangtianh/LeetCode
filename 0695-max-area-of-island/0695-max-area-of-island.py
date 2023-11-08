from collections import deque 
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.res = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        vertical = len(grid)
        horizontal = len(grid[0])

        def valid(x, y):
            return x in range(vertical) and y in range(horizontal)

        def bfs(x, y):
            q = deque()
            grid[x][y] = 0
            res = 1
            q.append((x, y))
            while q:
                curX, curY = q.popleft()
                for dx, dy in directions:
                    newX, newY = curX + dx, curY + dy
                    if valid(newX, newY) and grid[newX][newY] == 1:
                        q.append((newX, newY))
                        res += 1
                        grid[newX][newY] = 0

            return res

        result = 0
        for i in range(vertical):
            for j in range(horizontal):
                if grid[i][j] == 1:
                    result = max(result, bfs(i, j))

        return result

