class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        res = 0
        d = {}
        for x, y in dominoes:
            if (x, y) in d:
                res += d[(x, y)]
                d[(x, y)] += 1
            elif (y, x) in d:
                res += d[(y, x)]
                d[(y, x)] += 1
            else:
                d[(x, y)] = 1
        return res