class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def f(amount):
            if amount == 0:
                return 0
            elif amount < 0:
                return math.inf
            
            res = math.inf

            for coin in coins:
                res = min(res, f(amount - coin))
            
            return res + 1
        
        res = f(amount)
        if res == math.inf:
            return -1
        else:
            return res