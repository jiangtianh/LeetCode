class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        step = 0
        m, n = len(grid), len(grid[0])
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        q = collections.deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "*":
                    q.append((i, j))
                    break
            if len(q) == 1:
                break

        while q:
            for _ in range(len(q)):
                x, y = q.popleft()

                for i, j in dirs:
                    newX, newY = x + i, y + j
                    if 0 <= newX < m and 0 <= newY < n:
                        if grid[newX][newY] == "#":
                            return step + 1
                        elif grid[newX][newY] == "O":
                            q.append((newX, newY))
                            grid[newX][newY] = "*"

            step += 1

        return -1