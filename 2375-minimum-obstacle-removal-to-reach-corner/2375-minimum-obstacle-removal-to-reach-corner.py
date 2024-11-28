class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visited = set()
        li = [(0, 0, 0)]
        m = len(grid)
        n = len(grid[0])
        
        while li:
            removed, x, y = heapq.heappop(li)
            if (x, y) in visited:
                continue 
            elif x == m - 1 and y == n - 1:
                return removed
            visited.add((x, y))
            for i, j in dirs:
                newX, newY = x + i, y + j
                if 0 <= newX < m and 0 <= newY < n:
                    if grid[newX][newY] == 1:
                        heapq.heappush(li, (removed+1, newX, newY))
                    else:
                        heapq.heappush(li, (removed, newX, newY))
        