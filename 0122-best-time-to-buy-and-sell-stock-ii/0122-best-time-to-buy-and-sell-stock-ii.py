class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prev = -1
        res = 0
        for i in range(len(prices)):
            price = prices[i]
            
            if i != len(prices) -1 and prices[i] < prices[i+1] and prev == -1:
                prev = price
            
            elif i != len(prices) - 1 and prices[i] > prices[i+1] and prev != -1:
                res += price - prev
                prev = -1
        
        if prev != -1:
            res += prices[-1] - prev
        
        return res
            
            
            
        