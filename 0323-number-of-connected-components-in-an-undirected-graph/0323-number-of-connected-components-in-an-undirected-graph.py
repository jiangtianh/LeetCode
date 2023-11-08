class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        graph = collections.defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        visited = set() 

        def dfs(i):
            visited.add(i)
            for edge in graph[i]:
                if edge not in visited:
                    dfs(edge)
        res = 0
        for edge in range(n):
            if edge not in visited:
                res += 1
                dfs(edge)

        return res