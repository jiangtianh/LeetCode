class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        @cache
        def f(i):
            if i == len(nums):
                return 0
            
            res = 1
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    res = max(res, f(j) + 1)
            
            
            return res
    
        res = 0
        for i in range(len(nums)):
            res = max(res, f(i))
        return res
        