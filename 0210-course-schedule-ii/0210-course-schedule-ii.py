class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        
        for x, y in prerequisites:
            graph[x].append(y)
        
        path = set() 
        visited = set() 
        res = []
        
        def dfs(i):
            
            path.add(i)
            
            for j in graph[i]:
                if j in path:
                    return False 
                if j not in visited:
                    if not dfs(j):
                        return False 
            
            path.remove(i)
            res.append(i)
            visited.add(i)
            return True
        
        for i in range(numCourses):
            if i not in visited:
                if not dfs(i):
                    return []
        return res
        