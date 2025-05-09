class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        @cache
        def f(target):
            if target < 0:
                return 0
            if target == 0:
                return 1
            res = 0
            for num in nums:
                res += f(target - num)
            return res
        return f(target)