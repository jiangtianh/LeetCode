class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        res = 0
        biggest = max(nums)
        count = 0

        for num in nums:
            if num == biggest:
                count += 1
                res = max(res, count)

            else:
                count = 0

        return res