class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zeros = 0
        res = 0
        count = 0
        l = 0

        for r, num in enumerate(nums):
            if num == 1:
                count += 1
            else:
                zeros += 1
            
            while zeros > 1:
                if nums[l] == 1:
                    count -= 1
                else:
                    zeros -= 1
                l += 1
            
            res = max(res, count)
        if res == len(nums):
            return res - 1
        return res