class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        total = 0
        res = 0
        for num in nums:
            total += num
            res = max(res, total)
            if total < 0:
                total = 0
        
        total = 0
        
        for num in nums:
            total += num 
            res = max(res, abs(total))
            if total > 0:
                total = 0
            
        
        return res