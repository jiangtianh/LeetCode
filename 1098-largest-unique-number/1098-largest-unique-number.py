class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)
        res = -1
        for n in counter:
            if counter[n] == 1:
                res = max(res, n)
        return res