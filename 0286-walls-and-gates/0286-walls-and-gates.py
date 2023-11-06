from collections import deque 
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        horizontal = len(rooms[0])
        vertical = len(rooms)
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        q = deque() 
        empty = 2147483647
        distance_to_gate = 0
        wall = -1

        visited = set()

        for i in range(vertical):
            for j in range(horizontal):
                if rooms[i][j] == 0:
                    q.append((i, j))
                    visited.add((i, j))
        
        print(q)
        while q:
            for _ in range(len(q)):
                x, y = q.popleft()
                
                rooms[x][y] = distance_to_gate

                for i, j in dirs:
                    newX, newY = x + i, y + j
                    if newX in range(vertical) and newY in range(horizontal) and (newX, newY) not in visited and rooms[newX][newY] == empty:   
                        q.append((newX, newY))
                        visited.add((newX, newY))
            distance_to_gate += 1


        