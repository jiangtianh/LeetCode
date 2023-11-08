class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:

        visited = set()
        visited.add((entrance[0], entrance[1]))
        horitontal = len(maze[0])
        vertical = len(maze)

        def valid(x, y):
            return x in range(vertical) and y in range(horitontal)

        q = collections.deque()

        dirs = [[1,0],[-1,0],[0, 1],[0,-1]]

        for dx, dy in dirs:
            newX, newY = entrance[0] + dx, entrance[1] + dy
            if valid(newX, newY) and maze[newX][newY] == ".":
                q.append((newX, newY))
                visited.add((newX, newY))
        
        res = 1
        while q:
            for _ in range(len(q)):
                curX, curY = q.popleft() 
                for dx, dy in dirs:
                    newX, newY = curX + dx, curY + dy
                    if not valid(newX, newY):
                        return res 
                    else:
                        if maze[newX][newY] == "." and (newX, newY) not in visited:
                            q.append((newX, newY))
                            visited.add((newX, newY))

            res += 1

        return -1







[["+",".","+","+","+","+","+"],
 ["+",".","+",".",".",".","+"],
 ["+",".","+",".","+",".","+"],
 ["+",".",".",".","+",".","+"],
 ["+","+","+","+","+",".","+"]]

















































