class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        res = 0
        
        for i in range(len(nums)):
            num = nums[i]
            lowerNeed = lower - num
            upperNeed = upper - num
            lowerIdx = bisect_left(nums, lowerNeed, 0, i)
            upperIdx = bisect_right(nums, upperNeed, 0, i)
            res += upperIdx - lowerIdx
        return res
