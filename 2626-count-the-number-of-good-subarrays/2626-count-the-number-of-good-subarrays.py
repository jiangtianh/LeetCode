class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        d = collections.defaultdict(int)
        pairs = 0
        res = 0
        l = 0
        for r, num in enumerate(nums):
            pairs += d[num]
            d[num] += 1
            while l <= r and pairs >= k:
                res += len(nums) - r 
                d[nums[l]] -= 1
                pairs -= d[nums[l]]
                l += 1
        return res