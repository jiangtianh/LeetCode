class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        visited = set()
        path = set()
        temp = []

        @cache
        def dfs(i):
            if len(graph[i]) == 0:
                temp.append(i)
                return True
            elif i in path:
                return False
            
            visited.add(i)
            path.add(i)
            res = True
            for neighbor in graph[i]:
                res = res and dfs(neighbor)
            path.remove(i)
            if res:
                temp.append(i)
            return res

        
        for i in range(len(graph)):
            if i not in visited:
                dfs(i)
        temp.sort()
        return temp
