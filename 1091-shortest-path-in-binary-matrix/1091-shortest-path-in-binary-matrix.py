class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        
        q = collections.deque() 
        q.append((0, 0))
        visited = set()
        visited.add((0, 0))
        directions = [[1, 1], [1, 0], [1, -1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1]]
        
        count = 1
        while q:
            for _ in range(len(q)):
                curX, curY = q.popleft() 
                if curX == len(grid) - 1 and curY == len(grid[0]) - 1:
                    return count
                for i, j in directions:
                    newX, newY = curX + i, curY + j
                    
                    if newX in range(len(grid)) and newY in range(len(grid[0])) and (newX, newY) not in visited and grid[newX][newY] == 0:
                        q.append((newX, newY))
                        visited.add((newX, newY)) 
                        
            count += 1
        
        return -1