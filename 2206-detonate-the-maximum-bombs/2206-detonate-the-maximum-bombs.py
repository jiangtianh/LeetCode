class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        def getDist(i ,j):
            x1, y1, r1 = bombs[i]
            x2, y2, r2 = bombs[j]
            return sqrt(abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2)
            

        graph = collections.defaultdict(list)

        for i in range(len(bombs)):
            r1 = bombs[i][2]
            for j in range(i+1, len(bombs)):
                r2 = bombs[j][2]
                dist = getDist(i ,j)
                if dist <= r1:
                    graph[i].append(j)
                if dist <= r2:
                    graph[j].append(i)

        visited = set()

        def dfs(i, visited):
            res = 1
            for neighbor in graph[i]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    res += dfs(neighbor, visited)
            
            return res
        
        res = 0

        for i in range(len(bombs)):
            res = max(res, dfs(i, set([i])))
        
        return res