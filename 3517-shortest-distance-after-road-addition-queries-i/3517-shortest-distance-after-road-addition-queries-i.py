class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        for i in range(1, n):
            graph[i-1].append(i)
        
        def f(graph, n):
            q = collections.deque()
            q.append(0)
            visited = set([0])
            dist = 0
            while q:
                for _ in range(len(q)):
                    cur = q.popleft()
                    if cur == n - 1:
                        return dist
                    for neighbor in graph[cur]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            q.append(neighbor)
                dist += 1
            return -1
        res = []
        for x, y in queries:
            graph[x].append(y)
            res.append(f(graph, n))
        return res            