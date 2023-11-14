class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        @cache 
        def f(i, haveStock):
            if i >= len(prices):
                return 0 
        
            if haveStock:
                option1 = f(i+1, True)
                option2 = f(i+1, False) + prices[i]
            else:
                option1 = f(i+1, False)
                option2 = f(i+1, True) - prices[i]
            return max(option1, option2)
    
        return f(0, False)