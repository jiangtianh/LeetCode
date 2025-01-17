class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        beginning = prices[0]
        res = 0 
        for i in range(len(prices)):
            beginning = min(beginning, prices[i])
            res = max(res, prices[i] - beginning)
        return res