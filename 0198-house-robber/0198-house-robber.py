class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def f(i):
            if i >= len(nums):
                return 0 
        
            return max(nums[i] + f(i + 2),  f(i + 1))
        return f(0)
        
        