class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        i = 0
        res = 0
        while i < len(costs) and coins >= costs[i]:
            coins -= costs[i]
            res += 1
            i += 1
        
        return res