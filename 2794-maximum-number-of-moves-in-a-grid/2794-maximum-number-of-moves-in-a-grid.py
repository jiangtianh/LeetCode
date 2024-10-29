class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        self.d = {}
        def check(x, y):
            return 0 <= x < m and 0 <= y < n
        directions = [-1, 0, 1]


        def f(x, y):
            if (x, y) in self.d:
                return self.d[(x, y)]
            res = 0
            num = grid[x][y]
            for i in directions:
                if check(x+i, y+1) and grid[x+i][y+1] > num:
                    res = max(res, f(x+i, y+1) + 1)
            self.d[(x, y)] = res
            return res


        res = 0
        for i in range(m):
            res = max(res, f(i, 0))
        
        return res
            