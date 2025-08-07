class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        n = len(fruits)
        
        firstKid = 0
        for i in range(n):
            firstKid += fruits[i][i]
            fruits[i][i] = 0

        dp1 = [[0] * n for _ in range(n)]

        seen1 = set()
        
        
        for x in range(n):
            for y in range(n - min(x+1, n-x), n):
                seen1.add((x, y))
                cur = 0
                for prevY in range(y-1, min(y+2, n)):
                    if (x-1, prevY) in seen1:
                        cur = max(cur, dp1[x-1][prevY])
                dp1[x][y] = fruits[x][y] + cur
        
        dp2 = [[0] * n for _ in range(n)]
        seen2 = set()

        for y in range(n):
            for x in range(n - min(y+1, n-y), n):
                seen2.add((x, y))
                cur = 0
                for prevX in range(x-1, min(x+2, n)):
                    if (prevX, y-1) in seen2:
                        cur = max(cur, dp2[prevX][y-1])
                dp2[x][y] += fruits[x][y] + cur


        return firstKid + dp1[n-1][n-1] + dp2[n-1][n-1]