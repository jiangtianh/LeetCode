class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = [[0] * n for _ in range(n)]
        
        for x, y, weight in flights:
            graph[x][y] = weight
        
        @cache
        def f(i, stop):
            if i == dst and stop >= -1:
                return 0
            
            if stop < -1:
                return math.inf 
            
            res = math.inf 
            for j in range(len(graph[i])):
                if graph[i][j] != 0:
                    temp = f(j, stop - 1)
                    if temp != math.inf:
                        res = min(res, temp + graph[i][j])
            return res
    
        res = f(src, k)
        if res == math.inf:
            return -1
        else:
            return res