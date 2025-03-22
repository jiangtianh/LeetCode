class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = collections.defaultdict(set)
        for x, y in edges:
            graph[x].add(y)
            graph[y].add(x)

        visited = set()
        def f(node):
            visited.add(node)
            res = 1
            li = [node]
            for neighbor in graph[node]:
                if neighbor not in visited:
                    count, temp = f(neighbor)
                    res += count
                    li.extend(temp)
            return res, li
        res = 0
        for i in range(n):
            if i not in visited:
                count, temp = f(i)
                cur = True
                for node in temp:
                    if len(graph[node]) != count - 1:
                        cur = False
                        break
                if cur:
                    res += 1
        return res