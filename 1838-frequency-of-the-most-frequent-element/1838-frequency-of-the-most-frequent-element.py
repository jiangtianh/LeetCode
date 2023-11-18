class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort() 
        res = 1
        
        r = 1
        l = 0
        
        while r < len(nums):
            size = r - l
            num = nums[r] 
            
            k -= (num - nums[r-1]) * size
            
            while k < 0:
                k += num - nums[l]
                l += 1
                
            res = max(res, r - l + 1)
            
            r += 1
            
            
        return res
            
        
            
            
            