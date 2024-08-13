class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:

        graph = collections.defaultdict(dict)
        for x, y, weight in roads:
            graph[x][y] = weight
            graph[y][x] = weight

        
        heap = [(0, 0)]
        ways = [0] * n
        ways[0] = 1
        dist = [math.inf] * n

        while heap:
            d, cur = heapq.heappop(heap)

            if dist[cur] < d:
                continue
            
            for neighbor in graph[cur]:
                if dist[neighbor] > d + graph[cur][neighbor]:
                    dist[neighbor] = d + graph[cur][neighbor]
                    ways[neighbor] = ways[cur]
                    heapq.heappush(heap, (d + graph[cur][neighbor], neighbor))

                elif dist[neighbor] == d + graph[cur][neighbor]:
                    ways[neighbor] = (ways[neighbor] + ways[cur]) % (10 ** 9 + 7)


        return ways[n-1]