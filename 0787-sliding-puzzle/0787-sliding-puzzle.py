class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        temp = []
        directions = [[1, 3],[0, 2, 4],[1, 5],[0, 4],[3, 5, 1],[4, 2]]
        for i in range(2):
            for j in range(3):
                temp.append(str(board[i][j]))
        board = "".join(temp)
        visited = set([board])
        q = collections.deque([board])
        res = "123450"

        def swap(board, visited):
            res = []
            board = list(board)
            zeroIdx = board.index("0")
            for dirc in directions[zeroIdx]:
                board[zeroIdx], board[dirc] = board[dirc], board[zeroIdx]
                temp = "".join(board)
                if temp not in visited:
                    visited.add(temp)
                    res.append("".join(board))
                board[zeroIdx], board[dirc] = board[dirc], board[zeroIdx]
            return res
        count = 0
        while q:
            for _ in range(len(q)):
                curBoard = q.popleft()
                if curBoard == res:
                    return count
                q.extend(swap(curBoard, visited))
            count += 1

        return -1