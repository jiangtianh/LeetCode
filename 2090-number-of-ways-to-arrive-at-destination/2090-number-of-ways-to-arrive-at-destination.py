class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph = collections.defaultdict(dict)
        for x, y, w in roads:
            graph[x][y] = w
            graph[y][x] = w
        
        ways = [0 for _ in range(n)]
        ways[0] = 1
        dists = [math.inf for _ in range(n)]
        dists[0] = 0
        heap = [[0, 0]]

        while heap:
            curDist, curNode = heapq.heappop(heap)
            if curDist > dists[curNode]:
                continue
            
            for neighbor in graph[curNode]:
                if dists[neighbor] > curDist + graph[curNode][neighbor]:
                    ways[neighbor] = ways[curNode]
                    dists[neighbor] = curDist + graph[curNode][neighbor]
                    heapq.heappush(heap, [curDist + graph[curNode][neighbor], neighbor])
                elif dists[neighbor] == curDist + graph[curNode][neighbor]:
                    ways[neighbor] += ways[curNode]
            
                
        return ways[-1] % (10 ** 9 + 7)
