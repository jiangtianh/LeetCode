class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        rows = [0] * 3
        cols = [0] * 3
        left, right = 0, 0
        player = 1

        for x, y in moves:
            rows[x] += player
            cols[y] += player

            if x == y:
                left += player
            if x + y == 2:
                right += player

            if any(abs(line) == 3 for line in (rows[x], cols[y], left, right)):
                return 'A' if player == 1 else 'B'

            player *= -1

        return 'Draw' if len(moves) == 9 else 'Pending'