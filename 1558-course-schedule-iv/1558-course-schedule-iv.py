class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        graph = collections.defaultdict(list)
        for x, y in prerequisites:
            graph[y].append(x)
    
        def f(i, visited):
            for nei in graph[i]:
                if nei not in visited:
                    visited.add(nei)
                    f(nei, visited)
        
        d = {}

        for i in range(numCourses):
            visited = set()
            f(i, visited)
            d[i] = visited
        
        res = []
        for x, y in queries:
            if x in d[y]:
                res.append(True)
            else:
                res.append(False)
        return res


