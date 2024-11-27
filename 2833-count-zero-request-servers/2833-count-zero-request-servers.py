class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        d = {}
        logs.sort(key=lambda x: x[1])
        l = r = 0

        res = {}
        
        for q in sorted(queries):
            while r < len(logs) and logs[r][1] <= q:
                server = logs[r][0]
                if server not in d:
                    d[server] = 0
                d[server] += 1
                r += 1
            
            while l < r and logs[l][1] < q - x:
                server = logs[l][0]
                d[server] -= 1
                if d[server] == 0:
                    d.pop(server)
                l += 1
            res[q] = n - len(d)
        
        result = [res[q] for q in queries]
        return result