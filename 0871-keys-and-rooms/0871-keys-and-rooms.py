from collections import deque
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set() 
        visited.add(0)

        q = deque()
        for key in rooms[0]:
            visited.add(key)
            q.append(key)

        while q:
            cur = q.popleft() 
            
            for key in rooms[cur]:
                if key not in visited:
                    q.append(key)
                    visited.add(key)
            

        return len(visited) == len(rooms)

        



