class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        graph = [0]
        x = n - 1
        y = 0
        direction = 1

        while x >= 0:
            graph.append(board[x][y])
            y += direction
            if y == n or y == -1:
                x -= 1
                direction *= -1
                y = 0 if y == -1 else n-1
        
        q = collections.deque([1])
        res = 0
        destination = n ** 2
        visited = set()

        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                if cur == destination:
                    return res
                if cur in visited:
                    continue
                visited.add(cur)


                for i in range(cur + 1, min(destination, cur + 6) + 1):
                    if graph[i] != -1:
                        q.append(graph[i])
                    else:
                        q.append(i)
            
            res += 1
        return -1