class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        d = collections.defaultdict(int)
        l = 0
        res = 0
        maxValue = max(nums)
        
        for r, num in enumerate(nums):
            d[num] += 1
            while d[maxValue] >= k:
                res += len(nums) - r
                d[nums[l]] -= 1
                l += 1

        return res