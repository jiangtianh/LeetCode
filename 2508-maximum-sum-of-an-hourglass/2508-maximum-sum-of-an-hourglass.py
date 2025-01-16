class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        sumOfThree = []
        m, n = len(grid), len(grid[0])

        for i in range(m):
            temp = []
            total = 0
            for j in range(n):
                total += grid[i][j]
                if j >= 2:
                    temp.append(total)
                    total -= grid[i][j-2]
        
            sumOfThree.append(temp)

        res = 0
        for i in range(m - 2):
            for j in range(n - 2):
                res = max(res, sumOfThree[i][j] + grid[i+1][j+1] + sumOfThree[i+2][j])
        
        return res