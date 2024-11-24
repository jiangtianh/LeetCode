class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        smallest = math.inf
        negativeCount = 0
        total = 0

        for row in matrix:
            for num in row:
                if num < 0:
                    negativeCount += 1
                total += abs(num)
                smallest = min(smallest, abs(num))

        if negativeCount % 2 == 0:
            return total
        else:
            return total - 2 * smallest
