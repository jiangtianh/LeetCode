class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        res = n
        resReachable = n
        graph = collections.defaultdict(dict)
        for x, y, weight in edges:
            graph[x][y] = weight
            graph[y][x] = weight

        
        def f(i):
            heap = [[0, i]]
            visited = set()
            while heap:
                dist, cur = heapq.heappop(heap)
                if cur in visited:
                    continue
                visited.add(cur)
                for neighbor in graph[cur]:
                    if neighbor not in visited and dist + graph[cur][neighbor] <= distanceThreshold:
                        heapq.heappush(heap, [dist + graph[cur][neighbor], neighbor])
            return len(visited)
        
        for i in range(n):
            reachable = f(i)
            if reachable <= resReachable:
                resReachable = reachable
                res = i

        return res