class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        big = arrays[0][-1]
        small = arrays[0][0]
        res = 0
        for i in range(1, len(arrays)):
            curBig = arrays[i][-1]
            curSmall = arrays[i][0]

            res = max(res, big - curSmall, curBig - small)

            small = min(small, curSmall)
            big = max(big, curBig)

        return res