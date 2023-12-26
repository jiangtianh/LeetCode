class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        
        self.res = []
        visited = set() 
        path = set()
        
        for x, y in prerequisites:
            graph[x].append(y)
            
        
        def f(i):
            for j in graph[i]:
                if j in path:
                    return False 
                
                if j not in visited:
                    
                    path.add(j)
                    visited.add(j)
                    if not f(j):
                        return False 
                    
                    path.remove(j)
            
            self.res.append(i)
            return True 
    
        for i in range(numCourses):
            if i not in visited:
                visited.add(i)
                path.add(i)
                if not f(i):
                    return []
                path.remove(i)
        return self.res
        
        
        