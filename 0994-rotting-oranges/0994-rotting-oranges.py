class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        goodOrangeCount = 0
        
        def check(x, y):
            return x in range(m) and y in range(n)
        
        q = collections.deque()
        visited = set()
        for i in range(m):
            for j in range(n):
                if check(i, j) and grid[i][j] == 2:
                    visited.add((i, j))
                    q.append((i, j))
                elif grid[i][j] == 1:
                    goodOrangeCount += 1
                          
                    
        res = 0
        while q:
            res += 1
            for _ in range(len(q)):
                curx, cury = q.popleft()
                
                for i, j in directions:
                    newx, newy = curx + i, cury + j
                    if check(newx, newy)  and grid[newx][newy] == 1 and (newx, newy) not in visited:
                        goodOrangeCount -= 1 
                        if goodOrangeCount == 0:
                            return res
                        grid[newx][newy] = 2
                        visited.add((newx, newy))
                        q.append((newx, newy))
                
            
            
        if goodOrangeCount != 0:
            return -1
        else:
            return 0
                    
                    
                    