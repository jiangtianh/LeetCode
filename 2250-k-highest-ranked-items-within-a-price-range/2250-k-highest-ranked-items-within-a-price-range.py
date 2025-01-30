class Solution:
    def highestRankedKItems(self, grid: List[List[int]], pricing: List[int], start: List[int], k: int) -> List[List[int]]:
        
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        m, n = len(grid), len(grid[0])
        low, high = pricing[0], pricing[1]

        q = collections.deque([start])

        dist = 0
        visited = set()
        visited.add((start[0], start[1]))
        res = []
        while q:
            for _ in range(len(q)):
                x, y = q.popleft()
                if low <= grid[x][y] <= high:
                    res.append([dist, grid[x][y], x, y])
                for i, j in dirs:
                    newX, newY = x + i, y + j
                    if 0 <= newX < m and 0 <= newY < n and grid[newX][newY] != 0 and (newX, newY) not in visited:
                        visited.add((newX, newY))
                        q.append((newX, newY))               
            dist += 1

        heapq.heapify(res)
        result = []
        while k and res:
            _, _, x, y = heapq.heappop(res)
            result.append([x, y])
            k -= 1
        return result