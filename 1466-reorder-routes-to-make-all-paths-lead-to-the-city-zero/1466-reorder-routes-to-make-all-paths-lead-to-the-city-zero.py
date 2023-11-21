class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        canReach = set()
        canReach.add(0)
        path = set()
        
        
        graph = collections.defaultdict(list)
        
        for x, y in connections:
            path.add((x, y))
            graph[x].append(y)
            graph[y].append(x)
        
        self.res = 0
        
        def dfs(x):
            for i in range(len(graph[x])):
                y = graph[x][i]
                if y not in canReach:
                    if (x, y) in path:
                        self.res += 1
                    canReach.add(y)
                    dfs(y)
                    
                    
        print(graph)
        dfs(0)
        print(canReach)
        return self.res
            
                
            
            