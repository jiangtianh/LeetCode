class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        
        def sort(li):
            graph = collections.defaultdict(list)
            res = []
            for x, y in li:
                graph[x].append(y)
            visited = set()
            path = set()
            self.hasLoop = False

            def f(n):
                visited.add(n)
                path.add(n)
                for neighbor in graph[n]:
                    if neighbor in path:
                        self.hasLoop = True
                    if neighbor not in visited:
                        f(neighbor)
                res.append(n)
                path.remove(n)

            for i in range(1, k+1):
                if i not in visited:
                    f(i)
            if self.hasLoop:
                return []
            res.reverse()
            return res

        matrix = [[0] * k for _ in range(k)]
        row = sort(rowConditions)
        col = sort(colConditions)
        if not row or not col:
            return []
        
        position = collections.defaultdict(list)
        for i, n in enumerate(row):
            position[n].append(i)
        for i, n in enumerate(col):
            position[n].append(i)
        print(position)
        for n in position:
            x = position[n][0]
            y = position[n][1]
            matrix[x][y] = n


        return matrix
