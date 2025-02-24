class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        graph = collections.defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        bobTimeLine = {}
        def traverseBob(node, time):
            nonlocal bobTimeLine
            if node == 0:
                bobTimeLine[node] = time
                return True
            bobTimeLine[node] = time
            for neighbor in graph[node]:
                if neighbor not in bobTimeLine and traverseBob(neighbor, time + 1):
                    return True
            bobTimeLine.pop(node)
            return False
        traverseBob(bob, 0)
        
        aliceVisited = set()
        print(bobTimeLine)

        def traverseAlice(node, time):
            nonlocal bobTimeLine
            
            if node in bobTimeLine and time == bobTimeLine[node]:
                res = amount[node] // 2
            elif node in bobTimeLine and time > bobTimeLine[node]:
                res = 0
            else:
                res = amount[node]

            later = -math.inf
            aliceVisited.add(node)
            for neighbor in graph[node]:
                if neighbor not in aliceVisited:
                    later = max(later, traverseAlice(neighbor, time + 1))
            aliceVisited.remove(node)
            return res + (later if later != -math.inf else 0)

        return traverseAlice(0, 0)
