class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        q = collections.deque()
        
        q.append(0)
        visited = set()
        visited.add(0)
        
        while q:
            cur = q.popleft() 
            for key in rooms[cur]:
                if key not in visited:
                    q.append(key)
                    visited.add(key)
        
        return len(visited) == len(rooms)