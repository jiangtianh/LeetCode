class Solution:
    def countPairsOfConnectableServers(self, edges: List[List[int]], signalSpeed: int) -> List[int]:
        graph = collections.defaultdict(dict)
        
        for x, y, w in edges:
            graph[x][y] = w
            graph[y][x] = w
        
        n = len(edges) + 1
        
        def f(node, prev, dist):
            res = 1 if (dist + graph[prev][node]) % signalSpeed == 0 else 0

            for neighbor in graph[node]:
                if neighbor != prev:
                    res += f(neighbor, node, dist + graph[prev][node])
            return res

        res = [0] * n

        for node in range(n):
            temp = []
            result = 0
            for neighbor in graph[node]:
                temp.append(f(neighbor, node, 0))

            for i in range(len(temp)):
                for j in range(i+1, len(temp)):
                    result += temp[i] * temp[j] 
            res[node] = result
        return res           
            
