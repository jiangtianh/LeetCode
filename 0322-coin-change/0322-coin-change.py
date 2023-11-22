class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def f(amount):
            if amount < 0:
                return math.inf 
            elif amount == 0:
                return 0 
            res = math.inf
            for coin in coins:
                temp = f(amount - coin)
                if temp != math.inf:
                    res = min(res, temp + 1)
            
            return res
        
        res = f(amount)
        if res == math.inf:
            return -1
        return res