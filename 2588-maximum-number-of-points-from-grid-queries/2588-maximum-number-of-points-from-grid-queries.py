class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        res = {}
        k = len(queries)
        m, n = len(grid), len(grid[0])
        sortedQ = sorted(queries)

        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        heap = [[grid[0][0], 0, 0]]
        visited = set()
        queryIdx = 0
        while heap:
            cur, x, y = heapq.heappop(heap)
            if (x, y) in visited:
                continue
            
            while queryIdx < k and sortedQ[queryIdx] <= cur:
                res[sortedQ[queryIdx]] = len(visited)
                queryIdx += 1
            
            visited.add((x, y))
        
            for i, j in dirs:
                newX, newY = x + i, y + j
                if 0 <= newX < m and 0 <= newY < n and (newX, newY) not in visited:
                    heapq.heappush(heap, [grid[newX][newY], newX, newY])
        
        while queryIdx < k:
            res[sortedQ[queryIdx]] = len(visited)
            queryIdx += 1

        return [res[q] for q in queries]