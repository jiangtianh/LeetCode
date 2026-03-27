class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        matrix = mat[:]
        m, n = len(mat), len(mat[0])

        k %= n

        for i in range(m):

            if i % 2 == 0:
                matrix[i] = matrix[i][k:] + matrix[i][:k]
            else:
                matrix[i] = matrix[i][-k:] + matrix[i][:-k]

        return mat == matrix