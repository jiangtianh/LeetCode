import heapq
from typing import List

class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        # Fix 2: Check if spawning on the first cell kills you
        if grid[0][0] >= health:
            return False
            
        heap = [(grid[0][0], 0, 0)]
        visited = set()
        m, n = len(grid), len(grid[0])
        dirs = [[0,1], [0,-1], [1,0], [-1,0]]
        
        while heap:
            cost, x, y = heapq.heappop(heap)
            
            if x == m - 1 and y == n - 1:
                return True
                
            if (x, y) in visited:
                continue

            visited.add((x, y))

            for i, j in dirs:
                newX, newY = x + i, y + j
                if 0 <= newX < m and 0 <= newY < n:
                    # Fix 1: Add the cost of the *target* cell, not the current one
                    newCost = cost + grid[newX][newY]
                    if newCost < health:
                        heapq.heappush(heap, (newCost, newX, newY))

        return False