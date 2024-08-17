class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:

        res = 0
        
        small = arrays[0][0]
        large = arrays[0][-1]

        for i in range(1, len(arrays)):
            s, l = arrays[i][0], arrays[i][-1]

            takeLeft = large - s
            takeRight = l - small

            res = max(res, takeLeft, takeRight)

            small = min(small, s)
            large = max(large, l)


        return res
