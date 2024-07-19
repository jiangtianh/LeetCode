class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])

        rows = [math.inf] * m
        cols = [-math.inf] * n

        for i in range(m):
            rows[i] = min(matrix[i])
        
        for i in range(n):
            for j in range(m):
                cols[i] = max(cols[i], matrix[j][i])
        
        res = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == cols[j] == rows[i]:
                    res.append(matrix[i][j])
        return res
