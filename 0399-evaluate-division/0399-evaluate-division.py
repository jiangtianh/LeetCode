class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = collections.defaultdict(collections.defaultdict)

        for i, [x, y] in enumerate(equations):
            graph[x][y] = values[i]
            graph[y][x] = 1 / values[i]

        visited = set() 
        
        print(graph)

        def dfs(dividend, target):
            if dividend not in graph:
                return -1
            if dividend == target:
                return 1
            res = -1
            for neighbor in graph[dividend]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    temp = dfs(neighbor, target) 
                    if temp != -1:
                        res = temp * graph[dividend][neighbor]
                    visited.remove(neighbor)
            return res
        res = []

        for x, y in queries:
            res.append(dfs(x, y))
        return res







