class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        start, end = 0, len(matrix) - 1

        while start < end:
            
            for i in range(end - start):

                topleft = matrix[start][start + i]

                matrix[start][start + i] = matrix[end - i][start] 

                matrix[end - i][start] = matrix[end][end - i]

                matrix[end][end - i] = matrix[start + i][end]

                matrix[start + i][end] = topleft

            start += 1
            end -= 1

                # topright = matrix[start + i][end]

                # bottomright = matrix[end][end - i]

                # bottomleft = matrix[end - i][start] 



