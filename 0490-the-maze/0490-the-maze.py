class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        visited = set()
        visited.add((start[0], start[1]))
        q = collections.deque()
        q.append(start)
        m, n = len(maze), len(maze[0])

        def inBound(x, y):
            return 0 <= x < m and 0 <= y < n
        def canMove(x, y):
            return maze[x][y] == 0
        
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        while q:
            curX, curY = q.popleft()
            if [curX, curY] == destination:
                return True 
            for i, j in dirs:
                x, y = curX, curY
                while inBound(x+i, y+j) and canMove(x+i, y+j):
                    x += i
                    y += j
                if (x, y) not in visited:
                    q.append((x, y))
                    visited.add((x, y))
        return False