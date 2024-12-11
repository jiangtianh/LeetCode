class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0
        res = 0

        for r, num in enumerate(nums):
            left, right = num - k, num + k

            while left > nums[l] + k or right < nums[l] - k:
                l += 1
            
            res = max(res, r - l + 1)

        return res