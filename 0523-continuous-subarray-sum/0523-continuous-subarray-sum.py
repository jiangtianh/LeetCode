class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        d = {}
        total = 0
        
        for i, num in enumerate(nums):
            total += num
            mod = total % k
            
            if mod == 0:
                if i != 0:
                    return True 
            
            if mod in d:
                if i - d[mod] > 1:
                    return True 
                
            else:
                d[mod] = i
                
        return False
        
        