class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[0])

        @cache
        def f(i):
            if i == len(pairs):
                return 0 
            end = pairs[i][1]
            res = 0
            for j in range(i+1, len(pairs)):
                if pairs[j][0] > end:
                    res = max(res, f(j))

            return res + 1
        res = 0
        for i in range(len(pairs)):
            res = max(res, f(i))
        return res