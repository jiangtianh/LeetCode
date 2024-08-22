class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        matrix = [[0] * n for _ in range(m)]

        for x, y in indices:

            for i in range(m):
                matrix[i][y] += 1
            for i in range(n):
                matrix[x][i] += 1
        res = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] % 2 == 1:
                    res += 1
        return res