class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])

        consecutiveOnes = [[0] * n for _ in range(m)]

        for j in range(n):
            count = 0
            for i in range(m):
                if matrix[i][j] == 1:
                    count += 1
                else:
                    count = 0
                consecutiveOnes[i][j] = count

        res = 0
        for li in consecutiveOnes:
            li.sort(reverse=True)   
            smallest = li[0]

            for i, num in enumerate(li):
                if num == 0:
                    break
                smallest = min(smallest, num)
                res = max(res, smallest * (i + 1))
        return res
                
