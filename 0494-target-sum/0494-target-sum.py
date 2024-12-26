class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @cache
        def f(i, cur):
            if i == len(nums):
                if cur == target:
                    return 1
                else:
                    return 0
            return f(i+1, cur + nums[i]) + f(i+1, cur - nums[i])            
        return f(0, 0)