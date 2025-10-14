class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        up = 1
        prev = 0
        res = 0
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                up += 1
            else:
                prev = up
                up = 1

            res = max(res, up // 2, min(up, prev))
        
        return res