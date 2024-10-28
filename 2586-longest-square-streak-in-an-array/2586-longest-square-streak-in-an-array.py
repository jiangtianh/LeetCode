class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort()
        self.res = 1

        @cache
        def f(i):
            if i >= len(nums):
                return 0
            num = nums[i]
            square = num ** 2
            idx = bisect_left(nums, square, i+1)
            if idx >= len(nums) or nums[idx] != square:
                return 1
            else:
                res = f(idx) + 1
            return res
        
        res = 1

        for i in range(len(nums)):
            res = max(res, f(i))
        
        if res < 2:
            return -1
        return res
        