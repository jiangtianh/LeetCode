class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m, n = len(grid1), len(grid1[0])
        direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        def check(x, y):
            return 0 <= x < m and 0 <= y < n and grid2[x][y] == 1
        self.isSub = True
        def f(x, y):
            grid2[x][y] = 0
            if grid1[x][y] != 1:
                self.isSub = False
            for i, j in direction:
                newX, newY = x + i, y + j
                if check(newX, newY):
                    f(newX, newY)
        
        res = 0
        for x in range(m):
            for y in range(n):
                if grid2[x][y] == 1:
                    self.isSub = True
                    f(x, y)
                    if self.isSub:
                        res += 1

        return res