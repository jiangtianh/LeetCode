class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        
        @cache
        def f(l, r, i):
            if i == len(multipliers):
                return 0
        
            return max(f(l + 1, r, i + 1) + multipliers[i] * nums[l], f(l, r - 1, i + 1) + multipliers[i] * nums[r])


        return f(0, len(nums) - 1, 0)