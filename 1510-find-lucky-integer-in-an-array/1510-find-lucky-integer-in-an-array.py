class Solution:
    def findLucky(self, arr: List[int]) -> int:
        counter = collections.Counter(arr)

        res = -1
        for n in counter:
            if counter[n] == n:
                res = max(res, n)
        return res