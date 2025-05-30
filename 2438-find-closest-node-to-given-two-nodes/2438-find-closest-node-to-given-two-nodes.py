class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        
        
        def bfs(node, visited, res):
            step = 0
            q = collections.deque([node])
            while q:
                for _ in range(len(q)):
                    cur = q.popleft()
                    if cur in visited:
                        continue 
                    visited.add(cur)
                    res[cur] = step
                    if edges[cur] != -1:
                        q.append(edges[cur])
                step += 1

        res1 = [-1] * len(edges)
        bfs(node1, set(), res1)
        res2 = [-1] * len(edges)
        bfs(node2, set(), res2)
        print(res1) 
        print(res2)
        resCount = math.inf
        res = -1
        for i in range(len(edges)):
            if res1[i] != -1 and res2[i] != -1:
                if resCount > max(res1[i], res2[i]):
                    resCount = max(res1[i], res2[i])
                    res = i
        
        return res