class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        total = 0
        l = 0
        res = 0

        for r, num in enumerate(nums):
            total += num
            while total * (r - l + 1) >= k:
                total -= nums[l]
                l += 1
            
            res += r - l + 1
        return res 