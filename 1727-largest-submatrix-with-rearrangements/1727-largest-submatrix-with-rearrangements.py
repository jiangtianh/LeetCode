class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        li = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        
        temp = [0] * len(matrix[0])

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 1:
                    temp[j] += 1
                else:
                    temp[j] = 0

                li[i][j] = temp[j]

        res = 0
        print(li)
        for i in range(len(li)):
            li[i].sort(reverse=True)

            smallest = li[i][0]
            for j in range(len(li[0])):
                if smallest > li[i][j]:
                    smallest = li[i][j]
                res = max(res, smallest * (j + 1))
            



        return res






