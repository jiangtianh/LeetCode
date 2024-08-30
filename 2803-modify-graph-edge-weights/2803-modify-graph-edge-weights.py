class Solution:
    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:
        graph = collections.defaultdict(dict)
        INF = int(2e9)
        for x, y, w in edges:
            if w != -1:
                graph[x][y] = w
                graph[y][x] = w

        def dijkstra(graph):
            heap = [(0, source)]
            visited = set()
            while heap:
                dist, cur = heapq.heappop(heap)
                if cur in visited:
                    continue
                if cur == destination:
                    return dist
                visited.add(cur)
                for neighbor in graph[cur]:
                    if neighbor not in visited:
                        heapq.heappush(heap, (dist + graph[cur][neighbor], neighbor))
    
            return math.inf 



        currentDist = dijkstra(graph)
        if currentDist < target:
            return []

        elif currentDist == target:
            for edge in edges:
                if edge[2] == -1:
                    edge[2] = INF
            return edges

        for i, (x, y, w) in enumerate(edges):
            if w == -1:
                edges[i][2] = 1

                graph[x][y] = 1
                graph[y][x] = 1

                newDist = dijkstra(graph)

                if newDist <= target:
                    edges[i][2] += target - newDist

                    for j in range(i+1, len(edges)):
                        if edges[j][2] == -1:
                            edges[j][2] = INF
                    return edges
        return []