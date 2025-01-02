class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        flip = 0
        l = 0
        res = 0

        for r, n in enumerate(nums):
            if n == 0:
                flip += 1
            while l <= r and flip > 1:
                if nums[l] == 0:
                    flip -= 1
                l += 1
            
            res = max(res, r - l + 1)
        return res
