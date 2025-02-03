class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        res = 1
        result = 1
        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                res += 1
                result = max(result, res)
            else:
                res = 1
        res = 1
        for i in range(1, len(nums)):
            if nums[i-1] > nums[i]:
                res += 1
                result = max(result, res)
            else:
                res = 1
        return result