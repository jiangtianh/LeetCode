class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        graph1 = collections.defaultdict(list)
        for x, y in edges1:
            graph1[x].append(y)
            graph1[y].append(x)
        graph2 = collections.defaultdict(list)
        for x, y in edges2:
            graph2[x].append(y)
            graph2[y].append(x)

        def bfs(node, graph, k):
            if k < 0:
                return 0
            q = collections.deque([node])
            visited = set([node])
            res = 1
            while k > 0 and q:
                for _ in range(len(q)):
                    cur = q.popleft()
                    for neighbor in graph[cur]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            q.append(neighbor)
                            res += 1
                k -= 1
            return res

        secondBiggest = 0
        for i in range(len(edges2) + 1):
            secondBiggest = max(secondBiggest, bfs(i, graph2, k-1))
        
        print(secondBiggest)
        res = []
        for i in range(len(edges1) + 1):
            res.append(bfs(i, graph1, k) + secondBiggest)
        return res