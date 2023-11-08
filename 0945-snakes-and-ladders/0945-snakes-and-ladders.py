class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)

        p = 1
        edges = {}
        for i in range(n):
            x = n - i - 1
            if i % 2 == 0:
                for y in range(n):
                    if board[x][y] != -1:
                        edges[p] = board[x][y]
                    p += 1
            else:
                for y in range(n-1, -1, -1):
                    if board[x][y] != -1:
                        edges[p] = board[x][y]
                    p += 1

        q = collections.deque()
        q.append(1)
        visited = {1}
        step = 0

        while q:
            step += 1
            for _ in range(len(q)):
                cur = q.popleft()
                for i in range(1, 7):
                    newN = cur + i
                    if newN in visited:
                        continue
                    if newN >= n ** 2:
                        return step

                    visited.add(newN)

                    if newN in edges:
                        edge = edges[newN]
                        if edge >= n ** 2:
                            return step
                        
                        q.append(edge)
                    else:
                        q.append(newN)
            
            

        return -1
