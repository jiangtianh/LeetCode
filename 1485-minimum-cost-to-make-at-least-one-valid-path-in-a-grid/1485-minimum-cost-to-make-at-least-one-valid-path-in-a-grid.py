class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = {1: [0, 1], 2: [0, -1], 3: [1, 0], 4: [-1, 0]}
        heap = [[0, 0, 0]]
        visited = set()

        while heap:
            cost, x, y = heapq.heappop(heap)
            if x == m - 1 and y == n - 1:
                return cost 
            if (x, y) in visited:
                continue
            visited.add((x, y))
            originalDirection = grid[x][y]            
            for direction in directions:
                i, j = directions[direction]
                newX, newY = x + i, y + j
                if 0 <= newX < m and 0 <= newY < n and (newX, newY) not in visited:
                    if direction == originalDirection:
                        newCost = cost
                    else:
                        newCost = cost + 1
                    heapq.heappush(heap, [newCost, newX, newY])
            


