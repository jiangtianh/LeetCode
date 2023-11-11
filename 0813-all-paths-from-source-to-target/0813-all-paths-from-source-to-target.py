class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.res = []
        n = len(graph)

        def f(i, temp, visited):
            if i == n - 1:
                temp.append(i)
                self.res.append(temp[:])
                temp.pop()
                return 
            
            temp.append(i)
            visited.add(i)

            for newNode in graph[i]:
                if newNode not in visited:
                    f(newNode, temp, visited)
            temp.pop() 
            visited.remove(i)
        
        f(0, [], set())
        return self.res