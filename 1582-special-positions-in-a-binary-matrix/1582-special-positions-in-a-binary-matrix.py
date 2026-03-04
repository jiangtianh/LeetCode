class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])

        def check(x, y):
            for i in range(n):
                if i != y:
                    if mat[x][i] == 1:
                        return False 
            for i in range(m):
                if i != x:
                    if mat[i][y] == 1:
                        return False 
            return True 
        res = 0
        row = [True] * m
        col = [True] * n
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1 and row[i] and col[j]:
                    if check(i, j):
                        res += 1
                        row[i] = False 
                        col[j] = False
        return res