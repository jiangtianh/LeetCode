class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        
        self.visited = set()
        self.visited.add(0)
        
        def dfs(n):
            for key in rooms[n]:
                if key not in self.visited:
                    self.visited.add(key)
                    dfs(key)
                    
        dfs(0)
        return len(self.visited) == len(rooms)