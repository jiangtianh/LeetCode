
from collections import deque, defaultdict

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        q = deque()
        visited = [False] * n
        matrix = defaultdict(list)

        for x, y in edges:
            matrix[x].append(y)
            matrix[y].append(x)

        q.append(source)
        while q:
            cur = q.popleft()
            if cur == destination:
                return True 

            if not visited[cur]:
                visited[cur] = True 
            
                for i in matrix[cur]:
                    q.append(i)
                
            
        return False