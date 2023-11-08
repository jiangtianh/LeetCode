class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        @cache
        def f(i, amount):
            if i == len(nums):
                if amount == target:
                    return 1
                else:
                    return 0
            else:
                return f(i + 1, amount + nums[i]) + f(i + 1, amount - nums[i])
        
        return f(0, 0)
        


