class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @cache
        def f(i, haveStock):
            
            if i == len(prices):
                return 0 
            
            if haveStock:
                return max(f(i+1, True), f(i+1, False) + prices[i])
            else:
                return max(f(i+1, False), f(i+1, True) - prices[i])
        
        return f(0, False)
            
            
            
        