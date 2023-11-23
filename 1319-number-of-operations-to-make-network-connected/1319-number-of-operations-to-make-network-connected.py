class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        
        if len(connections) < n - 1:
            return -1 

        graph = collections.defaultdict(set)

        for x, y in connections:
            graph[x].add(y)
            graph[y].add(x)

        self.visited = set()

        def f(i):
            for j in graph[i]:
                if j not in self.visited:
                    self.visited.add(j)
                    f(j)
        res = -1
        for i in range(n):
            if i not in self.visited:
                self.visited.add(i)
                f(i)
                res += 1
            
        return res


