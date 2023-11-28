class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        
        n = len(grid)
        directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0,1], [1, -1], [1, 0], [1, 1]]

        def check(x, y):
            return x in range(n) and y in range(n) and grid[x][y] == 0

        q = collections.deque() 
        
        q.append((0, 0))
        visited = {(0,0)}
        res = 1
        while q:
            
            for _ in range(len(q)):
                curx, cury = q.popleft() 

                if curx == n - 1 and cury == n - 1:
                    return res

                for i, j in directions:
                    newx = curx + i
                    newy = cury + j
                    if check(newx, newy) and (newx, newy) not in visited:
                        visited.add((newx, newy))
                        q.append((newx, newy))
            res += 1
            
        return -1




