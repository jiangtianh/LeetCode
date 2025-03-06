class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        counter = collections.Counter()
        print(n)
        for row in grid:
            for num in row:
                counter[num] += 1
        res = [-1, -1]

        for i in range(1, (n ** 2) + 1):
            if counter[i] == 0:
                res[1] = i
            elif counter[i] == 2:
                res[0] = i
        return res