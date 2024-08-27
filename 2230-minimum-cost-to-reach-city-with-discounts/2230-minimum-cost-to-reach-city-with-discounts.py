class Solution:
    def minimumCost(self, n: int, highways: List[List[int]], discounts: int) -> int:
        graph = collections.defaultdict(dict)
        for x, y, toll in highways:
            graph[x][y] = toll
            graph[y][x] = toll

        heap = [(0, 0, discounts)]
        visited = set()


        while heap:
            toll, city, discount = heapq.heappop(heap)
            if (city, discount) in visited:
                continue
            visited.add((city, discount))
            if city == n-1:
                return toll

            for neighbor in graph[city]:
                if (neighbor, discount) not in visited:
                    heapq.heappush(heap, (toll+graph[city][neighbor], neighbor, discount))
                if discount > 0 and (neighbor, discount-1) not in visited:
                    heapq.heappush(heap, (toll+graph[city][neighbor]//2, neighbor, discount-1))
        
        return -1
        




