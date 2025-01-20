class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        d = {}
        for x in range(m):
            for y in range(n):
                d[mat[x][y]] = (x, y)
        
        row = [0] * m
        col = [0] * n

        for i, num in enumerate(arr):
            x, y = d[num]
            row[x] += 1
            col[y] += 1
            if row[x] == n or col[y] == m:
                return i
        
