class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        d = {0:1}
        total = 0
        res = 0
        for num in nums:
            total += num 
            
    
            if total - k in d:
                res += d[total - k]
            d[total] = d.get(total, 0) + 1
            
      
        
        return res
        
        
            
        
