class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        length = len(edges)
        graph = collections.defaultdict(dict)

        for i in range(length):
            x, y = edges[i]
            succ = succProb[i]
            graph[x][y] = succ
            graph[y][x] = succ
        
        heap = [(-1.0, start_node)]
        visited = set()
        while heap:
            succ, cur = heapq.heappop(heap)

            if cur == end_node:
                return -succ

            if cur in visited:
                continue
            visited.add(cur)
            for neighbor in graph[cur]:
                if neighbor not in visited:
                    heapq.heappush(heap, (succ * graph[cur][neighbor], neighbor))
            




        return 0