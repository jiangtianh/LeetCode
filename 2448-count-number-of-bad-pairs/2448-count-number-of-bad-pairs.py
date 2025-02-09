class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        count = 0
        d = collections.defaultdict(int)

        for i, n in enumerate(nums):
            x = n - i
            count += d[x]
            d[x] += 1
        n = len(nums)
        return (n * (n-1) // 2) - count