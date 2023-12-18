class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        Sum = 0
        l = 0
        res = len(nums) + 1
        
        for i, num in enumerate(nums):
            Sum += num 
            
            while Sum >= target:
                res = min(res, i - l + 1)
                
                Sum -= nums[l]
                l += 1
    
        if res > len(nums):
            return 0
        return res
        
        
        
        