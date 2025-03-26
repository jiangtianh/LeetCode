class Solution:
    def minimumDistance(self, n: int, edges: List[List[int]], s: int, marked: List[int]) -> int:
        graph = collections.defaultdict(dict)
        for x, y, weight in edges:
            graph[x][y] = min(weight, graph[x].get(y, math.inf))
        marked = set(marked)

        heap = [[0, s]]
        visited = set()
 
        while heap:
            dist, cur = heapq.heappop(heap)
            if cur in visited:
                continue
            elif cur in marked:
                return dist
            visited.add(cur)
            for neighbor in graph[cur]:
                
                heapq.heappush(heap, [dist + graph[cur][neighbor], neighbor])            


        return -1
