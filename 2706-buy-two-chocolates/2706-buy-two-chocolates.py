class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        smallest = math.inf
        secondSmallest = math.inf
        
        
        for p in prices:
            if p < smallest:
                secondSmallest = smallest
                smallest = p
            elif p < secondSmallest:
                secondSmallest = p
            
        res = smallest + secondSmallest
        print(res)
        if res > money:
            return money 
        else:
            return money - res
        
        