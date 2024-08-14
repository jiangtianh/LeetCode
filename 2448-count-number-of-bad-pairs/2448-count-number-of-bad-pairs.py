class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        d = collections.defaultdict(int)
        res = 0


        for i, num in enumerate(nums):
            n = num - i
            res += d[n]
            d[n] += 1
        n = len(nums)

        return n * (n-1) // 2 - res
