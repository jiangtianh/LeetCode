class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        
        res = 0
        
        for i in range(1, len(prices)):
            lowest = min(lowest, prices[i])
            
            res = max(res, prices[i] - lowest)
        
        return res
        