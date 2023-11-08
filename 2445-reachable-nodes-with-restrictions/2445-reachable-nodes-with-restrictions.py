class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int: 
        self.res = 0

        graph = collections.defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        s = set(restricted)

        visited = set()

        def dfs(n):
            res = 1
            for neighbor in graph[n]:
                if neighbor not in visited and neighbor not in s:
                    visited.add(neighbor)
                    res += dfs(neighbor)
            return res



        visited.add(0)
        return dfs(0)

