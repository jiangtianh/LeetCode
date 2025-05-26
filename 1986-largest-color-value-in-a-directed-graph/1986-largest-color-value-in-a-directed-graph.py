class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        graph = collections.defaultdict(list)
        for x, y in edges:
            graph[x].append(y)

        topoSort = []
        visited = set()
        path = set()
        def f(node):
            visited.add(node)
            path.add(node)
            for neighbor in graph[node]:
                if neighbor in path:
                    return False
                if neighbor not in visited:
                    if not f(neighbor):
                        return False
            topoSort.append(node)
            path.remove(node)
            return True
        for node in range(n):
            if node not in visited:
                if not f(node):
                    return -1
        topoSort.reverse()

        print(topoSort)
        dp = [[0] * 26 for _ in range(len(topoSort))]

        allColors = set(colors)
        print(allColors)
        visited = set()
        def count(node):
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    count(neighbor)
                for color in allColors:
                    colorIdx = ord(color) - ord('a')
                    neighborCount = dp[neighbor][colorIdx]
                    dp[node][colorIdx] = max(dp[node][colorIdx], neighborCount)
            dp[node][ord(colors[node]) - ord('a')] += 1
        
        for node in topoSort:
            if node not in visited:
                count(node)
        
        return max(max(li) for li in dp)


        

