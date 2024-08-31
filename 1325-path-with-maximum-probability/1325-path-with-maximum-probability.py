class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = collections.defaultdict(dict)

        for i in range(len(edges)):
            x, y = edges[i]
            p = succProb[i]
        
            graph[x][y] = p
            graph[y][x] = p
        
        heap = [[-1, start_node]]
        visited = set()
        while heap:
            prob, cur = heapq.heappop(heap)

            if cur == end_node:
                return -prob
            
            if cur in visited:
                continue 
            visited.add(cur)
            for nei in graph[cur]:
                if nei not in visited:
                    heapq.heappush(heap, [prob * graph[cur][nei], nei])
        
        return 0