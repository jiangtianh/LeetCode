class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        inY = collections.defaultdict(int)
        outY = collections.defaultdict(int)
        inYCount = outYCount = 0
        n = len(grid)
        def isInY(x, y):
            if x <= n // 2:
                left = x == y
                right = x + y == n - 1
                return left or right
            else:
                return y == n // 2
        
        for x in range(n):
            for y in range(n):
                num = grid[x][y]
                if isInY(x, y):
                    inY[num] += 1
                    inYCount += 1
                else:
                    outY[num] += 1
                    outYCount += 1
        

        res = math.inf
        for inYN in range(3):
            for outYN in range(3):
                if inYN == outYN:
                    continue
                res = min(res, inYCount - inY[inYN] + outYCount - outY[outYN])
        return res